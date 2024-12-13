# IP Geolocation Tracker  

![IP-Geolocation-Tracker Jenderal92](https://github.com/user-attachments/assets/3cbc41f3-7942-4807-96cb-dd778922e9af)


A Python 2.7 tool for tracking geographical locations based on IP addresses. This lightweight and efficient tracker fetches IP geolocation data such as city, region, country, and coordinates using the `ipinfo.io` API.

## Features  
- **Track IP Geolocation:** Input any IP address to find its geographical location.  
- **Automatic IP Detection:** Automatically uses the device's public IP if no IP is provided.  
- **Detailed Information:** Displays city, region, country, latitude, and longitude.  

## Installation  

1. **Clone the Repository:**  
   ```bash
   git clone https://github.com/Jenderal92/ip-geolocation-tracker.git
   cd ip-geolocation-tracker
   ```

2. **Install Dependencies:**  
   Ensure you have Python 2.7 installed. Then, install the required `requests` library:  
   ```bash
   pip install requests
   ```

---

## Usage  

1. Run the script in your terminal:  
   ```bash
   python ip_geolocation.py
   ```

2. Enter an IP address to track when prompted.  
   - Leave the input empty to automatically track your public IP.  

3. View the output, which includes:  
   - IP Address  
   - City  
   - Region  
   - Country  
   - Latitude and Longitude  

## Example Output  

```plaintext
===========================================
   IP Geolocation Tracker
   Created By : Python 2.7
===========================================

Enter IP address to track or press Enter to track your IP: 8.8.8.8
Searching for location of IP: 8.8.8.8

Location Information:
IP Address: 8.8.8.8
City: Mountain View
Region: California
Country: US
Latitude: 37.386, Longitude: -122.084
```

---
