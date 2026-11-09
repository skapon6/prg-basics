import figures
import turtle

window = turtle.Screen()
window.bgcolor("lightgreen")

pen = turtle
pen.speed(5)

pen.penup()
pen.goto(-200, 100)
pen.pendown()
figures.draw_square(80)

pen.penup()
pen.goto(-50, 100)
pen.pendown()
figures.draw_square(80)

pen.penup()
pen.goto(-200, 0)
pen.pendown()
figures.draw_trangle(80)

pen.penup()
pen.goto(-50, 0)
pen.pendown()
figures.draw_trangle(80)

pen.penup()
pen.goto(-200, -100)
pen.pendown()
figures.draw_rectangle(100, 60)

pen.penup()
pen.goto(-50, -100)
pen.pendown()
figures.draw_rectangle(100, 60)

pen.hideturtle()
window.mainloop()
