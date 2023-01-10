from PIL import Image


# converting the image
def convert_img(img_name, size, threshold):
    """WCZYTANIE ZDJECIA, ZAMIANA NA SZARY, PRZESKALOWANIE"""
    with Image.open(img_name) as img_a:
        width, height = img_a.size
        n_2, m_2 = w_h(width, height, size)
        img_a = img_a.convert("L")
        img_a = img_a.resize((n_2, m_2))
        img_a = img_a.point(lambda p: 255 if p > threshold else 0)
    return img_a


# creating the matrix
def create_matrix(img):
    """ TWORZENIE LISTY 0 1 """
    n_h = img.height
    m_w = img.width
    pixels = [[img.getpixel((i, j)) for i in range(m_w)] for j in range(n_h)]
    # replacing pixel values in matrix: 1 - black, 0 - white
    for i in range(n_h):
        for j in range(m_w):
            if pixels[i][j] == 255:
                pixels[i][j] = 0
            else:
                pixels[i][j] = 1
    return pixels


def save_matrix_to_file(pixels, file):
    """PRZEPISANIE PRZEROBIONEGO ZDJECIA DO PLIKU"""
    matrix = open(file, "w")
    for line in pixels:
        for i in line:
            matrix.write(str(i))
        matrix.write("\n")
    matrix.close()


def div_five(a_1):
    """ZWRACA LICZBE ZAOKRAGLONA DO 5"""
    if a_1 % 5 <= 2:
        a_1 = a_1 - (a_1 % 5)
    else:
        a_1 = a_1 + (5 - (a_1 % 5))
    return a_1


def w_h(width, height, size):
    """PROPORCJONALNE SKALOWANIE ZDJECIA"""
    print("Dimensions:", width, height)
    if width < height:
        m_1 = size
        n_1 = int((m_1 * height) / width)
        n_1 = 5 * round(n_1/5)

    else:
        n_1 = size
        m_1 = int((n_1 * width) / height)
        m_1 = 5 * round(m_1/5)
    print("wymiary", m_1, n_1)
    return m_1, n_1


IMG_SIZE = 20
IMAGE_NAME = "palma.png"

converted = convert_img(IMAGE_NAME, IMG_SIZE, 160)
converted.show()
matrix_1 = create_matrix(converted)
save_matrix_to_file(matrix_1, "matrix.txt")
