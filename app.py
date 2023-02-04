from flask import Flask, render_template

app = Flask(__name__, static_folder='static')

@app.route("/")
def index():
    return render_template("index.html")

@app.route("/book")
def book():
    return render_template("book.html")

@app.route("/offers")
def offers():
    return render_template("offers.html")

@app.route("/contact")
def contact():
    return render_template("contact.html")

if __name__ == "__main__":
    app.run(debug=True)
