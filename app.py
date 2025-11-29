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
        {
            "title": "History of British Slang",
            "content": (
                "British slang has a rich and ancient history. As early as the 17th–18th centuries, "
                "groups such as criminals, sailors, soldiers, and theatre performers developed their "
                "own specialized vocabularies. These early slang words often expressed humor, sarcasm, "
                "social criticism, or coded communication."
            )
        },
        {
            "title": "Early British Slang (17th–18th century)",
            "content": (
                "One of the earliest known slang dictionaries, 'The Dictionary of the Canting Crew' (1699), "
                "recorded the secret language of thieves and beggars. Some early slang words entered "
                "standard English and are still used today."
            )
        },
        {
            "title": "Examples (17th–18th century)",
            "table": [
                ["Slang word", "Meaning"],
                ["Addle Pate", "A foolish or inconsiderate person"],
                ["Bull Calf", "A clumsy, awkward fellow"],
                ["Corny-Faced", "A face covered with pimples"],
                ["Death’s Head Upon a Mop-Stick", "A miserable, skinny person"],
                ["Fussock", "A messy, disorganized old woman"]
            ]
        },
        {
            "title": "British vs American English",
            "content": (
                "British English differs from American English in pronunciation, intonation, spelling, "
                "vocabulary, and some grammar patterns. These differences developed over centuries of "
                "independent evolution."
            )
        },
        {
            "title": "Pronunciation Differences",
            "table": [
                ["British English", "American English"],
                ["Schedule — [ʃ]", "Schedule — [sk]"],
                ["Either/neither — [ai]", "Either/neither — [i]"],
                ["Mafia, Natasha — [æ]", "Mafia, Natasha — [a]"],
                ["Better — [t]", "Better — [d]"],
                ["City — [t]", "City — [d]"]
            ]
        },
        {
            "title": "Intonation Differences",
            "content": (
                "British English generally has a richer melodic intonation: the voice rises and falls more "
                "noticeably. American English is more monotone and often spoken at a slightly higher pitch. "
                "To many learners, British English sounds smooth and refined, while American English sounds "
                "more direct and emphatic."
            )
        },
        {
            "title": "Spelling Differences",
            "table": [
                ["British English", "American English"],
                ["Colour, honour", "Color, honor"],
                ["Favourite", "Favorite"],
                ["Centre, theatre", "Center, theater"],
                ["Catalogue, dialogue", "Catalog, dialog"],
                ["Realise, analyse", "Realize, analyze"],
                ["Counsellor", "Counselor"],
                ["Modelling", "Modeling"],
                ["Encyclopaedia", "Encyclopedia"]
            ]
        },
        {
            "title": "Vocabulary Differences",
            "content": "Britain and the United States often use completely different words for everyday objects."
        },
        {
            "title": "Vocabulary Examples",
            "table": [
                ["British English", "American English"],
                ["Autumn", "Fall"],
                ["Ill", "Sick"],
                ["Underground", "Subway"],
                ["Petrol", "Gasoline"],
                ["Shop", "Store"],
                ["Luggage", "Baggage"],
                ["Pharmacy", "Drugstore"]
            ]
        },
        {
            "title": "Grammar Differences",
            "table": [
                ["British English", "American English"],
                ["I have read this book.", "I read this book."],
                ["Have you got a brother?", "Do you have a brother?"],
                ["At the weekend", "On the weekend"]
            ]
        },
        {
            "title": "British Slang",
            "content": (
                "British slang is expressive, witty, often ironic, and varies greatly by region. "
                "It includes both traditional expressions and modern youth slang influenced by media, "
                "music, and multicultural London English (MLE)."
            )
        },
        {
            "title": "Examples of British Slang",
            "table": [
                ["Slang", "Meaning"],
                ["Alright?", "A casual greeting similar to 'How are you?'"],
                ["Mate", "Friend, buddy, pal"],
                ["Cheers", "Thank you / goodbye / good health"],
                ["Luv / Love", "Friendly term of address"],
                ["Spot on", "Exactly right"],
                ["Bang on", "Absolutely correct"],
                ["Not my cup of tea", "Not something I like"],
                ["I can't be bothered", "I'm too lazy / I don't feel like it"],
                ["That's rubbish!", "That's nonsense / bad"],
                ["Gutted", "Very upset"],
                ["Bloody hell!", "Strong emotion: surprise, anger, or frustration"]
            ]
        }
    ]
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

if __name__ == "__main__":
    app.run(debug=True)
