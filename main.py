from dithering import Dithering
from image_loader import ImageLoader
from image_plotter import ImagePlotter
import time


def main():
    image = ImageLoader('birds512gray.jpg').img
    image_plotter = ImagePlotter(2)

    image_plotter.plot(image)

    time1 = time.time()
    image = Dithering(image, 2).dither()
    time2 = time.time()
    print(time2 - time1)

    image_plotter.plot(image)


if __name__ == "__main__":
    main()
