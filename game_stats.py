class GameStats:
    '''Track statistics for the whole game and eventually save '''

    def __init__(self, ai_game):
        '''Initialize stats'''

        self.settings = ai_game.settings
        self.reset_stats()

        # Determines if the game is still going or not, changes to false on game over
        self.game_active = True

    def reset_stats(self):
        '''Initialize stats that can be changed during the game'''
        # Adjust the number of ships left based on the ships limit in settings
        self.ships_left = self.settings.ship_limit