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
requirements = python3,kivy==2.3.1,kivymd

# Orientation of the app
orientation = portrait

# Fullscreen setting
fullscreen = 1

# Android Permissions
android.permissions = READ_EXTERNAL_STORAGE,WRITE_EXTERNAL_STORAGE,MANAGE_EXTERNAL_STORAGE

# Hide status bar
android.hide_statusbar = 1

# Minimum API level
android.minapi = 21

# Target API level
android.api = 33

# NDK version
android.ndk = 25c

# NDK API level
android.ndk_api = 21

# Private storage
android.private_storage = True

# Package type
android.packaging = default

# Accept Android SDK license
android.accept_sdk_license = True

[buildozer]
# Log level
log_level = 2

# Warn if using root
warn_on_root = 1

# Build directory
build_dir = ./build
