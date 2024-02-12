# 0x13. Firewall
## Overview
This project focuses on understanding and implementing firewall configurations to enhance server security. You will delve into concepts related to web stack debugging and explore the importance of firewalls in securing servers.

## Concepts
For this project, you are expected to focus on the following concept:

Web stack debugging

## Background Context
Firewalls are essential components of server security. They regulate incoming and outgoing network traffic based on predetermined security rules. In this project, you will explore firewall configurations and their impact on server security.

## Resources
### Read or watch:

What is a firewall

### Additional Information
Telnet Usage: As explained in the web stack debugging guide concept page, telnet is a useful tool to check if sockets are open. For example, you can use telnet to check if port 22 is open on a server by running: telnet web-02.holberton.online 22. Successful connection indicates that the port is open.
Testing Environment: Note that the school network filters outgoing connections via a network-based firewall. To test your work on web-01, perform the test from outside of the school network, like from your web-02 server. SSH into your web-02 server to bypass the school's network firewall.
Warning: Be cautious with firewall rules. Blocking essential ports like port 22/TCP can result in loss of SSH access to your server. Ensure to unblock necessary ports before logging out of your server.
Note: Containers on demand cannot be used for this project due to Docker container limitations.

## Disclaimer
Be diligent and cautious while configuring firewall rules to avoid unintentional disruptions to server accessibility and security.
