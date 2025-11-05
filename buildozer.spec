#
# [app] Section - Metadata and Files
#
[app]
title = Mobile Data Recovery
package.name = datarecovery
package.domain = com.yourname.datarecovery

source.dir = .
source.include_exts = py,png,jpg,jpeg,kv,atlas,ttf,json

version = 1.0.0

# NOTE: Updated KivyMD and Kivy to slightly more recent common versions.
requirements = python3,kivy==2.2.1,kivymd==1.1.1,plyer,android,openssl,pyjnius

# NOTE: Updated API levels for better compatibility and to address JDK issues.
# android.api = Target API level (Recommend 33 or 34 for modern support)
# android.minapi = Minimum API level
# android.sdk = The version of the Android SDK Build Tools (often handled by the toolchain)
# android.ndk = Specific NDK version (25b is often recommended for newer builds)
android.api = 33
android.minapi = 21
android.sdk = 33
android.ndk = 25b
android.ndk_api = 21
# NOTE: Explicitly set JDK version (often 11 is required for API 31+)
android.jdk = 17

android.permissions = READ_EXTERNAL_STORAGE,WRITE_EXTERNAL_STORAGE,MANAGE_EXTERNAL_STORAGE

android.features = android.software_xml

orientation = portrait

icon.filename = %(source.dir)s/assets/icons/app_icon.png
presplash.filename = %(source.dir)s/assets/icons/presplash.png

#
# [buildozer] Section - Build Settings
#
[buildozer]
log_level = 2

# NOTE: Added arm64-v8a for 64-bit support.
android.arch = armeabi-v7a, arm64-v8a

org.gradle.jvmargs = -Xmx2048m
android.enable_androidx = True
