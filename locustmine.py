from locust import HttpUser, task, between

class ApiUser(HttpUser):
    wait_time = between(5, 10)  # Customize wait time as needed

    @task(weight=2)  # Adjust weight for task frequency
    def upload_file(self):
        # Prepare authentication (replace with your API's method)
        auth = ("bonaradha", "quixyradhika")

        # Set content type (multipart/form-data for file uploads)
        headers = {"Content-Type": "multipart/form-data"}

        # Replace with your API's URL and file path
        url = "http://127.0.0.1:5000"
        file_path = "C:\Locust\radhikalocust.txt"

        with open(file_path, "rb") as file:  # Open file in binary mode
            files = {"file": file}  # Dictionary for file parameter

            # Make the POST request
            response = self.client.post(url, auth=auth, files=files, headers=headers)

            # Handle errors and verify response (adapt based on your API)
            if response.status_code != 200:
                print(f"Error uploading file: {response.reason}")
            else:
                print(f"File uploaded successfully: {response.text}")
