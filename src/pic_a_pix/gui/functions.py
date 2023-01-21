from PIL import ImageColor
import pygame

# Changing color
def hex_to_rgb(hex):
    rgb = ImageColor.getcolor(hex, "RGB")
    return rgb


# Checking if buttom clicked
def check_if_clicked(mouse_pos, box_pos):
    if mouse_pos[0] >= box_pos[0] and mouse_pos[0] <= box_pos[0] + box_pos[2]:
        if mouse_pos[1] >= box_pos[1] and mouse_pos[1] <= box_pos[0] + box_pos[2]:
            return True
