def is_empty(stack):
    return len(stack) == 0

def push(stack, item):
    stack.append(item)

def pop(stack):
    if not is_empty(stack):
        return stack.pop()
    else:
        print("Stack is empty. Cannot pop from an empty stack.")
        return None

def peek(stack):
    if not is_empty(stack):
        return stack[-1]
    else:
        print("Stack is empty. Cannot peek an empty stack.")
        return None

def display(stack):
    if not is_empty(stack):
        print("Stack Contents:")
        for item in reversed(stack):
            print(item)
    else:
        print("Stack is empty.")

# Example usage:
stack = []

# Push elements onto the stack
push(stack, 1)
push(stack, 2)
push(stack, 3)

# Display stack contents
display(stack)

# Peek at the top element
print("Peek:", peek(stack))

# Pop elements from the stack
print("Pop:", pop(stack))
print("Pop:", pop(stack))
print("Pop:", pop(stack))

# Attempting to pop from an empty stack
print("Pop:", pop(stack))
