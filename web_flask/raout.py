from flask import Flask, request, jsonify
from Oorem import User, Base, engine, sessionmaker # Import your ORM setup

app = Flask(__name__)

# Configure SQLAlchemy session
Session = sessionmaker(bind=engine)
session = Session()

# Initialize MySQL connection

@app.route("/users", methods=['POST'])
def home():
   return 'hllo'

if __name__ == "__main__":
    """ Main Function """
    app.run(host='0.0.0.0', port=5000, debug=True)  # Enable debug mode
