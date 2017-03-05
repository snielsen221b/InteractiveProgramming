import pygame
import time
pygame.init()


class Text:

    def __init__(self, text=''):
        self.gameDisplay = pygame.display.set_mode((800, 600))
        self.text = text
        self.black = (0, 0, 0)
        self.white = (255, 255, 255)
        self.red = (255, 0, 0)

    def message(self, font):
        textSurface = font.render(self.text, True, self.white)
        return textSurface, textSurface.get_rect()

    def message_display(self):
        """
        x = 0, y = 0
        largeText = pygame.font.SysFont("monospace", 15)
        label = font.render("text", 1, color)
        screen.blit(label, (x,y))
        """
        largeText = pygame.font.SysFont("monospace", 20)
        TextSurf, TextRect = self.message(largeText)
        self.gameDisplay.blit(TextSurf, TextRect)
        pygame.display.update()
        time.sleep(2)



class Game:
    def __init__(self):
        self.clock = pygame.time.Clock()
        self.crashed = False

    def window(self):

        pygame.display.set_caption('Here be a riddle')
        riddle = Text("What word becomes shorter when you add two letters to it?")
        #Ans = short
        riddle.message_display()

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
