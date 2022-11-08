from flask import Flask, render_template, request
from calculator import evaluate

app = Flask(__name__)

@app.route("/")
def index():
    return render_template("index.html")

@app.route("/result", methods=["GET","POST"])
def add2():
    output = request.form.to_dict()
    expression = output["expression"]
    result= evaluate(expression)
    return render_template("index.html",result=result)

if __name__ == "__main__":
    app.run(debug=True)