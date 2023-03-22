import re
from flask import Flask, request, Response , render_template

# Create an instance of the Flask class and set the name of the application
app = Flask(__name__)

# Define a Flask route for the root URL of the web application
@app.route('/', methods=['GET', 'POST'])
def index():
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