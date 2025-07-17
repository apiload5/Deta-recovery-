[app]

# Title of your application
title = Ticno Data Recovery

# Package name
package.name = ticonorecovery

# Package domain
package.domain = org.ticno

# Source code directory
source.dir = .

# Included file types
source.include_exts = py,png,jpg,kv,atlas

# Version
version = 1.0

# Entry point of the app
entrypoint = main.py

# Application requirements
requirements = python3,kivy

# Orientation of the app
orientation = portrait

# Fullscreen setting
fullscreen = 1

# Android Permissions
android.permissions = READ_EXTERNAL_STORAGE,WRITE_EXTERNAL_STORAGE

# Hide status bar
android.hide_statusbar = 1

# Minimum API level
android.minapi = 21

# Target API level
android.api = 30

# NDK version
android.ndk = 23b

# NDK API level
android.ndk_api = 21

# Private storage
android.private_storage = True

# Package type
android.packaging = default

# Optional: Add icon and presplash
# icon.filename = data/icon.png
# presplash.filename = data/presplash.png

# Optional Java version
android.gradle_dependencies = com.android.support:appcompat-v7:28.0.0

[buildozer]

# Log level
log_level = 2

# Warn if using root
warn_on_root = 1

# Build directory
build_dir = ./build

# Uncomment if you want to reuse the SDK/NDK location
# android.sdk_path = /path/to/android/sdk
# android.ndk_path = /path/to/android/ndk

