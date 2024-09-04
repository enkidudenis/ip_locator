import os
import sys
import urllib2
import json
import argparse

def get_api_key(args):
    if args.keyless:
        return None
    elif args.api_key:
        return args.api_key
    elif 'IP2LOCATION_API_KEY' in os.environ:
        return os.environ['IP2LOCATION_API_KEY']
    else:
        print("API key is required unless running in keyless mode. Pass it as a command-line argument, set it as an environment variable 'IP2LOCATION_API_KEY', or use --keyless.")
        sys.exit(1)

def get_ip_info(api_key, ip):
    if api_key:
        url = "https://api.ip2location.io/?key={0}&ip={1}".format(api_key, ip)
    else:
        url = "https://api.ip2location.io/?ip={0}".format(ip)
    
    custom_user_agent = "Mozilla/5.0 (compatible; MyCustomApp/1.0; +http://mycustomapp.com)"
    headers = {"User-Agent": custom_user_agent}
    
    request = urllib2.Request(url, headers=headers)
    
    try:
        response = urllib2.urlopen(request)
        data = response.read()
        return json.loads(data)
    except urllib2.HTTPError as e:
        print("HTTPError: {0}".format(e.code))
        sys.exit(1)
    except urllib2.URLError as e:
        print("URLError: {0}".format(e.reason))
        sys.exit(1)

def find_nearest_cidr(ip_info):
    # Placeholder function: Replace this with a real implementation
    # For demonstration, it returns a hardcoded CIDR block for the same country
    country_code = ip_info.get("country_code")
    if country_code:
        return "Nearest CIDR in {0}: Example CIDR block".format(country_code)
    else:
        print("Country code not found in IP information.")
        sys.exit(1)

if __name__ == "__main__":
    parser = argparse.ArgumentParser(description="IP Locator Tool using IP2Location API")
    parser.add_argument("--api-key", type=str, help="API key for IP2Location (if not using keyless mode)")
    parser.add_argument("--keyless", action="store_true", help="Run in keyless mode (no API key required)")
    
    args = parser.parse_args()
    api_key = get_api_key(args)
    
    ip = raw_input("Enter an IP address: ")  # Use raw_input() in Python 2.7
    ip_info = get_ip_info(api_key, ip)
    
    print("Coordinates for IP {0}: Latitude {1}, Longitude {2}".format(
        ip, ip_info.get('latitude'), ip_info.get('longitude')))
    
    nearest_cidr = find_nearest_cidr(ip_info)
    print(nearest_cidr)
