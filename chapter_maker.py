import requests
from PIL import Image
from io import BytesIO
from utils import clear, get_page_soup


class ChapterMaker():
    '''
    params:
        url<str>: url of a page which contains the desired images
    '''

    def __init__(self, url):
        self.url = url

    def get_image_urls(self):
        '''
        retrieves a list of the urls of all img elements with a class of "text-center"

        returns:
            List<str>: image urls
        '''
        soup = get_page_soup(self.url)
        divs = soup.find_all(class_="text-center")

        img_urls = []
        for div in divs:
            img = div.find("img")
            if img:
                img_url = img['src']
                if 'png' in img_url or 'jpg' in img_url or 'jpeg' in img_url:
                    img_url = img_url.replace('\\r', '')
                    img_urls.append(img_url)
        return img_urls

    def stream_image(self, url):
        '''
        params:
            url<str>: an image url

        returns:
            response<obj>: a request object holding the loaded image
        '''
        try:
            return requests.get(url, stream=True)
        except Exception:
            print(f"Couldn't stream {url}")

    def get_images(self):
        '''
        returns:
            List<Image>: A list of PIL Image objects
        '''
        img_urls = self.get_image_urls()

        images = []
        dot_string = '.'

        for i, url in enumerate(img_urls):
            img_resp = self.stream_image(url)
            if img_resp:
                img = Image.open(BytesIO(img_resp.content)).convert('RGB')
                images.append(img)

                # dot_ctr = dot_string * round(10*i/len(img_urls))
                progress = round(100 * (i/len(img_urls)), 1)
                if i % 2 == 0:
                    clear()
                    print(f"getting images - {progress}%")
        return images

    def create_pdf(self, dir):
        '''
        params:
            dir<str>: The filename/path the pdf should be saved under
        '''
        images = self.get_images()
        images[0].save(dir, "PDF", resolution=100.0,
                       save_all=True, append_images=images[1:])
        del images


# for debugging purposes
# if __name__ == "__main__":
#     url = 'https://ww7.readsnk.com/chapter/shingeki-no-kyojin-chapter-135/'
#     cm = ChapterMaker(url)
#     cm.create_pdf('test.pdf')