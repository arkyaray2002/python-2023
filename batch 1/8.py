class Length:
    def __init__(self):
        self.feet = 0
        self.inches = 0

    def set_length(self, feet, inches):
        self.feet = feet
        self.inches = inches

    def get_length(self):
        return (self.feet, self.inches)

    def __str__(self):
        return f"Length is : {self.feet} feet and {self.inches} inches"

    def __add__(self, l2):
        self.feet += l2.feet
        self.inches += l2.inches
        if self.inches > 12:
            self.inches -= 12
            self.feet += 1

l1 = Length()
l2 = Length()

l1.set_length(5, 11)
l2.set_length(5, 6)

print(l1.get_length(), l2.get_length())

print(l1)
print(l2)
l1 + l2
print(l1)
