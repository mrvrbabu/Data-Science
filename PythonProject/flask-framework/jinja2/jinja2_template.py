from flask import Flask, render_template, request

getpost = Flask(__name__)


@getpost.route('/')
def index():
    return 'Welcome to index page'


@getpost.route('/about', methods=['GET'])
def about():
    return render_template('about.html')


# @getpost.route('/form', methods=['GET', 'POST'])
# def postform():
#     if request.method == 'POST':
#         name = request.form['name']
#         return f"Welcome {name} !"
#     return render_template('form.html')


@getpost.route('/submit', methods=['GET', 'POST'])
def form():
    if request.method == 'POST':
        name = request.form['name']
        return None
        # return f"Welcome {name} !"
    return render_template('form.html')


if __name__ == "__main__":
    getpost.run(debug=True, host='0.0.0.0', port='5002')
