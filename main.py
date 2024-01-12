import requests


def get_iss_position():

    # Make a get request to get the ISS position information.
    response = requests.get(url="http://api.open-notify.org/iss-now.json")
    # Response.raise_for_status() will raise an HTTPError if the HTTP request returned an unsuccessful status code.
    response.raise_for_status()
    # Get the data
    iss_data = response.json()

    return iss_data["iss_position"]


print(get_iss_position())
