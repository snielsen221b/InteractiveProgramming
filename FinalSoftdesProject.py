import pygame
import time
pygame.init()


class Text:

    """
        This class makes text in the window. It is called in the Game class.
        It can refer to text within the buttons or above them.
    """
    def __init__(self, text='', color=(255, 255, 255), size=(150, 450, 100, 50)):
        # takes in text and color from Game class
        self.text = text
        self.color = color
        self.size = size
        self.clock = pygame.time.Clock()

    def message(self, font):
        # Defines the surface the text is written on.
        textSurface = font.render(self.text, True, self.color)
        return textSurface, textSurface.get_rect()

    def message_display(self, gameDisplay):
        # Displays message with font, size, text, and then pauses half a sec.
        largeText = pygame.font.SysFont("monospace", 20)
        TextSurf, TextRect = self.message(largeText)
        gameDisplay.blit(TextSurf, TextRect)
        pygame.display.update()
        time.sleep(2)  # How long game pauses before next step appears

    def button_text_display(self, gameDisplay):
        x = self.size[0]
        y = self.size[1]
        w = self.size[2]
        h = self.size[3]
        smallText = pygame.font.SysFont("monospace", 40)
        textSurf, textRect = self.message(smallText)
        textRect.center = (x+(w/2), y+(h/2))
        gameDisplay.blit(textSurf, textRect)
        pygame.display.update()
        # self.clock.tick(1)

class Button:
    """
    This defines the buttons that appear in the game. The buttons are called in
    the Game cass and take in the button sizes, color, and color the button
    changes to when the mouse hovers over it.
    """
    def __init__(self, size=(150, 450, 100, 50), buttontext='', color=(200, 0, 0),
                 color_bright=(255, 0, 0)):
        # initial values are defined in case the program doesn't. These values
        # are updated from the Gane class with self.size = size, etc.
        self.size = size
        self.color = color
        self.white = (255, 255, 255)
        self.gameDisplay = pygame.display.set_mode((800, 600))
        self.color_bright = color_bright
        self.mouse = pygame.mouse.get_pos()
        self.click = pygame.mouse.get_pressed()

    def make_rectangle(self, gameDisplay):
        # Draws the rectangle that defines the button with a color and size
        # pulled from itself.
        x = self.size[0]
        y = self.size[1]
        w = self.size[2]
        h = self.size[3]
        mouse = pygame.mouse.get_pos()
        if x+w > mouse[0] > x and y+h > mouse[1] > y:
            pygame.draw.rect(gameDisplay, self.color_bright, self.size)
        else:
            pygame.draw.rect(gameDisplay, self.color, self.size)

    def button_action(self, gameDisplay, action=None):
        self.click = pygame.mouse.get_pressed()
        mouse = pygame.mouse.get_pos()
        mouse_right_of_left_side = self.size[0] < mouse[0]
        mouse_left_of_right_side = mouse[0] < self.size[0]+self.size[2]
        mouse_in_box_x = mouse_right_of_left_side and mouse_left_of_right_side
        mouse_lower_than_top = mouse[1] > self.size[1]
        mouse_higher_than_bottom = mouse[1] < self.size[1] + self.size[3]
        mouse_in_box_y = mouse_lower_than_top and mouse_higher_than_bottom
        mouse_in_box = mouse_in_box_x and mouse_in_box_y
        if mouse_in_box:
            self.make_rectangle(gameDisplay)
            if self.click[0] == 1 and action is not None:
                action()
        else:
            self.make_rectangle(gameDisplay)

    def congrats(self):
        gameDisplay = pygame.display.set_mode((800, 600))
        caption3 = Text("Congratulations!", self.white, size=(300, 100, 10, 10))
        caption3.button_text_display(gameDisplay)

    def wrong(self):
        gameDisplay = pygame.display.set_mode((800, 600))
        caption4 = Text("Wrong!", self.white, size=(300, 100, 10, 10))
        caption4.button_text_display(gameDisplay)

class Game:
    """
    This is the master class of the Game. All of our other classes are called
    from here. It runs through the different classes in to produce the gameplay
    experience.
    """
    def __init__(self):
        # This is where all the other variables such as color and size that
        # were referenced earlier are defined.
        self.gameDisplay = pygame.display.set_mode((800, 600))
        self.clock = pygame.time.Clock()
        self.crashed = False
        self.black = (0, 0, 0)
        self.white = (255, 255, 255)
        self.red = (255, 0, 0)
        self.green = (0, 255, 0)
        self.blue = (0, 0, 255)
        self.mystery = (65, 7, 100)
        self.bright_mystery = (115, 57, 150)
        self.mystery2 = (0, 230, 100)
        self.bright_mystery2 = (50, 107, 200)

    def window(self):
        # In this function a window opens with text and two buttons. You solve
        # the riddle in the text to choose the correct button which frees you
        # from the room.
        pygame.display.set_caption('Escape the Softdes Room')
        riddle = Text("What word becomes shorter when"
                      " you add two letters to it?", self.white)
        # Ans = short
        riddle.message_display(self.gameDisplay)

        button1 = Button(size=(100, 200, 200, 350), color=(self.mystery),
                         color_bright=(self.red))
        caption1 = Text("Short", self.white, size=(100, 200, 200, 350))
        button2 = Button(size=(500, 200, 200, 350), color=(self.mystery2),
                         color_bright=(self.blue))
        caption2 = Text("Tall", self.white, size=(500, 200, 200, 350))

        while not self.crashed:
            for event in pygame.event.get():
                # print(event)
                if event.type == pygame.QUIT:
                    self.crashed = True
                    pygame.quit()
                    quit()

            button1.button_action(self.gameDisplay, button1.congrats)
            caption1.button_text_display(self.gameDisplay)
            button2.button_action(self.gameDisplay, button2.wrong)
            caption2.button_text_display(self.gameDisplay)

            pygame.display.update()
            self.clock.tick(60)
        pygame.quit()
        quit()


if __name__ == '__main__':
    potatotester = Game()
    potatotester.window()
