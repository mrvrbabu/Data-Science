# from flask import Flask

# app = Flask(__name__)

# @app.route('/hello/<name>')
# def index(name):
#     return f"Hell {name}!"


# @app.route('/blog/<int:postID>')
# def blogpost(postID):
#     return f"Blog post number is {postID}"

# @app.route('/blog/<float:floatID>')
# def floatpost(floatID):
#     return f"Blog post float version is {floatID}"


# if __name__ == '__main__':
#     app.run(debug=True, host='0.0.0.0')


########

# from flask import Flask

# app = Flask(__name__)

# @app.route('/flask')
# def flask():
#     return "Welcome to flask"

# @app.route('/python/')
# def python():
#     return "Welcome to python"


# if __name__ == '__main__':
#     app.run(debug=True, host='0.0.0.0')


from flask import Flask, render_template

'''
This creates an interface of the Flask class
which will be your WSGI(Web Server Gateway Interface) application 
'''

# WSGI Application
app = Flask(__name__)


@app.route('/')
def index():
    return render_template("index.html")


@app.route('/index')
def welcome():
    return "Welcome to my page..."


@app.route('/about')
def about():
    return render_template('aboutus.html')


if __name__ == '__main__':
    app.run(debug=True, host='0.0.0.0', port=5001)
