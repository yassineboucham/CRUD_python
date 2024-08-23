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
   return jsonify([user.__dict__ for user in users])

# Get User by ID
@app.route('/users/<int:id>', methods=['GET']) ## Defines a route for retrieving a specific user by ID using HTTP GET requests.
def get_user(id):
   user = session.query(User).filter(User.id == id).first() ## Queries for a user with the given ID
   if user:
      return jsonify(user.__dict__) #Returns the user’s details as a JSON response if the user is found.
   else:
      return jsonify({'message': 'User not found'}), 404 #Returns an error message and HTTP status code 404

# Update User by ID
@app.route('/users/<int:id>', methods=['PUT']) ## Defines a route for updating a specific user by ID using HTTP PUT requests.
def update_user(id):
   data = request.get_json() ## Extracts the updated data from the request body.
   user = session.query(User).filter(User.id == id).first() ## Finds the user with the given ID.
   if user:
      user.username = data['username']
      user.email = data['email']
      user.address = data['address']
      user.phone = data['phone']
      user.password = data['password']
      session.commit()
      return jsonify({'message', 'User updated successfully'})
   else:
      return jsonify({'message': 'User not found'}), 404

# Delete User by ID
@app.route('/user/<int:id>', methods = ['DELETE']) ## Defines a route for deleting a specific user by ID using HTTP DELETE requests.
def delete_user(id):
   user = session.query(User).filter(User.id == id).first() ## Finds the user with the given ID.
   if user:
      session.delete(user) ## Deletes the user from the session.
      session.commit() ## Commits the transaction to the database.
      return jsonify({'message': 'User deleted successfully'})
   else:
      return jsonify({'message': 'User not found'}), 404

if __name__ == "__main__":
    """ Main Function """
    app.run(host='0.0.0.0', port=5000, debug=True)  # Enable debug mode
