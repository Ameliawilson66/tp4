#Amelia Wilson
#tp4: intro arcade EXERCICE1

import arcade
import random

SCREEN_WIDTH = 800
SCREEN_HEIGHT = 600

COLORS = [arcade.color.BLUE, arcade.color.RED, arcade.color.ORANGE, arcade.color.YELLOW, arcade.color.GREEN, arcade.color.ROYAL_PURPLE, arcade.color.MAGENTA]

class Rectangle():
    def __init__(self, x,y,c, w, h):
        self.centre_x = x
        self.centre_y = y
        self.width = w
        self.height = h
        self.color = c
        self.tilt_angle = 0

    def draw(self):
        #paramètres du rectangle(centre(axe des x), centre(axe des y), longueur, largeur, angle d'inclinaison, couleur)
        arcade.draw_rectangle_filled(self.centre_x, self.centre_y, self.width, self.height, self.color, self.tilt_angle)


class MyGame(arcade.Window):
    #ouverture de la fenêtre + nom: exercice 1
    def __init__(self):
        super().__init__(SCREEN_WIDTH, SCREEN_HEIGHT, "Exercice #1")
        self.liste_rectangle = []

    def draw(self):
        # remplir la fenêtre avec 20 cercles(position et couleur aléatoire)
        for _ in range(1):
            center_x = random.randint(0 + random.randint(SCREEN_WIDTH))
            center_y = random.randint(0 + random.randint(SCREEN_HEIGHT))
            color = random.choice(COLORS)
            rectangle = Rectangle(center_x, center_y, color)
            self.liste_rectangle.append(rectangle)

    def on_draw(self):
        #dessine le cerle lorsque la fenêtre est ouverte
        arcade.start_render()
        for rectangle in self.liste_rectangle:
            rectangle.draw()

    def on_mouse_press(self, x: int, y: int , button: int, modifiers: int):
        if button == arcade.MOUSE_BUTTON_RIGHT:
            for rectangle in self.liste_rectangle:
                self.liste_rectangle.append(rectangle)

        elif button == arcade.MOUSE_BUTTON_RIGHT:
            #si le bouton droite de la souris est cliqué, la couleur du cercle cliqué est changée à une nouvelle couleure aléatoire
            for cercle in self.liste_cercles:
                self.liste_cercles.append(cercle)



def main():
    my_game = MyGame()

    arcade.run()


main()
