from selenium import webdriver
import time
import patch

class bcolors:
    HEADER = '\033[95m'
    OKBLUE = '\033[94m'
    OKCYAN = '\033[96m'
    OKGREEN = '\033[92m'
    WARNING = '\033[93m'
    FAIL = '\033[91m'
    ENDC = '\033[0m'
    BOLD = '\033[1m'
    UNDERLINE = '\033[4m'


class GoogleImageScraper():
    def __init__(self, webdriver_path, search_key="cat", headless=True, min_resolution=(0, 0), max_resolution=(1920, 1080)):
        #check if chromedriver is updated
        while(True):
            try:
                options = webdriver.ChromeOptions()
                options.add_argument("--remote-debugging-port=9222");
                if(headless):
                    options.add_argument('--headless')
                driver = webdriver.Chrome(executable_path=webdriver_path, chrome_options=options)
                print("[INFO] Started chromium browser")
                driver.set_window_size(1400,1050)
                print("[INFO] Set window size")
                driver.get("https://google.com")
                print("[INFO] Visited google.com")
                try:
                    driver.find_element_by_id("W0wltc").click()
                except Exception as e:
                    print("Failed to refuse cookies!")
                    print(e)
                break
            except:
                #patch chromedriver if not available or outdated
                try:
                    driver
                except NameError:
                    is_patched = patch.download_lastest_chromedriver()
                else:
                    is_patched = patch.download_lastest_chromedriver(driver.capabilities['version'])
                if (not is_patched):
                    exit("[ERR] Please update the chromedriver.exe in the webdriver folder according to your chrome version:https://chromedriver.chromium.org/downloads")
        self.driver = driver
        self.search_key = search_key
        self.webdriver_path = webdriver_path
        self.url = "https://www.google.com/search?q=%s&source=lnms&tbm=isch&sa=X&ved=2ahUKEwie44_AnqLpAhUhBWMBHUFGD90Q_AUoAXoECBUQAw&biw=1920&bih=947"%(search_key)
        self.headless=headless
        self.min_resolution = min_resolution
        self.max_resolution = max_resolution

    def find_image_urls(self, key: str, load_time: int):
        self.search_key = key
        self.url = "https://www.google.com/search?q=%s&source=lnms&tbm=isch&sa=X&ved=2ahUKEwie44_AnqLpAhUhBWMBHUFGD90Q_AUoAXoECBUQAw&biw=1920&bih=947"%(self.search_key)
        print("[INFO] Gathering image links")
        image_url=""
        self.driver.get(self.url)
        try:
            #find and click image
            imgurl = self.driver.find_element_by_xpath('//*[@id="islrg"]/div[1]/div[%s]/a[1]/div[1]/img'%("1"))
            imgurl.click()
            print("[INFO] Clicked on image successfully")
        except Exception:
            print("[EXCEPTION] Couldn't click on image")

        try:
            #select image from the popup
            class_names = ["n3VNCb"]
            time.sleep(load_time)
            images = [self.driver.find_elements_by_class_name(class_name) for class_name in class_names if len(self.driver.find_elements_by_class_name(class_name)) != 0 ][0]
            time.sleep(load_time)
            for image in images:
                #only download images that starts with http
                src_link = image.get_attribute("src")
                if(("http" in  src_link) and (not "encrypted" in src_link)):
                    print(f"{bcolors.OKBLUE} [INFO] {self.search_key} \t {src_link}{bcolors.ENDC}")
                    image_url = src_link
                    break
                else:
                    print(bcolors.FAIL + "[ERROR] Couldn't extract valid link" + bcolors.ENDC)
        except Exception:
            print("[EXCEPTION] Unable to get link")
            return "\n"

        print("[INFO] Google search ended")
        return image_url + "\n"
