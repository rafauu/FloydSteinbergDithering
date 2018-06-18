from dithering import Dithering
from image_loader import ImageLoader
from image_plotter import ImagePlotter


def main():
    image = ImageLoader('birds512.jpg').get_image()
    image_plotter = ImagePlotter(2)

    image_plotter.plot(image)
    image = Dithering(image).dither()
    image_plotter.plot(image)


if __name__ == "__main__":
    main()
