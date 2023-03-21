#Amelia Wilson
#tp4: intro arcade EXERCICE1

import arcade
import random

SCREEN_WIDTH = 800
SCREEN_HEIGHT = 600

COLORS = [arcade.color.BLUE, arcade.color.RED, arcade.color.ORANGE, arcade.color.YELLOW, arcade.color.GREEN, arcade.color.ROYAL_PURPLE, arcade.color.MAGENTA]

class Balle():
    def __init__(self, r,x,y,c):
        self.rayon = r
        self.centre_x = x
        self.centre_y = y
        self.color = (c)

    def draw(self):
        #paramètres du cercle(centre(axe des x), centre(axe des y), rayon, couleur)
        arcade.draw_circle_filled(self.centre_x, self.centre_y, self.rayon, self.color)

class Rectangle():
    def __init__(self, x,y,c):
        self.centre_x = x
        self.centre_y = y
        self.color = c
        self.width = random.randint(10, 30)
        self.height = random.randint(10, 30)
        self.color = COLORS
        self.tilt_angle = 0

    def draw(self):
        #paramètres du rectangle(centre(axe des x), centre(axe des y), longueur, largeur, angle d'inclinaison, couleur)
        arcade.draw_rectangle_filled(self.centre_x, self.centre_y, self.width, self.height, self.color, self.tilt_angle)


class MyGame(arcade.Window):
    #ouverture de la fenêtre + nom: exercice 1
    def __init__(self):
        super().__init__(SCREEN_WIDTH, SCREEN_HEIGHT, "Exercice #1")
        self.liste_cercles = []
        self.liste_rectangle = []



    def setup(self):
        # remplir la fenêtre avec 20 cercles(position et couleur aléatoire)
        for _ in range(0):
            rayon = random.randint(10, 30)
            center_x = random.randint(0 + rayon, SCREEN_WIDTH - rayon)
            center_y = random.randint(0 + rayon, SCREEN_HEIGHT - rayon)
            color = random.choice(COLORS)
            cercle= Balle(rayon, center_x, center_y, color)
            self.liste_cercles.append(cercle)

    def draw(self):
        # remplir la fenêtre avec 20 cercles(position et couleur aléatoire)
        for _ in range(1):
            center_x = random.randint(0 + random.randint(SCREEN_WIDTH) - width)
            center_y = random.randint(0 + random.randint(SCREEN_HEIGHT) - height)
            color = random.choice(COLORS)
            rectangle = Rectangle(center_x, center_y, color)
            self.liste_rectangle.append(rectangle)

    def on_draw(self):
        #dessine le cerle lorsque la fenêtre est ouverte
        arcade.start_render()

        for cercle in self.liste_cercles:
            cercle.draw()
        for rectangle in self.liste_rectangle:
            rectangle.draw()

    def on_mouse_press(self, x: int, y: int , button: int, modifiers: int):
        if button == arcade.MOUSE_BUTTON_LEFT:
            for rectangle in self.liste_rectangle:
                self.liste_rectangle.append(rectangle)

        elif button == arcade.MOUSE_BUTTON_RIGHT:
            #si le bouton droite de la souris est cliqué, la couleur du cercle cliqué est changée à une nouvelle couleure aléatoire
            for cercle in self.liste_cercles:
                self.liste_cercles.append(cercle)



def main():
    my_game = MyGame()
    my_game.setup()

    arcade.run()


main()
