import os
import platform
import webbrowser
import requests

def add_hosts_entry(site_name):
    hosts_file = get_hosts_file_path()
    entry = "127.0.0.1 " + site_name

    try:
        with open(hosts_file, "a") as file:
            file.write(entry + "\n")
        print(f"Added {site_name} to /etc/hosts file.")

        if is_site_up(site_name):
            open_in_browser(site_name)
        else:
            print(f"Warning: {site_name} is not reachable.")
    except IOError as e:
        print(f"Error: {str(e)}")

def is_site_up(site_name):
    try:
        response = requests.head("http://" + site_name)
        return response.status_code == requests.codes.ok
    except requests.exceptions.RequestException:
        return False

def open_in_browser(site_name):
    webbrowser.open("http://" + site_name)
    print(f"Opened {site_name} in a browser.")

def get_hosts_file_path():
    system = platform.system()
    if system == "Linux" or system == "Darwin":
        return "/etc/hosts"
    else:
        raise OSError(f"Unsupported operating system: {system}")

# Input(Give Site name)
site_name = input("Enter the site name (e.g., example.com): ")
add_hosts_entry(site_name)

