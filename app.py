
from flask import Flask, render_template, request, redirect, send_from_directory, url_for, session, flash

app = Flask(__name__, template_folder='pages')


@app.route('/')
def index():
    return render_template('template.html')


@app.route('/assets/<path:path>')
def send_assets(path):
    return send_from_directory('assets', path)


if __name__ == '__main__':
    app.run(debug=True)
