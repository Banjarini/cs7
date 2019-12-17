import serial
import turtle
ser = serial.Serial('COM3',baudrate=9600, timeout=1)
wn = turtle.Screen()
wn.title("clock")
wn.bgcolor("#FF0000")

SCALE = 1.0
line = turtle.Turtle()
line.speed(100)
line.hideturtle()
for i in range(10):
                data = ser.readline().decode()
                print(data)
while 1:
        data = ser.readline().decode()
        print(len(data))
        print(type(data))
        line.goto(0,0)
        line.left(1)
        print(data)
        line.pendown()
        line.forward(200)
        
