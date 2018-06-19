import matplotlib.image as mp_img


class ImageLoader:
    def __init__(self, image_name: str):
        self.img = mp_img.imread(image_name)
        self.img.setflags(write=1)
