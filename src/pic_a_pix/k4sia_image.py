from typing import List, Tuple

from PIL import Image


def convert_img(img_name: str, size: int, threshold: int) -> Image.Image:
    """Loading the image and converting it"""
    with Image.open(img_name) as img_a:
        width, height = img_a.size
        n_2, m_2 = w_h(width, height, size)
        img_a = img_a.convert("L")
        img_a = img_a.resize((n_2, m_2))
        img_a = img_a.point(lambda p: 255 if p > threshold else 0)
    return img_a


def create_solution(img: Image.Image) -> List[List[int]]:
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


def div_five(a_1: int) -> int:
    """Returns a number rounded to 5"""
    if a_1 % 5 <= 2:
        a_1 = a_1 - (a_1 % 5)
    else:
        a_1 = a_1 + (5 - (a_1 % 5))

    return a_1


def w_h(width: int, height: int, size: int) -> Tuple[int, int]:
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
