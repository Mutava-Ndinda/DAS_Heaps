# queue1 = []
# queue1.append("name")
# queue1.append("age")
# queue1.append("phone number")
# queue1.append("country")
# print(queue1)
# #removing elements from a queue
# queue1.pop(0)
# print(queue1.pop(0))
# #implementation of queue.Queue
# from queue import Queue
# q = Queue(maxsize = 4)
# #inserting elements
# q.put(10)
# q.put(20)
# q.put(30)
# q.put(40)
# #checking if the queue if full
# print(q.full())
# #checking if the queue is empty
# print(q.empty())
# #removing an element from the queue
# print(q.get())

class Queue:
    def __init__(self):
        self.items = []

    def is_empty(self):
        return len(self.items) == 0

    def enqueue(self, item):
        self.items.append(item)

    def dequeue(self):
        if not self.is_empty():
            return self.items.pop(0)
        else:
            raise IndexError("dequeue from an empty queue")

    def peek(self):
        if not self.is_empty():
            return self.items[0]
        else:
            raise IndexError("peek from an empty queue")

    def size(self):
        return len(self.items)

    def __str__(self):
        return str(self.items)


if __name__ == "__main__":
    queue = Queue()
    queue.enqueue(1)
    queue.enqueue(2)
    queue.enqueue(3)
    print("Queue after enqueuing 1, 2, 3:", queue)

    print("Dequeued item:", queue.dequeue())
    print("Front_item:", queue.peek())
    print("Size of queue:", queue.size())
    print("Is queue empty?", queue.is_empty())
