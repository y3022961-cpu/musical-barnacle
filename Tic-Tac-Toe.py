#Programme for the game of tic-tac-toe
import turtle

window=turtle.Screen()
window.title("Tic-tac-toe!!!")   #Appearance of the game
window.bgcolor("white")
window.setup(width=400,height=400)

player=turtle.Turtle()
player.ht()            
player.color("pink")
player.pensize(20)
for i in range(2):
    player.penup()
    player.goto(-300,100-200*i)
    player.pendown()
    player.forward(600)
player.right(90)
for i in range(2):
    player.penup()
    player.goto(-100+200*i,300)
    player.pendown()
    player.forward(600)

T=((-230,230),(0,230),(230,230),(-230,0),(0,0),(230,0),(-230,-230),(0,-230),(230,-230))
X=()
O=()

x=turtle.Turtle()
x.color("yellow")
x.pensize(20)
o=turtle.Turtle()
o.pensize(20)
count1=0
count2=1


for m in range(8):
    
    m=int(input("Enter position number for x:"))
            
    x.penup()
    x.goto(T[m])
    x.right(45)
    x.forward(45)
    x.left(180)
    x.pendown()
    x.forward(95)
    x.right(135)
    x.penup()
    x.forward(67)
    x.right(135)
    x.pendown()
    x.forward(95)
    x.penup()
    x.goto(0,0)
    x.right(45)
    count1+=1
    X=X+tuple([m])
    draw=turtle.Turtle()
    draw.pensize(20)
    draw.color("blue")
    draw.penup()
    if 0 in X and 1 in X and 2 in X:
        draw.goto(-300,200)
        draw.pendown()
        draw.forward(600)
        break
    if count1==count2==5:
        break
    else:
        m=int(input("Enter the position number for o:"))
        
        o.penup()
        o.goto(T[m])
        o.pendown()
        o.color("black")
        o.circle(45)
        o.penup()
        o.goto(0,0)
        count2+=1
        O=O+tuple([m])
print(X)
print(O)

    
    
    

    
    
        
  

     
    



    
    
