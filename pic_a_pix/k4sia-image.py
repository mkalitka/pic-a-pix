from PIL import Image

# converting the image
def convert_img(img_name, size, threshold):
    with Image.open(img_name) as img:
        width, height = img.size
        n, m =w_h(width,height, size)
        img = img.convert('L')
        img = img.resize((n, m))
        img = img.point(lambda p: 255 if p > threshold else 0)
    return img

# creating the matrix
def create_matrix(img):
    n = img.height
    m = img.width
    pixels = [[img.getpixel((i, j)) for i in range(m)] for j in range(n)]
    # replacing pixel values in matrix: 1 - black, 0 - white
    for i in range(n):
        for j in range(m):
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

def div_five(n):
    if n % 5 <= 2:
        return n - (n % 5)
    else:
        return n + (5 - (n % 5))
def w_h (width, height, size) :
    if width > height:
        m = size
        n = int((m * width) / height)
        n = div_five(n)
    else:
        n = size
        m = int((n * width) / height)
        m = div_five(m)
        m, n = n,m
    return n, m

size=20
im = 'palma.png'

converted = convert_img(im, size, 160)
converted.show()
matrix = create_matrix(converted)
save_matrix_to_file(matrix, 'matrix.txt')
for line in matrix:
    print(line)
