# IP Locator
This is a simple Jython script to locate a location of an IP address. Just run this script and enter the IP address and viola, you get the coordinate of the IP!

## Requirements
In order to start to use this script, you will need to have python 2.7 and Jython 2. Currently Jython only support Python 2.7.

A quick way to get Jython is to find a version from https://mvnrepository.com/artifact/org.python/jython-standalone, and then download the `jar` file from there. Place the `jar` file in the same directory with the script and you are ready to get started.

This script used IP2Location.io API to provide the coordinates information. You can straightaway use it without API key, or sign up with a free one to get more quotas.

## Example usage

To view all the options availble, you can run the command `java -jar jython-standalone-2.x.x.jar ip_locator.py -h`. You will the output like this:

```Bash
usage: ip_locator.py [-h] [--api-key API_KEY] [--keyless]

IP Locator Tool using IP2Location API

optional arguments:
  -h, --help         show this help message and exit
  --api-key API_KEY  API key for IP2Location (if not using keyless mode)
  --keyless          Run in keyless mode (no API key required)
```

The script supports both keyless and API key mode, but keep in mind that the keyless API had a daily limitation.

To use this script, simply choose one of the mode, and supply API key for `--api-key` mode.

For example, if you run keyless, just run this command: `java -jar jython-standalone-2.x.x.jar ip_locator.py --keyless`. You will be prompted to input an IP address to continue. Just enter an IP address and press the ENTER key. And you can know the coordinates of the IP address instantly.

```Bash
Enter an IP address: 8.8.8.8
Coordinates for IP 8.8.8.8: Latitude 37.38605, Longitude -122.08385
```

