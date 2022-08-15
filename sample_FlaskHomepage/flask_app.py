from flask import Flask, render_template, request

app = Flask(__name__)

@app.route("/")
@app.route("/home/")
@app.route("/about/")
@app.route("/contact/")
def index():
    rule = request.url_rule
    if 'home' in rule.rule:
        return render_template("home.html",home=True)
    if 'about' in rule.rule:
        return render_template("about.html",about=True)
    if 'contact' in rule.rule:
        return render_template("contact.html",contact=True)
    return render_template("home.html",home=True)

if __name__ == "__main__":
    app.run(debug=True)
