from setuptools import setup, find_packages

PACKAGES = find_packages()

setup(
    name='TeleBash',
    version='0.0.1',
    packages=PACKAGES,
    url='https://github.com/sadmonad/TeleBash',
    license='',
    author='sadmonad',
    author_email='sadmonad@gmail.com',
    description='Manage your linux server via Telegram'
)
