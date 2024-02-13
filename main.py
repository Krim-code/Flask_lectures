from flask import Flask, render_template


app = Flask(__name__)

menu = ["Главная", "Галерея","О нас"]
@app.route("/")
@app.route("/index")
def index():
    return render_template("index.html" ,menu=menu, title = "Главная")



@app.route("/about")
def about():
    return render_template("about.html", title = "О компании")

if __name__ == "__main__":
    app.run(debug=True )
