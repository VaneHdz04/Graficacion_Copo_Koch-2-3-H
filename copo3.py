import turtle

# --- Función recursiva: curva de Koch ---
def koch_curve(t, length, level):
    if level == 0:
        t.forward(length)
    else:
        length /= 3.0
        koch_curve(t, length, level-1)
        t.left(60)
        koch_curve(t, length, level-1)
        t.right(120)
        koch_curve(t, length, level-1)
        t.left(60)
        koch_curve(t, length, level-1)

# --- Configuración de la ventana ---
screen = turtle.Screen()
screen.bgcolor("black")

# --- Configuración de la tortuga ---
t = turtle.Turtle()
t.speed(0)
t.color("cyan")
t.hideturtle()

# --- Posición inicial ---
t.penup()
t.goto(-150, 80)   # mover la tortuga para centrar el dibujo
t.left(60)         # orientación inicial
t.pendown()

# --- Parámetros del copo ---
nivel = 4      # profundidad de recursión
longitud = 300 # longitud inicial

# --- Dibujar los dos lados superiores ---
koch_curve(t, longitud, nivel)  # primer lado
t.right(120)                    # giro para el segundo lado
koch_curve(t, longitud, nivel)  # segundo lado

turtle.done()
