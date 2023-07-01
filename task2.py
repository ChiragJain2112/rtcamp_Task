import os
import sys
import requests
import tarfile


def create_wordpress_site(site_name):
    # Check if a site name is provided
    if not site_name:
        print("Please provide a site name as a command-line argument.")
        return

    # Download the latest WordPress version
    download_url = "https://wordpress.org/latest.tar.gz"
    response = requests.get(download_url)
    if response.status_code != 200:
        print("Failed to download the latest WordPress version.")
        return

    # Extract the WordPress archive
    tar_filename = "latest.tar.gz"
    with open(tar_filename, "wb") as file:
        file.write(response.content)

    with tarfile.open(tar_filename, "r:gz") as tar:
        tar.extractall()

    # Move the WordPress files to the site directory
    os.mkdir(site_name)
    os.system(f"mv wordpress/* {site_name}")
    os.system("rm -r wordpress")

    # Cleanup downloaded files
    os.remove(tar_filename)

    print(f"WordPress site '{site_name}' created successfully!")


if __name__ == "__main__":
    site_name = sys.argv[1] if len(sys.argv) > 1 else None
    create_wordpress_site(site_name)

