# Use a base image with necessary libraries
FROM ubuntu:22.04

# Install dependencies and add the PPA
RUN apt-get update && apt-get install -y \
    software-properties-common \
    && add-apt-repository ppa:xtradeb/apps \
    && apt-get update \
    && apt-get install -y \
    ungoogled-chromium \
    chromium-chromedriver \
    libnss3 \
    libgbm1 \
    tor \
    curl \
    gnupg \
    ca-certificates \
    libatk-bridge2.0-0 \
    libgtk-3-0 \
    libx11-xcb1 \
    libxcomposite1 \
    libxdamage1 \
    libxrandr2 \
    libxss1 \
    libxtst6 \
    libxshmfence1 \
    python3-pip \
    && rm -rf /var/lib/apt/lists/*

RUN pip3 install selenium webdriver-manager beautifulsoup4

COPY newtest.py /app/newtest.py
COPY all_git_passes.py /app/all_git_passes.py

# Set working directory
WORKDIR /app

