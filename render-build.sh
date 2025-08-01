#!/usr/bin/env bash
# Install dependencies for Chrome
apt-get update
apt-get install -y wget curl unzip gnupg

# Download and install Chrome
wget https://dl.google.com/linux/direct/google-chrome-stable_current_amd64.deb
apt-get install -y ./google-chrome-stable_current_amd64.deb
