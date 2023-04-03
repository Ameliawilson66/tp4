#Amelia Wilson
#tp4: intro arcade EXERCICE1

import arcade
import random

SCREEN_WIDTH = 800
SCREEN_HEIGHT = 600

COLORS = [arcade.color.BLUE, arcade.color.RED, arcade.color.ORANGE, arcade.color.YELLOW, arcade.color.GREEN, arcade.color.ROYAL_PURPLE, arcade.color.MAGENTA]

class Cercle():
    #rayon, x, y, change_x, change_y, color
    def __init__(self, r, x, y, v_x, v_y, c):
        self.rayon = r
        self.centre_x = x
        self.centre_y = y
        self.change_x = v_x
        self.change_y = v_y
        self.color = (c)

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


class MyGame(arcade.Window):
    #ouverture de la fenêtre + nom: exercice 1
    def __init__(self):
        super().__init__(SCREEN_WIDTH, SCREEN_HEIGHT, "Exercice #1")
        self.liste_cercles = []



    def on_draw(self):
        arcade.start_render()
        for cercle in self.liste_cercles:
            cercle.draw()


    def on_update(self, delta_time: float):
        #dessine le cerle lorsque la fenêtre est ouverte
        arcade.start_render()
        for cercle in self.liste_cercles:
            cercle.on_update()

    def on_mouse_press(self, x: int, y: int, button: int, modifiers: int):

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
