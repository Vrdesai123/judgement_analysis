import setuptools

setuptools.setup(
    name="app",
    version="1.0",
    packages=['src', 'testing'],
    entry_points={
        'console_scripts': ['app=src.main', ]
    },
)