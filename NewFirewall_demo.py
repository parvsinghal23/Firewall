import re
from flask import Flask, request, Response , render_template

# Create an instance of the Flask class and set the name of the application
app = Flask(__name__)

# Define a function to check if the user has answered at least one firewall security question
def has_answered_security_question():
    enable_firewall1 = request.form.get('enable_firewall1')
    enable_firewall2 = request.form.get('enable_firewall2')
    return enable_firewall1 is not None or enable_firewall2 is not None or request.method == 'GET'

# Define a Flask route for the root URL of the web application
@app.route('/', methods=['GET', 'POST'])
def index():
    # If the request method is POST (i.e. the user has submitted data)
    if request.method == 'POST':
        # Check if the user has answered at least one firewall security question and if the answer is yes or no
        if not has_answered_security_question() or (request.form.get('question') == 'yes' or request.form.get('question') == 'no'):
            return "Please answer at least one security question with a yes or no response to access the input box."

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
                return render_template('formvalidation.html')
            else:
                # If potential security issues are found, return an error message
                return "Security scan detected potentially malicious content in your data."
        if enable_firewall1 == 'no':
            return "Data submitted successfully!"
            return render_template('formvalidation.html')

        # Check if the user wants to enable the second firewall security
        enable_firewall2 = request.form.get('enable_firewall2')
        if enable_firewall2 == 'yes':
            # Import the security_scan function from the second firewall_security module
            from firewall_security import security_scan

            # Call the security_scan function to check for potential security issues
            if security_scan(data):
                # If the data passes the security scan, return a success message
                return "Data submitted successfully!"
                return render_template('formvalidation.html')
            else:
                # If potential security issues are found, return an error message
                return "Security scan detected potentially malicious content in your data."
        
        if enable_firewall2 == 'no':
            return "Data submitted successfully!"
            return render_template('formvalidation.html') 
    # If neither firewall security is enabled, simply return a success message
 



    # If the request method is not POST, return an HTML form asking the user which firewall security they want to enable
    
    else:
        return '''
   <!DOCTYPE html>
<html>
  <head>
    <title>Web Application Firewall</title>
    <script>
      function hasAnsweredSecurityQuestion() {

        var enable_firewall1 = document.getElementsByName('enable_firewall1')[0].checked;
        var enable_firewall2 = document.getElementsByName('enable_firewall2')[0].checked;
  
        if (enable_firewall1 || enable_firewall2 ) {
          return true;
          } 

        else {
          alert('Please answer at least one security question to access the input box.');
          return false;
          }
        }
    </script>
  </head>
  <body>
    <h1>Welcome to the Web Application Firewall!</h1>
    <form method="post" onsubmit="return hasAnsweredSecurityQuestion()">
      <p>
        <label for="enable_firewall1">Do you want to enable the first firewall security?</label><br>
        <input type="radio" name="enable_firewall1" value="yes" onclick="document.getElementsByName('enable_firewall2')[1].disabled = false; document.getElementsByName('enable_firewall2')[1].checked = false; if (this.value === 'yes') { document.getElementsByName('enable_firewall2')[0].disabled = true; } else { document.getElementsByName('enable_firewall2')[0].disabled = false; }">Yes
        <input type="radio" name="enable_firewall1" value="no" onclick="document.getElementsByName('enable_firewall2')[0].checked = false; document.getElementsByName('enable_firewall2')[1].disabled = true;">No
      </p>
      <p>
        <label for="enable_firewall2">Do you want to enable the second firewall security?</label><br>
        <input type="radio" name="enable_firewall2" value="yes" onclick="document.getElementsByName('enable_firewall1')[1].disabled = false; document.getElementsByName('enable_firewall1')[1].checked = false; if (this.value === 'yes') { document.getElementsByName('enable_firewall1')[0].disabled = true; } else { document.getElementsByName('enable_firewall1')[0].disabled = false; }">Yes
        <input type="radio" name="enable_firewall2" value="no" onclick="document.getElementsByName('enable_firewall1')[0].checked = false; document.getElementsByName('enable_firewall1')[1].disabled = true;">No
      </p>
      <p>
        <label for="data">Data:</label><br>
        <textarea name="data" rows="10" cols="30"></textarea>
      </p>
      <p>
        <input type="submit" value="Submit">
      </p>
    </form>
  </body>
</html>
'''

# Start the Flask application and set it to run in debug mode
if __name__ == '__main__':
    app.run(debug=True)