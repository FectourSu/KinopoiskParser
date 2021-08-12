
# Kinopoisk.ru parser by movie id on Python :shipit:

## Table of Contents
- [Getting Started](#getting-started)
    - [Installing packages](#installing-packages)
- [Quick Start Guide](#quick-start-guide)
- [Settings](#settings)
- [Final recommendations](#final-recommendations)

## Getting Started

To get started using application follow the instructions below.
This project was written on python 3.9, but it was also tested on version 3.7

### Installing packages:

```sh
pip install beautifulsoup4 
```
```sh
pip install aiohttp
```
```sh
pip install requests
```
```sh
pip install logging
```
```sh
pip install argparse
```
```sh
pip install fake-useragent
```
```sh
pip install webdriver-manager
```
```sh
pip install lxml 
```
```sh
pip install configparser 
```
```sh
pip install selenium
```
```sh
pip install pyinstaller #if you want compile to exe
```
## Quick Start Guide

Launching the application is as simple as possible: \
python [nameofscript] [filmid]

```py
python kinopoisk.py 389
```
After parsing, the result will be placed in the created src folder
In the "src" folder, you can find ready-made parsed movies in .json format

### If you wants

To compile the application, use the PyInstall package connected above

```sh
python -m PyInstall --onefile kinopoisk.py
```
in the dist folder you can find the compiled version of the program

## Settings

The main parsing settings will be described here
If you have registered on https://kinopoiskapiunofficial.tech/ and got your own api, in this case, you can have your api in settings.ini
```sh
[GENERAL]
api = <YOUR API>
```
UPD: The api from the test account was used in the repository

## Final recommendations
The parser is built on using the xpath element, that is, there should be no binding to the class name of the object.
But... the author is a trash coder...
And therefore, the parser uses partially class name blocks, it is required to update it in settings.ini, as their developers change on the site
### For example
At the moment, the class of the main page is as follows: styles_root__2gHIX
in the settings, the last part of it is taken
```sh
[PARSER]
page = __2gHIX # you need to change it as the styles are updated
```
Have a nice parsing / Приятного парсинга :trollface: