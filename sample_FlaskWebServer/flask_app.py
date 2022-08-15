# 30. Simple Web Server with Flask

from flask import Flask, render_template, request

app = Flask(__name__)

@app.route("/")
@app.route("/home/")
@app.route("/about/")
def index():
    rule = request.url_rule
    if 'home' in rule.rule:
        return render_template("home.html",home=True)
    if 'about' in rule.rule:
        return render_template("about.html",about=True)

    return render_template("home.html",home=True)

if __name__ == "__main__":
    app.run(debug=True)
