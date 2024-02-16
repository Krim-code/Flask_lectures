from flask import Flask, render_template, request,flash,session,redirect, url_for,abort


app = Flask(__name__)

app.config["SECRET_KEY"] = "CH2,)7Vhr!YnmZM6AOU,n9Q}J"
menu = [
            {"name":"Главная","url":"/"},
            {"name":"О нас","url":"/about"},
            {"name":"Обратная связь","url":"/contact"},
        ]
@app.route("/")
@app.route("/index")
def index():
    return render_template("index.html" ,menu=menu, title = "Главная")



@app.route("/about")
def about():
    return render_template("about.html", title = "О компании", menu=menu)

@app.route("/profile/<path:username>")
def profile(username):
    if 'userLogged' not in session or session['userLogged'] != username:
        abort(401)

    return f"Пользователь -- {username}"


@app.route('/contact', methods = ['POST', 'GET'])
def contact():
    if request.method == 'POST':
        if len(request.form['name']) >= 2:
            flash("Сообщение доставлено", category="success")
        else:
            flash("Ошибка доставки", category="error")
    return render_template("contact.html" ,menu=menu, title = "Обратная связь")

@app.errorhandler(404)
def pageNotFound(error):
   return render_template("page404.html" ,menu=menu, title = "Cтраница не найдена")

@app.route("/login", methods = ['POST', 'GET'])
def login():
    if 'userLogged' in session:
        return redirect(url_for('profile', username=session["userLogged"]))
    elif request.method == "POST":
        #вывести с помощью flash сообщение о неправильном логине или пароле
        if request.form['name'] == "Test" and request.form['psw'] == "123":
            session['userLogged'] = request.form['name']
            return redirect(url_for('profile', username=session["userLogged"]))
    return render_template("login.html" ,menu=menu, title = "Логин")


if __name__ == "__main__":
    app.run(debug=True )
