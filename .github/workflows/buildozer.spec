name: Build APK

on:
  push:
    branches: [ main ]
  workflow_dispatch:

jobs:
  build:
    runs-on: ubuntu-22.04

    steps:
      - uses: actions/checkout@v4

      - name: Set up Python
        uses: actions/setup-python@v5
        with:
          python-version: '3.10'

      - name: Install Dependencies
        run: |
          sudo apt-get update
          sudo apt-get install -y git zip unzip openjdk-17-jdk python3-pip autoconf libtool pkg-config zlib1g-dev libncurses5-dev libncursesw5-dev libreadline-dev libsqlite3-dev libgdbm-dev libdb5.3-dev libbz2-dev libexpat1-dev liblldb-dev libffi-dev libssl-dev
          pip install --upgrade pip
          pip install buildozer cython kivy

      - name: Accept Android Licenses
        run: |
          mkdir -p ~/.android
          touch ~/.android/repositories.cfg
          yes | buildozer android accept_sdk_license || true

      - name: Build with Buildozer
        run: |
          buildozer -v android debug

      - name: Upload APK
        uses: actions/upload-artifact@v4
        with:
          name: app-release
          path: bin/*.apk
          
