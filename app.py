from flask import Flask, render_template, request, redirect, url_for, session, flash
from flask_sqlalchemy import SQLAlchemy
from werkzeug.security import generate_password_hash, check_password_hash
import os
from datetime import datetime
from flask_login import LoginManager, login_required, login_user, logout_user, current_user
from functools import wraps

#настройка личного ключа безопасности
app = Flask(__name__)
app.config['SECRET_KEY'] = 'your-secret-key-here-change-it-in-production'
basedir = os.path.abspath(os.path.dirname(__file__))
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///' + os.path.join(basedir, 'users.db')
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
app.secret_key = "super-secret-key"

db = SQLAlchemy(app)
def login_required_custom(f):
    @wraps(f)
    def wrapper(*args, **kwargs):
        if not session.get("user_id"):
            return redirect(url_for("login"))
        return f(*args, **kwargs)
    return wrapper

class User(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String(80), unique=True, nullable=False)
    password_hash = db.Column(db.String(120), nullable=False)

    email = db.Column(db.String(120))
    last_name = db.Column(db.String(120))
    interests = db.Column(db.Text)

    def set_password(self, password):
        self.password_hash = generate_password_hash(password)

    def check_password(self, password):
        return check_password_hash(self.password_hash, password)

    def __repr__(self):
        return f'<User {self.username}>'

class SlangFact(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    region = db.Column(db.String(50), nullable=False)
    title = db.Column(db.String(200), nullable=False)
    content = db.Column(db.Text, nullable=False)
    user_id = db.Column(db.Integer, db.ForeignKey('user.id'), nullable=True)  # Nullable for system facts
    is_system = db.Column(db.Boolean, default=False, nullable=False)  # True for unchangeable system facts
    created_at = db.Column(db.DateTime, default=datetime.utcnow)
    updated_at = db.Column(db.DateTime, default=datetime.utcnow, onupdate=datetime.utcnow)

    def __repr__(self):
        return f'<SlangFact {self.region}: {self.title}>'

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

# Предустановленные факты о сленге
DEFAULT_SLANG_FACTS = {
    "america": [
        {
            "title": "The Origins of 'Cool'",
            "content": "The word 'cool' as we know it today originated in jazz culture of the 1930s-1940s. Musicians used it to describe something sophisticated or excellent. It has since become one of the most versatile slang words in American English, expressing approval, indifference, or calmness."
        },
        {
            "title": "Valley Girl Slang",
            "content": "The 1980s 'Valley Girl' slang popularized phrases like 'like, totally' and 'gag me with a spoon'. This trend started in California's San Fernando Valley and spread nationwide through media, shaping how young Americans spoke for decades."
        },
        {
            "title": "Internet Slang Evolution",
            "content": "American English has been the dominant source of internet slang. Terms like 'LOL' (laugh out loud), 'BRB' (be right back), and 'YOLO' (you only live once) originated in American online communities before spreading globally."
        }
    ],
    "great-britain": [
        {
            "title": "Cockney Rhyming Slang",
            "content": "One of the most fascinating features of British slang is Cockney rhyming slang, originating in London's East End. Phrases like 'apples and pears' (stairs) and 'trouble and strife' (wife) replace words with rhyming phrases, often dropping the rhyming part in actual use."
        },
        {
            "title": "Royal Influence on Language",
            "content": "British slang often reflects class distinctions. Working-class slang differs significantly from upper-class expressions. The Queen's English, though not slang itself, influenced what was considered 'proper' versus 'slang' throughout British history."
        },
        {
            "title": "Football (Soccer) Slang",
            "content": "Football culture heavily influences British slang. Terms like 'pitch' (field), 'match' (game), and expressions like 'it's a game of two halves' have entered everyday British English. Football chants also contribute to slang vocabulary."
        }
    ],
    "canada": [
        {
            "title": "The 'Eh' Phenomenon",
            "content": "The interjection 'eh' is perhaps Canada's most famous linguistic marker. Used to seek agreement or confirmation, it appears in questions and statements. While often stereotyped, it's genuinely common in Canadian speech, especially in casual conversation."
        },
        {
            "title": "French Influence on Canadian Slang",
            "content": "Canadian English incorporates many French loanwords due to bilingualism. Words like 'toque' (winter hat), 'dépanneur' (corner store in Quebec), and expressions like 'double-double' (coffee with two creams, two sugars from Tim Hortons) show this unique blend."
        },
        {
            "title": "Hockey Terminology",
            "content": "Ice hockey deeply influences Canadian slang. Terms from hockey enter everyday speech, and expressions like 'hat trick' (three goals) are widely understood. Hockey culture creates a shared vocabulary across English and French-speaking Canadians."
        }
    ],
    "australia": [
        {
            "title": "Diminutives Everywhere",
            "content": "Australian English loves creating diminutives by adding '-o', '-ie', or '-y' endings. Examples include 'arvo' (afternoon), 'brekkie' (breakfast), 'barbie' (barbecue), and 'maccas' (McDonald's). This creates a friendly, informal tone characteristic of Australian speech."
        },
        {
            "title": "Unique Australian Expressions",
            "content": "Australian slang includes unique expressions like 'fair dinkum' (genuine/true), 'strewth' (exclamation of surprise), and 'crikey' (made famous by Steve Irwin). These expressions reflect Australian humor and down-to-earth culture."
        },
        {
            "title": "Aboriginal Language Influence",
            "content": "Australian English incorporates many words from Aboriginal languages, especially for native animals and plants. Words like 'kangaroo', 'koala', 'boomerang', and 'billabong' entered English through early contact with Indigenous Australians."
        }
    ],
    "new-zealand": [
        {
            "title": "Maori Words in Everyday Speech",
            "content": "New Zealand English incorporates many Maori words, reflecting the country's bicultural identity. Terms like 'kia ora' (hello/greeting), 'ka pai' (well done/good), 'whanau' (extended family), and 'kai' (food) are commonly used by all New Zealanders."
        },
        {
            "title": "The 'As' Intensifier",
            "content": "New Zealanders frequently use 'as' as an intensifier, similar to 'very' or 'really'. Phrases like 'sweet as', 'choice as', or 'good as' are characteristic of Kiwi speech. This construction is unique to New Zealand English."
        },
        {
            "title": "Unique Kiwi Slang",
            "content": "New Zealand has distinctive slang terms like 'jandals' (flip-flops), 'dairy' (corner store), 'chilly bin' (cooler), and 'bach' (holiday home). These terms reflect New Zealand's isolation and unique culture, often confusing visitors from other English-speaking countries."
        }
    ]
}

def migrate_slang_fact_table():
    """Миграция: добавляет колонку is_system, если её нет"""
    from sqlalchemy import inspect, text
    try:
        inspector = inspect(db.engine)
        # Проверяем, существует ли таблица
        if 'slang_fact' in inspector.get_table_names():
            columns = [col['name'] for col in inspector.get_columns('slang_fact')]
            
            if 'is_system' not in columns:
                try:
                    # SQLite не поддерживает BOOLEAN напрямую, используем INTEGER
                    db.session.execute(text("ALTER TABLE slang_fact ADD COLUMN is_system INTEGER DEFAULT 0"))
                    db.session.commit()
                    print("Migration: Added is_system column to slang_fact table")
                except Exception as e:
                    print(f"Migration error: {e}")
                    db.session.rollback()
    except Exception as e:
        # Таблица не существует, db.create_all() создаст её с правильной структурой
        print(f"Table slang_fact doesn't exist yet, will be created by db.create_all(): {e}")

def init_default_slang_facts():
    """Инициализирует предустановленные факты о сленге в базе данных"""
    for region, facts in DEFAULT_SLANG_FACTS.items():
        for fact_data in facts:
            # Проверяем, не существует ли уже такой факт
            existing = SlangFact.query.filter_by(
                region=region,
                title=fact_data["title"],
                is_system=True
            ).first()
            
            if not existing:
                new_fact = SlangFact(
                    region=region,
                    title=fact_data["title"],
                    content=fact_data["content"],
                    user_id=None,  # Системные факты не имеют пользователя
                    is_system=True
                )
                db.session.add(new_fact)
    
    db.session.commit()

#Создание таблиц базы данных при запуске
with app.app_context():
    db.create_all()
    migrate_slang_fact_table()
    init_default_slang_facts()


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

        if not user or not user.check_password(password):
            flash("Incorrect login or password", "error")
            return render_template("login.html", nav=NAV)

        # успешный вход
        session["user_id"] = user.id
        session["username"] = user.username

        return redirect(url_for("home"))

    return render_template("login.html", nav=NAV)




@app.route("/register", methods=["GET", "POST"])
def register():
    if request.method == "POST":
        username = request.form.get("username")
        password = request.form.get("password")

        if User.query.filter_by(username=username).first():
            flash("Username already exists", "error")
            return render_template("register.html", nav=NAV)

        new_user = User(username=username)
        new_user.set_password(password)

        db.session.add(new_user)
        db.session.commit()

        # авто-вход после регистрации
        session["user_id"] = new_user.id
        session["username"] = new_user.username

        flash("Registration successful!", "success")
        return redirect(url_for("home"))

    return render_template("register.html", nav=NAV)


@app.route('/logout')
def logout():
    session.pop('user_id', None)
    session.pop('username', None)
    flash('You have been logged out.', 'info')
    return redirect(url_for('login'))

@app.route("/profile", methods=["GET", "POST"])
@login_required_custom
def profile():
    user = User.query.get(session["user_id"])

    if request.method == "POST":
        user.email = request.form.get("email")
        user.last_name = request.form.get("last_name")
        user.interests = request.form.get("interests")

        db.session.commit()
        flash("Profile updated successfully", "success")
        return redirect(url_for("profile"))

    return render_template(
        "profile.html",
        user=user,
        nav=NAV
    )

@app.route("/test")
def test():
    return render_template("test.html", nav=NAV, title="Dialect Test")

REGION_NAMES = {
    "america": "American English",
    "canada": "Canadian English",
    "australia": "Australian English",
    "great-britain": "British English",
    "new-zealand": "New Zealand English"
}

@app.route("/slang-facts/<region>", methods=["GET", "POST"])
@login_required_custom
def slang_facts(region):
    if region not in REGION_NAMES:
        flash("Region not found", "error")
        return redirect(url_for("home"))
    
    if request.method == "POST":
        title = request.form.get("title", "").strip()
        content = request.form.get("content", "").strip()
        
        if not title or not content:
            flash("Title and content are required", "error")
        else:
            new_fact = SlangFact(
                region=region,
                title=title,
                content=content,
                user_id=session["user_id"]
            )
            db.session.add(new_fact)
            db.session.commit()
            flash("Fact added successfully!", "success")
            return redirect(url_for("slang_facts", region=region))
    
    # Сначала системные факты, затем пользовательские (новые сначала)
    facts = SlangFact.query.filter_by(region=region).order_by(
        SlangFact.is_system.desc(),  # Системные факты сначала (True > False)
        SlangFact.created_at.desc()
    ).all()
    
    return render_template(
        "slang_facts.html",
        nav=NAV,
        region=region,
        region_name=REGION_NAMES[region],
        facts=facts,
        title=f"Slang Facts - {REGION_NAMES[region]}"
    )

@app.route("/slang-facts/<region>/edit/<int:fact_id>", methods=["GET", "POST"])
@login_required_custom
def edit_slang_fact(region, fact_id):
    fact = SlangFact.query.get_or_404(fact_id)
    
    # Проверка, что факт не является системным
    if fact.is_system:
        flash("System facts cannot be edited", "error")
        return redirect(url_for("slang_facts", region=region))
    
    # Проверка, что факт принадлежит текущему пользователю
    if fact.user_id != session["user_id"]:
        flash("You can only edit your own facts", "error")
        return redirect(url_for("slang_facts", region=region))
    
    if request.method == "POST":
        fact.title = request.form.get("title", "").strip()
        fact.content = request.form.get("content", "").strip()
        
        if not fact.title or not fact.content:
            flash("Title and content are required", "error")
        else:
            db.session.commit()
            flash("Fact updated successfully!", "success")
            return redirect(url_for("slang_facts", region=region))
    
    return render_template(
        "edit_slang_fact.html",
        nav=NAV,
        region=region,
        region_name=REGION_NAMES.get(region, region),
        fact=fact,
        title=f"Edit Fact - {REGION_NAMES.get(region, region)}"
    )

@app.route("/slang-facts/<region>/delete/<int:fact_id>", methods=["POST"])
@login_required_custom
def delete_slang_fact(region, fact_id):
    fact = SlangFact.query.get_or_404(fact_id)
    
    # Проверка, что факт не является системным
    if fact.is_system:
        flash("System facts cannot be deleted", "error")
        return redirect(url_for("slang_facts", region=region))
    
    # Проверка, что факт принадлежит текущему пользователю
    if fact.user_id != session["user_id"]:
        flash("You can only delete your own facts", "error")
        return redirect(url_for("slang_facts", region=region))
    
    db.session.delete(fact)
    db.session.commit()
    flash("Fact deleted successfully!", "success")
    return redirect(url_for("slang_facts", region=region))

if __name__ == "__main__":
    app.run(debug=True)

login_manager = LoginManager(app)
login_manager.login_view = "login"
