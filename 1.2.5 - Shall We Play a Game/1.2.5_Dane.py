import turtle as trtl
import random as rand

#Setup
wn = trtl.Screen()

area = trtl.Turtle()

user_trtl = trtl.Turtle(shape="circle")
user_trtl.penup()


current_direction = ""

arrow = trtl.Turtle(shape="arrow")
arrow.hideturtle()
arrow.penup()
arrow.goto(300,300)

middle=(0,0)
top=(0,50)
right=(50,0)
bottow=(0,-50)
left=(-50,0)


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

wn.listen()

def check_key(key):
  wn.tracer(True)
  if key == "Up":
    user_trtl.goto(user_trtl.xcor(), user_trtl.ycor()+50)
  if key == "Right":
    user_trtl.goto(user_trtl.xcor()+50, user_trtl.ycor())
  if key == "Down":
    user_trtl.goto(user_trtl.xcor(), user_trtl.ycor()-50)
  if key == "Left":
    user_trtl.goto(user_trtl.xcor()-50, user_trtl.ycor())

for key_press in {"Up", "Down", "Left", "Right"}: 
  wn.onkeypress(lambda l=key_press: check_key(l), key_press)

#Random Objects



#Score



#Win/Loss Screen


wn = trtl.Screen()
wn.mainloop()