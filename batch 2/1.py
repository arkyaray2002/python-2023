d = {}
while True:
    print("Enter the product name and product price. 'n' to exit")
    data = input()
    if data == 'n':
        print("Data entry completed")
        break
    else:
        p_name, p_price = data.split()[0], int(data.split()[1])
        d[p_name] = p_price

p_input = input("Enter a product name: ")

try:
    print(f"Price of {p_input} is {d[p_input]}")
except KeyError:
    print(f"{p_input} doesnt exist in your dictionary")

min_range, max_range = list(map(int, input("Enter the price range: \n").split()))
print(f"All products of your dictionary in the range {min_range} - {max_range}")
for key, value in d.items():
    if min_range <= value <= max_range:
        print(f"Price of {key} : {value} ")

