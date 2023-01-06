from PIL import Image


# converting the image
def convert_img(img_name, n, threshold):
    with Image.open(img_name) as img:
        img = img.convert('L')
        img = img.resize((n, n))
        img = img.point(lambda p: 255 if p > threshold else 0)
    return img


# creating the matrix
def create_matrix(img):
    n = img.height
    pixels = [[img.getpixel((i, j)) for i in range(n)] for j in range(n)]

    # replacing pixel values in matrix: 1 - black, 0 - white
    for i in range(n):
        for j in range(n):
            if pixels[i][j] == 255:
                pixels[i][j] = 0
            else:
                pixels[i][j] = 1
    return pixels


def save_matrix_to_file(pixels, file):
    matrix = open(file, 'w')
    for line in pixels:
        for i in line:
            matrix.write(str(i))
        matrix.write('\n')
    matrix.close()


converted = convert_img('test_image.png', 20, 125)
converted.show()
matrix = create_matrix(converted)
save_matrix_to_file(matrix, 'matrix.txt')
for line in matrix:
    print(line)