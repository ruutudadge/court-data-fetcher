#!/usr/bin/env bash
apt-get update
apt-get install -y wget unzip curl

# Install Chrome
wget https://dl.google.com/linux/direct/google-chrome-stable_current_amd64.deb
apt-get install -y ./google-chrome-stable_current_amd64.deb

# Verify install
google-chrome --version
