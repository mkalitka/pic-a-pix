from PIL import Image


# converting the image
def convert_img(img_name, size, threshold):
    """Loading the image and converting it"""
    with Image.open(img_name) as img_a:
        width, height = img_a.size
        n_2, m_2 = w_h(width, height, size)
        img_a = img_a.convert("L")
        img_a = img_a.resize((n_2, m_2))
        img_a = img_a.point(lambda p: 255 if p > threshold else 0)
    return img_a


# creating the solution
def create_solution(img):
    """Creating a solution array"""
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


def columns_and_rows(img):
    n_h = img.height
    m_w = img.width
    pixels = [[img.getpixel((i, j)) for i in range(m_w)] for j in range(n_h)]
    rows, cols = [[] for i in range(n_h)], [[] for i in range(m_w)]
    """Counting blocks of black pixels by rows"""
    for i in range(n_h):
        sum_pix = 0
        for j in range(m_w):
            if pixels[i][j] == 255 and sum_pix != 0:
                rows[i].append(sum_pix)
                sum_pix = 0
            elif pixels[i][j] != 255:
                sum_pix += 1
        if sum_pix != 0:
            rows[i].append(sum_pix)
    """Counting blocks of black pixels by columns"""
    for i in range(m_w):
        sum_pix = 0
        for j in range(n_h):
            if pixels[j][i] == 255 and sum_pix != 0:
                cols[i].append(sum_pix)
                sum_pix = 0
            elif pixels[j][i] != 255:
                sum_pix += 1
        if sum_pix != 0:
            cols[i].append(sum_pix)
    r_and_c = (rows, cols)
    return r_and_c


def save_nonotuple_to_file(img, r_and_c, file):
    """Saving a number of black pixels from rows and columns to a file"""
    nono = open(file, "w")
    nono.write(f"{img.height} {img.width}\n")
    for r_c in r_and_c:
        for line in r_c:
            if len(line) == 0:
                nono.write("0")
            for numb in line:
                nono.write(f"{numb} ")
            nono.write("\n")
    nono.close()


def div_five(a_1):
    """Returns a number rounded to 5"""
    if a_1 % 5 <= 2:
        a_1 = a_1 - (a_1 % 5)
    else:
        a_1 = a_1 + (5 - (a_1 % 5))
    return a_1


def w_h(width, height, size):
    """Scaling the picture"""
    print("Dimensions:", width, height)
    if width < height:
        m_1 = size
        n_1 = int((m_1 * height) / width)
        n_1 = 5 * round(n_1 / 5)

    else:
        n_1 = size
        m_1 = int((n_1 * width) / height)
        m_1 = 5 * round(m_1 / 5)
    print("Board Dimensions", m_1, n_1)
    return m_1, n_1


IMG_SIZE = 20
IMAGE_NAME = "palma.png"
converted = convert_img(IMAGE_NAME, IMG_SIZE, 160)
converted.show()
nonotuple = columns_and_rows(converted)
save_nonotuple_to_file(converted, nonotuple, "nono_board.txt")
solution = create_solution(converted)
