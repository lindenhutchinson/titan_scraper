from chapter_maker import ChapterMaker
from utils import clear, get_page_soup

class ChaptersDownloader():
    '''
    params:
        url<str>: the url containing a list of chapters
        dir<str>: the directory to save the chapters into, with a trailing /

    '''
    def __init__(self, url, dir):
        self.url = url
        self.dir = dir



    def get_chapter_urls(self):
        '''
        fetches a list of chapter urls that can iterated over to download all chapters
        
        returns:
            list<str>: list of chapter urls

        '''
        soup = get_page_soup(self.url)
        divs = soup.find_all(class_=["text-center", "flex"])

        chap_urls = {}
        divs.reverse()
        for div in divs:
            chap = div.find("a")
            if chap:
                href = chap['href']
                if 'chapter' in href and href not in chap_urls:
                    title = href[href.find('-chapter')+1:]
                    chap_urls.update({title: href})

        return chap_urls

    def run(self, start=0):
        '''
        params: 
            start<int>: (optional) start downloading chapters from this number rather than the beginning
        '''
        chap_urls = self.get_chapter_urls()

        ctr = 0
        for title, url in chap_urls.items():
            if ctr <= start+1 and start > 0:
                ctr += 1
                continue
            clear()
            print(f"Getting {title}")
            ctr += 1
            cm = ChapterMaker(url)
            cm.create_pdf(f"{self.dir+title}.pdf")
