from turtle import Turtle
from random import randint

one = Turtle() # turtle object

#Turtle object has attributes for colour and shape

one.color('red')
one.shape('turtle')
one.penup()
one.goto(-160,100)  #to goto the position
one.pendown()

two =Turtle()
two.color('blue')
two.shape('turtle')
two.penup()
two.goto(-160,70)  #to goto the position
two.pendown()

three =Turtle()
three.color('green')
three.shape('turtle')
three.penup()
three.goto(-160,40)  #to goto the position
three.pendown()

four =Turtle()
four.color('yellow')
four.shape('turtle')
four.penup()
four.goto(-160,10)  #to goto the position
four.pendown()

# telling turtles to move forward

for movement in range(100):
    one.forward(randint(1,5))
   # one.left(randint(1,5))
    #one.right(randint(1,5))
    
    two.forward(randint(1,5))
    three.forward(randint(1,5))
    four.forward(randint(1,5))

input('Please enter to close')