# Variable Rule 

# Jinja template 

'''
{{ }} expression to print out in html 
{% .... %} Conditions and loops 
{#... #} This is for comments
'''
from flask import Flask, render_template, request

getpost = Flask(__name__)


@getpost.route('/')
def index():
    return 'Welcome to index page'


@getpost.route('/about', methods=['GET'])
def about():
    return render_template('about.html')


@getpost.route('/submit', methods=['GET', 'POST'])
def submit():
    if request.method == 'POST':
        name = request.form['name']
        return f"Welcome {name} !"
    return render_template('form.html')

# Variable Rule 

@getpost.route('/success/<score>')
def success(score):
    return "You have scored " + score


# Jinja2 Template 

@getpost.route('/marks/<int:myscore>')
def marks(myscore):
    res=""
    if myscore >= 50:
        res="PASSED"
    else:
        res="FAILED"
        
    return render_template('results.html', results=res)


@getpost.route('/successres/<int:myscore>')
def successres(myscore):
    res=""
    if myscore >= 50:
        res="PASSED"
    else:
        res="FAILED"
        
    exp = {'score': myscore, "res": res}
        
    return render_template('myresults.html', results=exp)

# if else condition 
@getpost.route('/successif/<int:newscore>')
def successif(newscore):
    return render_template('successifi.html', newscore=newscore)


if __name__ == "__main__":
    getpost.run(debug=True, host='0.0.0.0', port='5000')
