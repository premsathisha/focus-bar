from setuptools import setup

APP = ['focus_bar.py']
DATA_FILES = []
OPTIONS = {
    'plist': {
        'LSUIElement': True,
        'CFBundleIdentifier': 'com.prem.focusbar',
        'CFBundleName': 'Focus Bar',
        'CFBundleDisplayName': 'Focus Bar',
        'CFBundleVersion': '1.0.0',
        'CFBundleShortVersionString': '1.0.0',
        'NSHumanReadableCopyright': '© 2024 Prem Sathisha'
    },
    'iconfile': 'icons.icns',
    'packages': ['rumps'],
}

setup(
    app=APP,
    data_files=DATA_FILES,
    options={'py2app': OPTIONS},
    setup_requires=['py2app'],
)
