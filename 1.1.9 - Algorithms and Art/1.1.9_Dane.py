import turtle as trtl





#make the clock (hour_hand size=(3,3))
trtl.speed(0)
trtl.penup()
trtl.goto(-200,100)
trtl.pendown()
trtl.circle(100)

#Hours

#12
trtl.penup()
trtl.goto(-210,280)
trtl.left(90)
trtl.pendown()
trtl.forward(10)
trtl.penup()
trtl.right(90)
trtl.forward(5)
trtl.pendown()
trtl.forward(5)
trtl.right(60)
trtl.forward(2)
trtl.right(60)
trtl.forward(9)
trtl.left(120)
trtl.forward(5)
trtl.penup()
###############


#1
trtl.goto(-160,270)
trtl.left(90)
trtl.pendown()
trtl.forward(14)
trtl.penup()
###############

#2
trtl.goto(-130,250)
trtl.pendown()
trtl.right(90)
trtl.forward(5)
trtl.right(60)
trtl.forward(2)
trtl.right(60)
trtl.forward(9)
trtl.left(120)
trtl.forward(5)
trtl.penup()
################

#3
trtl.goto(-110,200)
trtl.pendown()
trtl.forward(3)
trtl.right(30)
trtl.forward(3)
trtl.right(90)
trtl.forward(3)
trtl.left(90)
trtl.forward(3)
trtl.right(90)
trtl.forward(3)
trtl.right(30)
trtl.forward(2)
trtl.right(30)
trtl.forward(2.5)
trtl.penup()
################

#4
trtl.goto(-125,160)
trtl.pendown()
trtl.left(90)
trtl.forward(5)
trtl.left(90)
trtl.forward(5)
trtl.left(90)
trtl.forward(5)
trtl.back(10)
trtl.penup()
################

#5

trtl.goto(-150,130)
trtl.pendown()
trtl.left(90)
trtl.forward(3)
trtl.left(90)
trtl.forward(5)
trtl.left(90)
trtl.circle(-2.5,180)
trtl.penup()
#################

#6
trtl.goto(-200,115)
trtl.pendown()
trtl.circle(5,180)
trtl.circle(2)
trtl.penup()
#################

#7
trtl.goto(-250,130)
trtl.pendown()
trtl.forward(5)
trtl.right(110)
trtl.forward(8)
trtl.penup()
#################

#8
trtl.goto(-280,155)
trtl.left(110)
trtl.pendown()
trtl.circle(3)
trtl.circle(-3)
trtl.penup()
#################

#9
trtl.goto(-290,195)
trtl.right(90)
trtl.pendown()
trtl.circle(-3)
trtl.forward(9)
trtl.penup()
#################

#10
trtl.goto(-280,250)
trtl.pendown()
trtl.forward(10)
trtl.penup()
trtl.left(90)
trtl.forward(8)
trtl.pendown()
trtl.circle(5)
trtl.penup()
#################

#11
trtl.goto(-250,280)
trtl.pendown()
trtl.right(90)
trtl.forward(8)
trtl.penup()
trtl.left(90)
trtl.forward(5)
trtl.left(90)
trtl.pendown()
trtl.forward(8)
trtl.penup()
trtl.goto(1000,1000)


#make lists for the time and different times of day
time_day=["1","2","3","4","5","6",",7","8","9","10","11","12","13","14","15","16","16","17","18","19","20","21","22","23","24"]

sun=["sun_up","sun_half","sun_down"]



#make new shape for hour hand
trtl.addshape("hour_hand",((-1,-12),(1,-12),(1,4),(3,4),(0,8),(-3,4),(-1,4),(-1,-12)))


#ask what time they want(1-24)

hour_hand = trtl.Turtle(shape="hour_hand")
hour_hand.turtlesize(3,3)



for time in time_day:
    time_input = int(trtl.textinput("What time of day is it", "What time is it?"))
    print(time_day)


#make it start at that time of day and go through a full day to where you started



wn = trtl.Screen()
wn.mainloop()