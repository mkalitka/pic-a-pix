import pygame
from pic_a_pix import k4sia_image
from pic_a_pix.gui import functions
max_tps = 60.0

WIDE, HIGH = 1080, 720
screen = pygame.display.set_mode((WIDE, HIGH))
display_color = functions.hex_to_rgb("#263238")

pygame.display.set_caption("Pic-a-Pix")

clock = pygame.time.Clock()
class BUTTON:
    def __init__(self, path, x, y, scale):
        self.image = pygame.image.load(path).convert_alpha()
        self.width = self.image.get_width() * scale
        self.heigh = self.image.get_height() * scale
        self.image = pygame.transform.scale(self.image, (int(self.width), int(self.heigh)))
        self.cliked = False
        self.x = x * WIDE - self.width/2
        self.y = y * HIGH - self.heigh/2
        self.rect = pygame.Rect(self.x, self.y,self.width,self.heigh)
    def draw_if(self):
        if self.cliked == False:
            screen.blit(self.image, self.rect)
    def draw_menu(self):
        action = False
        pos = pygame.mouse.get_pos()
        if self.rect.collidepoint(pos):
            action = True
            self.cliked = True
        return action
def main():
    global display_color
    run = True
    delta = 0.0
    button_cre = BUTTON("icons/create.png",0.5,0.75,0.3)
    button_img = BUTTON("icons/from_img.png",0.5,0.4,0.7)
    while run:
        # Initialization
        pygame.init()
        # Drawing
        screen.fill(display_color)
        # Drawing object
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                run = False
            elif event.type == pygame.MOUSEBUTTONDOWN:
                action_cre = button_cre.draw_menu()
                action_img = button_img.draw_menu()
                button_img.cliked = False
                if button_cre.cliked == True:
                    button_img.cliked = True
                if action_img == True:
                    pass
                if action_cre == True:
                    pass
        button_cre.draw_if()
        button_img.draw_if()
        # Ticking
        delta += clock.tick() / 1000.0
        while delta > 1 / max_tps:
            delta -= 1 / max_tps
        pygame.display.flip()
    pygame.quit()
if __name__ == "__main__":
    main()
