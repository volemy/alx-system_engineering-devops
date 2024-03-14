# 0x1A. Application server

## Overview
This project focuses on setting up an application server to serve dynamic content for the AirBnB clone project. The application server will complement the existing Nginx web server setup, enhancing the web infrastructure to handle dynamic requests efficiently.

## Background Context
In web infrastructure, a web server, such as Nginx, is primarily responsible for serving static content like HTML, CSS, and image files. However, for dynamic content generation, an application server is required. In this project, we'll integrate an application server, configure it to work alongside Nginx, and serve the AirBnB clone project.

## Resources
Application server vs web server
How to Serve a Flask Application with Gunicorn and Nginx on Ubuntu 16.04
Running Gunicorn
Be careful with the way Flask manages slash in route - strict_slashes
Upstart documentation

## Requirements
### General
README.md: A comprehensive README.md file is mandatory, providing an overview, instructions, and context for the project.
Python Version: Everything Python-related must be done using Python 3.
Config Files: All configuration files must have meaningful comments to explain their purpose and usage.
Bash Scripts
Execution Environment: All files will be interpreted on Ubuntu 16.04 LTS.
Execution Permissions: All Bash script files must be executable.
Shellcheck: Your Bash script must pass Shellcheck without any errors.
Shebang: The first line of all Bash scripts should be exactly #!/usr/bin/env bash.
Comments: The second line of all Bash scripts should be a comment explaining the script's purpose.
Servers
Web Servers: Set up and configure the application server on web-01 and web-02 servers.
Load Balancer: Ensure that the load balancer (lb-01) is configured to distribute traffic between web servers.
Server Details: The table lists the server details, including names, usernames, IPs, and states.

Set up development with Python
Install the net-tools package on the server.
Git clone the AirBnB_clone_v2 repository on the web-01 server.
Configure the Flask application to serve its content from the route /airbnb-onepage/ on port 5000.
Ensure that the Flask application object is named app.
Example command to run the Flask application:
bash
Copy code
python3 -m web_flask.0-hello_route
