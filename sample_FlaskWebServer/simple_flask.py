from flask import Flask, render_template, request

app = Flask(__name__)

@app.route("/")
@app.route("/home/")
@app.route("/python/")
def index():
    rule = request.url_rule
    if 'home' in rule.rule:
        return "Welcome Home !!!"
    if 'python' in rule.rule:
        return "<h1>알고리즘으로 배우는 파이썬</h1>"

    return "hello world !!!"

if __name__ == "__main__":
    app.run(debug=True)
