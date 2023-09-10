from flask import Flask, render_template
from markupsafe import escape

app = Flask(__name__)
def end():
    return """
    </div>
    <footer class="containter">
        <p>&copy; Kacper Siciarz</p>
    </footer>
</body>
</html>"""

@app.route("/")
def index():
    return render_template('index.html')

@app.route('/<number>')
def ksiega(number):
    number = int(number[1:])
    if(number>=1 or number<=12):
        return index() + render_template(f'k{number}.html') + end()
    else:
        return index() + end()

# @app.route("/k1")
# def k1():
#     return index() + render_template('k1.html') + end()

# @app.route("/k2")
# def k2():
#     return index() + render_template('k2.html') + end()

# @app.route("/k3")
# def k3():
#     return index() + render_template('k3.html') + end()

# @app.route("/k4")
# def k4():
#     return index() + render_template('k4.html') + end()

# @app.route("/k5")
# def k5():
#     return index() + render_template('k5.html') + end()

# @app.route("/k6")
# def k6():
#     return index() + render_template('k6.html') + end()

# @app.route("/k7")
# def k7():
#     return index() + render_template('k7.html') + end()

# @app.route("/k8")
# def k8():
#     return index() + render_template('k8.html') + end()

# @app.route("/k9")
# def k9():
#     return index() + render_template('k9.html') + end()

# @app.route("/k10")
# def k10():
#     return index() + render_template('k10.html') + end()

# @app.route("/k11")
# def k11():
#     return index() + render_template('k11.html') + end()

# @app.route("/k12")
# def k12():
#     return index() + render_template('k12.html') + end()
