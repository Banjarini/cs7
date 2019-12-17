
import turtle
import time

print("Python Turtle Analog Clock")
print("By Cliffton")



ok = False
while not(ok):
 print("\nANALOG CLOCK")
 offset = int(input("Enter offset from GMT (-11 to 11) :"))
 if offset >= -11 and offset <= 11:
  ok = True
  
wn = turtle.Screen()
wn.title("clock")
wn.bgcolor("#FFFFFF")

SCALE = 1.0 

# dial
mark = turtle.Turtle()

msg = ""
mark.goto(0, -10)  
mark.color("#000000")
mark.pendown()
mark.write(msg, move=False, align="center", font=("Arial", 15, "bold"))

mark.hideturtle()


mark.speed(200)
mark.shape("circle")
mark.penup()
mark.right(90)
mark.forward(240)
mark.pendown()
mark.left(90)
mark.pensize(6)
mark.circle(240)
mark.right(90)
mark.penup()
mark.backward(240)
mark.left(90)

for i in range(60):
      if i % 5 == 0:
            mark.pensize(6)
            mark.penup()
            mark.forward(200*SCALE)
            mark.pendown()
            mark.forward(20*SCALE)
            mark.penup()
            mark.backward(220*SCALE)
      else:
            mark.pensize(2)
            mark.penup()
            mark.forward(200*SCALE)
            mark.pendown()
            mark.forward(10*SCALE)
            mark.penup()
            mark.backward(210*SCALE)      
      mark.right(6)


update = True 
updateSecond = True 
while True: 
      b = time.gmtime(time.time()) 
      m = b.tm_min 
      s = b.tm_sec 
      if update:
           
            hour = turtle.Turtle()
            hour.left(90)
            hour.speed(100*SCALE)
            hour.pensize(10)
            hour.shape("blank")
            hour.right(((b.tm_hour + offset) % 12) * 30 + b.tm_min * 0.5 )
            hour.backward(30*SCALE)
            hour.forward(160*SCALE)

     
            minute = turtle.Turtle()
            minute.speed(100)
            minute.shape("blank")
            minute.left(90)
            minute.pensize(6)
            minute.right((b.tm_min) * 6)
            minute.backward(30*SCALE)
            minute.forward(180*SCALE)

            update = False
            
      if updateSecond:
        
            second = turtle.Turtle()
            second.speed(100)
            second.shape("blank")
            second.color("red")
            second.left(90)
            second.pensize(3)
            second.right((b.tm_sec) * 6)
            second.backward(30*SCALE)
            second.forward(190*SCALE)
            updateSecond = False

      time.sleep(0.3)
      b = time.gmtime(time.time())
      new_min = b.tm_min
      new_sec = b.tm_sec

      if new_min != m:
            update = True
            hour.clear() 
            hour.reset()
            minute.clear()
            minute.reset()
      if new_sec != s:
            updateSecond = True
            second.clear()
            second.reset()
            
