from flask import Blueprint, render_template, request, url_for, redirect

home = Blueprint('home', __name__, url_prefix='/home')


@home.route('/')
def home_page():
    return render_template('home/index.html')


@home.route('/search', methods=['POST'])
def search():
    print(request.form)
    return redirect(url_for('stock.quote', symbol=request.form['symbol']))