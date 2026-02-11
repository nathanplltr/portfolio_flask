from flask import Flask

app = Flask(__name__)

@app.route('/')
def home():
    return "Bienvenue sur ma page d'accueil !"

@app.route('/about')
def about():
    return "À propos de moi : Je suis en train d'apprendre à développer des applications web avec Flask !"

@app.route("/map")
def map():
    # C'est votre nouvelle page
    return render_template("map.html")

if __name__ == '__main__':
        app.run(debug=True)