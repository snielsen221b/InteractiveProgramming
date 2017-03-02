import pygame
pygame.init()


class Game:
    def __init__(self):
        self.gameDisplay = pygame.display.set_mode((800, 600))
        self.clock = pygame.time.Clock()
        self.crashed = False

    def window(self):

        pygame.display.set_caption('Here be a riddle')

        while not self.crashed:

            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    self.crashed = True

                print(event)

            pygame.display.update()
            self.clock.tick(60)

        pygame.quit()
        quit()

    class Text:

        def __init__(self, text='', font=''):
            self.text = text
            self.font = font
            self.black = (0,0,0)
            self.white = (255,255,255)
            self.red = (255,0,0)

        def message():
            textSurface = font.render(self.text, True, self.black)
            return textSurface, textSurface.get_rect()


if __name__ == '__main__':
    potatotester = Game()
    potatotester.window()
