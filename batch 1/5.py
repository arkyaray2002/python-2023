s1 = set(input("Enter city names for set 1: ").split())
s2 = set(input("Enter city names for set 2: ").split())

print(f"Union : {s1 | s2}")
print(f"Intersesction : {s1 & s2}")
print(f"Symmetric difference : {s1.symmetric_difference(s2)}")

print(set([x.upper() for x in s1]))
print(set([x.lower() for x in s2]))
