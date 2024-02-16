def power(n, p):
    if p == 1:
        return n
    else:
        return n * power(n, p-1)

def show_employee(name, salary):
    print(f"name: {name}. salary: {salary}")
    
