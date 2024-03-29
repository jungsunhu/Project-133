# importing modules from flask library
from flask import Flask , render_template

# creating instance of class Flask, by providing __name__ keyword as argument
app = Flask(__name__)

# write the routes using decorator functions
# default route or 'URL'
@app.route("/index")
def home():

    name = "Kylie Gray" # write your name
    age = "24" # write your age

    return render_template('index.html' , name = name , age = age)

# define the route to father webpage
@app.route("/father")
def home():

    name = "Andrew Gray" # write your name
    age = "36" # write your age

    return render_template('father.html' , name = name , age = age)

# define the route to mother webpage
@app.route("/mother")
def home():

    name = "Ciara Gray" # write your name
    age = "34" # write your age

    return render_template('motehr.html' , name = name , age = age)

# define the route to friends webpage
@app.route("/friend")
def home():

    name = "Azim Rizk" # write your name
    age = "26" # write your age

    return render_template('friend.html' , name = name , age = age)

# add other routes, if you want




# run the file
if __name__  ==  '__main__':
    app.run(debug=True)
