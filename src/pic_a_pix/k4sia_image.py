from typing import List, Tuple
from PIL import Image


def convert_img(img_name: str, lvl: int, threshold: int) -> Image.Image:
    """Loading the image and converting it"""
    with Image.open(img_name) as img_a:
        width, height = img_a.size
        n_2, m_2 = w_h(width, height, lvl)
        img_a = img_a.convert("L")
        img_a = img_a.resize((n_2, m_2))
        img_a = img_a.point(lambda p: 255 if p > threshold else 0)
    return img_a


def create_matrix(img: Image.Image) -> List[List[int]]:
    """Creating a solution array"""
    height = img.height
    width = img.width
    pixels = [[img.getpixel((i, j)) for i in range(width)] for j in range(height)]

    # Replacing pixel values in matrix: 1 - black, 0 - white
    for i in range(height):
        for j in range(width):
            if pixels[i][j] == 255:
                pixels[i][j] = 0
            else:
                pixels[i][j] = 1

    return pixels


def columns_and_rows(img: Image.Image) -> Tuple[List[List[int]], List[List[int]]]:
    """Counts black and white pixels and returns them as rows and columns"""
    n_h = img.height
    m_w = img.width

    pixels = [[img.getpixel((i, j)) for i in range(m_w)] for j in range(n_h)]
    rows, cols = [[] for _ in range(n_h)], [[] for _ in range(m_w)]

    # Counting blocks of black pixels by rows
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

    # Counting blocks of black pixels by columns
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


def w_h(width: int, height: int, lvl: int) -> Tuple[int, int]:
    """Scaling the picture"""
    print("Dimensions:", width, height)
    if lvl == 0:  # easy
        size_w = 10
        size_h = 20
    if lvl == 1:  # medium
        size_w = 15
        size_h = 30
    if lvl == 2:  # hard
        size_w = 20
        size_h = 40

    if width < height:
        n_1 = size_h
        m_1 = int((n_1 * width) / height)
        m_1 = 5 * round(m_1 / 5)
    else:
        m_1 = size_w
        n_1 = int((m_1 * width) / height)
        n_1 = 5 * round(n_1 / 5)
        m_1, n_1 = n_1, m_1

    print("Board Dimensions", m_1, n_1)

    return m_1, n_1
