from PIL import ImageColor
from tkinter import filedialog
import pygame

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
            if correct_arr[i][j] != to_check_arr[j][i] and to_check_arr[j][i] != -1:
                return 0

    return 1


# Get file's path
def open_file():
    path = filedialog.askopenfile(
        title="Select a File",
        filetypes=[
            ("All files", IMG_EXTS),
            ("JPEG files", IMG_EXTS),
            ("PNG files", "*.png"),
        ],
    )

    return path


# Test open_file function
# p = open_file()
# (k4sia_image.convert_img(p.name, 1, 90)).show()

# Class for button
class BUTTON:
    def __init__(self, path, x, y, scale, WIDE, HIGH):
        self.image = pygame.image.load(path).convert_alpha()
        self.width = self.image.get_width() * scale
        self.heigh = self.image.get_height() * scale
        self.image = pygame.transform.scale(
            self.image, (int(self.width), int(self.heigh))
        )
        self.cliked = False
        self.x = x * WIDE - self.width / 2
        self.y = y * HIGH - self.heigh / 2
        self.rect = pygame.Rect(self.x, self.y, self.width, self.heigh)
        self.shake_speed = 6
        self.shake_duration = 500  # 0.5 sekundy
        self.click_time = 0
        self.original_x = self.x
        self.HIGH = HIGH
        self.WIDE = WIDE

    def if_cliked(self):
        action = False
        pos = pygame.mouse.get_pos()
        if self.rect.collidepoint(pos):
            action = True
            self.cliked = True
            self.click_time = pygame.time.get_ticks()
        return action

    def update(self, screen, if_correct):
        if self.cliked == True and if_correct == False:
            time_since_click = pygame.time.get_ticks() - self.click_time
            if time_since_click > self.shake_duration:
                self.click_time = 0
                self.cliked = False
                self.rect.x = self.original_x
            else:
                self.rect.x += self.shake_speed
                self.shake_speed = -self.shake_speed
        elif if_correct == True and self.cliked == True:
            win = True
            # font = pygame.font.SysFont('A', 35)
            # text= font.render('X', True, (0,0,0))
            font = pygame.font.Font(None, 36)
            while win:
                for event in pygame.event.get():
                    if event.type == pygame.KEYDOWN:
                        if event.key == pygame.K_ESCAPE:
                            run = False
                            pygame.quit()
                    if event.type == pygame.QUIT:
                        run = False
                        pygame.quit()
                screen.fill((0, 255, 0))
                # screen.blit(text,self.WIDE//2,self.HIGH // 2,1)
                text = font.render("YOU WIN", 1, (0, 0, 0))
                screen.blit(text, (self.WIDE // 2, self.HIGH // 2, 1, 1))
                pygame.display.flip()
        screen.blit(self.image, self.rect)
