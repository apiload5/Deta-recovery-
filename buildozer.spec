name: Build APK

on:
  push:
    branches:
      - main

jobs:
  build:
    runs-on: ubuntu-latest

    steps:
      - name: Checkout Code
        uses: actions/checkout@v4

      - name: Set up Python
        uses: actions/setup-python@v4
        with:
          python-version: '3.9'

      - name: Install System Dependencies
        run: |
          sudo apt-get update
          sudo apt-get install -y \
            git zip unzip openjdk-17-jdk \
            python3-pip python3-setuptools python3-venv \
            libffi-dev libssl-dev libjpeg-dev zlib1g-dev \
            libstdc++6 libbz2-dev libreadline-dev libncurses5-dev

      - name: Install Buildozer and Cython
        run: |
          pip install --upgrade pip
          pip install cython
          pip install buildozer

      - name: Install Android SDK & Build Tools
        run: |
          mkdir -p $HOME/.buildozer/android/platform/android-sdk
          cd $HOME/.buildozer/android/platform/android-sdk
          wget https://dl.google.com/android/repository/commandlinetools-linux-11076708_latest.zip -O cmdline-tools.zip
          unzip cmdline-tools.zip
          mkdir -p cmdline-tools/latest
          mv cmdline-tools/* cmdline-tools/latest/
          yes | cmdline-tools/latest/bin/sdkmanager --sdk_root=$HOME/.buildozer/android/platform/android-sdk \
            "platforms;android-30" \
            "build-tools;30.0.3" \
            "platform-tools" \
            "tools"

      - name: Build APK
        run: |
          buildozer android debug

      - name: Upload APK
        uses: actions/upload-artifact@v4
        with:
          name: TicnoDataRecovery.apk
          path: bin/*.apk
          
