from image import Image
import matplotlib.pyplot as plt


class ImagePlotter:
    def __init__(self, quantity: int):
        self.fig = plt.figure()
        self.quantity = quantity
        self.already_plotted = 0

    def plot(self, image: Image) -> None:
        self.already_plotted += 1

        if self.already_plotted <= self.quantity:
            self.fig.add_subplot(1, self.quantity,
                                 self.already_plotted).imshow(image.raw_image)
            plt.axis('off')

        if self.already_plotted == self.quantity:
            plt.show()
