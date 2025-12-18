from flask import Flask, render_template, request, redirect, url_for, session, flash
from flask_sqlalchemy import SQLAlchemy
from werkzeug.security import generate_password_hash, check_password_hash
import os
from flask_login import LoginManager, login_required, login_user, logout_user, current_user

#настройка личного ключа безопасности
app = Flask(__name__)
app.config['SECRET_KEY'] = 'your-secret-key-here-change-it-in-production'
basedir = os.path.abspath(os.path.dirname(__file__))
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///' + os.path.join(basedir, 'users.db')
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
app.secret_key = "super-secret-key"

db = SQLAlchemy(app)
class User(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String(80), unique=True, nullable=False)
    password_hash = db.Column(db.String(120), nullable=False)

    def set_password(self, password):
        #сохраняет пароль
        self.password_hash = generate_password_hash(password)

    def check_password(self, password):
        #соотвествует ли данный пароль прошлому паролю
        return check_password_hash(self.password_hash, password)

    def __repr__(self):
        return f'<User {self.username}>'

NAV = [
    {"slug": "home", "title": "Home"},
    {"slug": "diversity", "title": "Diversity"},
    {"slug": "america", "title": "America"},
    {"slug": "canada", "title": "Canada"},
    {"slug": "australia", "title": "Australia"},
    {"slug": "great-britain", "title": "Great Britain"},
    {"slug": "new-zealand", "title": "New Zealand"},
    {"slug": "about", "title": "About"},
   # {"slug": "profile", "title": "Profile"},

]

HOME_CONTENT = {
    "title": "The 5 faces of English",
    "why": [
        "Cultural Immersion: Learning different varieties of English allows you to immerse yourself in different cultures and societies...",
        "Professional Opportunities: Learning different varieties of English can be beneficial for professional development...",
        "Linguistic diversity: Each variation of the English language has its own characteristics...",
        "Travel and Communication: Learning different varieties of English makes it easier to travel and communicate..."
    ],
}

from regions.america import REGION_AMERICA
from regions.canada import REGION_CANADA
from regions.greatbritain import REGION_GB
from regions.australia import REGION_AU
from regions.newzealand import REGION_NZ

REGIONS = {
    "great-britain": REGION_GB,
    "america": REGION_AMERICA,
    "canada": REGION_CANADA,
    "australia": REGION_AU,
    "new-zealand": REGION_NZ
}

#Создание таблиц базы данных при запуске
with app.app_context():
    db.create_all()


import random

DIALECT_TESTS = {
    "American English": [
        "Candy",
        "Trash can",
        "Sidewalk",
        "Gas station",
        "Apartment"
    ],
    "British English": [
        "Sweets",
        "Bin",
        "Pavement",
        "Petrol station",
        "Flat"
    ],
    "Canadian English": [
        "Toque",
        "Washroom",
        "Loonie",
        "Double-double",
        "Eh"
    ],
    "Australian English": [
        "Lollies",
        "Arvo",
        "Thongs",
        "Servo",
        "Brekkie"
    ],
    "New Zealand English": [
        "Jandals",
        "Dairy",
        "Chilly bin",
        "Sweet as",
        "Togs"
    ]
}

@app.route("/")
def index():
    if 'user_id' in session:
        return redirect(url_for('login'))
    else:
        return redirect(url_for('login'))

@app.route("/home")
def home():
    return render_template("home.html", nav=NAV, home_content=HOME_CONTENT)

@app.route("/about/")
def about():
    return render_template("about.html", title="About the Project", nav=NAV)

@app.route("/<slug>/")
def page(slug):
    if slug == "home":
        return redirect(url_for('home'))
    if slug == "diversity":
        return render_template(
            "region.html",
            nav=NAV,
            region={
                "title": "Diversity of words",
                "sections": [
                    {
                        "title": "Introduction",
                        "content": "Here is a comparison table showing how different English-speaking countries use different words for the same things.",
                    },
                    {
                        "title": "Vocabulary Comparison Table",
                        "table": [
                            ["Object", "USA", "UK","Canada", "Australia", "New Zealand"],
                            ["Candy / Sweet", "Candy", "Sweets","Candy", "Lollies", "Lollies"],
                            ["Flip-flops", "Flip-flops", "Flip-flops", "Flip-flops", "Thongs", "Jandals"],
                            ["Sweater", "Sweater", "Jumper", "Jumper", "Jumper", "Jumper"],
                            ["Garbage bin", "Trash can", "Bin", "Bin", "Bin", "Rubbish bin"],
                            ["Sausage", "Sausage", "Sausage","Sausage", "Snag", "Sausage"],
                            ["Afternoon", "Afternoon", "Afternoon","Afternoon", "Arvo", "Arvo"],
                        ],
                    }
                ],
            }
        )

    region = REGIONS.get(slug)
    if region:
        return render_template("region.html", nav=NAV, region=region)
    return render_template("region.html", nav=NAV, region={"title":"Not found","sections":[{"title":"404","content":"Страница не найдена"}]}), 404

@app.route("/diversity")
def diversity():
    return render_template("diversity.html", nav=NAV, title="Diversity")

@app.route("/dialect-test")
def dialect_test():
    dialect, words = random.choice(list(DIALECT_TESTS.items()))

    return render_template(
        "dialect_test.html",
        nav=NAV,
        dialect=dialect,
        words=words,
        title="Dialect Recognition Test"
    )

@app.route("/login", methods=["GET", "POST"])
def login():
    if request.method == "POST":
        username = request.form.get("login")
        password = request.form.get("password")

        user = User.query.filter_by(username=username).first()

        if user and user.check_password(password):
            # сохраняем данные в session
            session["login"] = user.username
            session["password"] = password  # учебный вариант
            session["last_name"] = request.form.get("last_name")
            session["email"] = request.form.get("email")

            return redirect(url_for("profile"))
        else:
            flash("Invalid username or password", "error")

    return render_template("login.html", nav=NAV)



@app.route("/register", methods=["GET", "POST"])
def register():
    if request.method == "POST":
        username = request.form.get("username")
        password = request.form.get("password")
        #проверяем, существует ли уже пользователь с таким именем
        existing_user = User.query.filter_by(username=username).first()
        if existing_user:
            flash('Username already exists. Please choose a different one.', 'error')
            return render_template("register.html", nav=NAV)
        #создаем нового пользователя
        new_user = User(username=username)
        new_user.set_password(password)

        try:
            db.session.add(new_user)
            db.session.commit()
            flash('Registration successful! Please log in.', 'success')
            #после успешной регистрации перенаправить на страницу входа
            return redirect(url_for('login'))
        except Exception as e:
            db.session.rollback()
            flash('An error occurred during registration. Please try again.', 'error')
            print(f"Database error: {e}")
            return render_template("register.html", nav=NAV)

    #если метод GET, просто отобразить форму
    return render_template("register.html", nav=NAV)

@app.route('/logout')
def logout():
    session.pop('user_id', None)
    session.pop('username', None)
    flash('You have been logged out.', 'info')
    return redirect(url_for('login'))

@app.route("/profile")
def profile():
    login = session.get("login")
    password = session.get("password")
    last_name = session.get("last_name")
    email = session.get("email")

    return render_template(
        "profile.html",
        login=login,
        password=password,
        last_name=last_name,
        email=email,
        nav=NAV
    )

@app.route("/test")
def test():
    return render_template("test.html", nav=NAV, title="Dialect Test")

if __name__ == "__main__":
    app.run(debug=True)

login_manager = LoginManager(app)
login_manager.login_view = "login"
