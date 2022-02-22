import turtle

wn = turtle.Screen()
wn.title("Animation demo")
wn.bgcolor("black")

class Player(turtle.Turtle):
    def __init__(self):
        turtle.Turtle.__init__(self)
        self.penup()
        self.shape("square")
        self.color("green")
        self.frame = 0

    def animate(self):
        if self.frame == 0:
          self.shape("circle")
          self.frame = 1
        elif self.frame == 1:
            self.shape("square")
            self.frame = 0

        wn.ontimer(self.animate, 500)

player = Player()
player.animate()

player2 = Player()
player2.goto(0,100)
player2.animate()

while True:
    wn.update()
    

wn.mainloop()