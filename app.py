from flask import Flask, render_template, url_for

app = Flask(__name__)

NAV = [
    {"slug": "home", "title": "Home"},
    {"slug": "diversity", "title": "Diversity of words"},
    {"slug": "america", "title": "America"},
    {"slug": "canada", "title": "Canada"},
    {"slug": "australia", "title": "Australia"},
    {"slug": "great-britain", "title": "Great Britain"},
    {"slug": "new-zealand", "title": "New Zealand"},
]

# Контент главной страницы
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

#страны
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
            "title": "Overview of New Zealand English",
            "content": (
                "New Zealand English (NZE) is a distinctive variety that developed primarily from British and "
                "Australian English influences. It is known for its unique vowel pronunciation, rising intonation, "
                "borrowed Maori vocabulary, and friendly Kiwi slang. The accent closely resembles Australian English "
                "but has several differences that make it recognisable worldwide."
            )
        },
        {
            "title": "History of New Zealand English",
            "content": (
                "New Zealand English formed in the 19th century when British settlers—mainly from southern England "
                "and Scotland—arrived in the region. Maori people, the indigenous population, contributed greatly "
                "to the vocabulary. Over time, the blend of British accents, isolation, and Maori influence shaped "
                "a unique and cohesive national English variety."
            )
        },
        {
            "title": "Pronunciation Features",
            "content": (
                "New Zealand English has several recognisable pronunciation features, especially its vowels."
            )
        },
        {
            "title": "Pronunciation Examples",
            "table": [
                ["Feature", "Example"],
                ["Short 'i' becomes 'uh'", "Fish and chips → 'fush and chups'"],
                ["Flattened 'e' sound", "Pen sounds like 'pin'"],
                ["Non-rhotic accent", "R not pronounced unless before a vowel"],
                ["Rising intonation", "Statements often sound like questions"],
                ["Closer vowels than Australian English", "Slightly tighter and sharper vowel sounds"]
            ]
        },
        {
            "title": "Vocabulary Features",
            "content": (
                "New Zealand English uses many Maori loanwords, and like Australian English, includes many shortened "
                "and informal expressions. Many nature-related words are unique to the region."
            )
        },
        {
            "title": "Common Maori Loanwords",
            "table": [
                ["Word", "Meaning"],
                ["Kia ora", "Hello / thank you / good health"],
                ["Whānau", "Family"],
                ["Kai", "Food / meal"],
                ["Aroha", "Love / compassion"],
                ["Puku", "Stomach"],
                ["Mana", "Prestige, authority, respect"]
            ]
        },
        {
            "title": "Unique New Zealand Words",
            "table": [
                ["Word", "Meaning"],
                ["Tramping", "Hiking"],
                ["Jandals", "Flip-flops"],
                ["Bach", "Small holiday house"],
                ["Togs", "Swimsuit"],
                ["Scroggin", "Trail mix"],
                ["Dairy", "Small corner shop / convenience store"]
            ]
        },
        {
            "title": "New Zealand Slang",
            "content": (
                "Kiwi slang is friendly, humorous, and often overlaps with Australian slang, but many expressions "
                "are uniquely New Zealand."
            )
        },
        {
            "title": "Examples of Kiwi Slang",
            "table": [
                ["Slang", "Meaning"],
                ["Sweet as", "All good / perfect"],
                ["Choice!", "Awesome / great"],
                ["Bro / cuzzy", "Friend / close mate"],
                ["Chur", "Thanks / cool / cheers"],
                ["Hard out", "Definitely / absolutely"],
                ["She’ll be right", "It will be fine"],
                ["Yarn", "Chat / talk"],
                ["Munted", "Broken / smashed / ruined"]
            ]
        },
        {
            "title": "Modern New Zealand Expressions",
            "content": (
                "Modern Kiwi English blends Maori vocabulary, youth slang, and global internet expressions."
            )
        },
        {
            "title": "Modern Examples",
            "table": [
                ["Slang", "Meaning"],
                ["Ghost chips", "Acting stupid (from a famous NZ ad)"],
                ["Skux", "Cool / stylish guy"],
                ["Buzzy", "Strange but interesting"],
                ["Wop-wops", "Very remote place"],
                ["Eh?", "Used at the end of sentences for emphasis"]
            ]
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
