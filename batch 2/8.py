class Stack:
    def __init__(self, size):
        self.tots = -1
        self.size = size - 1
        self.stack = []

    def push(self, val):
        if self.tots >= self.size:
            print("Stack is Full!")
            return
        else:
            self.stack.append(val)
            self.tots += 1

    def pop(self):
        if self.tots < 0:
            print("Stack is Empty!")
            return
        else:
            self.stack.pop()
            self.tots -= 1

    def peep(self):
        print(f"Stack({self.tots}):")
        for each in self.stack[::-1]:
            print(each)


n = int(input("Enter the size of your stack"))
stack1 = Stack(n)
flag = True
while flag:
    ch = int(input("Enter 1 to push. 2 to pop. 3 to display: "))
    match ch:
        case 1:
            stack1.push(int(input("Enter the element to be pushed: ")))
        case 2:
            stack1.pop()
            print("TOTS popped from the stack!")

        case 3:
            stack1.peep()

        case _:
            print("Wrong input")

    flag = bool(int(input("Continue? 1 -> yes. 0 -> exit")))

print("Code ended")
