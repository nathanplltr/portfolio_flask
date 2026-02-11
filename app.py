from flask import Flask, render_template

app = Flask(__name__)

@app.route('/')
def home():
    return render_template("index.html")


@app.route('/about')
def about():
    return render_template("about.html")

@app.route("/contact")
def afficher_ma_carte():  # On change 'map' en 'afficher_ma_carte'
    return render_template("contact.html")

if __name__ == '__main__':
        app.run(debug=True, port=5000)