import pygame,functions
WIDE, HIGH = 1080, 720
screen = pygame.display.set_mode((WIDE, HIGH))
clock = pygame.time.Clock()
max_tps = 60.0
display_color = functions.hex_to_rgb("#263238")
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
    def costam(self):
        cos = self.rect
        return cos      
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
    speed = 5
    click_time = 0
    move_duration = 2000
    rect = button_cre.costam()
    x = rect[0]
    y = rect[1]
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
                click_time = pygame.time.get_ticks()
        time_sice
        button_cre.draw_if()
        # Ticking
        delta += clock.tick() / 1000.0
        while delta > 1 / max_tps:
            delta -= 1 / max_tps
        pygame.display.flip()
    pygame.quit()
if __name__ == "__main__":
    main()