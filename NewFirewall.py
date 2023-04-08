import re
from flask import Flask, request, Response , render_template,redirect,url_for

# Define a list of valid username and password combinations
USERS = {
   'admin': 'password123',
    'user': 'password456',
    'user1': 'password789'
}

# Create an instance of the Flask class and set the name of the application
app = Flask(__name__)

# Define a function to check if the given username and password are valid
def authenticate(username, password):
    return username in USERS and USERS[username] == password

# Define a Flask route for the login page
@app.route('/login', methods=['GET', 'POST'])
def login():
    if request.method == 'POST':
        # Get the submitted username and password from the form
        username = request.form.get('username')
        password = request.form.get('password')

        # Check if the provided credentials are valid
        if authenticate(username, password):
            # If the credentials are valid, redirect to the main page
            return render_template('index.html')
        else:
            # If the credentials are invalid, show an error message
            return render_template('login.html', error='Invalid username or password')
    else:
        # If the request method is not POST, show the login form
        return render_template('login.html')


# Define a Flask route for the root URL of the web application
@app.route('/', methods=['GET', 'POST'])
def index():
     # Check if the user is authenticated
  
    if not request.authorization:
        # If not authenticated, redirect to the login page
        return redirect(url_for('login'))

    # If the user is authenticated, continue with the normal logic
    # If the request method is POST (i.e. the user has submitted data)
    if request.method == 'POST':
        # Get the submitted data from the form
        data = request.form['data']

        # Check if the user wants to enable the first firewall security
        enable_firewall1 = request.form.get('enable_firewall1')
        if enable_firewall1 == 'yes':
            # Import the security_scan function from the first firewall_security module
            from firewall_security import security_scan

            # Call the security_scan function to check for potential security issues
            if security_scan(data):
                # If the data passes the security scan, return a success message
                return "Data submitted successfully!"
            else:
                # If potential security issues are found, return an error message
                return "Security scan detected potentially malicious content in your data."

        # Check if the user wants to enable the second firewall security
        enable_firewall2 = request.form.get('enable_firewall2')
        if enable_firewall2 == 'yes':
            # Import the security_scan function from the second firewall_security module
            from firewall_security import security_scan_2

            # Call the security_scan function to check for potential security issues
            if security_scan_2(data):
                # If the data passes the security scan, return a success message
                return "Data submitted successfully!"
            else:
                # If potential security issues are found, return an error message
                return "Security scan detected potentially malicious content in your data."

        # If neither firewall security is enabled, simply return a success message
        return "Data submitted successfully!"

   
   
    # If the request method is not POST, return an HTML form asking the user which firewall security they want to enable
    else:
        return render_template('index.html')


# Start the Flask application and set it to run in debug mode
if __name__ == '__main__':
    app.run(debug=True)