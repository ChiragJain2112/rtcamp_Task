import subprocess
import sys


def check_docker_installed():
    try:
        subprocess.check_output(["docker", "--version"])
        return True
    except FileNotFoundError:
        return False


def check_docker_compose_installed():
    try:
        subprocess.check_output(["docker-compose", "--version"])
        return True
    except FileNotFoundError:
        return False


def install_docker():
    subprocess.run(["sudo", "apt","install","docker.io","-y"])
    subprocess.run(["sudo", "usermod", "-aG", "docker", "$USER"])
    subprocess.run(["sudo","systemctl", "start","docker"])
    subprocess.run(["sudo", "docker", "--version"])


def install_docker_compose():
    subprocess.run(["sudo", "apt","install","docker-compose", "-y"])
    subprocess.run(["sudo", "docker-compose", "--version"])


def main():
    if not check_docker_installed():
        print("Docker is not installed. Installing Docker...")
        install_docker()
        print("Docker installed successfully.")
    else:
        print("Docker is already installed.")

    if not check_docker_compose_installed():
        print("Docker Compose is not installed. Installing Docker Compose...")
        install_docker_compose()
        print("Docker Compose installed successfully.")
    else:
        print("Docker Compose is already installed.")


if __name__ == "__main__":
    main()

