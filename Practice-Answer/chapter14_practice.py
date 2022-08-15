class Car:
    def __init__(self, color='red', power=2000):
        self.color = color
        self.power = power
        self.speed = 0

    def forward(self, speed):
        self.speed += speed
        return '앞으로 전진 : 시속 {} km'.format(self.speed)

    def backward(self):
        pass

class Sonata(Car):
    def __init__(self, color, power, size):
        super().__init__(color, power)
        self.size = size

    def backward(self, speed):
        self.speed -= speed
        return '뒤로 후진 : 시속 {} km'.format(self.speed)

class Volvo(Car):
    def __init__(self, color, power, size, price):
        super().__init__(color, power)
        self.size = size
        self.price = price

    def forward(self, speed):
        self.speed = speed * 2
        return "시속 {} km 로 달리는 Volvo".format(self.speed)

    def backward(self):
        return "후진 불가"

sonata = Sonata('black', 1800, 5)
volvo = Volvo('white', 2500, 7, 5000000)

print(sonata.color)
print(sonata.forward(100))
print(sonata.backward(30))

print(volvo.color)
print(volvo.price)
print(volvo.forward(100))
print(volvo.backward())
