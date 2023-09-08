import pandas as pd

# Load the Excel file containing student data
data = pd.read_excel('students.xlsx')

# Define a function to search for a student by SAP ID and return their details
def get_student_details(sap_id):
    # Convert sap_id to integer if it's a string
    if isinstance(sap_id, str):
        sap_id = int(sap_id)

    # Search for matching SAP ID in the "Sap ID" column
    student_data = data.loc[data['Sap ID'] == sap_id]

    if not student_data.empty:
        # Convert the row of the matching student to a dictionary
        return student_data
    else:
        return 'Student not found'
    
# print(get_student_details(1234))



