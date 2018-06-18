import matplotlib.pyplot as plt
import matplotlib.image as mpimg

img = mpimg.imread('birds512.jpg')
img.setflags(write=1)
size = img.__len__()
fig = plt.figure()

first_img = fig.add_subplot(1, 2, 1).imshow(img)
plt.axis('off')

for y in range(0, size):
    for x in range(0, size):
        if x == 0 or x == size-1 or y == size-1:
            continue
        img[x+1][y] += img[x+1][y]

second_img = fig.add_subplot(1, 2, 2).imshow(img)
plt.axis('off')

plt.show()
