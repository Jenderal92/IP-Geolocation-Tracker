import requests
import json

def print_banner():
    banner = """
    ===========================================
       IP Geolocation Tracker
       Created By : Python 2.7
    ===========================================
    """
    print banner
def get_geolocation(ip):
    try:
        url = "https://ipinfo.io/{}/json".format(ip)
        response = requests.get(url)
        data = response.json()

        location = data.get('loc', 'Location not found')
        city = data.get('city', 'City not found')
        country = data.get('country', 'Country not found')
        region = data.get('region', 'Region not found')

        if location != 'Location not found':
            lat, lon = location.split(',')
            lat, lon = float(lat), float(lon)
        else:
            lat, lon = None, None

        return {
            'IP': ip,
            'City': city,
            'Region': region,
            'Country': country,
            'Latitude': lat,
            'Longitude': lon
        }
    except requests.exceptions.RequestException as e:
        return "Error in fetching data: {}".format(e)

def display_location(ip):
    print "Searching for location of IP: {}".format(ip)
    result = get_geolocation(ip)
    
    if isinstance(result, dict):
        print "\nLocation Information:"
        print "IP Address: {}".format(result['IP'])
        print "City: {}".format(result['City'])
        print "Region: {}".format(result['Region'])
        print "Country: {}".format(result['Country'])
        if result['Latitude'] and result['Longitude']:
            print "Latitude: {}, Longitude: {}".format(result['Latitude'], result['Longitude'])
        else:
            print "Location coordinates not available."
    else:
        print result

if __name__ == "__main__":
    print_banner()  
    ip_input = raw_input("Enter IP address to track: ").strip()
    
    if not ip_input:
        ip_input = requests.get('https://api.ipify.org').text
        print "Your IP is {}".format(ip_input)
    
    display_location(ip_input)
