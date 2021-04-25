from chapters_downloader import ChaptersDownloader
from chapter_merger import merge_pdfs
from utils import get_page_soup


class VolumeScraper():
    def __init__(self, url):
        self.url = url

    def get_volumes(self):
        soup = get_page_soup(self.url)

        header = [el for el in soup.find(id="Colossal_Editions").next_elements]

        print(header)



if __name__ == "__main__":
    v = VolumeScraper('https://attackontitan.fandom.com/wiki/List_of_Attack_on_Titan_chapters')
    v.get_volumes()
    # chap_url = 'https://ww7.readsnk.com/manga/shingeki-no-kyojin/'
    # cd = ChaptersDownloader(chap_url, './')
    # cd.run(135)

    # merge_pdfs('./chapters/', './test.pdf', 5)
