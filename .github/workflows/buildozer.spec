[app]
title = SigmaBot
package.name = sigmabot
package.domain = org.test
source.dir = .
source.exts = py,png,jpg,kv,atlas
version = 0.1
requirements = python3,kivy
orientation = portrait
fullscreen = 0

# Указываем стабильные версии SDK, чтобы Buildozer не ругался на aidl и build-tools:
android.api = 31
android.min_api = 21
android.sdk = 31
android.ndk = 25b
android.accept_sdk_license = True
