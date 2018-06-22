from dithering import Dithering
from image_loader import ImageLoader
from image_plotter import ImagePlotter
from binarization import Binarization
from copy import deepcopy
from time import time


def main():
    image = ImageLoader('blue.jpg').image
    binarized_image = deepcopy(image)
    dithered_image = deepcopy(image)
    print("Images loaded")

    Binarization(binarized_image, 140).binarize()
    print("Binarization done")

    t1 = time()
    Dithering(dithered_image, 2).dither()
    t2 = time()
    print("Dithering done with time: ", t2 - t1)

    image_plotter = ImagePlotter(3)
    image_plotter.plot(image)
    image_plotter.plot(binarized_image)
    image_plotter.plot(dithered_image)


if __name__ == "__main__":
    main()
