from setuptools import setup

setup(
    name='TeleBash',
    version='0.0.1',
    packages=['tests', 'TeleBash',
              'TeleBash.core', 'TeleBash.core.bot', 'TeleBash.commands'],
    url='https://github.com/sadmonad/TeleBash',
    license='',
    author='sadmonad',
    author_email='sadmonad@gmail.com',
    description='Manage your linux server via Telegram'
)
