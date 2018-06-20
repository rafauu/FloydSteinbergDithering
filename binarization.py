class Binarization:
    def __init__(self, image: [], threshold: int):
        self.image = image
        self.width = len(image[0])
        self.height = len(image)
        self.colors_per_channel = 255
        self.threshold = threshold

    def binarize(self):
        for y in range(0, self.width):
            print(y)
            for x in range(0, self.height):
                self._apply_threshold(x, y)

    def _apply_threshold(self, x: int, y: int):
        self.image[x][y] = [(color > self.threshold) * self.colors_per_channel
                            for color in self.image[x][y]]
