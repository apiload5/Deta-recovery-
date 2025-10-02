[app]
title = Mobile Data Recovery
package.name = datarecovery
package.domain = com.yourname.datarecovery

source.dir = .
source.include_exts = py,png,jpg,jpeg,kv,atlas,ttf,json

version = 1.0.0

requirements = python3,kivy==2.1.0,kivymd,plyer,android,openssl,pyjnius

android.api = 30
android.minapi = 21
android.sdk = 23
android.ndk = 23b
android.ndk_api = 21

android.permissions = READ_EXTERNAL_STORAGE,WRITE_EXTERNAL_STORAGE,MANAGE_EXTERNAL_STORAGE

android.features = android.software_xml

orientation = portrait

icon.filename = %(source.dir)s/assets/icons/app_icon.png
presplash.filename = %(source.dir)s/assets/icons/presplash.png

[buildozer]
log_level = 2

android.arch = armeabi-v7a

org.gradle.jvmargs = -Xmx2048m
android.enable_androidx = True
