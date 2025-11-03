import turtle as trtl
import random as rand
import time

#Setup
wn = trtl.Screen()

plus = trtl.Turtle()
plus.speed(0)

user_trtl = trtl.Turtle(shape="circle")
user_trtl.penup()

trtl.addshape("object_arrow",((-1,-12),(1,-12),(1,4),(3,4),(0,8),(-3,4),(-1,4),(-1,-12)))
arrow = trtl.Turtle(shape="object_arrow")
arrow.hideturtle()
arrow.penup()
arrow.shapesize(3)


middle=(0,0)
top=(0,50)
right=(50,0)
bottom=(0,-50)
left=(-50,0)

countdown = trtl.Turtle()
countdown.hideturtle()


collision_shape = "square"

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

#Win/Loss Screen
countdown.penup()
countdown.goto(-200,100)
countdown.write("Dodge the arrows!!", font=("Arial", 45, "bold"))
time.sleep(1)
countdown.clear()
countdown.goto(-15,100)
countdown.write("3", font=("Arial", 45, "bold"))
time.sleep(1)
countdown.clear()
countdown.write("2", font=("Arial", 45, "bold"))
time.sleep(1)
countdown.clear()
countdown.write("1", font=("Arial", 45, "bold"))
time.sleep(1)
countdown.clear()
countdown.write("GO", font=("Arial", 45, "bold"))
time.sleep(1)
countdown.clear()

#User Movement

##make trtl move freely when ine middle
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
##restrict that movement everywhere else
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
def arrow_right():
  arrow.goto(300,0)
  arrow.showturtle()
  arrow.setheading(180)
  arrow.forward(700)
  arrow.hideturtle()

def arrow_left():
  arrow.goto(-300,0)
  arrow.showturtle()
  arrow.setheading(0)
  arrow.forward(700)
  arrow.hideturtle()


def arrow_top():
  arrow.goto(0,300)
  arrow.showturtle()
  arrow.setheading(270)
  arrow.forward(700)
  arrow.hideturtle()

def arrow_bottom():
  arrow.goto(0,-300)
  arrow.showturtle()
  arrow.setheading(90)
  arrow.forward(700)
  arrow.hideturtle()
 
rand_list = [arrow_right, arrow_top, arrow_left, arrow_bottom]

score = 0
score_writer = trtl.Turtle()
score_writer.penup()
score_writer.hideturtle()
score_writer.goto(200,200)
score_writer.write(score, font=("Arial", 45, "bold"))

for i in range(10):
  current_direction = rand.choice(rand_list)
  current_direction()
  score+=1
  score_writer.clear()
  score_writer.write(score, font=("Arial", 45, "bold"))

countdown.write("Faster!!", font=("Arial", 45, "bold"))
time.sleep()
countdown.clear()
arrow.speed(4)
for i in range(10):
  current_direction = rand.choice(rand_list)
  current_direction()
  score+=1
  score_writer.clear()
  score_writer.write(score, font=("Arial", 45, "bold"))

#collision


pixel_size = 100
if (abs(user_trtl.xcor()-arrow.xcor())< pixel_size):
  if(abs(user_trtl.ycor()-arrow.ycor())<pixel_size):
    print("you hit the arrow")
    arrow.shape(collision_shape)
    user_trtl.shape(collision_shape)
    arrow.fillcolor("red")
    user_trtl.fillcolor("red")








wn = trtl.Screen()
wn.mainloop()