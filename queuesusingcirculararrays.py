class CIRCULARARRAYQUEUE:

#A queue as discussed will use the FIFO principle.
#This is a circular queue - imagina an array as a circle where after the last position, we wrap back to the first position.
# This prevents us from having to shift all elements when we remove/ dequeue items form the front

#We start by defining the max number of elemnts that our queue will hold

    DEFAULT_CAPACITY = 10

    def __init__(self):

#We can continue to create an empty queue by initializing 3 important things:
# I  . _data: which is a list filled with None values , the array...
#II. _size: how many actual elements are at a given timestamp, we will initialize it to zero
#III. _front: the index or the position where the first element is located, we initialize it to zero

# create a list/our array, with DEFAULT_CAPACITY slots, all filled with None.
#You can think of this as creating 10 empty parking slots in a circular parking
        self._data = [None] * CIRCULARARRAYQUEUE.DEFAULT_CAPACITY

#here we keep track of how many elements that are actually in the list.
#for this case the number of cars that are actually parked
        self._size = 0

#and here we keep track of the first ar we parked at the lot
        self._front = 0

    def __len__(self):
        return self._size

    def is_empty(self):
        return self._size == 0

    def first(self):
        if self.is_empty():
            raise Empty('Queue is Empty')# how this exception is raised is by calling the class exception and passing the exception type/message

        #the front element is at position self._front in our array
        return self._data[self._front]

    def dequeue(self):
        if self.is_empty():
            raise Empty('Queue is Empty')

        #here we get the element at the front of the queue, and save it in an attribute
        item_to_dequeue = self._data[self._front]

        #then clear the old front position to help with garbage collection, Python will clean up teh memory better this way
#GARBAGE COLLECTION - a technique manual or autonomous that handles memory alocation and deallocation, ensuring efficient use of memory
        self._data[self._front] = None

        #move the front pointer to the next position
        self._front = (self._front + 1) % len(self._data)

        #we now have one less element in the queue so decrease the queue sixe by 1
        self._size -= 1

        return item_to_dequeue

    def enqueue(self, element):
        if self._size == len(self._data):
            self._resize(2 * len(self._data))#double the capacity

        #calculate where to put the new element(at the back of the queue)

        back_of_the_queue = (self._front + self._size) % len(self._data)

        #place the new element at the newly obtained back position of our queue, where enqueueing takes place
        self._data[back_of_the_queue] = element

        #we now have one more element in the queue, thus we increment the size
        self._size += 1

#WHAT IF THE QUEUE IS FULL BUT WE STILL NEED TO ENQUEUE
    def _resize(self, new_capacity):

        #create a new bigger array
        old_data = self._data #hold the existing data in our queue in the old_data attribute
        self._data = [None] * new_capacity #resizing the new_capacity factor

        #then we copy all elements from the old array to the new one, starting from the front and going in the queue order
        current_index = self._front
        for item in range(self._size):
            #copy each element to the new array in order
            self._data[item] = old_data[current_index]
            #move the next element and remember to wrap around if necessary
            current_index = (current_index + 1) % len(old_data)

        #finally we reset the front the front to the position 0 since we reorganissed everything
        self._front = 0

#this is the class spoken of earlier with a custom exception message for empty queue operations
class Empty(Exception):
    def _init_(self, message='Queue is empty'):
        self.message = message
        super()._init_(self.message)



if __name__ == "__main__": #this check is mostly used to avoid running the contents of this block when imported into another file
    #create a new queue
    queue = CIRCULARARRAYQUEUE()

    print("QUEUES USING CIRCULAR ARRAYS")
    print(f"The initial queue size is: {len(queue)}")
    print(f"Is the queue empty? {queue.is_empty()}")


#ENQUEUE OUR QUEUE
    print("\n Enqueueing our Queue")
    elements_to_enqueue = ['Alice', 'Bob', 'William', 'Dorothy', 'Jessica']


    for person in elements_to_enqueue:
        queue.enqueue(person)
        print(f"Added{person}. Queue size is now: {len(queue)}")


#show the front element without removing it
    print(f"\n Person at the front of the line: {queue.first()}")

    #remove some elements dequeue operations then return it
    for i in range(3):
        served_person = queue.dequeue()
        print(f"Served: {served_person}. Queue size is now: {len(queue)}")

    #to demo the circular nature we can induce an overflow and see is it behaves correctly
    print("\n Adding more people to induce a wrap aroung in the array")
    more_people = ['Frank', 'Linda', 'Ford']

    for person in  more_people:
        queue.enqueue(person)
        print(f"Added {person}. Queue i=size is now: {len(queue)}")

    #show what is left in the queue
    print(f"\n Perosn currently at the front: {queue.first()}")
    print(f"\nTotal people still in the queue: {len(queue)}")

    #demonstate the wrap-around by showing internal state
    print(f"\n Internal details:")
    print(f"\nFront index: {queue._front}")
    print(f"\n Array contents: {queue._data}")

#NB - None values are empty slots in our circular array










