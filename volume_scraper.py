from chapter_merger import merge_pdfs
from utils import get_page_soup

class VolumeScraper():
    '''
    For scraping the Colossal Edition volume definitions of Attack on Titan, so that the downloaded chapters
    can be merged into their respective volumes

    params:
        out_dir<str>: The directory the merged volumes should be saved into, must include a trailing /
    '''
    def __init__(self, out_dir):
        self.url = 'https://attackontitan.fandom.com/wiki/List_of_Attack_on_Titan_chapters'
        self.out_dir = out_dir

    def merge_volumes(self):
        volumes = self.get_volumes()
        for key, values in volumes.items():
            vol_name = f"{self.out_dir}volume-{key}.pdf"
            start = values['start'] if key != 1 else 0 # don't need a starting value if this is the first volume
            end = values['end'] if key != 6 else 0 # don't need a finishing value if this is the final volume
            # TODO prepend the volume image before adding the volume's chapters
            merge_pdfs('./chapters/',vol_name, start, end)

    def get_volumes(self):
        soup = get_page_soup(self.url)

        header = soup.find(id="Colossal_Editions")
        tables = header.find_all_next('table')
        vol_num = 1
        volumes = {}
        chap_num = 1
        for table in tables:
            chapters = []
            rows = table.find_all("tr")

            if 4 <= len(rows) <= 5:
                chap_list_row = rows[3]
                titles = [t.get_text() for t in chap_list_row.find_all('li')]
                img = chap_list_row.find("img")
                if img:
                    img_src = img['data-src']
                    img_url = img_src[:img_src.index('/revision')]
                else:
                    img_url = ''

                volumes.update({
                    vol_num:{
                        'vol_img':img_url,
                        'start':chap_num,
                        'end':chap_num+len(titles)
                    }
                })
                vol_num+=1
                chap_num+=len(titles)

        return(volumes)