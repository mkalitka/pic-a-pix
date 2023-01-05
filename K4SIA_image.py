from PIL import Image

n = 25
with Image.open('test_image.jpg') as im:
    im = im.convert('L')
    im1 = im.resize((n, n))
    treshold = 125
    im2 = im1.point(lambda p: 255 if p > treshold else 0)
    im2.show()