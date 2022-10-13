from setuptools import setup

setup(
    name='pizzaapi',
    packages=['pizzaapi'],
    include_package_data=True,
    install_requires=[
        'flask',
        'flask_mongoengine',
        'rq',
        'redis',
        'pytest'
    ],
)