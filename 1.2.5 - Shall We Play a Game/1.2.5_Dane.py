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

##score
score = 0
score_writer = trtl.Turtle()
score_writer.penup()
score_writer.hideturtle()
score_writer.goto(200,200)
score_writer.write(score, font=("Arial", 45, "bold"))

game_running = True

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

#Start Screen
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

#Definitons

##make trtl move freely when ine middle
def game_over():
  global game_running
  game_running = False
  countdown.goto(-100,100)
  countdown.write("You Lose...", font=("Arial", 45, "bold"))

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

forward_legth =15

def arrow_right():
  arrow.goto(300,0)
  arrow.showturtle()
  arrow.setheading(180)
  for step in range(60):
    if not game_running:
      break
    arrow.forward(forward_legth)
    if arrow.distance(user_trtl) < 40:
      game_over()
      print("you hit the arrow")
      break
    wn.update()
    time.sleep(0.02)
  arrow.hideturtle()

def arrow_left():
  arrow.goto(-300,0)
  arrow.showturtle()
  arrow.setheading(0)
  for step in range(60):
    if not game_running:
      break
    arrow.forward(forward_legth)
    if arrow.distance(user_trtl) < 40:
      game_over()
      print("you hit the arrow")
      break
    wn.update()
    time.sleep(0.02)
  arrow.hideturtle()

def arrow_top():
  arrow.goto(0,300)
  arrow.showturtle()
  arrow.setheading(270)
  for step in range(60):
    if not game_running:
      break
    arrow.forward(forward_legth)
    if arrow.distance(user_trtl) < 40:
      game_over()
      print("you hit the arrow")
      break
    wn.update()
    time.sleep(0.02)
  arrow.hideturtle()

def arrow_bottom():
  arrow.goto(0,-300)
  arrow.showturtle()
  arrow.setheading(90)
  for step in range(60):
    if not game_running:
      break
    arrow.forward(forward_legth)
    if arrow.distance(user_trtl) < 40:
      game_over()
      print("you hit the arrow")
      break
    wn.update()
    time.sleep(0.02)
  arrow.hideturtle()

wn.listen()
#User Movement

for key_press in {"Up", "Down", "Left", "Right"}: 
  wn.onkeypress(lambda l=key_press: check_key(l), key_press)

#Random Object Movement

rand_list = [arrow_right, arrow_top, arrow_left, arrow_bottom]

trtl_distance = user_trtl.distance(arrow)

#rand movement
arrow.speed(10)
for i in range(10):
  if not game_running:
    break
  current_direction = rand.choice(rand_list)
  current_direction()
  if not game_running:
    break
  score+=1
  score_writer.clear()
  score_writer.write(score, font=("Arial", 45, "bold"))
  if arrow.distance(user_trtl) < 40:
    game_over()
if score == 10:
  countdown.write("Faster!!", font=("Arial", 45, "bold"))
  forward_legth += 10
time.sleep(2)
countdown.clear()
arrow.speed(4)
for i in range(10):
  if not game_running:
    break
  current_direction = rand.choice(rand_list)
  current_direction()
  score+=1
  score_writer.clear()
  score_writer.write(score, font=("Arial", 45, "bold"))
  if arrow.distance(user_trtl) < 40:
    game_over()
    break
if score == 20:
  score_writer.goto(-100,100)
  score_writer.write("You Win!!", font=("Arial", 45, "bold"))

wn = trtl.Screen()
wn.mainloop()