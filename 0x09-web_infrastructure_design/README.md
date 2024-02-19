# 0x09. Web infrastructure design

## Overview
This project aims to delineate the roles and functionalities of the Application Server and Web Server in a distributed web infrastructure. By separating these components into distinct servers and incorporating a Load-Balancer, the design aims for enhanced scalability, performance, and fault tolerance.

## Design Components
1 Server: This serves as the foundational infrastructure where all other components are hosted.

1 Load-Balancer (HAproxy): Configured as a cluster with another instance for load distribution and high availability.

## Components:

Web Server: Dedicated server for handling incoming HTTP/HTTPS requests and serving static content.
Application Server: Dedicated server for executing the application logic, processing dynamic content, and interacting with the database.
Database: Dedicated server for storing and managing data.
Infrastructure Specifics
Load-Balancer:
Why: To distribute incoming traffic across multiple servers, ensuring optimal resource utilization, scalability, and high availability.
Web Server:
Why: To handle and process incoming HTTP/HTTPS requests, serve static content, and interact with the Load-Balancer and Application Server.
Application Server:
Why: To execute the application-specific logic, process dynamic content, manage user sessions, and interact with the database.
Database:
Why: To store, manage, and retrieve data required for the application, ensuring data integrity, consistency, and reliability.
## Conclusion
By segregating components into dedicated servers and leveraging a Load-Balancer for traffic distribution, this design offers a robust and scalable web infrastructure. The distinct roles of the Application Server and Web Server ensure efficient resource utilization and facilitate the seamless functioning of complex web applications.
