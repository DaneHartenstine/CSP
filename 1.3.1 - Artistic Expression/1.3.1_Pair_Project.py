import turtle as trtl
wn = trtl.Screen()


def clear(x,y):
    trtl.clear()
wn.onclick(clear)



#Ask what branch of military
boat_image = "navy boat.gif"
navy_image = "navy.gif"
airforce_image = "air_force.gif"
jet_image = "jet.gif"
tank_image = "tank.gif"
army_image = "army.gif"
humvee_image = "humvee.gif"
marine_image = "marines.gif"
rocket_image = "rocket.gif"
space_image = "space_force.gif"
lighthouse_image = "lighthouse.gif"
coastguard_image = "coast_guard.gif"

#envelope
def envelope(): 
    trtl.pensize(5)   
    trtl.color("black")
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

#Show branch of military in background
def navy ():
    wn.addshape(boat_image)
    boat = trtl.Turtle(shape=boat_image)
    wn.addshape(navy_image)
    navy_e = trtl.Turtle(shape=navy_image)
    navy_e.penup()
    navy_e.speed(0)
    navy_e.goto(200,200)
    trtl.color("white")
    trtl.pensize(600)
    trtl.pendown()
    trtl.forward(200)
    envelope()

def airforce():
    wn.addshape(airforce_image)
    wn.addshape(jet_image)
    jet = trtl.Turtle(shape=jet_image)
    airforce_e = trtl.Turtle(shape=airforce_image)
    airforce_e.penup()
    airforce_e.speed(0)
    airforce_e.goto(200,200)
    trtl.color("white")
    trtl.pensize(600)
    trtl.pendown()
    trtl.forward(200)
    envelope()

def army():
    wn.addshape(army_image)
    wn.addshape(tank_image)
    tank = trtl.Turtle(shape=tank_image)
    army_e = trtl.Turtle(shape=army_image)
    army_e.penup()
    army_e.speed(0)
    army_e.goto(200,200)
    trtl.color("white")
    trtl.pensize(600)
    trtl.pendown()
    trtl.forward(200)
    envelope()

def marine():
    wn.addshape(marine_image)
    wn.addshape(humvee_image)
    humvee = trtl.Turtle(shape=humvee_image)
    marine_e = trtl.Turtle(shape=marine_image)
    marine_e.penup()
    marine_e.speed(0)
    marine_e.goto(200,200)
    trtl.color("white")
    trtl.pensize(600)
    trtl.pendown()
    trtl.forward(200)
    envelope()

def spaceforce():
    wn.addshape(space_image)
    wn.addshape(rocket_image)
    rocket = trtl.Turtle(shape=rocket_image)
    space_e = trtl.Turtle(shape=space_image)
    space_e.penup()
    space_e.speed(0)
    space_e.goto(-200,200)
    trtl.color("white")
    trtl.pensize(600)
    trtl.pendown()
    trtl.forward(200)
    envelope()

def coastguard():
    wn.addshape(coastguard_image)
    wn.addshape(lighthouse_image)
    lighthouse = trtl.Turtle(shape=lighthouse_image)
    coastguard_e = trtl.Turtle(shape=coastguard_image)
    coastguard_e.penup()
    coastguard_e.speed(0)
    coastguard_e.goto(200,200)
    trtl.color("white")
    trtl.pensize(6000)
    trtl.pendown()
    trtl.forward(200)
    envelope()



branch_list = [navy, airforce, army, marine, spaceforce, coastguard]

army()

#branch = trtl.textinput("Branch of Military","What Branch of Military Did You Serve In?(navy, airforce, army, marine, spaceforce, coastguard)")

#while branch not in branch_list:
    #trtl.textinput("Thats Not A Branch, Spelling Error","What Branch of Military Did You Serve In?")




#message


#Flag



wn.mainloop()