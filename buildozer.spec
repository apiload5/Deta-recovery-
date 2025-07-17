[app]

# (str) Title of your application
title = Ticno Data Recovery

# (str) Package name
package.name = ticonorecovery

# (str) Package domain (unique reverse domain-style)
package.domain = org.ticno

# (str) Source code directory
source.dir = .

# (list) Source files to include (comma separated)
source.include_exts = py,png,jpg,kv,atlas

# (str) Application versioning (method 1)
version = 1.0

# (list) Application requirements
requirements = python3,kivy

# (str) Presplash of the application
#presplash.filename = %(source.dir)s/data/presplash.png

# (str) Icon of the application
#icon.filename = %(source.dir)s/data/icon.png

# (str) Supported orientation (portrait, landscape or all)
orientation = portrait

# (bool) Indicate if the application should be fullscreen or not
fullscreen = 1

# (bool) Hide the statusbar
android.hide_statusbar = 1

# (str) Supported Android API
android.api = 30

# (int) Minimum API your APK will support
android.minapi = 21

# (str) Android NDK version to use
android.ndk = 23b

# (str) Android NDK API to use. This is the minimum API your app will support, it should usually match android.minapi.
android.ndk_api = 21

# (bool) Use --private data storage (True) or --dir public storage (False)
android.private_storage = True

# (bool) Android logcat filters to use
log_level = 2

# (list) Permissions
android.permissions = READ_EXTERNAL_STORAGE,WRITE_EXTERNAL_STORAGE

# (str) Entry point of the application
entrypoint = main.py

# (str) Packaging method
android.packaging = default

# (bool) Copy library instead of making a libpymodules.so
copy_libs = 1

# (str) Path to build artifact storage, absolute or relative to spec file
# build_dir = ./build

# (str) Custom source folders for requirements
# (Separate multiple paths with commas)
# requirements.source = 

# (bool) Create a landscape version (useful for tablets)
# landscape = False

# (str) Command line to run after build (e.g. install)
# postbuild = 

# (str) Custom Java package name for your app
# android.package = com.example.myapp

[buildozer]

# (str) Buildozer log level (0 = error only, 1 = normal, 2 = verbose, 3 = debug)
log_level = 2

# (str) Path to build artifact storage, absolute or relative to spec file
build_dir = ./build

# (str) Path to Python-for-Android git clone (if empty, it will clone automatically)
# p4a.source_dir = 

# (str) Path to the folder containing android SDK and NDK tools
# android.sdk_path = 

# (str) Path to the android NDK directory (if empty, it will be installed automatically)
# android.ndk_path = 

# (str) Path to the android SDK directory (if empty, it will be installed automatically)
# android.sdk_path = 

# (str) Path to a custom version of Cython
# cython_path = 

# (bool) Enable verbose output for every command
warn_on_root = 1

# (str) Additional command line arguments to pass when invoking python-for-android
# p4a.extra_args = 


