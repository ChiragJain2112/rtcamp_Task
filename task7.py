import os
import platform
import webbrowser
import requests
import subprocess
import shutil

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

def enable_site():
    subprocess.run(["docker-compose", "up", "-d"])
    print("Site enabled. Containers started.")

def disable_site():
    subprocess.run(["docker-compose", "down"])
    print("Site disabled. Containers stopped.")

def delete_site():
    disable_site()
    shutil.rmtree("site_directory")  # Replace "site_directory" with the actual directory of your site
    print("Site deleted. Containers stopped and local files removed.")

def get_hosts_file_path():
    system = platform.system()
    if system == "Linux" or system == "Darwin":
        return "/etc/hosts"
    else:
        raise OSError(f"Unsupported operating system: {system}")


site_name = input("Enter the site name (e.g., example.com): ")

action = input("Enter the action (enable/disable/delete): ")
if action == "enable":
    add_hosts_entry(site_name)
    enable_site()
elif action == "disable":
    disable_site()
elif action == "delete":
    delete_site()
else:
    print("Invalid action. Please specify 'enable', 'disable', or 'delete'.")

