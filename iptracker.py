import socket
import requests

def get_geolocation(ip_or_domain):
    try:
        # If input looks like a domain, resolve to IP
        if not ip_or_domain.replace('.', '').isdigit():
            ip_address = socket.gethostbyname(ip_or_domain)
        else:
            ip_address = ip_or_domain
        
        print(f"IP Address: {ip_address}")

        # Query IP geolocation API
        response = requests.get(f"http://ip-api.com/json/{ip_address}")
        data = response.json()

        if data['status'] == 'success':
            print(f"Country: {data['country']}")
            print(f"Region: {data['regionName']}")
            print(f"City: {data['city']}")
            print(f"Latitude: {data['lat']}")
            print(f"Longitude: {data['lon']}")
            print(f"ISP: {data['isp']}")
        else:
            print("Failed to get geolocation data")
    except Exception as e:
        print(f"Error: {e}")

if __name__ == "__main__":
    user_input = input("Enter a domain or IP address: ")
    get_geolocation(user_input)
