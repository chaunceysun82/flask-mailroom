import os

from flask import Flask, render_template, request, redirect, url_for, session

from model import Donation, Donor, Admin

from peewee import DoesNotExist

from passlib.hash import pbkdf2_sha256

app = Flask(__name__)
# app.secret_key = b"\xe0,C\xce\xc3\xab\xe7Q\xf0\xe9H]\x8a\x14s'W\x1d\xa4\xb0\xeaS\xd8\x1b"
app.secret_key = os.environ.get('SECRET_KEY').encode()


@app.route('/')
def home():
    return redirect(url_for('all'))


@app.route('/donations')
def all():
    donations = Donation.select()
    return render_template('donations.jinja2', donations=donations)


@app.route('/login', metqqhods=['GET', 'POST'])
def login():
    if request.method == 'POST':
        try:
            user = Admin.get(Admin.user == request.form.get('username'))
        except DoesNotExist:
            user = None

        if user and pbkdf2_sha256.verify(request.form.get('password'), user.password):
            session['username'] = request.form['password']

            return redirect(url_for('create'))
        return render_template('login.jinja2', error="Incorrect username or password")
    return render_template('login.jinja2')


@app.route('/create', methods=['GET', 'POST'])
def create():
    if 'username' not in session:
        return redirect(url_for('login'))
    else:
        if request.method == 'POST':
            try:
                donor = Donor.get(name=request.form.get('name'))
            except DoesNotExist:
                donor = Donor.create(name=request.form.get('name'))

            Donation.create(donor=donor, value=request.form.get('amount'))

            return redirect(url_for('all'))

        return render_template('create.jinja2')


@app.route('/view')
def view():
    try:
        donor = Donor.get(name=request.args.get('name'))
    except DoesNotExist:
        return render_template('view.jinja2', error="Donor does not exist")

    donations = Donation.select().where(Donation.donor == donor)
    return render_template('donations.jinja2', donations=donations)


if __name__ == "__main__":
    port = int(os.environ.get("PORT", 6738))
    app.run(host='0.0.0.0', port=port)

