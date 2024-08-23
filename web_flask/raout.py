from flask import Flask, render_template, request, redirect
from Oorem import User, session

app = Flask(__name__)

# Initialize MySQL connection

@app.route("/", strict_slashes=False)
def home():
   return 'hllo'

if __name__ == "__main__":
    """ Main Function """
    app.run(host='0.0.0.0', port=5000, debug=True)  # Enable debug mode
