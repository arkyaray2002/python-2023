class PyConverter:
    def __init__(self, length, unit):
        self.length = length
        self.unit = unit

    def centimeters(self):
        if self.unit == 'centimeters':
            return self.length
        elif self.unit == 'meters':
            return self.length * 100
        elif self.unit == 'kilometers':
            return self.length * 10000
        else:
            raise ValueError

    def meters(self):
        if self.unit == 'centimeters':
            return self.length/100
        elif self.unit == 'meters':
            return self.length 
        elif self.unit == 'kilometers':
            return self.length * 100
        else:
            raise ValueError

    def kilometers(self):
        if self.unit == 'centimeters':
            return self.length / 10000
        elif self.unit == 'meters':
            return self.length / 100
        elif self.unit == 'kilometers':
            return self.length
        else:
            raise ValueError


ob = PyConverter(16, 'centimeters')
try:
    print(ob.centimeters())
    print(ob.meters())
    print(ob.kilometers())
except ValueError:
    print("Incorrect parameter")
