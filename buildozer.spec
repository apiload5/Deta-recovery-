[app]
title = Ticno Data Recovery
package.name = datarecovery
package.domain = com.yourname.datarecovery

source.dir = .
source.include_exts = py,png,jpg,kv,atlas,ttf

version = 1.0
requirements = python3,kivy,kivymd,plyer,android

orientation = portrait

[buildozer]
log_level = 2

[app]
presplash.filename = %(source.dir)s/assets/presplash.png
icon.filename = %(source.dir)s/assets/icon.png
