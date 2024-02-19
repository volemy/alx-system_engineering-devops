#!/usr/bin/env bash

# Step 1: Check Nginx Configuration
echo "Checking Nginx configuration..."
nginx -t

# Step 2: Check Nginx Status
echo "Checking Nginx status..."
systemctl status nginx

# Step 3: Check Listening Ports
echo "Checking listening ports..."
netstat -tuln | grep ':80'

# Step 4: Check Firewall Rules
echo "Checking firewall rules..."
iptables -L | grep '80'

# Step 5: Check for Other Services
echo "Checking for other services on port 80..."
lsof -i :80

# Step 6: Restart Nginx
echo "Restarting Nginx..."
systemctl restart nginx

# Step 7: Verify Nginx is listening on port 80
echo "Verifying Nginx is listening on port 80..."
netstat -tuln | grep ':80'

echo "Nginx configuration and port 80 listening status checked and fixed."
