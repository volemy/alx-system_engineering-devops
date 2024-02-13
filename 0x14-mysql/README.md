# 0x14. MySQL
## Description
This project is part of the Holberton School curriculum and focuses on MySQL, database administration, and web stack debugging.

## Concepts
For this project, we cover the following concepts:

## Database administration
Web stack debugging
How to Install MySQL 5.7.x
# To install MySQL 5.7.x on your system, follow these steps:

Open a terminal.

Run the following command to add the MySQL APT repository to your system:

bash
Copy code
sudo sh -c 'echo "deb http://repo.mysql.com/apt/ubuntu bionic mysql-5.7" >> /etc/apt/sources.list.d/mysql.list'
Update the package lists to refresh the information about available packages:

bash
Copy code
sudo apt update
Install MySQL 5.7.x using the following command:

bash
Copy code
sudo apt install mysql-server-5.7
During the installation process, you will be prompted to set a root password for MySQL. Follow the on-screen instructions to set a secure password.

After the installation is complete, MySQL 5.7.x should be installed on your system.

## Requirements
Allowed editors: vi, vim, emacs
All files interpreted on Ubuntu 16.04 LTS
All files should end with a new line
A README.md file, at the root of the project folder, is mandatory
All Bash script files must be executable
Bash scripts must pass Shellcheck (version 0.3.7-5~ubuntu16.04.1 via apt-get) without any error
The first line of all Bash scripts should be #!/usr/bin/env bash
The second line of all Bash scripts should be a comment explaining what the script is doing
