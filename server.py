from flask import Flask, render_template
from blueprints.stock import stock
from blueprints.home import home


app = Flask(__name__)
# Register your bluepriont
app.register_blueprint(stock)
app.register_blueprint(home, url_prefix='/home')

