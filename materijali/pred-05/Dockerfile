FROM ubuntu:20.04

# Install Python
RUN apt update
RUN apt install -y python3

# Install pip and other python installation tools
RUN apt install -y python3-pip
RUN python3 -m pip install --upgrade pip setuptools wheel

# Check if Python has been setup correctly
RUN python3 --version
