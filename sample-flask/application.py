from pickle import TRUE
from flask import *
app = Flask(__name__)

@app.route("/")
def index():
  return "<h1>Hello World</h1>"

if __name__ == "__main__":
  app.run(debug=True)
