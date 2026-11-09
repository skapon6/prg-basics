import figures
import turtle

window = turtle.Screen()
window.bgcolor("lightgreen")

pen = turtle
pen.speed(5)

figures.draw_square(100)

pen.hideturtle()
window.mainloop()
