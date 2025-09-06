
import requests

def get_public_ip():
    try:
        response = requests.get("https://api.ipify.org?format=json")
        return response.json().get("ip")
    except requests.RequestException:
        return None

def get_location(ip):
    try:
        response = requests.get(f"https://ipinfo.io/{ip}/json")
        data = response.json()
        return {
            "IP": ip,
            "City": data.get("city"),
            "Region": data.get("region"),
            "Country": data.get("country"),
            "Location": data.get("loc"), 
        }
    except requests.RequestException:
        return None

def display_location_info():
    ip = get_public_ip()
    if not ip:
        print("Unable to fetch public IP.")
        return

    location = get_location(ip)
    if not location:
        print("Unable to fetch location data.")
        return

    print("Your PC's approximate location:")
    for key, value in location.items():
        print(f"{key}: {value}")

if __name__ == "__main__":
    display_location_info()