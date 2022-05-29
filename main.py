import random

from flask import Flask, render_template, make_response, request

app = Flask(__name__)


@app.route('/')
def index():
    return render_template("index.html")


@app.route('/about')
def about_me():
    return render_template("about.html")


@app.route('/portfolio')
def portfolio():
    return render_template("portfolio.html")


@app.route('/portfolio/fur_salon')
def fur_salon():
    return render_template("index_fur_salon.html")


@app.route('/portfolio/boogle')
def boogle():
    return render_template("boogle_index.html")


@app.route('/portfolio/fakebook')
def fakebook():
    return render_template("fakebook_index.html")


@app.route('/portfolio/game', methods=["GET"])
def game():
    secret_number = request.cookies.get("secret_number")

    response = make_response(render_template("game.html"))
    if not secret_number:
        new_secret = random.randint(1, 30)
        response.set_cookie("secret_number", str(new_secret))

    return response


@app.route('/result', methods=["POST"])
def result():
    guess = int(request.form.get("guess"))
    secret_number = int(request.cookies.get("secret_number"))

    if guess == secret_number:
        message = f"Correct! The secret number is {secret_number}."
        response = make_response(render_template("result.html", message=message))
        response.set_cookie("secret_number", str(random.randint(1, 30)))
        return response

    elif guess > secret_number:
        message = "Your guess is not correct... Try something smaller."
        return render_template("result.html", message=message)

    elif guess < secret_number:
        message = "Your guess is not correct... Try something bigger."
        return render_template("result.html", message=message)


if __name__ == '__main__':
    app.run(use_reloader=True, debug=True)
