import os
import platform

def add_hosts_entry(site_name):
    hosts_file = get_hosts_file_path()
    entry = "127.0.0.1 " + site_name

    try:
        with open(hosts_file, "a") as file:
            file.write(entry + "\n")
        print(f"Added {site_name} to /etc/hosts file.")
    except IOError as e:
        print(f"Error: {str(e)}")

def get_hosts_file_path():
    system = platform.system()
    if system == "Linux" or system == "Darwin":
        return "/etc/hosts"
    else:
        raise OSError(f"Unsupported operating system: {system}")

site_name = "example.com"
add_hosts_entry(site_name)

