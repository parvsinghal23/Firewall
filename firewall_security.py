import re

# Define a function to check for security issues in submitted data
def security_scan(data):
    # Look for HTML script tags/cross-site scripting attacks
    if re.search("(\<(script)\>)", data):
        return False

    # Check for common SQL injection attacks
    if re.search("((\%27)|(\')|(\-\-)|(\%23))[^\n]*((\%27)|(\')|(\-\-)|(\%23))", data):
        return False
    
    # Look for various potential attacks using special characters
    elif re.search("((\%3C)|<)[^(\%3E)|>]+((\%3E)|>)", data):
        return False
    elif re.search("((\%3C)|<)[^\n]+((\%3E)|>)", data):
        return False
    elif re.search("';'", data):
        return False
    elif re.search('";"', data):
        return False
    elif re.search("((\%3D)|(=))[^\n]*((\%27)|(\')|(\-\-)|(\%3B)|(;))", data):
        return False
    elif re.search("--", data):
        return False
    elif re.search("\*", data):
        return False
    elif re.search("\|", data):
        return False

    elif re.search("[^\w\s]", data):
        return False

    # limits the input data length to 10,000 characters
    # prevent buffer overflow attacks
    elif len(data) > 10000:
        return False

    # If no potential security issues are found, return True
    else:
        return True

def security_scan_2(data):
    # Look for proxy address
    if re.search(r'(?i)(?<![\d.])(?:\d{1,3}\.){3}\d{1,3}(?::\d+)?(?![\d.])', data):
        return False
    # checks that the email address string has a valid format
    elif not re.search(r'^[a-zA-Z0-9_+-]+@[a-zA-Z0-9-]+\.[a-zA-Z]{2,}$', data):
        return False

    # If no potential security issues are found, return True
    else:
        return True