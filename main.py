#Amelia Wilson
#tp4: intro arcade

import arcade
import random

SCREEN_WIDTH = 800
SCREEN_HEIGHT = 600

COLORS = [arcade.color.BLUE, arcade.color.FANDANGO_PINK,
         arcade.color.FRENCH_ROSE, arcade.color.GOLDEN_POPPY]

class Cercle():
   def __init__(self):
       self.rayon = 90
       self.centre_x = 500
       self.centre_y = 400
       self.color = (155, 150, 225)

   def draw(self):
       #arcade.draw_circle_filled(center_x, center_y, rayon, color)
       pass


class MyGame(arcade.Window):
   def __init__(self):
       super().__init__(SCREEN_WIDTH, SCREEN_HEIGHT, "Exercice #1")
       self.liste_cercles = []

   def setup(self):
       # remplir la liste avec 20 objets de type Cercle
       for _ in range(20):
           rayon = random.randint(10, 50)
           center_x = random.randint(90 + rayon, SCREEN_WIDTH - rayon)
           center_y = random.randint(90 + rayon, SCREEN_HEIGHT - rayon)
           color = random.choice(COLORS)

   def on_draw(self):
       arcade.start_render()

       for cercle in self.liste_cercles:
           cercle.draw()


def main():
   my_game = MyGame()
   my_game.setup()

   arcade.run()


main()
