from PIL import ImageColor
from tkinter import filedialog
from pic_a_pix import k4sia_image
import pygame

IMG_EXTS = r"*.png; *.jpg"

# Changing color
def hex_to_rgb(hex_color):
    rgb = ImageColor.getcolor(hex_color, "RGB")
    return rgb

# Checking if buttom clicked
def check_if_clicked(mouse_pos, box_pos):

    if mouse_pos[0] >= box_pos[0] and mouse_pos[0] <= box_pos[0] + box_pos[2]:
        if mouse_pos[1] >= box_pos[1] and mouse_pos[1] <= box_pos[0] + box_pos[2]:
            return True
# Checking if solution is correct
def check_solution(correct_arr, to_check_arr):
    n = len(correct_arr)
    for i in range(n):
        m = len(correct_arr[i])
        for j in range(m):
            if correct_arr[i][j] != to_check_arr[i][j]:
                return 0
    return 1

#Get file's path
def file_open():
    path = filedialog.askopenfile(title = "Select a File",
                                  filetypes=(".png, .jpg", IMG_EXTS))

    return path

#Test file_open function
p = file_open()
(k4sia_image.convert_img(p.name, 40, 90)).show()