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
        {
            "title": "History of American Slang",
            "content": (
                "American slang began forming in the 18th–19th centuries and developed rapidly under "
                "influences such as immigration, frontier life, jazz culture, mass media, and the Internet. "
                "Each historical period added unique expressions to the language, reflecting cultural shifts."
            )
        },
        {
            "title": "18th–19th Century American Slang",
            "content": (
                "During the Industrial Revolution and the early formation of the United States, many new slang "
                "terms appeared. Immigration, gold rush culture, and rapid urban growth contributed to the "
                "emergence of uniquely American vocabulary."
            )
        },
        {
            "title": "Examples (18th–19th century)",
            "table": [
                ["Slang word", "Meaning"],
                ["Clam", "A dollar"],
                ["Dewdropper", "An unemployed young man who sleeps all day"],
                ["Noodle juice", "Tea"],
                ["Cat’s meow", "Something stylish or luxurious"]
            ]
        },
        {
            "title": "The Jazz Age (1920s)",
            "content": (
                "The 1920s brought jazz culture, youth rebellion, and new communication styles. "
                "Musicians invented words that quickly spread nationwide, such as 'groovy', 'hip', and 'cool'. "
                "Women’s independence also influenced slang during this era."
            )
        },
        {
            "title": "Examples (1920s)",
            "table": [
                ["Slang word", "Meaning"],
                ["Bombing", "Poor performance"],
                ["Chops", "Musical talent"],
                ["Jam", "Informal music session"],
                ["Threads", "Stylish clothes"]
            ]
        },
        {
            "title": "1940s–1960s Slang",
            "content": (
                "Mid-century slang was shaped by World War II, television, and the rise of teenage culture. "
                "Rock ‘n’ roll introduced phrases like 'cool cat' and 'far out'. Anti-war movements contributed "
                "more political and expressive slang."
            )
        },
        {
            "title": "Examples (1940–1960s)",
            "table": [
                ["Slang word", "Meaning"],
                ["Twitterpatted", "Very much in love"],
                ["Cancelled stamp", "Shy and modest girl"],
                ["Tickety-boo", "Everything is fine"],
                ["Jeddarty-jiddarty", "Something confusing"]
            ]
        },
        {
            "title": "The Digital Revolution (1990s–2000s)",
            "content": (
                "The Internet transformed slang creation. Abbreviations and online expressions spread instantly "
                "across forums, chats, and early social media platforms. Many of them are still widely used."
            )
        },
        {
            "title": "Examples (1990–2000s)",
            "table": [
                ["Slang word", "Meaning"],
                ["LOL", "Laugh Out Loud"],
                ["TBH", "To Be Honest"],
                ["IDK", "I don't know"],
                ["BRB", "Be Right Back"]
            ]
        },
        {
            "title": "Modern Internet Slang (2000–2025)",
            "content": (
                "Emerging from social media, gaming culture, streaming platforms, and meme communities, "
                "modern slang spreads globally in hours. Many expressions originate from TikTok, Twitter, "
                "and online fandoms."
            )
        },
        {
            "title": "Examples (2000–2025)",
            "table": [
                ["Slang word", "Meaning"],
                ["GOAT", "Greatest Of All Time"],
                ["No cap 🧢", "Honestly, no lie"],
                ["Slay", "Do something brilliantly"],
                ["Delulu", "Being overly optimistic or in illusions"]
            ]
        },
        {
            "title": "Differences Between American and British English",
            "content": (
                "American English differs from British English in pronunciation, intonation, spelling, vocabulary, "
                "and sometimes grammar. These differences developed through centuries of cultural separation."
            )
        },
        {
            "title": "Pronunciation Differences",
            "table": [
                ["British English", "American English"],
                ["Schedule: [ʃ]", "Schedule: [sk]"],
                ["Either/neither: [ai]", "Either/neither: [i]"],
                ["Car: [a:]", "Car: [a:r]"],
                ["Better: [t]", "Better: [d]"],
            ]
        },
        {
            "title": "Spelling Differences",
            "table": [
                ["British", "American"],
                ["Colour", "Color"],
                ["Favourite", "Favorite"],
                ["Centre / theatre", "Center / theater"],
                ["Realise / analyse", "Realize / analyze"]
            ]
        },
        {
            "title": "Vocabulary Differences",
            "table": [
                ["British English", "American English"],
                ["Autumn", "Fall"],
                ["Ill", "Sick"],
                ["Petrol", "Gasoline"],
                ["Underground", "Subway"],
                ["Shop", "Store"]
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
            "title": "Modern American Slang (General Use)",
            "content": "Common everyday American slang expressions used in casual speech."
        },
        {
            "title": "Examples of American Slang",
            "table": [
                ["Slang", "Meaning"],
                ["What's up? / Sup?", "Universal greeting"],
                ["Yo!", "Informal greeting or attention grabber"],
                ["I'm down", "I agree / I'm in"],
                ["For sure", "Absolutely"],
                ["My bad", "My mistake"],
                ["That's sick!", "Amazing, awesome"],
                ["Are you kidding me?", "Strong surprise"]
            ]
        }
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
"australia": {
    "title": "Australia",
    "sections": [
        {
            "title": "Overview of Australian English",
            "content": (
                "Australian English (AusE) is a unique variety that developed from British, Irish, and later "
                "multinational influences. It is known for its distinctive pronunciation, relaxed rhythm, and "
                "creative slang. Many expressions reflect Australian lifestyle, humour, nature, and multiculturalism."
            )
        },
        {
            "title": "History of Australian English",
            "content": (
                "Australian English formed in the early 19th century when British and Irish settlers, convicts, "
                "and soldiers arrived on the continent. The blending of many British regional accents created a "
                "new, stable variety within just two to three generations. Later migration from Europe and Asia "
                "also influenced vocabulary and pronunciation."
            )
        },
        {
            "title": "Pronunciation Features",
            "content": (
                "Australian English pronunciation resembles British English but has several distinctive features:"
            )
        },
        {
            "title": "Pronunciation Examples",
            "table": [
                ["Feature", "Example"],
                ["Flat /æ/ sound", "‘Cat’ sounds like ‘ket’"],
                ["R is not pronounced", "Car → ‘cah’, weather → ‘weath-ah’"],
                ["High rising intonation", "Statements sometimes sound like questions"],
                ["Nasal vowels", "Slight nasal quality compared to other accents"],
                ["Broad accent", "Strong slang-style pronunciation (rural areas)"]
            ]
        },
        {
            "title": "Vocabulary Features",
            "content": (
                "Australian vocabulary contains many unique words related to nature, climate, animals, "
                "and daily life. Abbreviations are extremely common in Australian English — more than in "
                "any other variety."
            )
        },
        {
            "title": "Common Australian Words",
            "table": [
                ["Word", "Meaning"],
                ["Bush", "Rural area / wilderness"],
                ["Arvo", "Afternoon"],
                ["Barbie", "Barbecue"],
                ["Brekkie", "Breakfast"],
                ["Sunnies", "Sunglasses"],
                ["Uni", "University"],
                ["Footy", "Australian football"],
                ["Mozzie", "Mosquito"]
            ]
        },
        {
            "title": "Australian Grammar Features",
            "content": "Grammar is similar to British English, but some expressions are uniquely Australian."
        },
        {
            "title": "Grammar Examples",
            "table": [
                ["Expression", "Meaning"],
                ["Heaps of", "A lot of"],
                ["Good on you!", "Well done / proud of you"],
                ["No worries", "It's okay / you're welcome / don't worry"],
                ["As well → as well / too", "Used more frequently than 'also'"]
            ]
        },
        {
            "title": "Influence of Indigenous Languages",
            "content": (
                "Many Australian English words come from Aboriginal languages, especially names of animals, "
                "plants, and geographical features. These words give Australian English its cultural depth."
            )
        },
        {
            "title": "Indigenous Loanwords",
            "table": [
                ["Word", "Meaning"],
                ["Kangaroo", "Large jumping marsupial"],
                ["Koala", "Tree-dwelling marsupial"],
                ["Boomerang", "Curved throwing tool"],
                ["Wombat", "Burrowing animal"],
                ["Billabong", "Waterhole / oxbow lake"]
            ]
        },
        {
            "title": "Australian Slang",
            "content": (
                "Australian slang (also known as 'Strine') is colourful, humorous, and full of abbreviations. "
                "It reflects the relaxed and friendly nature of Australian culture."
            )
        },
        {
            "title": "Popular Australian Slang",
            "table": [
                ["Slang", "Meaning"],
                ["G'day", "Hello"],
                ["Mate", "Friend"],
                ["No worries", "Everything is okay"],
                ["Fair dinkum", "Genuine / honest / real"],
                ["She’ll be right", "Everything will be fine"],
                ["Ripper", "Fantastic / great"],
                ["Chockers", "Very full / crowded"],
                ["Macca’s", "McDonald's"],
                ["Bogan", "Uncouth person; similar to 'redneck'"],
                ["Servo", "Gas station"],
                ["Bottle-o", "Liquor store"]
            ]
        },
        {
            "title": "Modern Australian Expressions",
            "content": "Some contemporary slang mixes English with global Internet culture and youth language."
        },
        {
            "title": "Modern Examples",
            "table": [
                ["Slang", "Meaning"],
                ["Yeah, nah", "Politely 'no'"],
                ["Nah, yeah", "Actually 'yes'"],
                ["Deadset", "Seriously / definitely"],
                ["Woop woop", "Very remote area"],
                ["Snag", "Sausage"],
                ["Trackies", "Track pants / joggers"]
            ]
        }
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
