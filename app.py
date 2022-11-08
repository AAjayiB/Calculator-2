from flask import Flask, render_template, request
from calculator import calculate

app = Flask(__name__)

@app.route("/")
def index():
    return render_template("index.html")

@app.route("/result", methods=["GET","POST"])
def add2():
    output = request.form.to_dict()
    expression = output["expression"]
    result= calculate(expression)
    return render_template("index.html",result=result)

if __name__ == "__main__":
    app.run(host="0.0.0.0")