# -------Flask first program----------- #

# import the Flask class from the flask package
from flask import Flask

# create application object
app = Flask(__name__)

# use decorator pattern
# to link view function to an url

@app.route("/")
@app.route("/hello")

# define view using a function, which returns a string

def hello_world():
    return "Hello world!"

# start the development server using the run() method
if __name__ == "__main__":
    app.run(host="0.0.0.0", port=80)
