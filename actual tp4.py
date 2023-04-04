#Amelia Wilson 401
#tp4

import arcade
import random

SCREEN_WIDTH = 800
SCREEN_HEIGHT = 600

COLORS = [arcade.color.BLUE, arcade.color.RED, arcade.color.ORANGE, arcade.color.YELLOW, arcade.color.GREEN, arcade.color.ROYAL_PURPLE, arcade.color.MAGENTA]

class Cercle():
    def __init__(self, r, x, y, v_x, v_y, c):
        self.rayon = r
        self.centre_x = x
        self.centre_y = y
        self.change_x = v_x
        self.change_y = v_y
        self.color = (c)

    # définir la manière de déplacment d'un cercle et ce qui arrive si il entre en collision avec la bordure de la fenêtre(il "rebondit")
    def on_update(self):
        self.centre_x += self.change_x
        self.centre_y += self.change_y

        if self.centre_x < self.rayon:
            self.change_x *= -1

        if self.centre_x > SCREEN_WIDTH - self.rayon:
            self.change_x *= -1

        if self.centre_y < self.rayon:
            self.change_y *= -1

        if self.centre_y > SCREEN_HEIGHT - self.rayon:
            self.change_y *= -1

    def draw(self):
        #paramètres du cercle(centre(axe des x), centre(axe des y), rayon, couleur)
        arcade.draw_circle_filled(self.centre_x, self.centre_y, self.rayon, self.color)


class Rectangle():

    def __init__(self, h, w, x,y, vx, vy,c):
        self.centre_x = x
        self.centre_y = y
        self.change_x = vx
        self.change_y = vy
        self.width = w
        self.height = h
        self.color = c
        self.tilt_angle = 0

    #définir la manière de déplacment d'un rectangle et ce qui arrive si il entre en collision avec la bordure de la fenêtre(il "rebondit")
    def on_update(self):
        self.centre_x += self.change_x
        self.centre_y += self.change_y

        if self.centre_x < self.width:
            self.change_x *= -1

        if self.centre_x > SCREEN_WIDTH - self.width:
            self.change_x *= -1

        if self.centre_y < self.height:
            self.change_y *= -1

        if self.centre_y > SCREEN_HEIGHT - self.height:
            self.change_y *= -1

    def draw(self):
        #paramètres du rectangle(centre(axe des x), centre(axe des y), longueur, largeur, angle d'inclinaison, couleur)
        arcade.draw_rectangle_filled(self.centre_x, self.centre_y, self.width, self.height, self.color, self.tilt_angle)

class MyGame(arcade.Window):
    #ouverture de la fenêtre + nom: exercice 1
    def __init__(self):
        super().__init__(SCREEN_WIDTH, SCREEN_HEIGHT, "Exercice #1")
        #inclu\affiche: les cercles et les rectangles + leurs propriétés
        self.liste_rectangle = []
        self.liste_cercles = []

    # dessiner les rectangles et les cercles
    def on_draw(self):

        arcade.start_render()
        for rectangle in self.liste_rectangle:
            rectangle.draw()
        for cercle in self.liste_cercles:
            cercle.draw()

    # définition du déplacement cu rectangle et du cercle
    def on_update(self, delta_time: float):

        arcade.start_render()
        for rectangle in self.liste_rectangle:
            rectangle.on_update()
        for cercle in self.liste_cercles:
            cercle.on_update()

#crée des rectangles et des cercles à l'endroit que l'on a cliqué
    def on_mouse_press(self, x: int, y: int, button: int, modifiers: int):
        #bouton droit = rectangle
        if button == arcade.MOUSE_BUTTON_RIGHT:
            height = random.randint(15, 50)
            width = random.randint(15, 50)
            change_x = random.randint(1, 10)
            change_y = random.randint(1, 10)
            color = random.choice(COLORS)
            rectangle = Rectangle(height, width, x, y, change_x, change_y, color)
            self.liste_rectangle.append(rectangle)

        #bouton gauche = cercle
        if button == arcade.MOUSE_BUTTON_LEFT:
            rayon = random.randint(15, 50)
            change_x = random.randint(1, 10)
            change_y = random.randint(1, 10)
            color = random.choice(COLORS)
            cercle = Cercle(rayon, x, y, change_x, change_y, color)
            self.liste_cercles.append(cercle)
def main():
    my_game = MyGame()
    arcade.run()


main()
