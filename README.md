# op.gg Python Scraper

A webscraper tool for the website: op.gg

Made on a Sunday afternoon XD

## Getting Started

These instructions will get you a copy of the project up and running on your local machine for development and testing purposes. See deployment for notes on how to deploy the project on a live system.

### Prerequisites

*Runs on terminal
- Requires the installation of Python 2.7
- Requires the installation of BeautifulSoup4 (use pip install)

### Downloads

```
git clone <$This repo>
```

On macOS:
```
easy_install pip  
pip install BeautifulSoup4
```

## Running the program

```
python scraper.py
```
- Enter the name of the champion
- Results will spill out from terminal :D

## Thoughts

- There is broken HTML from op.gg, found through: https://validator.w3.org/nu/?doc=http%3A%2F%2Fna.op.gg%2Fchampion%2Fashe%2Fstatistics%2Fadc
- Implementing a rune and build scrape is not possible because of the website's limitations... maybe it will be fixed in the future.


