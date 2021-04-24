from chapters_downloader import ChaptersDownloader
from chapter_merger import merge_pdfs

if __name__ == "__main__":
    # chap_url = 'https://ww7.readsnk.com/manga/shingeki-no-kyojin/'
    # cd = ChaptersDownloader(chap_url, './chapters/')
    # cd.run(135)

    merge_pdfs('./chapters/', 'titans15.pdf', 15)
