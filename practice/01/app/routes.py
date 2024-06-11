import random
from flask import render_template, request
from app import app


@app.route("/")
@app.route("/index")
def index():
    return render_template("index.html", title="index")


@app.route("/today-dinner")
def today_dinner():
    foods = [
        "가재 비스크",
        "농부의 점심",
        "대황 파이",
        "바나나 푸딩",
        "블랙베리 코블러",
        "스파게티",
        "아티초크 소스",
        "오믈렛",
        "청나래고사리 리조또",
        "망고 스티키 라이스",
        "피자",
        "핑크 케이크",
        "행운의 점심",
    ]
    target = random.choice(foods)
    return render_template("today_dinner.html", target=target, title="menu")


@app.route("/throw")
def throw():
    return render_template("throw.html", title="throw")


@app.route("/catch")
def catch():
    word = request.args.get("word")
    return render_template("catch.html", word=word, title=word)


@app.route("/lotto-create")
def lotto_create():
    return render_template("lotto_create.html")


@app.route("/lotto")
def lotto():
    number = int(request.args.get("set_number"))
    send = list()

    for i in range(number):
        temp = random.sample(range(1, 46), k=6)
        send.append(temp)

    return render_template("lotto.html", send=send)
