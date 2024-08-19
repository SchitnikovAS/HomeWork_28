class Hourse:
    def __init__(self, x_distance: int = 0,  sound: str = 'Frrr'):
        self.x_distance = x_distance
        super().__init__()

    def run(self, dx: int) -> None:
        self.x_distance += dx


class Eagle:
    def __init__(self, y_distance: int = 0, sound: str = 'I train, eat, sleep, and repeat'):
        self.y_distance = y_distance
        self.sound = sound

    def fly(self, dy: int) -> None:
        self.y_distance += dy


class Pegasus(Hourse, Eagle):
    def __init__(self):
        super().__init__()

    def move(self, dx: int, dy: int) -> None:
        self.run(dx)
        self.fly(dy)

    def get_pos(self) -> tuple[int, int]:
        return self.x_distance, self.y_distance

    def voice(self) -> str:
        print(self.sound)


p1 = Pegasus()

print(p1.get_pos())
p1.move(10, 15)
print(p1.get_pos())
p1.move(-5, 20)
print(p1.get_pos())

p1.voice()
