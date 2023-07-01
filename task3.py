import subprocess
import sys

def run_docker_compose_file(file_path, command):
    try:
        subprocess.run(["docker-compose", "-f", file_path] + command, check=True)
    except subprocess.CalledProcessError as e:
        print(f"Error: {e}")
        sys.exit(1)

if __name__ == "__main__":
    if len(sys.argv) < 2:
        print("python lemp_stack.py <command>")
        sys.exit(1)
    
    file_path = "docker-compose.yml"
    command = sys.argv[1:]
    run_docker_compose_file(file_path, command)

