import requests

from config import API_KEY, API_URL


def get_tracking_data(tracking_number: str) -> requests.Response:
    """
    That much simple API request.
    """
    headers = {
        "DHL-API-Key": API_KEY,
    }
    params = {
        "trackingNumber": tracking_number,
    }
    response = requests.get(
        API_URL + "/shipments",
        headers=headers,
        params=params,
    )
    return response
