import turtle as trtl
import random as rand

#Setup
wn = trtl.Screen()

area = trtl.Turtle()



#area for movement of user

area.penup()
area.goto(-25,75)
area.pendown()
for plus in range(4):
  area.forward(50)
  area.right(90)
  area.forward(50)
  area.left(90)
  area.forward(50)
  area.right(90)
area.hideturtle()

#User Movement

def check_key(key):
  wn.tracer(True)


for key_press in {"Up", "Down", "Left", "Right"}: 
  wn.onkeypress(lambda l=key_press: check_key(l), key_press)

#Random Objects



#Score



#Win/Loss Screen


wn = trtl.Screen()
wn.mainloop()