import socket
target_host = input("Enter your target host:")
target_port = input("Enter your port:")
# Create a socket obj
client = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
# socket.AF_INET = we use ipv4 standard or hostname
# This is be a tcp client
