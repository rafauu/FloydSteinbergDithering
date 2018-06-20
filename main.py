from dithering import Dithering
from image_loader import ImageLoader
from image_plotter import ImagePlotter
from binarization import Binarization
import copy


def main():
    image = ImageLoader('kittens2_gray.jpg').img
    binarized_image = copy.deepcopy(image)
    dithered_image = copy.deepcopy(image)

    Binarization(binarized_image, 140).binarize()
    Dithering(dithered_image, 2).dither()

    image_plotter = ImagePlotter(3)
    image_plotter.plot(image)
    image_plotter.plot(binarized_image)
    image_plotter.plot(dithered_image)


if __name__ == "__main__":
    main()
