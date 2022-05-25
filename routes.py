from flask import Flask, render_template, request, redirect, url_for
from Forms import PaymentForm

app = Flask(__name__)

@app.route("/")
def main_page():
    return redirect(url_for("home"))

@app.route("/home")
def home():
    return render_template("home.html")

@app.route("/aboutUs")
def about_us():
    return render_template("aboutUs.html")

@app.route("/cart")
def cart():
    return render_template("cart.html")

@app.route("/payment")
def payment():
    payment_form = PaymentForm(request.form)
    if (request.method == "POST"):
        return redirect(url_for("thank_you"))
    return render_template("payment.html", form=payment_form)

@app.route("/thankyou")
def thank_you():
    return render_template("thankyou.html")

@app.route("/purchased1")
def gi_purchased():
    return render_template("confirm1.html")

@app.route("/purchased2")
def hi3_purchased():
    return render_template("confirm2.html")

@app.route("/purchased3")
def aot_purchased():
    return render_template("confirm3.html")

@app.route("/purchased4")
def bnha_purchased():
    return render_template("confirm4.html")