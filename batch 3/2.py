class Queue:
    def __init__(self, size):
        self.size = size
        self.queue = []

    def is_empty(self):
        return self.queue == []

    def is_full(self):
        return len(self.queue) == self.size

    def enqueue(self, val):
        if self.is_full():
            print("Queue is Full!")
            return
        else:
            self.queue.append(val)

    def dequeue(self):
        if self.is_empty():
            print("Queue is Empty!")
            return
        else:
            return self.queue.pop(0)

    def display(self):
        print("Queue:")
        for i in self.queue:
            print(i, end=" ")
        print()


queue1 = Queue(int(input("Enter the size of the queue")))
flag = True
while flag:
    ch = int(input("Enter 1 to enqueue. 2 to dequeue. 3 to display: "))
    match ch:
        case 1:
            queue1.enqueue(int(input("Enter the element to be pushed: ")))

        case 2:
            val = queue1.dequeue()
            val and print(f"{val} dequeued from the queue")

        case 3:
            queue1.display()

        case _:
            print("Wrong input")

    flag = bool(int(input("Continue? 1 -> yes. 0 -> exit")))

print("Code ended")


