from setuptools import setup, find_packages

setup(
    name='TeleBash',
    version='0.2.1',
    packages=find_packages(exclude='tests'),
    install_requires=['python-telegram-bot == 11.1.0'],
    url='https://github.com/sadmonad/TeleBash',
    license='',
    author='sadmonad',
    author_email='sadmonad@gmail.com',
    description='Manage your linux server via Telegram'
)
