#Amelia Wilson
#tp4: intro arcade EXERCICE1

import arcade
import random

SCREEN_WIDTH = 800
SCREEN_HEIGHT = 600

COLORS = [arcade.color.BLUE, arcade.color.RED, arcade.color.ORANGE, arcade.color.YELLOW, arcade.color.GREEN, arcade.color.ROYAL_PURPLE, arcade.color.MAGENTA]

class Cercle():
    def __init__(self, r,x,y,c):
        self.rayon = r
        self.centre_x = x
        self.centre_y = y
        self.color = (c)

    def draw(self):
        #paramètres du cercle(centre(axe des x), centre(axe des y), rayon, couleur)
        arcade.draw_circle_filled(self.centre_x, self.centre_y, self.rayon, self.color)


class MyGame(arcade.Window):
    #ouverture de la fenêtre + nom: exercice 1
    def __init__(self):
        super().__init__(SCREEN_WIDTH, SCREEN_HEIGHT, "Exercice #1")
        self.liste_cercles = []



    def setup(self):
        # remplir la fenêtre avec 20 cercles(position et couleur aléatoire)
        for _ in range(20):
            rayon = random.randint(20, 40)
            center_x = random.randint(0 + rayon, SCREEN_WIDTH - rayon)
            center_y = random.randint(0 + rayon, SCREEN_HEIGHT - rayon)
            color = random.choice(COLORS)
            cercle= Cercle(rayon, center_x, center_y, color)
            self.liste_cercles.append(cercle)

    def on_draw(self):
        #dessine le cerle lorsque la fenêtre est ouverte
        arcade.start_render()

        for cercle in self.liste_cercles:
            cercle.draw()

    def on_mouse_press(self, x: int, y: int , button: int, modifiers: int):
        if button == arcade.MOUSE_BUTTON_LEFT:
            #si le bouton gauche de la souris est cliqué, le cercle cliqué est effacé
            for cercle in self.liste_cercles:
                if x < cercle.centre_x + cercle.rayon and cercle.centre_x - cercle.rayon < x and y < cercle.centre_y + cercle.rayon:
                    self.liste_cercles.remove(cercle)

        elif button == arcade.MOUSE_BUTTON_RIGHT:
            #si le bouton droite de la souris est cliqué, la couleur du cercle cliqué est changée à une nouvelle couleure aléatoire
            for cercle in self.liste_cercles:
                if x < cercle.centre_x + cercle.rayon and cercle.centre_x - cercle.rayon < x and y < cercle.centre_y + cercle.rayon:

                    cercle.colour = random.choice(COLOURS)



def main():
    my_game = MyGame()
    my_game.setup()

    arcade.run()


main()
