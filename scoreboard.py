import pygame.font

class Scoreboard:
    '''A class to report scoring information'''

    def __init__(self, ai_game):
        '''Initialize scorekeeping attributes'''
        self.screen = ai_game.screen
        self.screen.rect = self.screen.get_rect()
        self.settings = ai_game.settings
        self.stats = ai_game.stats

        # Set font for scoreboard
        self.text_color = (30, 30, 30)
        self.font = pygame.font.SysFont(None, 48)

        # Prep initial score image
        self.prep_score()

    def prep_score(self):
        pass