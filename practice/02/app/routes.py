from flask import render_template, request
from app import app


@app.route("/")
@app.route("/index")
def index():
    return render_template("index.html", title="index")


@app.route("/throw")
def throw():
    return render_template("throw.html", title="throw")


@app.route("/catch")
def catch():
    target = request.args.get("target")
    return render_template("catch.html", target=target, title="catch")


@app.route("/number-print/<number>")
def number_print(number):
    return render_template("number_print.html", number=number, title=number)


@app.route("/calculate/<number1>/<number2>")
def calculate(number1, number2):
    n1, n2 = int(number1), int(number2)
    result = {
        "plus": n1 + n2,
        "minus": n1 - n2,
        "times": n1 * n2,
        "quotient": n1 // n2,
    }
    return render_template("calculate.html", result=result, title=calculate)
