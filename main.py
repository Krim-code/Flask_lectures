from flask import Flask, render_template, url_for


app = Flask(__name__)

menu = [
            {"name":"Главная","url":"/"},
            {"name":"О нас","url":"/about"},
        ]
@app.route("/")
@app.route("/index")
def index():
    print(url_for('index'))
    return render_template("index.html" ,menu=menu, title = "Главная")



@app.route("/about")
def about():
    print(url_for('about'))
    return render_template("about.html", title = "О компании", menu=menu)

@app.route("/profile/<path:username>")
def profile(username):
    print(url_for('profile', username = "11"))
    return f"Пользователь -- {username}"

if __name__ == "__main__":
    app.run(debug=True )
