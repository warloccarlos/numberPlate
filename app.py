from flask import Flask, render_template, url_for, request
from numberPlate import numplate

app = Flask(__name__)


@app.route("/", methods=['GET', 'POST'])
def index():
    return render_template('index.html')


@app.route("/seed", methods=['GET', 'POST'])
def seed():
    if request.method == 'POST':
        seed = request.form.get('seed')
        options = numplate(int(seed))
        count = len(options)
        return render_template('seed.html', options=options, count=count, show='yes')
    return render_template('seed.html')


@app.route('/destiny', methods=['GET', 'POST'])
def destiny():
    if request.method == 'POST':
        destiny = request.form.get('destiny')
        options = numplate(int(destiny))
        count = len(options)
        return render_template('destiny.html', options=options, count=count, show='yes')
    return render_template('destiny.html')


@app.route("/about")
def about():
    return render_template('about.html')


if __name__ == '__main__':
    app.run()
