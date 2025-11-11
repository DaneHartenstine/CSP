import turtle as trtl

#Envelope
trtl.speed(0)
trtl.hideturtle()
trtl.penup()
trtl.goto(-200,100)
trtl.pendown()
for i in range(2):
    trtl.forward(400)
    trtl.right(90)
    trtl.forward(200)
    trtl.right(90)
trtl.goto(0,0)
trtl.goto(200,100)
trtl.penup()
trtl.goto(0,25)
trtl.color("red")
trtl.fillcolor("red")   
trtl.pendown() 
trtl.begin_fill()
trtl.circle(-20)
trtl.end_fill()

#Ask what branch of military

#message


#Show branch of military in background


#Eagle 


#Flag


wn = trtl.Screen()
wn.mainloop()