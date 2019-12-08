import turtle
import getfailed
sc= turtle.Screen()
turtle.listen()
board = turtle.Turtle()
board.hideturtle() 
def draw_filled_rectangle(board,x1,y1,x2,y2,fill):
  board.fillcolor(fill)
  board.setheading(0)
 
  board.begin_fill()
  board.up()
  board.goto(x1,y1)
  board.down()
  board.forward(abs(x1-x2))
  board.left(90)
  board.forward(abs(y1-y2))
  board.left(90)
  board.forward(abs(x1-x2))
  board.left(90)
  board.forward(abs(y1-y2))
  board.end_fill()
fails = getfailed.getfails()
i=0
def add():
    global i
    global fails
    if i < len(fails)-1:
        i=i+1
        drawall(i)
        print "add"
def less():
    global i
    if i > 0:
        i=i-1
        drawall(i)
        print "less"
def quit():
    turtle.bye()

def drawone():
    failsh=((42,31),(43,35),(24,16),(45,41),(69,41),(78,99))

    cp_bl=failsh[0]   
    cp_tr=failsh[1]
    t1_bl=failsh[2]
    t1_tr=failsh[3]
    t2_bl=failsh[4]
    t2_tr=failsh[5]
    
    turtle.penup()
    turtle.setpos(20,10)
    turtle.hideturtle()
    turtle.pendown()
    
    turtle.write("Currently on: "+str(failsh),align="center",font=("PaleVioletRed2",10))
    draw_filled_rectangle(board,cp_bl[0],cp_bl[1],cp_tr[0],cp_tr[1],"black")
    draw_filled_rectangle(board,t1_bl[0],t1_bl[1],t1_tr[0],t1_tr[1],"grey")
    draw_filled_rectangle(board,t2_bl[0],t2_bl[1],t2_tr[0],t2_tr[1],"grey")
def drawall(i):


    board.clear()
    board.reset() 
    board.hideturtle() 
    turtle.clear()
    turtle.hideturtle()
    cp_bl=fails[i][0]   
    cp_tr=fails[i][1]
    t1_bl=fails[i][2]
    t1_tr=fails[i][3]
    t2_bl=fails[i][4]
    t2_tr=fails[i][5]
    
    turtle.penup()
    turtle.setpos(20,150)
    turtle.hideturtle()
    turtle.pendown()
    
    turtle.write("Currently on: "+str(fails[i]),align="center",font=("PaleVioletRed2",10))
    draw_filled_rectangle(board,cp_bl[0],cp_bl[1],cp_tr[0],cp_tr[1],"black")
    draw_filled_rectangle(board,t1_bl[0],t1_bl[1],t1_tr[0],t1_tr[1],"grey")
    draw_filled_rectangle(board,t2_bl[0],t2_bl[1],t2_tr[0],t2_tr[1],"grey")
    turtle.onkey(add,"Right")
    turtle.onkey(add,'l')
    turtle.onkey(less,"Left")
    turtle.onkey(less,'h')
    turtle.onkey(quit,'q')    
drawall(i)
a=raw_input("")
