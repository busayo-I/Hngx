from flask import Flask, request, jsonify
import datetime
app = Flask(__name__)

@app.route('/api', methods=['GET'])
def get_info():
    # Get slack_name from the user
    slack_name = request.args.get('slack_name')

     # Get track from the user
    track = request.args.get('track')

    #Creating an empty dictionary to store user data
    user_data = {}

    if slack_name:
        user_data['slack_name'] = slack_name

    # Get track from the user
    #track = request.args.get('track')
    if track:
        user_data['track'] = track

    #getting the current day and UTC time
    #current_day = "Sunday"
    #utc_time = "2023-09-10T07:00:18Z"
    current_day = datetime.datetime.now().strftime("%A")
    utc_time = datetime.datetime.utcnow().strftime("%Y-%m-%dT%H:%M:%SZ")

    # Creating a GitHub URLs for the provided track
    github_repo_url = f"https://github.com/busayo-I/Hngx.git"
    github_file_url = f"https://github.com/busayo-I/Hngx/blob/main/api.py"

    # the response data
    response_data = {
        "slack_name": slack_name,
        "current_day": current_day,
        "utc_time": utc_time,
        "track": track,
        "github_file_url":github_file_url,
        "github_repo_url": github_repo_url,
        "status_code": 200
    }

    # Return the response in JSON format
    return jsonify(response_data), 200

if __name__ == '__main__':
    app.run()
