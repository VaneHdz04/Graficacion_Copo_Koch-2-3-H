from flask import Flask, jsonify, render_template, send_file
import math
import matplotlib.pyplot as plt

app = Flask(__name__)

# ---------------- FUNCIONES ----------------
def koch_curve(iterations, length, x, y, heading, pts):
    """Genera los puntos del fractal siguiendo la lógica del Turtle"""
    if iterations == 0:
        rad = math.radians(heading)
        x2 = x + length * math.cos(rad)
        y2 = y + length * math.sin(rad)
        pts.append((x2, y2))
        return x2, y2, heading
    else:
        iterations -= 1
        length /= 3.0
        # 1
        x, y, heading = koch_curve(iterations, length, x, y, heading, pts)
        heading += 60
        # 2
        x, y, heading = koch_curve(iterations, length, x, y, heading, pts)
        heading -= 120
        # 3
        x, y, heading = koch_curve(iterations, length, x, y, heading, pts)
        heading += 60
        # 4
        x, y, heading = koch_curve(iterations, length, x, y, heading, pts)
        return x, y, heading

def build_fractal(iterations, length):
    """
    Genera los puntos del copo de Koch:
    - posición inicial: (-150, 80)
    - orientación inicial: 60°
    - dibuja los dos lados superiores consecutivos
    """
    pts = [(-150, 80)]
    x, y, hdg = -150, 80, 60
    x, y, hdg = koch_curve(iterations, length, x, y, hdg, pts)
    hdg -= 120  # giro para el segundo lado
    x, y, hdg = koch_curve(iterations, length, x, y, hdg, pts)
    return pts

def save_fractal_as_png(pts, color, filename="static/fractal.png"):
    plt.figure(figsize=(6,6), facecolor="black")
    xs, ys = zip(*pts)
    plt.plot(xs, ys, color=color)
    plt.axis("equal")
    plt.axis("off")
    plt.savefig(filename, dpi=200, bbox_inches="tight", facecolor="black")
    plt.close()

# ---------------- RUTAS ----------------
@app.route("/")
def index():
    return render_template("index.html")

@app.route("/koch/<int:iterations>/<int:length>/<int:rapidez>/<string:color>")
def fractal(iterations, length, rapidez, color):
    pts = build_fractal(iterations, length)
    return jsonify({"points": pts, "rapidez": rapidez, "color": f"#{color}"})

@app.route("/export/<int:iterations>/<int:length>/<string:color>")
def export(iterations, length, color):
    pts = build_fractal(iterations, length)
    save_fractal_as_png(pts, f"#{color}")
    return send_file("static/fractal.png", mimetype="image/png", as_attachment=True)

if __name__ == "__main__":
    app.run(debug=True)
