"""
   *Flask: The main class used to create a Flask application.
   *request: Used to access incoming request data.
   *jsonify: A helper function to convert data to JSON format for responses.
   *Oorem: Your custom module that contains SQLAlchemy setup (engine, Base, User, and Session).
"""
from flask import Flask, request, jsonify
from Oorem import User, Base, engine, session # Import your ORM setup

app = Flask(__name__) # Creates an instance of the Flask application.

# Create User
@app.route("/users", methods=['POST']) ## Defines a route for creating a user using HTTP POST requests.
def create_user():
   data = request.get_json() ## Extracts JSON data from the request body.
   new_user = User(
      username=data['username'],
      email=data['email'],
      address=data['address'],
      phone=data['phone'],
      password=data['password']
   )
   session.add(new_user) ## Adds the new user to the session.
   session.commit() ## Commits the transaction to the database.
   return jsonify({'message': 'User created successfully'}, 201) ## Returns a JSON response with a success message

# Get All Users
@app.route('/users', methods=['GET']) ## Defines a route for retrieving all users using HTTP GET requests.
def get_users():
   users = session.query(User).all() ## Queries the database for all user records.
   ## Converts user objects to dictionaries and returns them as a JSON response.
   return jsonify([users.__dict__ for user in users])

if __name__ == "__main__":
    """ Main Function """
    app.run(host='0.0.0.0', port=5000, debug=True)  # Enable debug mode
