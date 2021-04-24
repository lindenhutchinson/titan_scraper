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
                if 'png' in img_url or 'jpg' in img_url:
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
        except:
            print(f"Couldn't stream {url}")

    def get_images(self):
        '''
        returns:
            List<Image>: A list of PIL Image objects
        '''
        img_urls = self.get_image_urls()

        images = []
        ctr=0
        dot_string='.'

        for url in img_urls:
            img_resp = self.stream_image(url)
            if img_resp:
                img = Image.open(BytesIO(img_resp.content)).convert('RGB')
                images.append(img)

                ctr+=1
                dot_ctr = dot_string * round(10*ctr/len(img_urls))
                clear()
                print(f"working{dot_ctr}")
        return images

    def create_pdf(self, dir):
        '''
        params:
            dir<str>: The filename/path the pdf should be saved under
        '''
        images = self.get_images()
        images[0].save(dir, "PDF", resolution=100.0,save_all=True, append_images=images[1:])
        del images
