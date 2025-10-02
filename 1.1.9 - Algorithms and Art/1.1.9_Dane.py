import turtle as trtl

import time

trtl.color("green")

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
hourslist= list(range(1, 25))
sunlist = ["sun rising", "sun up", "sun setting", "sun down"]

sun_state_for_hour = []
for h in hourslist:
    if 6 <= h <= 8:
        sun_state_for_hour.append(sunlist[0])
    elif 9 <= h <= 17:
        sun_state_for_hour.append(sunlist[1])
    elif 18 <= h <= 19:
        sun_state_for_hour.append(sunlist[2])
    else:
        sun_state_for_hour.append(sunlist[3])

sun_positions = [
    -120, -120, -120, -120, -120, -80, -40, 0,   # 1-8
    120, 120, 120, 120, 120, 120, 120, 120, 120, # 9-17
    80, 40, -20, -120, -120, -120, -120, -120    # 18-24
]

#make new shape for hour hand
trtl.addshape("hour_hand",((-1,-12),(1,-12),(1,4),(3,4),(0,8),(-3,4),(-1,4),(-1,-12)))


#ask what time they want(1-24)

hour = trtl.Turtle(shape="hour_hand")
hour.color("green")
hour.penup()
hour.hideturtle()


minute = trtl.Turtle(shape="hour_hand")
minute.penup()
minute.color("green")
minute.hideturtle()
minute.goto(-200,200)
minute.turtlesize(3,4)
minute.left(90)
minute.forward(35)
minute.showturtle()

sun = trtl.Turtle()
sun.shape("circle")
sun.color("yellow")
sun.turtlesize(5,5)
sun.penup()
sun.goto(0, -120)



starthour=int(trtl.textinput("What time", "What time is it(1-12)?"))


hour.turtlesize(3,3)
hour.goto(-200,200)


hourangle=0
wn = trtl.Screen()


#for each number print it from the list
if starthour ==1:
    for i in range(24): 
        hour.setheading(30*-hourangle+60)
        hour.forward(30)
        hour.stamp()
        hour.goto(-200,200)
        time.sleep(2)
        hour.clearstamps()
        hourangle +=1
        real_hour = (starthour + i - 1) % 24
        state = sun_state_for_hour[real_hour]
        sun.goto(0, sun_positions[real_hour])
        if 6 <= real_hour <= 17:    # day hours
            wn.bgcolor("skyblue")
        else:                        # night hours
            wn.bgcolor("black")
        

elif starthour==2:
    for i in range(24): 
        hour.setheading(30*-hourangle+30)
        hour.forward(30)
        hour.stamp()
        hour.goto(-200,200)
        time.sleep(2)
        hour.clear()
        hourangle +=1
        real_hour = (starthour + i - 1) % 24
        sun.goto(-200, sun_positions[real_hour])
        if 6 <= real_hour <= 17:    # day hours
            wn.bgcolor("skyblue")
        else:                        # night hours
            wn.bgcolor("black")
elif starthour==3:
    for i in range(24): 
        hour.setheading(30*-hourangle)
        hour.forward(30)
        hour.stamp()
        hour.goto(-200,200)
        time.sleep(2)
        hour.clear()
        hourangle +=1
        real_hour = (starthour + i - 1) % 24
        sun.goto(0, sun_positions[real_hour])
        if 6 <= real_hour <= 17:    # day hours
            wn.bgcolor("skyblue")
        else:                        # night hours
            wn.bgcolor("black")
elif starthour==4:
    for i in range(24): 
        hour.setheading(30*-hourangle-30)
        hour.forward(30)
        hour.stamp()
        hour.goto(-200,200)
        time.sleep(2)
        hour.clear()
        hourangle +=1
        real_hour = (starthour + i - 1) % 24
        sun.goto(0, sun_positions[real_hour])
        if 6 <= real_hour <= 17:    # day hours
            wn.bgcolor("skyblue")
        else:                        # night hours
            wn.bgcolor("black")
elif starthour==5:
    for i in range(24): 
        hour.setheading(30*-hourangle-60)
        hour.forward(30)
        hour.stamp()
        hour.goto(-200,200)
        time.sleep(2)
        hour.clear()
        hourangle +=1
        real_hour = (starthour + i - 1) % 24
        sun.goto(0, sun_positions[real_hour])
        if 6 <= real_hour <= 17:    # day hours
            wn.bgcolor("skyblue")
        else:                        # night hours
            wn.bgcolor("black")
elif starthour==6:
    for i in range(24): 
        hour.setheading(30*-hourangle-90)
        hour.forward(30)
        hour.stamp()
        hour.goto(-200,200)
        time.sleep(2)
        hour.clear()
        hourangle +=1
        real_hour = (starthour + i - 1) % 24
        sun.goto(0, sun_positions[real_hour])
        if 6 <= real_hour <= 17:    # day hours
            wn.bgcolor("skyblue")
        else:                        # night hours
            wn.bgcolor("black")
elif starthour==7:
    for i in range(24): 
        hour.setheading(30*-hourangle-120)
        hour.forward(30)
        hour.stamp()
        hour.goto(-200,200)
        time.sleep(2)
        hour.clear()
        hourangle +=1
        real_hour = (starthour + i - 1) % 24
        sun.goto(0, sun_positions[real_hour])
        if 6 <= real_hour <= 17:    # day hours
            wn.bgcolor("skyblue")
        else:                        # night hours
            wn.bgcolor("black")
elif starthour==8:
    for i in range(24): 
        hour.setheading(30*-hourangle-150)
        hour.forward(30)
        hour.stamp()
        hour.goto(-200,200)
        time.sleep(2)
        hour.clear()
        hourangle +=1
        real_hour = (starthour + i - 1) % 24
        sun.goto(0, sun_positions[real_hour])
        if 6 <= real_hour <= 17:    # day hours
            wn.bgcolor("skyblue")
        else:                        # night hours
            wn.bgcolor("black")
elif starthour==9:
    for i in range(24): 
        hour.setheading(30*-hourangle-180)
        hour.forward(30)
        hour.stamp()
        hour.goto(-200,200)
        time.sleep(2)
        hour.clear()
        hourangle +=1
        real_hour = (starthour + i - 1) % 24
        sun.goto(0, sun_positions[real_hour])
        if 6 <= real_hour <= 17:    # day hours
            wn.bgcolor("skyblue")
        else:                        # night hours
            wn.bgcolor("black")
elif starthour==10:
    for i in range(24): 
        hour.setheading(30*-hourangle+150)
        hour.forward(30)
        hour.stamp()
        hour.goto(-200,200)
        time.sleep(2)
        hour.clear()
        hourangle +=1
        real_hour = (starthour + i - 1) % 24
        sun.goto(0, sun_positions[real_hour])
        if 6 <= real_hour <= 17:    # day hours
            wn.bgcolor("skyblue")
        else:                        # night hours
            wn.bgcolor("black")
elif starthour==11:
    for i in range(24): 
        hour.setheading(30*-hourangle+120)
        hour.forward(30)
        hour.stamp()
        hour.goto(-200,200)
        time.sleep(2)
        hour.clear()
        hourangle +=1
        real_hour = (starthour + i - 1) % 24
        sun.goto(0, sun_positions[real_hour])
        if 6 <= real_hour <= 17:    # day hours
            wn.bgcolor("skyblue")
        else:                        # night hours
            wn.bgcolor("black")
elif starthour==12:
    for i in range(24): 
        hour.setheading(30*-hourangle+90)
        hour.forward(30)
        hour.stamp()
        hour.goto(-200,200)
        time.sleep(2)
        hour.clear()
        hourangle +=1
        real_hour = (starthour + i - 1) % 24
        sun.goto(0, sun_positions[real_hour])
        if 6 <= real_hour <= 17:    # day hours
            wn.bgcolor("skyblue")
        else:                        # night hours
            wn.bgcolor("black")




wn = trtl.Screen()
wn.mainloop()