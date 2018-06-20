from numpy import clip


class Dithering:
    def __init__(self, image: [], colors_qty: int):
        self.image = image
        self.width = len(image[0])
        self.height = len(image)
        self.colors_qty = colors_qty
        self.colors_per_channel = 255
        self.factor = self.colors_per_channel/(self.colors_qty - 1)

    def dither(self) -> []:
        for y in range(0, self.width - 1):
            print(y)
            for x in range(1, self.height - 1):
                self._quantize_pixel(x, y)
        return self.image

    def _quantize_pixel(self, x: int, y: int) -> None:
        old_pixel = self.image[x][y]
        new_pixel = self._find_closest_colors(old_pixel)
        quant_error = old_pixel - new_pixel
        self.image[x][y] = new_pixel

        self._propagate_error(x + 1, y, quant_error * 0.4375)
        self._propagate_error(x - 1, y + 1, quant_error * 0.1875)
        self._propagate_error(x, y + 1, quant_error * 0.3125)
        self._propagate_error(x + 1, y + 1, quant_error * 0.0625)

    def _find_closest_colors(self, pixel: []) -> []:
        return [round(color/self.factor)*self.factor for color in pixel]

    def _propagate_error(self, x: int, y: int, quant_error: []) -> None:
        clip(self.image[x][y] + quant_error,
             0, self.colors_per_channel,
             out=self.image[x][y])
