import pygame
import time
pygame.init()


class Text:

    """
        This class makes text in the window. It is called in the Game class.
        It can refer to text within the buttons or above them.
    """
    def __init__(self, text='', color=(255, 255, 255)):
        # takes in text and color from Game class
        self.text = text
        self.color = color

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
        time.sleep(0.5) # How long game pauses before next step (buttons) appear


class Button:
    """
    This defines the buttons that appear in the game. The buttons are called in
    the Game cass and take in the button sizes, color, and color the button
    changes to when the mouse hovers over it.
    """
    def __init__(self, size=(150, 450, 100, 50), color=(200, 0, 0), color_bright=(255, 0, 0)):
        # initial values are defined in case the program doesn't. These values
        # are updated from the Gane class with self.size = size, etc.
        self.size = size
        self.color = color
        self.color_bright = color_bright

    def make_rectangle(self, gameDisplay):
        # Draws the rectangle that defines the button with a color and size
        # pulled from itself.
        #mouse = pygame.house.get_pos()
        #if 100+200 > mouse[0] > 100 and 200+350 > mouse[1] > 350:
        #    pygame.draw.rect(gameDisplay, self.color_bright, self.size)
        #else:
            pygame.draw.rect(gameDisplay, self.color, self.size)


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
        # In this function a window opens with text and a button. You solve the
        # riddle in the text to choose the correct button which frees you from
        # the room.
        pygame.display.set_caption('Escape the Softdes Room')
        riddle = Text("What word becomes shorter when you add two letters to it?", self.white)
        # Ans = short
        riddle.message_display(self.gameDisplay)

        button1 = Button(size=(100, 200, 200, 350), color=(self.mystery), color_bright=(self.bright_mystery))
        button1.make_rectangle(self.gameDisplay)

        # caption1 = Text("Short", self.white)
        # caption1.message_display(self.gameDisplay)

        button2 = Button(size=(500, 200, 200, 350), color=(self.mystery2))
        button2.make_rectangle(self.gameDisplay)

        while not self.crashed:

            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    self.crashed = True

                print(event)

            pygame.display.update()
            self.clock.tick(60)

        pygame.quit()
        quit()


if __name__ == '__main__':
    potatotester = Game()
    potatotester.window()
