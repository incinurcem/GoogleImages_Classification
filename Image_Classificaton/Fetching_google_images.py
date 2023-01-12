from multiprocessing.sharedctypes import Value
from selenium import webdriver
from selenium.webdriver.common.by import By
import requests
import io
from datetime import datetime as dt
from PIL import Image
import time
import os
from selenium.webdriver.chrome.options import Options



#Settings

options = Options()
options.use_chronium = True
options.add_argument("--headless")
options.add_argument('--disable-blink-features=AutomationControlled')
options.binary_location = "/Applications/Google Chrome.app/Contents/MacOS/Google Chrome"
driver = webdriver.Chrome(chrome_options=options,
                          executable_path=r'/Users/cem/Downloads/denemee/chromedriver.exe')
driver.get('http://google.com/')
print("Chrome Browser Invoked")



#Function to find images from Google images

def get_images_from_google(driver, delay, max_images, url):
	def scroll_down(driver):
		driver.execute_script("window.scrollTo(0, document.body.scrollHeight);")
		time.sleep(delay)

	url = url
	driver.get(url)

	image_urls = set()
	skips = 0
	while len(image_urls) + skips < max_images:
		scroll_down(driver)
		thumbnails = driver.find_elements(By.CLASS_NAME, "Q4LuWd")

		for img in thumbnails[len(image_urls) + skips:max_images]:
			try:
				img.click()
				time.sleep(delay)
			except:
				continue

			images = driver.find_elements(By.CLASS_NAME, "n3VNCb")
			for image in images:
				if image.get_attribute('src') in image_urls:
					max_images += 1
					skips += 1
					break

				if image.get_attribute('src') and 'http' in image.get_attribute('src'):
					image_urls.add(image.get_attribute('src'))
					print(f"Found {len(image_urls)} ")
                    
                            
	return image_urls




#Function to download images from Google images

def download_image(down_path, url, file_name, image_type='jpeg',
                   verbose=True):
   
     try:
              time = dt.now()
              curr_time = time.strftime('%H:%M:%S')
             
              
              headers = {
             'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64; rv:95.0) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/108.0.0.0 Safari/537.36', }
         
              url = str(url)
              response = requests.get(
                  url, headers=headers, timeout=10, allow_redirects=False)
              img_content = response.content
              img_file = io.BytesIO(img_content)
              image = Image.open(img_file)
         
              file_pth = down_path + file_name

              with open(file_pth, 'wb') as file:
                image.save(file, image_type)
   
              if verbose == True:
               print(f'The image: {file_pth} downloaded successfully at {curr_time}.')
     except Exception as e:
          print(f'Unable to download image from Google Photos due to\n: {str(e)}')




if __name__ == '__main__':
    

    google_urls = ['https://www.google.com/search?q=%CE%BF%CE%BC%CE%B9%CF%87%CE%BB%CF%8E%CE%B4%CE%B7%CF%82+%CE%BA%CE%B1%CE%B9%CF%81%CF%8C%CF%82+%CF%84%CE%BF%CF%80%CE%AF%CE%BF+%CE%BF%CE%BC%CE%AF%CF%87%CE%BB%CE%B7&tbm=isch&ved=2ahUKEwjUnNrc85_8AhWSNewKHTg5CxIQ2-cCegQIABAA&oq=%CE%BF%CE%BC%CE%B9%CF%87%CE%BB%CF%8E%CE%B4%CE%B7%CF%82+%CE%BA%CE%B1%CE%B9%CF%81%CF%8C%CF%82+%CF%84%CE%BF%CF%80%CE%AF%CE%BF+%CE%BF%CE%BC%CE%AF%CF%87%CE%BB%CE%B7&gs_lcp=CgNpbWcQA1CgHligHmCqIWgAcAB4AIABkwGIAYcCkgEDMC4ymAEAoAEBqgELZ3dzLXdpei1pbWfAAQE&sclient=img&ei=YhiuY9TjJJLrsAe48qyQAQ&bih=789&biw=1440&rlz=1C5CHFA_enTR970TR970',
                   'https://www.google.com/search?q=%CE%BF%CE%BC%CE%B9%CF%87%CE%BB%CF%8E%CE%B4%CE%B7%CF%82+%CE%BA%CE%B1%CE%B9%CF%81%CF%8C%CF%82+%CF%84%CE%BF%CF%80%CE%AF%CE%BF+%CE%BF%CE%BC%CE%AF%CF%87%CE%BB%CE%B7&tbm=isch&ved=2ahUKEwjUnNrc85_8AhWSNewKHTg5CxIQ2-cCegQIABAA&oq=%CE%BF%CE%BC%CE%B9%CF%87%CE%BB%CF%8E%CE%B4%CE%B7%CF%82+%CE%BA%CE%B1%CE%B9%CF%81%CF%8C%CF%82+%CF%84%CE%BF%CF%80%CE%AF%CE%BF+%CE%BF%CE%BC%CE%AF%CF%87%CE%BB%CE%B7&gs_lcp=CgNpbWcQA1CgHligHmCqIWgAcAB4AIABkwGIAYcCkgEDMC4ymAEAoAEBqgELZ3dzLXdpei1pbWfAAQE&sclient=img&ei=YhiuY9TjJJLrsAe48qyQAQ&bih=789&biw=1440&rlz=1C5CHFA_enTR970TR970']


    labels = [
        'foggy2', 'foggy3'
    ]


    if len(google_urls) != len(labels):
        raise ValueError(
            'The length of the url list does not match the labels list.')
    



    #Part of uploading images

    player_path = 'images/dataset/'

    for lbl in labels:
        if not os.path.exists(player_path + lbl):
            print(f'Making directory: {str(lbl)}')
            os.makedirs(player_path+lbl)

    #Max 80 photos can upload
    for url_current, lbl in zip(google_urls, labels):
        urls = set(get_images_from_google(driver, 0, 80, url_current))
       
        for i, url in enumerate(urls, start=824):
            download_image(down_path=f'images/dataset/{lbl}/',
                           url=url,
                           file_name=str(i+1) + '.jpg',
                           verbose=True)
