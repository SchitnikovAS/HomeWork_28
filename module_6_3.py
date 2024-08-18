class Hourse:
    def __init__(self, x_distance: int = 0, y_distance: int = 0, sound: str = 'Frrr'):
        self.x_distance = x_distance
        super().__init__(y_distance, sound)

    def run(self, dx: int) -> int:
        self.x_distance += dx
        return self.x_distance


class Eagle:
    def __init__(self, y_distance: int = 0, sound: str = 'I train, eat, sleep, and repeat'):
        self.y_distance = y_distance
        self.sound = sound

    def fly(self, dy: int) -> int:
        self.y_distance += dy
        return self.y_distance


class Pegasus(Hourse, Eagle):
    def __init__(self, x_distance: int = 0, y_distance: int = 0, sound: str = 'I train, eat, sleep, and repeat'):
        super().__init__(x_distance, y_distance, sound)

    def move(self, dx: int, dy: int) -> tuple[int, int]:
        return self.run(dx), self.fly(dy)

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
