"""
    Module for creating player animations and effects
    author: Joshua Akangah
    date: 10/9/20
"""
from CONFIG.settings import *

class Animation:
    """
    Class animation
    """
    def __init__(self, sprites, scale, frame_duration=0.1):
        """
        __init__ method of animation class
        :param sprites: A list of all images to be included in the animation
        eg. ['assets/player/Move1.png', 'assets/player/Move2.png', 'assets/player/Move3.png']
        :param frame_duration: The amount of time (in seconds) between each frame.  By default it is set to 0.1
        :param scale: Scale factor to use to scale sprites
        eg. A scale of 0.5 scales the image to half its size
        The full path of the sprites have to be included in the string
        """
        self.images = []
        for i in sprites:
            image = pygame.image.load(i).convert_alpha()
            images = pygame.transform.scale(image, (int(image.get_rect().width * scale), int(image.get_rect().height * scale)))
            self.images.append(images)
        self.animation_time = frame_duration
        self.current_time = 0
        self.animation_frames = len(self.images)
        self.current_frame = 0
        self.index = 0
        self.alpha = 255
        self.blink_speed = 1 # constant fade speed

    def animate(self, dt, hold=False):
        """
        Method to update sprites to make an animation
        :param dt: deltatime to update animaton from
        :return: None
        """
        if not hold:
            # only update the animation when not holding
            self.current_time += dt

            if self.current_time >= self.animation_time*FPS:
                self.current_time = 0
                self.index = (self.index + 1) % len(self.images)
                self.image = self.images[self.index]

    def reset_animation(self):
        self.current_frame = 0

    def get_current_image(self):
        """
        Method to return the current image in the animation
        This method can be particularly useful when you want to end an animation when the last image of an animation is reached
        :return: pygame.image
        """
        return self.images[self.index]

    def get_current_rect(self):
        return self.get_current_image().get_rect()

    def is_last_image(self):
        """
        Method to check is if current image is the last in the list
        This method is helpful when using explosion animations to prevent the animation from repeating
        when the last image is reached
        :return: bool
        """

        return self.images.index(self.get_current_image()) == len(self.images) - 1

    def blink(self, display, N):
        """
        Animation to make player sprite blink N times
        """
        tempBG = pygame.Surface((self.get_current_rect().width, self.get_current_rect().height)).convert()
        tempBG.blit(display, (-x, -y))
        tempBG.blit(self.get_current_image(), (0, 0))
        while N != 0:
            if self.alpha > 0:
                tempBG.set_alpha(self.alpha)
                self.alpha -= self.blink_speed
                # handle blit
                # display.blit(tempBG, (x, y))
            elif self.alpha < 255:
                # wont work now
                tempBG.set_alpha(self.alpha)
                self.alpha += self.blink_speed
                # handle blit
            N -= 1

    def __str__(self):
        return f'{self.images}'
