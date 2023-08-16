class Vec2:
    def __init__(self, x: float, y : float):
        self.x = x
        self.y = y
    def to_tuple(self):
        return (self.x, self.y)
    def __str__(self):
        return f"x = {self.x}, y = {self.y}"
def to_vec(a : tuple):
    return Vec2(a[0], a[1])
