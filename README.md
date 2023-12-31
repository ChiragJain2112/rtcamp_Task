# Prerequisites before installing and running the script in your ubuntu machine.
* Python3
* To install python3 by runing th below command in the privilege mode(as a root user):
* `sudo su`
* `apt install python3 -y`
*  Ubuntu is Debian Based operating system which use apt or apt-get, red hat based operating system use yum to install the new packages.
# Task1 
**Create a command-line script in Python to perform this task, Checking if docker and docker-compose is installed on the system. If not present, install the missing 
packages.**
<br>
To install docker and docker-compose run the task1 script in your Ubuntu machine which is Debian based operation system follow the below steps:
* `python3 task1.py`
* First, it will check the docker and docker-compose is installed or not in the system, if it is installed in the system it will print the message docker and docker-compsoe is installed, if not then the further script will exicute by itself.
# Task2
**Create a command line script in python, the script should be able to create a WordPress site using the latest WordPress Version. Please provide a way for the user to provide the site name as a command-line argument.**
* The script having a simple work just to create wordpress site using the latest WordPress version and have created a way for user to provide the site name as per their convenience.
* `python3 task2.py mysite/yoursite/firstsite/othersite` (named the site as per the choice).
*  The script just need python3 for the exicution, it can be executed in any Linux distros.
# Task3
**Create a command line script in python, it must be a LEMP stack running inside containers (Docker) and a docker-compose file is a must.**
* Let's understand about the LEMP stack.
  1. L-Linux.
  2. E-Nginx.
  3. M-Mysql.
  4. P-PHP.
* So, the first step towards the creation of LEMP stack which will be running inside the Docker container but creating multiple containers at a single time by just a singal click, docker-compose file is must. As you can see, the source code contain the docker-compose with version "3.9" with 3 containers under the singal service.
* When we will execute the `task3.py` file, it will be searching for docker-compose file with appropiate docker-compose command like
  1. `docker-compose up -d`
  2. `docker-compose down`
  3. `dcoker-compose ps`
  4. `docker-compose build`
  5. `docker-compose logs`
  6. `docker-compose restart`
  7. `docker-compose start`
  8. `docker-compose stop`
* You don't need to write full command as written above, just write the last keyword like `up -d/down/stop/start/build/logs/ps` etc. Inside the task3.py file everything is setup properly in appropiate manner.
# Task4
**Create the command line script in python to create a /etc/hosts entry for example.com pointing to localhost. Here we are assuming the user has provided example.com as the site name**
* By executing this file with command `python3 task4.py` it will prompt into the etc folder and search for hosts file and make a entry example.com which is pointing to localhost `127.0.0.1 example.com`.
* In this file task4.py we already provided the site name as example.com so at the time of execution it wil not ask for site name as input.
* Just apply the command `python3 task4.py`.
# Task5
**Create the command line script in python which prompt the user to open example.com in a browser if all goes well and the site is up and healthy.**
* This script will prompt the user to open the example.com in browser as we have discussed above, how the script is making an entry into the /etc/hosts file.
* When we wil be executing the file `python3 task5.py`, it will ask for the site name as per our choice.
# Task6
**Create the command line script in python to add another subcommand to enable/disable the site (stopping/starting the containers)**
* Creating two more function in same script, whenever the one execute the `task6.py` file by applying the command `python3 task6.py`
* Then, on the terminal a query will be asking by the script for enabling/disabling the site (stopping/starting).
* User just have to type what the one want to do with it.
# Task7
**Create the command line script in python to add one more subcommand to delete the site (deleting containers and local files).**
* Creating one more function in same script, whenever the one execute the `task7.py` file by applying command `python3 task7.py`
* Then, on the terminal a query will be asking by the script for deleting the site with the container and it's local file's.
