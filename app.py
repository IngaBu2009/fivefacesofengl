from flask import Flask, render_template

from regions.america import REGION_AMERICA
from regions.canada import REGION_CANADA
from regions.greatbritain import REGION_GB
from regions.australia import REGION_AU
from regions.newzealand import REGION_NZ

app = Flask(__name__)

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
    "great-britain": REGION_GB,
    "america": REGION_AMERICA,
    "canada": REGION_CANADA,
    "australia": REGION_AU,
    "new-zealand": REGION_NZ
}


@app.route("/")
def index():
    return render_template("index.html", nav=NAV, home=HOME_CONTENT)

@app.route("/about/")
def about():
    return render_template("about.html", title="About the Project", nav=NAV)

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
