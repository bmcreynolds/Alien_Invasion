import pygame.font

class Button:
    '''Create a class to manage all buttons'''

    def __init__(self, ai_game, msg):
        '''Initialize button attributes'''

        self.screen = ai_game.screen
        self.screen_rect = self.screen.get_rect()

        # Set the dimensions and properties of the button
        self.width, self.height = 200, 50
        self.button_color = (0, 255, 0)
        self.text_color = (255, 255,255)
        self.font = pygame.font.SysFont(None, 48)

        # Build the buttons rect and location
        self.rect = pygame.Rect(0, 0, self.width, self.height)
        self.rect.center = self.screen_rect.center

        # Message
        self._prep_message(msg)

    def _prep_message(self, msg):
        '''Turn the desired text into a rendered image and center it the button'''

        # Render image
        self.msg_image = self.font.render(msg, True, self.text_color, self.button_color)

        # Get the Rect dimensions of the freshly rendered image and assign it to a variable
        self.msg_image_rect = self.msg_image.get_rect()

        # Assign the center of the buttons rect to the center of the message image
        self.msg_image_rect.center = self.rect.center

    def draw_button(self):
        '''Draw the actual button and the text'''
        # Add self (the button) to the screen with the specified color and position)
        self.screen.fill(self.button_color, self.rect)
        # Add the text image to the screen in the position
        self.screen.blit(self.msg_image, self.msg_image_rect)