from image import Image
from numpy import clip
from itertools import product


class Dithering:
    def __init__(self, image: Image, colors_qty: int):
        self.image = image
        self.factor = image.colors_per_channel/(colors_qty - 1)

    def dither(self) -> []:
        for (y, x) in product(range(0, self.image.width - 1),
                              range(1, self.image.height - 1)):
            self._quantize_pixel(x, y)

    def _quantize_pixel(self, x: int, y: int) -> None:
        old_pixel = self.image.raw_image[x][y]
        new_pixel = self._find_closest_colors(old_pixel)
        quant_error = old_pixel - new_pixel
        self.image.raw_image[x][y] = new_pixel

        self._propagate_error(x + 1, y, quant_error * 0.4375)
        self._propagate_error(x - 1, y + 1, quant_error * 0.1875)
        self._propagate_error(x, y + 1, quant_error * 0.3125)
        self._propagate_error(x + 1, y + 1, quant_error * 0.0625)

    def _find_closest_colors(self, pixel: []) -> []:
        return [round(color/self.factor)*self.factor for color in pixel]

    def _propagate_error(self, x: int, y: int, quant_error: []) -> None:
        clip(self.image.raw_image[x][y] + quant_error,
             0, self.image.colors_per_channel,
             out=self.image.raw_image[x][y])
