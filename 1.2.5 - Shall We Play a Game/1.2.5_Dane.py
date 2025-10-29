import turtle as trtl
import random as rand


#Setup
wn = trtl.Screen()

plus = trtl.Turtle()
plus.speed(0)

user_trtl = trtl.Turtle(shape="circle")
user_trtl.penup()

current_direction = ""

arrow = trtl.Turtle(shape="arrow")
arrow.hideturtle()
arrow.penup()


middle=(0,0)
top=(0,50)
right=(50,0)
bottom=(0,-50)
left=(-50,0)





#area for movement of user

plus.penup()
plus.goto(-25,75)
plus.pendown()
for area in range(4):
  plus.forward(50)
  plus.right(90)
  plus.forward(50)
  plus.left(90)
  plus.forward(50)
  plus.right(90)
plus.hideturtle()

#User Movement




#make trtl move freely when ine middle
def check_key(key):
  wn.tracer(True)
  if user_trtl.pos() == middle:
    if key == "Up":
      user_trtl.goto(user_trtl.xcor(), user_trtl.ycor()+50)
    if key == "Right":
      user_trtl.goto(user_trtl.xcor()+50, user_trtl.ycor())
    if key == "Down":
      user_trtl.goto(user_trtl.xcor(), user_trtl.ycor()-50)
    if key == "Left":
      user_trtl.goto(user_trtl.xcor()-50, user_trtl.ycor())
#restrict that movement everywhere else
  if user_trtl.pos() == top:
    if key == "Down":
      user_trtl.goto(user_trtl.xcor(), user_trtl.ycor()-50)
  if user_trtl.pos() == bottom:
    if key == "Up":
      user_trtl.goto(user_trtl.xcor(), user_trtl.ycor()+50)
  if user_trtl.pos() == right:
    if key == "Left":
      user_trtl.goto(user_trtl.xcor()-50, user_trtl.ycor())
  if user_trtl.pos() == left:
    if key == "Right":
      user_trtl.goto(user_trtl.xcor()+50, user_trtl.ycor())

wn.listen()

for key_press in {"Up", "Down", "Left", "Right"}: 
  wn.onkeypress(lambda l=key_press: check_key(l), key_press)


#Random Objects

arrow_direction = []

rand_list = ["arrow_right", "arrow_top", "arrow_left", "arrow_bottom"]

def arrow_right():
  arrow.goto(300,0)
  arrow.showturtle()
  arrow.setheading(180)

def arrow_left():
  arrow.goto(-300,0)
  arrow.showturtle()
  arrow.setheading(0)

def arrow_top():
  arrow.goto(0,300)
  arrow.showturtle()
  arrow.setheading(270)

def arrow_bottom():
  arrow.goto(0,-300)
  arrow.showturtle()
  arrow.setheading(90)




#Score



#Win/Loss Screen


wn = trtl.Screen()
wn.mainloop()