from flask import Flask, render_template, request, redirect, url_for, session, flash
from flask_sqlalchemy import SQLAlchemy
from werkzeug.security import generate_password_hash, check_password_hash
import os

#настройка личного ключа безопасности
app = Flask(__name__)
app.config['SECRET_KEY'] = 'your-secret-key-here-change-it-in-production'
basedir = os.path.abspath(os.path.dirname(__file__))
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///' + os.path.join(basedir, 'users.db')
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

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
    {"slug": "diversity", "title": "Diversity of words"},
    {"slug": "america", "title": "America"},
    {"slug": "canada", "title": "Canada"},
    {"slug": "australia", "title": "Australia"},
    {"slug": "great-britain", "title": "Great Britain"},
    {"slug": "new-zealand", "title": "New Zealand"},
    {"slug": "about", "title": "About"},
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



@app.route("/")
def index():
    if 'user_id' in session:
        return redirect(url_for('login'))
    else:
        return redirect(url_for('login'))

@app.route("/home")
def home():
    return render_template("home.html", nav=NAV)

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
                            ["Object", "USA", "UK", "Australia", "New Zealand"],
                            ["Candy / Sweet", "Candy", "Sweets", "Lollies", "Lollies"],
                            ["Flip-flops", "Flip-flops", "Flip-flops", "Thongs", "Jandals"],
                            ["Sweater", "Sweater", "Jumper", "Jumper", "Jumper"],
                            ["Garbage bin", "Trash can", "Bin", "Bin", "Rubbish bin"],
                            ["Sausage", "Sausage", "Sausage", "Snag", "Sausage"],
                            ["Afternoon", "Afternoon", "Afternoon", "Arvo", "Arvo"],
                        ],
                    }
                ],
            }
        )

    region = REGIONS.get(slug)
    if region:
        return render_template("region.html", nav=NAV, region=region)
    return render_template("region.html", nav=NAV, region={"title":"Not found","sections":[{"title":"404","content":"Страница не найдена"}]}), 404

@app.route("/login", methods=["GET", "POST"])
def login():
    if request.method == "POST":
        username = request.form.get("username")
        password = request.form.get("password")

        #найти пользователя в базе данных по имени
        user = User.query.filter_by(username=username).first()

        #проверить, существует ли пользователь и правильный ли пароль
        if user and user.check_password(password):
            session['user_id'] = user.id
            session['username'] = user.username
            flash(f'Welcome, {user.username}!', 'success')
            return redirect(url_for('home'))
        else:
            #ОШИБКА
            flash('Invalid username or password', 'error')
            return render_template("login.html", nav=NAV)

    #если метод GET, просто отобразить форму
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

if __name__ == "__main__":
    app.run(debug=True)