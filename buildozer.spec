[app]

# Application title
title = Whatsapp Recording 

# Application package name (unique identifier)
package.name = whatsapp_vice_recording

# Application domain (used for package name)
package.domain = org.ticno

# Source code directory
source.include_exts = py,png,jpg,kv,atlas

# Application version (major.minor.revision)
version = 1.0.0

# Application requirements (dependencies)
requirements = python3,kivy==2.3.0,kivymd,pyaudio,sounddevice

# Primary application entry point
source.include_patterns = assets/*,images/*,fonts/*

# Orientation (portrait or landscape)
orientation = portrait

# Android permissions
android.permissions = INTERNET,READ_EXTERNAL_STORAGE,WRITE_EXTERNAL_STORAGE

# Android API level
android.api = 30

# Minimum Android SDK version
android.minapi = 21

# Target Android SDK version
android.ndk = 23b

# Android architecture (armeabi-v7a, arm64-v8a, x86, x86_64)
android.arch = armeabi-v7a

# Android app icon
icon.filename = %(source.dir)s/assets/icon.png

# Presplash screen (optional)
presplash.filename = %(source.dir)s/assets/presplash.png

# Log level (debug, info, warning, error, critical)
log_level = 2

# Fullscreen mode (0 = disabled, 1 = enabled)
fullscreen = 0

# Window style (0 = normal, 1 = borderless)
window.style = 0

# Preserve Python environment (0 = disabled, 1 = enabled)
preserve_python_environment = 0

# Debug mode (0 = disabled, 1 = enabled)
debug = 1

# Build mode (debug or release)
# release mode mein signing key aur password ki zarurat hogi
# debug mode mein yeh zaruri nahi hai
# mode = debug

# Signing key (release mode ke liye)
# android.keystore = %(source.dir)s/keystore.jks
# android.keystore.password = your_password
# android.keyalias = your_alias
# android.keyalias.password = your_alias_password

# Buildozer log level (0 = minimal, 1 = verbose)
log_level_buildozer = 1

# Buildozer build directory
buildozer.build_dir = .buildozer

# Buildozer bin directory
buildozer.bin_dir = .bin

# Buildozer log directory
buildozer.log_dir = .logs

# Buildozer cache directory
buildozer.cache_dir = .cache

# Buildozer dist directory
buildozer.dist_dir = bin

# Buildozer source directory
buildozer.source_dir = .

# Buildozer spec file
buildozer.spec_file = buildozer.spec

# Buildozer force build (0 = disabled, 1 = enabled)
buildozer.force_build = 0

# Buildozer force clean build (0 = disabled, 1 = enabled)
buildozer.force_clean_build = 0

# Buildozer force rebuild (0 = disabled, 1 = enabled)
buildozer.force_rebuild = 0

# Buildozer force reinstall (0 = disabled, 1 = enabled)
buildozer.force_reinstall = 0

# Buildozer force recompile (0 = disabled, 1 = enabled)
buildozer.force_recompile = 0

# Buildozer force redownload (0 = disabled, 1 = enabled)
buildozer.force_redownload = 0

# Buildozer force reextract (0 = disabled, 1 = enabled)
buildozer.force_reextract = 0

# Buildozer force repackage (0 = disabled, 1 = enabled)
buildozer.force_repackage = 0

# Buildozer force resign (0 = disabled, 1 = enabled)
buildozer.force_resign = 0

# Buildozer force rezip (0 = disabled, 1 = enabled)
buildozer.force_rezip = 0

# Buildozer force rezipalign (0 = disabled, 1 = enabled)
buildozer.force_rezipalign = 0

# Buildozer force rezipalign (0 = disabled, 1 = enabled)
buildozer.force_rezipalign = 0

# Buildozer force rezipalign (0 = disabled, 1 = enabled)
buildozer.force_rezipalign = 0
