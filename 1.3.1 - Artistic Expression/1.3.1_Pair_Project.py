import turtle as trtl
wn = trtl.Screen()

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

trtl.penup()
trtl.color("black")
trtl.goto(-100,150)
trtl.write("Click me!", font=("Arial", 45, "bold"))

def clear(x,y):
    trtl.clear()
wn.onclick(clear)



#Ask what branch of military
boat_image = "navy boat.gif"

def navy ():
    wn.addshape(boat_image)
    boat = trtl.Turtle(shape=boat_image)
    

def airforce():
    fasd
def army():
    asfg
def marine():
    afeg
def spaceforce():
    qwr
def coastguard():
    wer


#branch_list = [navy, airforce, army, marine, spaceforce, coastguard]

#message


#Show branch of military in background


#Eagle 


#Flag



wn.mainloop()