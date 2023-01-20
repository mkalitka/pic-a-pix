import pygame , functions
max_tps = 60.0

WIDE , HIGH  = 1080 , 720
screen = pygame.display.set_mode((WIDE,HIGH))
display_color = functions.hex_to_rgb("#263238")

pygame.display.set_caption("Pic-a-Pix")

clock = pygame.time.Clock()
TPImage = pygame.image.load("/home/mikol/Downloads/324977038_699397155072774_590940961041445160_n.png").convert()
class BUTTON:
    def __init__(self,color, position):
        self.color = functions.hex_to_rgb(color)
        self.position = position
    def BOX(self):
        obj_lenght = HIGH * 0.32
        heigh_obj =  HIGH * 0.5 - obj_lenght/2
        width_obj =  WIDE * self.position - obj_lenght/2
        box = pygame.Rect(width_obj,heigh_obj,obj_lenght,obj_lenght)
        pygame.draw.rect(screen,self.color, box)
        return (box)
# class Window:
#     def __int__(self, win):
#         self.win = win
#     def
def main():
    global box, display_color
    run = True
    delta = 0.0
    clicked = False
    in_pos_1,in_pos_2,in_pos_3 = False,False,False
    while run:
        #Initialization
        pygame.init()

        # Drawing
        screen.fill(display_color)
        # Drawing object
        if clicked == False:
            # BOX_1
            box = BUTTON("#1261B0", 0.5).BOX()
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                run = False
            elif event.type == pygame.MOUSEBUTTONDOWN:
                mouse_pos = pygame.mouse.get_pos()
                if functions.check_if_clicked(mouse_pos , box):
                    clicked = True


        #image
        # screen.blit(TPImage, (100, 200))
        #Ticking
        delta += clock.tick()/1000.0
        while delta > 1/max_tps:
            delta -= 1/max_tps
        pygame.display.flip()
    pygame.quit()
if __name__ == "__main__":
    main()