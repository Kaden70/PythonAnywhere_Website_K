from flask import Flask, render_template, request
from random import choice
import string

nouns = [
    "+arm+", "red", "plant", "milk", "cereal", "game", "Plants vs. Zombies",
    "Kaden", "improvised explosive device", "United States", "oil", "shotgun",
    "Kitters", "Munger", "baked bean", "peashooter", "citron", "ant: .",
    "the big one", "Zomboss", "King K. Rool", "Sayori", "Brownie!",
    "White White", "Gordon Freeman", "The Combine", "power armor", "The Matrix",
    "Kim Jong Un", "Donald Trump", "Extra Special Forces", "{:-)",
    "Kim Jong Dos", "Diddy Kong", "Ice Climber", "Terry Davis", "Kim Jong Tres",
    "Hays", "Connor", "Iain", "Geo Metry Desh", "cool dude B)", "Clubstep",
    "blueberry milk", "Vinchint", "Lesser Dog", "Ashleen", "Lineux", "Coley",
    "Diddy's party", "RyLee"
]
verbs = [
    "blackmailed", "coerced", "bonked", "exploded", "slathered", "Kadenified",
    "erased", "lasered", "tazed", "altered", "became special", ":)", "jellied",
    "squeezed", "juiced", "obliterated", "kidnapped", "fed", "eaten",
    "hee-hee-hee-ha'd", "slimed", "tapped-out", "contraband searched"
]
adjectives = [
    ":-}", "large", "based", "pink", "gelatinous", "ultra cool",
    "wickly cool", "big boy", "brilliant", "special", "cloudy", "radioactive",
    "dusty", "nuclear", "boring and plain", "a little bit too normal", ":(",
    "funny", "uncommonly rare", "Tedilicious"
]

accepted_hex_chars = ["0", "1", "2", "3", "4", "5", "6", "7", "8", "9", "A", "B", "C", "D", "E", "F", "a", "b", "c", "d", "e", "f"]

app = Flask(__name__)

# This function is used for the hex code route.
def valid_hex_chars(parameter_name: str) -> bool:
    for char in parameter_name:
        if char not in accepted_hex_chars:
            return False
    return True

# Functions used for the Caesar Cipher
def alphabet_position(char):
    return string.ascii_lowercase.find(char.lower())

def shift_character(char, shift):
    if char.lower() not in string.ascii_lowercase:
        return char
    new_index = (alphabet_position(char) + shift)%26
    new_char = string.ascii_lowercase[new_index]
    if char.isupper():
        return new_char.upper()
    else:
        return new_char

def encrypt_with_shift(text, shift):
    new_message = ''
    for char in text:
        new_message += shift_character(char, shift)
    return new_message
# End of functions used for the Caesar Cipher

@app.route('/')
def hello_world():
    return '''
    <head>
        <link rel="stylesheet" href="static/style.css">
    </head>
    <body>
        <h1>Hello World</h1>
        <div>
            <h2>Website</h2>
            <p style="color: red;">Python</p><br>
            <button><a href="https://github.com/Kaden70">Click this button</a></button><br>
            <form><br>
                <input type="Hello"></input>
            </form>
            <a href="https://kaden70.github.io/">Github Site</a><br>
            <a href="/grapefruit">Go to the Grapefruit Page</a><br>
            <a href="/lime">Go to the Lime Page</a><br>
            <a href="/pvzgw2">Go to the PVZGW2 Page</a><br>
            <a href="/giftest">Go the the Gif Test Page</a><br>
            <a href="/madlibpage">Go to the Madlibs Page</a><br>
            <a href="/first_form">Go to the Form</a><br>
            <a href="/hex_form">Go to the Hex Color Page (Starter Code Used)</a><br>
            <a href="/web_caesar">Go the the Caesar Cipher Page (Starter Code Used)</a>
        </div>
    </body>
    '''

@app.route("/grapefruit")
def grapefruit():
    return '''
    <head>
        <style>
            body {
                background-color: #EB8676;
            }
            .middle {
                display: block;
                margin-right: auto;
                margin-left: auto;
                width: 50%;
            }
        </style>
    </head>
    <body>
        <a href="/">Back</a>
        <h1 style="text-align: center;">Grapefruit Page</h1><br>
        <img src="https://pngimg.com/uploads/grapefruit/grapefruit_PNG15251.png" class="middle">
    </body>
    '''

@app.route("/lime")
def lime():
    return '''
    <head>
        <style>
            body {
                background-color: #E8F48C;
            }
            .middle {
                display: block;
                margin-right: auto;
                margin-left: auto;
                width: 50%;
            }
        </style>
    </head>
        <a href="/">Back</a>
        <h1 style="text-align: center;">Lime Page</h1>
        <br>
        <img src="https://pngimg.com/uploads/lime/lime_PNG18.png" style="display: block; width: 50%; margin-left: auto; margin-right: auto;">
    <body>
    </body>
    '''

@app.route("/pvzgw2")
def pvzgw2():
    return '''
    <head>
        <style>
            body {
                background: repeating-conic-gradient(
                    #6a5acd 0% 25%,
                    #3cb371 0% 50%
                );
                background-size: 75px 75px;
            }
        </style>
    </head>
    <body>
        <div style="position: absolute; padding: 6px; border: 2px solid black; background-color: lightgray; top: 0%; left: 0%; right: 0%;">
            <a href="/">Back</a>
            <h1 style="text-align: center; position: relative;">PVZGW2</h1>
        </div><br>
        <div style="border: 4px solid black; margin-top: 40%; margin-left: 40%; margin-right: 40%;">
            <h1>Pea</h1><br>
            <img src="https://static.tvtropes.org/pmwiki/pub/images/peashutur.png" style="display: block; margin-left: auto; margin-right: auto;">
        </div>
    </body>
    '''

@app.route("/giftest")
def gifTest():
    return '''
    <html>
    <head>
        <style>
            body {
                background: url("https://clan.fastly.steamstatic.com/images/8331399/b9bc4cae11a01e78843e204c15a11041c5c99f82.gif") no-repeat;
                background-size: cover;
            }
        </style>
    </head>
    <body>
        <a href="/">Back</a>
    </body>
    </html>
    '''

@app.route("/madlibpage")
def madlib_stuff():
    return render_template("og_template.html",
        n = choice(nouns),
        n2 = choice(nouns),
        n3 = choice(nouns),
        n4 = choice(nouns),
        a = choice(adjectives),
        a2 = choice(adjectives),
        v = choice(verbs),
        v2 = choice(verbs)
    )

@app.route("/first_form")
def first_form():
    return render_template("first_form.html")

@app.route("/first_form_results", methods=["POST"])
def results():
    color = request.form["color"].lower().strip()
    colorList = ["red", "blue", "green", "yellow", "white", "black", "brown", "pink", "purple", "gray", "orange", "pastel", "maroon", "salmon"]
    game = request.form["game"]
    number = request.form["number"]
    if color not in colorList:
        color = "{0} is not a valid color sorry on here yet sorry".format(color.title())
    else:
        color = color.title()
    return render_template("fform_results.html", color = color, game = game.title(), number = number)

@app.route('/hex_form', methods=["GET", "POST"])
def hex_form():
    if request.method == 'POST':
        hex = request.form['hex']
        if not valid_hex_chars(hex) or len(hex) < 6 or len(hex) > 6:
            hex = 'FF0000'
            feedback = "Invalid color. It might be because you entered more than 6 characters, less than 6 characters, or entered an invalid character."
        elif len(hex) == 6 and valid_hex_chars(hex):
            hex = hex
            feedback = "Submitted!"
    else:
        hex = '00FF00'
        feedback = ''

    return render_template("hex_form.html", hex = hex, feedback = feedback)

@app.route("/web_caesar", methods=["GET", "POST"])
def web_caesar():
    if request.method == 'POST':
        o_message = request.form.get("Text_Entered")
        Shift_Number = int(request.form.get("Shift_Number"))
        Cypher = request.form.get("Cypher")
        if Cypher == "encrypt":
            c_message = encrypt_with_shift(o_message, Shift_Number)
        elif Cypher == "decrypt":
            c_message = encrypt_with_shift(o_message, -Shift_Number)
        else:
            c_message = ""

        display_text = c_message
    else:
        o_message = ""
        c_message = ""
        Shift_Number = ""
        display_text = ""
        Cypher = ""
    return render_template("web_caesar.html", o_message = o_message, c_message = c_message, Shift_Number = Shift_Number, Cypher = Cypher, display_text = display_text)
