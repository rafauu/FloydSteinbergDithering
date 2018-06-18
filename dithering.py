class Dithering:
    def __init__(self, image: []):
        self.image = image
        self.size = image.__len__()

    def dither(self) -> []:
        for y in range(0, self.size):
            for x in range(0, self.size):
                if x == 0 or x == self.size - 1 or y == self.size - 1:
                    continue
                self.image[x + 1][y] += self.image[x + 1][y]
        return self.image
