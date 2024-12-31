from setuptools import setup, find_packages

setup(
    name='ray_package',  # Your package name
    version='0.1.0',
    packages=find_packages(),
    install_requires=['requests'],  # Dependencies
    description='A package to interact with Discord Guilds',
    author='Your Name',
    author_email='your_email@example.com',
    url='https://github.com/yourusername/ray_package',  # Replace with your repo URL
    classifiers=[
        'Programming Language :: Python :: 3',
        'License :: OSI Approved :: MIT License',
        'Operating System :: OS Independent',
    ],
)
