import time
import requests
from datetime import datetime

# Global dictionary to track the last time a request was sent
last_recognition_request_time = {}

# Function to send HTTP request to backend
def send_recognition_request(employee_id):
    current_time = time.time()
    current_date = datetime.today().date()  # Get today's date
    # Get the employee ID prefix (splitting by underscore)
    employee_id_prefix = employee_id.split('_')[0]
    
    # Check if the employee_id has been processed before and if it's a new day
    if employee_id_prefix in last_recognition_request_time:
        
        last_request_time = last_recognition_request_time[employee_id_prefix]
        last_request_date = datetime.fromtimestamp(last_request_time).date() 
        
        # If it's the same day, skip the request
        if last_request_date == current_date:
            print(f"Skipped {employee_id} because it's already been processed today.")
            return
    
    
    # Construct the URL for the request
    url = f"http://localhost:3000/api/attendance/id={employee_id_prefix}&time={current_time}"

    try:
        last_recognition_request_time[employee_id_prefix] = current_time # ! dont forget to remove this when bakend work
        # Send the request to the backend
        response = requests.get(url)
        if response.status_code == 200:
            print(f"Successfully sent recognition request for {employee_id}")
            # last_recognition_request_time[employee_id_prefix] = current_time  # Update the last request time for this employee
        else:
            print(f"Failed to send recognition request for {employee_id}, status code: {response.status_code}")
    except Exception as e:
        print(f"Error sending recognition request: {''}")
