from flask import Flask,render_template

app = Flask(__name__)


@app.route('/')
def index():  # put application's code here
    return render_template('client/index.html')

@app.route('/donate')
def donate():  # put application's code here
    return render_template('client/donate.html')


@app.route('/aboutus')
def aboutus():  # put application's code here
    return render_template('client/aboutus.html')


@app.route('/contact')
def contact():  # put application's code here
    return render_template('client/contact_index.html')

if __name__ == '__main__':
    app.run()
