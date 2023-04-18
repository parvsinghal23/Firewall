import pandas as pd

# Load the Excel file containing student data
data = pd.read_excel('students.xlsx')

# Define a function to search for a student by SAP ID and return their name
def get_student_name(sap_id):
    student_data = data.loc[data['SAP ID'] == sap_id]
    if len(student_data) > 0:
        return student_data.iloc[0, 1] # return the name in the next column
    else:
        return 'Student not found'

