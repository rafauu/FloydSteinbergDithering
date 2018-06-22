import matplotlib.image as mp_img
from image import Image


class ImageLoader:
    def __init__(self, image_name: str):
        raw_image = mp_img.imread(image_name)
        raw_image.setflags(write=1)
        self.image = Image(raw_image)
