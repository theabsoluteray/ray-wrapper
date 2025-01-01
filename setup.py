from setuptools import setup, find_packages

setup(
    name='rayuwu', 
    version='0.2.0',
    packages=find_packages(),
    install_requires=['requests'], 
    description='A package to interact with Discord API',
    author='harsh',
    author_email='me.harshu.yt.04@gmail.com',
    url='https://github.com/theabsoluteray/ray-wrapper',  
    classifiers=[
        'Programming Language :: Python :: 3',
        'License :: OSI Approved :: MIT License',
        'Operating System :: OS Independent',
    ],
)
