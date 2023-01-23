from PIL import ImageColor
from tkinter import filedialog

IMG_EXTS = r"*.png *.jpg *.jpeg *.jfif *.pjpeg *.pjp *.webp"
IMG_JPEG = r"*.jpg *.jpeg *.jfif *.pjpeg *.pjp"

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
            if correct_arr[i][j] != to_check_arr[i][j] and to_check_arr[i][j] != -1:
                return 0
    return 1

#Get file's path
def file_open():
    path = filedialog.askopenfile(title = "Select a File",
                                  filetypes=[("All files", IMG_EXTS),
                                             ("JPEG files", IMG_EXTS),
                                             ("PNG files", "*.png")])
    return path

#Test file_open function
# p = file_open()
# (k4sia_image.convert_img(p.name, 1, 90)).show()
