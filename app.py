from flask import Flask, render_template, url_for

app = Flask(__name__)

# Навигация (копия структуры с сайта)
NAV = [
    {"slug": "home", "title": "Home"},
    {"slug": "diversity", "title": "Diversity of words"},
    {"slug": "america", "title": "America"},
    {"slug": "canada", "title": "Canada"},
    {"slug": "australia", "title": "Australia"},
    {"slug": "great-britain", "title": "Great Britain"},
    {"slug": "new-zealand", "title": "New Zealand"},
]

# Контент главной страницы (основной текст с Google Sites)
HOME_CONTENT = {
    "title": "The 5 faces of English",
    #"lead": (
    #   "Our project is called “Sweet, lollies and candies – choose your English” "
    #    "because we decided to help people learn the variations of English in different Anglican countries. "
    #    "And in particular in America, Great Britain, Canada and Australia."
    # ),
    "why": [
        "Cultural Immersion: Learning different varieties of English allows you to immerse yourself in different cultures and societies. Each country has its own unique traditions, customs and history, which are reflected in the language. Learning different varieties of English helps you understand local expressions, accents, and cultural nuances, which enriches your language skills and allows you to better understand and interact with native speakers.",
        "Professional Opportunities: Learning different varieties of English can be beneficial for professional development. Some companies or industries may prefer a particular variation of English, and knowing that variation can be an advantage when looking for a job or advancing your career. For example, knowledge of British English can be useful when working in the UK or with British companies.",
        "Linguistic diversity: Each variation of the English language has its own characteristics in grammar, pronunciation and vocabulary. Studying different variations allows us to delve deeper into these differences and better understand how language develops and adapts to different contexts. This may be especially interesting for people interested in linguistics and linguistics.",
        "Travel and Communication: Learning different varieties of English makes it easier to travel and communicate with native speakers from different countries. When you travel, you encounter different accents and expressions, and knowing different varieties of English helps you better understand and be understood in different situations."
    ],
        #"sources": [
        #    "https://www.planetware.com/tourist-attractions/australia-aus.htm",
        #    "https://en.wikipedia.org/wiki/History_of_the_United_States",
            # ... можно перечислить остальные источники
    #]
}

#егионов
REGIONS = {
    "america": {
        "title": "America",
        "sections": [
            {"title": "Culture", "content": "Короткое описание культуры Америки..."},
            {"title": "History", "content": "Короткое описание истории..."},
            {"title": "Attractions", "content": "Достопримечательности..."},
            {"title": "Language", "content": "Особенности английского языка в США..."},
        ]
    },
    "canada": {
        "title": "Canada",
        "sections": [
            {"title": "Culture", "content": "Короткое описание культуры Канады..."},
            {"title": "History", "content": "Короткое описание истории..."},
            {"title": "Attractions", "content": "Достопримечательности..."},
            {"title": "Language", "content": "Особенности английского языка в Канаде..."},
        ]
    },
    "australia": {
        "title": "Australia",
        "sections": [
            {"title": "Culture", "content": "что-то про австралию"},
            {"title": "History", "content": "Короткое описание истории..."},
            {"title": "Attractions", "content": "Достопримечательности..."},
            {"title": "Language", "content": "Особенности английского языка в Австралии..."},
        ]
    },
    "new-zealand": {
        "title": "New Zealand",
        "sections": [
        {
            "title": "Culture",
            "content": "New Zealand has a rich blend of Māori and European (Pākehā) cultural traditions. "
                       "The Māori language and customs play a major role in national identity, and concepts like "
                       "‘whānau’ (family) and ‘mana’ (prestige/honour) are widely respected."
        },
        {
            "title": "History",
            "content": "New Zealand was originally settled by the Māori people in the 13th century. "
                       "European explorers arrived in the 17th century, and British colonization intensified in the 19th century. "
                       "The Treaty of Waitangi (1840) is a foundational historical document."
        },
        {
            "title": "Attractions",
            "content": "New Zealand is famous for its breathtaking landscapes: fjords, volcanoes, beaches, and mountains. "
                       "Popular destinations include Milford Sound, Rotorua, Tongariro National Park, and Hobbiton."
        },
        {
            "title": "Language",
            "content": "New Zealand English has its own unique pronunciation and vocabulary. "
                       "It includes many Māori loanwords such as ‘kia ora’ (hello), ‘kai’ (food) and ‘haka’ (dance/challenge). "
                       "The accent is similar to Australian English, but softer and more vowel-shifted."
        }
    ]
},

    "great-britain": {
        "title": "Great Britain",
        "sections": [
            {"title": "Culture", "content": "Короткое описание культуры Британии..."},
            {"title": "History", "content": "Короткое описание истории..."},
            {"title": "Attractions", "content": "Достопримечательности..."},
            {"title": "Language", "content": "Особенности британского английского..."},
        ],

    },
}

@app.route("/")
def index():
    return render_template("index.html", nav=NAV, home=HOME_CONTENT)

@app.route("/<slug>/")
def page(slug):
    if slug == "home":
        return index()
    if slug == "diversity":
        return render_template("region.html", nav=NAV, region={"title": "Diversity of words", "sections":[{"title":"Intro","content":"Материал о разнообразии слов..."}]})
    region = REGIONS.get(slug)
    if region:
        return render_template("region.html", nav=NAV, region=region)
    return render_template("region.html", nav=NAV, region={"title":"Not found","sections":[{"title":"404","content":"Страница не найдена"}]}), 404

if __name__ == "__main__":
    app.run(debug=True)
