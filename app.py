from flask import Flask, render_template
from forms import LoginForm

app = Flask(__name__)
users = {"n.chandra.kalyani@gmail.com": "ka@@@@9",
         "kalyaninunna@gmail.com": 1234}

app.config['SECRET_KEY'] = 'dfewfew123213rwdsgert34tgfd1234trgf'


@app.route('/')
def home():  # put application's code here
    return render_template("home.html")


@app.route("/login", methods=['GET', 'POST'])
def login():
    form = LoginForm()
    if form.validate_on_submit():
        for u_email, u_password in users.items():
            if u_email == form.email.data and u_password == form.password.data:
                return render_template("login.html", message="Successfully Logged In")
        return render_template("login.html", form=form, message="Incorrect Email or Password")
    elif form.errors:
        print(form.errors.items())
    return render_template("login.html", form=form)


if __name__ == '__main__':
    app.run()
