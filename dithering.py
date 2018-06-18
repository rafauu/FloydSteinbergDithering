import numpy as np


class Dithering:
    def __init__(self, image: []):
        self.image = image
        self.size = len(image)
        self.colors_per_channel = 255

    def dither(self) -> []:
        for y in range(0, self.size):
            print(y)
            for x in range(0, self.size):
                if x == 0 or x == self.size - 1 or y == self.size - 1:
                    continue
                self._quantize_pixel(x, y)
                # return self.image  # just for testing
        return self.image

    def _quantize_pixel(self, x: int, y: int) -> None:
        new_pixel = self._find_closest_colors(self.image[x][y], 4)
        quant_error = self.image[x][y] - new_pixel
        self.image[x][y] = new_pixel
        # print(quant_error)
        # print(quant_error * 7 / 16)
        self.image[x + 1][y] += [np.uint8(int(ch)) for ch in quant_error * 7 / 16]
        # print(self.image[x + 1][y])
        # print(int(-13.234375))
        # print(np.uint8(int(-13.666)))
        self.image[x - 1][y + 1] += [np.uint8(ch) for ch in quant_error * 3 / 16]
        self.image[x][y + 1] += [np.uint8(ch) for ch in quant_error * 5 / 16]
        self.image[x + 1][y + 1] += [np.uint8(ch) for ch in quant_error * 1 / 16]

    def _find_closest_colors(self, pixel: [], colors_qty: int) -> []:
        factor = self.colors_per_channel/colors_qty
        # print(pixel)
        pixel = [round(color/factor)*factor for color in pixel]
        # print(pixel)
        return pixel
