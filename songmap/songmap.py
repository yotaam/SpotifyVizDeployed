from flask import Flask, jsonify, render_template

app = Flask(__name__)

@app.route("/")
def index():
    return render_template("globe.html")

from werkzeug.middleware.proxy_fix import ProxyFix

app.wsgi_app = ProxyFix(app.wsgi_app)

if __name__ == "__main__":
    from gunicorn.app.wsgiapp import run
    run()

