class Vector3():
    def __init__(self, x, y, z):
        self.x = x
        self.y = y
        self.z = z

    def __add__(self, v):
        return Vector3(self.x + v.x, self.y + v.y, self.z + v.z)

    def __sub__(self, v):
        return Vector3(self.x - v.x, self.y - v.y, self.z - v.z)

    def __mul__(self, n):
        return Vector3(self.x * n, self.y * n, self.z * n)

    def __truediv__(self, n):
        return Vector3(self.x / n, self.y / n, self.z / n)

    @property
    def length(self):
        return (self.x ** 2 + self.y ** 2 + self.z ** 2) ** 0.5

    def __str__(self):
        return 'Vector3({},{},{})'.format(self.x, self.y, self.z)

    def dot(self, v):
        return self.x * v.x + self.y * v.y + self.z * v.z

    def cross(self, v):
        return Vector3(self.y * v.z - self.z * v.y,
                       self.z * v.x - self.x * v.z,
                       self.x * v.y - self.y * v.x)

    def distance(self, v):
        return ((self.x - v.x) ** 2 + (self.y - v.y) ** 2 + (self.z - v.z) ** 2) ** 0.5
