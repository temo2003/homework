from turtle import*


#we want to paint house
 
#step1: draw a square

speed(50)
width(7)
color("purple")
forward(200)
left(90)
forward(200)
left(90)
forward(200)
left(90)
forward(200)
left(90)
#and of square

#drawing a door
forward(70)
color("yellow")
begin_fill()
left(90)
forward(100) #height of the door
right(90)
forward(60)
right(90)
forward(100)
end_fill()


penup()
goto(200,200)
pendown()
color("red")
begin_fill()
right(150)
forward(200)
left(120)
forward(200)
end_fill()
 
#drawing a window
penup() 
left(30)
forward(40)
pendown()
color("brown")
begin_fill()
left(90)
forward(40)
right(90)
forward(40)
right(90)
forward(40)
end_fill()

penup()
left(90)
forward(120)
left(90)
forward(200)
left(90)
forward(120)
pendown()
begin_fill()
left(90)
forward(40)
right(90)
forward(40)
right(90)
forward(40)
end_fill()

#drawing a ladder

penup()
right(90)
forward(160)
right(90)
forward(70)
pendown()
color("black")
left(70)
forward(120)
right(60)
forward(60)
right(120)
forward(40)
right(60)
forward(60)
left(60)
forward(40)
left(120)
forward(60)
left(60)
forward(40)
left(180)
forward(90)
right(70)
forward(60)




exitonclick()
 