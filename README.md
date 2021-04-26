# titan_scraper
A web scraper for downloading Attack On Titan manga

Requirements:

    - BeautifulSoup (pip install beautifulsoup4)

    - Image (pip install pillow)

    - requests (pip install requests)

Running main.py requires a 'chapters' folder in the same directory you are running the script in.
This will download all chapters of Attack On Titan into the 'chapters' folder.

If the script has stopped for any reason while downloading, you can start it again at the point you are up to by passing a number to cd.run()

Eg: cd.run(5) will start downloading chapters starting at chapter 5.

