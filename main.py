import undetected_chromedriver.v2 as uc
import chromedriver_autoinstaller
import time

class Bot:
    def __init__(self) -> None:
        chromedriver_autoinstaller.install()
        self.chrome_version = chromedriver_autoinstaller.get_chrome_version().split('.')[0]
        self.driver = self._init_driver()
        self._start_up()

    def _init_driver(self):
        options = uc.ChromeOptions()
        options.add_argument("--disable-notifications")
        options.add_argument("--disable-popup-blocking")
        options.add_argument("--start-maximized")
        driver = uc.Chrome(options= options, version_main=self.chrome_version)
        return driver

    def _start_up(self, url='https://www.douyin.com/'):
        self.driver.get(url)
        time.sleep(2)
        btn_close = self.driver.find_elements('xpath', '//div[@class="dy-account-close"]')
        if btn_close:
            btn_close[0].click()
        time.sleep(5)

if __name__ == '__main__':
    bot = Bot()
    bot.driver.quit()