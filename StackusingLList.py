# Enhanced Stack Implementation Using Linked List
# Includes additional features like size tracking, iteration, and better error handling

class StackNode:
    def __init__(self, value):
        self.value = value
        self.next = None


class LinkedListStack:
    def __init__(self):
        self.top = None
        self._size = 0  # Track stack size for O(1) size operations

    def is_empty(self):
        """Check if stack is empty"""
        return self.top is None

    def size(self):
        """Return the number of elements in the stack"""
        return self._size

    def push(self, value):
        """Add element to top of stack"""
        new_node = StackNode(value)
        new_node.next = self.top
        self.top = new_node
        self._size += 1

    def pop(self):
        """Remove and return top element"""
        if self.is_empty():
            raise IndexError("pop from empty stack")

        popped_value = self.top.value
        self.top = self.top.next
        self._size -= 1
        return popped_value

    def peek(self):
        """Return top element without removing it"""
        if self.is_empty():
            raise IndexError("peek from empty stack")
        return self.top.value

    def clear(self):
        """Remove all elements from stack"""
        self.top = None
        self._size = 0

    def to_list(self):
        """Convert stack to list (top to bottom)"""
        result = []
        current = self.top
        while current:
            result.append(current.value)
            current = current.next
        return result

    def __len__(self):
        """Support len() function"""
        return self._size

    def __bool__(self):
        """Support truthiness testing"""
        return not self.is_empty()

    def __iter__(self):
        """Make stack iterable (from top to bottom)"""
        current = self.top
        while current:
            yield current.value
            current = current.next

    def __str__(self):
        """String representation of stack"""
        if self.is_empty():
            return "Stack: []"
        values = " -> ".join(str(val) for val in self)
        return f"Stack (top to bottom): [{values}]"

    def __repr__(self):
        """Detailed representation for debugging"""
        return f"LinkedListStack(size={self._size}, top={self.peek() if not self.is_empty() else None})"


# Performance comparison function
def compare_stack_implementations():
    """Compare linked list stack vs Python list for stack operations"""
    import time

    # Test with large number of operations
    n = 100000

    # Linked List Stack
    ll_stack = LinkedListStack()
    start_time = time.time()

    for i in range(n):
        ll_stack.push(i)

    for i in range(n):
        ll_stack.pop()

    ll_time = time.time() - start_time

    # Python List as Stack
    list_stack = []
    start_time = time.time()

    for i in range(n):
        list_stack.append(i)

    for i in range(n):
        list_stack.pop()

    list_time = time.time() - start_time

    print(f"Linked List Stack: {ll_time:.4f} seconds")
    print(f"Python List Stack: {list_time:.4f} seconds")
    print(f"Ratio: {ll_time / list_time:.2f}x")


# Example usage and testing
if __name__ == "__main__":
    # Basic operations
    stack = LinkedListStack()

    # Test pushing elements
    for i in [5, 10, 15, 20]:
        stack.push(i)

    print(stack)  # Stack representation
    print(f"Size: {len(stack)}")
    print(f"Top element: {stack.peek()}")

    # Test iteration
    print("Elements (top to bottom):", list(stack))

    # Test popping
    print(f"Popped: {stack.pop()}")
    print(f"After pop: {stack}")

    # Test edge cases
    try:
        empty_stack = LinkedListStack()
        empty_stack.pop()  # Should raise error
    except IndexError as e:
        print(f"Caught expected error: {e}")

    # Performance comparison
    print("\nPerformance Comparison:")
    compare_stack_implementations()

    # Memory usage demonstration
    print(f"\nStack with 1000 elements uses individual nodes")
    big_stack = LinkedListStack()
    for i in range(1000):
        big_stack.push(i)
    print(f"Size: {len(big_stack)}, Top: {big_stack.peek()}")