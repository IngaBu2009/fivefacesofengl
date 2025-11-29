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
        {
            "title": "Overview of Canadian English",
            "content": (
                "Canadian English (CanE) is a unique blend of British and American features. "
                "Historical ties with Britain shaped spelling and grammar, while geographical "
                "proximity to the United States influenced pronunciation, vocabulary, and slang. "
                "Canada also has strong French cultural influence, especially in Quebec, which adds "
                "unique loanwords and expressions to everyday speech."
            )
        },
        {
            "title": "Historical Development",
            "content": (
                "Canadian English began forming in the 18th–19th centuries after British loyalists "
                "migrated north during and after the American Revolution. Later immigration from Britain, "
                "Ireland, France, and Europe enriched the language even more. Today, Canadian English "
                "is considered one of the five major varieties of English worldwide."
            )
        },
        {
            "title": "Pronunciation Features",
            "content": (
                "Canadian English pronunciation resembles American General English but has unique features:"
            )
        },
        {
            "title": "Pronunciation Examples",
            "table": [
                ["Feature", "Example"],
                ["Canadian Raising", "‘About’ → pronounced closer to ‘a-boat’"],
                ["Merged vowels", "‘Caught’ and ‘cot’ sound the same"],
                ["T-word flapping", "‘Butter’ pronounced as ‘budder’"],
                ["Rounded ‘o’", "Slightly more rounded vowels in some regions"]
            ]
        },
        {
            "title": "Spelling in Canadian English",
            "content": (
                "Spelling in Canada mixes British and American traditions. This makes the system "
                "visually recognizable and distinct."
            )
        },
        {
            "title": "Spelling Examples",
            "table": [
                ["Canadian", "British", "American"],
                ["Colour", "Colour", "Color"],
                ["Centre", "Centre", "Center"],
                ["Cheque", "Cheque", "Check"],
                ["Organize / Organise", "Organise", "Organize"],
                ["Licence (noun)", "Licence", "License"]
            ]
        },
        {
            "title": "Vocabulary Differences",
            "content": (
                "Canada uses many words shared with British English, but also has its own "
                "regional expressions, often influenced by Indigenous languages and French."
            )
        },
        {
            "title": "Vocabulary Examples",
            "table": [
                ["Canadian Word", "Meaning"],
                ["Washroom", "Bathroom / restroom"],
                ["Loonie", "One-dollar coin"],
                ["Toonie", "Two-dollar coin"],
                ["Chesterfield", "Couch / sofa"],
                ["Hydro", "Electricity (from ‘hydroelectric power’)"]
            ]
        },
        {
            "title": "French Influence in Canadian English",
            "content": (
                "In bilingual regions, many everyday terms are influenced by French. "
                "This makes Canadian English notably different from both British and American varieties."
            )
        },
        {
            "title": "French-derived Canadian Terms",
            "table": [
                ["Word", "Meaning"],
                ["Québécois", "Person from Quebec; also a dialect"],
                ["Dep", "Convenience store (from dépanneur)"],
                ["Poutine", "Canadian dish of fries, cheese curds, gravy"],
                ["Terrace", "Patio / outdoor seating area"]
            ]
        },
        {
            "title": "Canadian Slang",
            "content": (
                "Canadian slang is friendly, humorous, and often region-specific. Many expressions "
                "come from Indigenous languages, French, or simply Canadian culture."
            )
        },
        {
            "title": "Examples of Canadian Slang",
            "table": [
                ["Slang", "Meaning"],
                ["Eh?", "Used to confirm, ask, or soften statements. A Canadian classic."],
                ["Toque", "Winter hat"],
                ["Keener", "A very eager student"],
                ["Double-double", "Coffee with 2 cream + 2 sugar (from Tim Hortons)"],
                ["Runners", "Sneakers / sports shoes"],
                ["Hang a Larry", "Turn left"],
                ["Hang a Roger", "Turn right"]
            ]
        },
        {
            "title": "Modern Canadian Expressions",
            "content": "Some modern Canadian slang is shared with American English but keeps its own flavour."
        },
        {
            "title": "Modern Examples",
            "table": [
                ["Slang", "Meaning"],
                ["Snowbirds", "Canadians who spend winter in warm countries"],
                ["Housecoat", "Bathrobe"],
                ["Freezie", "Frozen ice treat / popsicle"],
                ["Pop", "Soda / soft drink"],
                ["Klick", "One kilometer (borrowed from military slang)"]
            ]
        }
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
