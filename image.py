class Image:
    colors_per_channel = 255

    def __init__(self, raw_image: []):
        self.raw_image = raw_image
        self.width = len(raw_image[0])
        self.height = len(raw_image)
