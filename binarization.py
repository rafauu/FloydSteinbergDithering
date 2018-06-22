from image import Image
from itertools import product


class Binarization:
    def __init__(self, image: Image, threshold: int):
        self.image = image
        self.threshold = threshold

    def binarize(self):
        for (y, x) in product(range(0, self.image.width),
                              range(0, self.image.height)):
            self._apply_threshold(x, y)

    def _apply_threshold(self, x: int, y: int):
        self.image.raw_image[x][y] = \
            [(color > self.threshold) * self.image.colors_per_channel
             for color in self.image.raw_image[x][y]]
