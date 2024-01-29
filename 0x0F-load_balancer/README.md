# 0x0F. Load Balancer

## Description
This project focuses on implementing a load balancer to improve the web stack's redundancy and reliability. By doubling the number of web servers and configuring a load balancer, the infrastructure can handle more traffic and maintain operation even if one server fails.

## Concepts
Load balancer
Web stack debugging

## Background Context
In this project, two additional servers are provided: gc-[STUDENT_ID]-web-02-XXXXXXXXXX and gc-[STUDENT_ID]-lb-01-XXXXXXXXXX. The goal is to automate the configuration of these servers using Bash scripts to set up a redundant and reliable web infrastructure.

## Resources
Introduction to load-balancing and HAproxy
HTTP header
Debian/Ubuntu HAProxy packages

## Requirements
Allowed editors: vi, vim, emacs
Interpreted on Ubuntu 16.04 LTS
Files should end with a new line
README.md file at the root of the project folder is mandatory
All Bash script files must be executable
Bash scripts must pass Shellcheck (version 0.3.7) without any error
First line of all Bash scripts: #!/usr/bin/env bash
Second line of all Bash scripts: a comment explaining the script's purpose
Usage
## Clone the repository.
Navigate to the project directory.
Execute the Bash scripts to automate the setup and configuration of the servers.
