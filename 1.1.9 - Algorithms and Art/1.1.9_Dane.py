import turtle as trtl



#make new shape for hour hand
trtl.addshape("hour_hand",((-1,-12),(1,-12),(1,4),(3,4),(0,8),(-3,4),(-1,4),(-1,-12)))


#make lists for the time and different times of day






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
trtl.forward(5)
trtl.right(60)
trtl.forward(2)
trtl.right(60)
trtl.forward(9)
trtl.left(120)
trtl.forward(5)
trtl.penup()


#ask what time they want(1-24)
time_start = int(trtl.textinput("What time of day is it", "What time is it?"))
hour_hand = trtl.Turtle(shape="hour_hand")
hour_hand.turtlesize(3,3)



#make it start at that time of day and go through a full day to where you started



wn = trtl.Screen()
wn.mainloop()