from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait

class LessonsPage:
    def __init__(self, driver):
        self.driver = driver
        self.lessons = (By.CSS_SELECTOR, "#tabbar > div > div.tab-header > div.tab-header__wrapper > div:nth-child(2)")
        self.last_video = (By.CSS_SELECTOR, "#app > div > div.container.container_mobile > div > div > div.new-lessons_content > div > div:nth-child(5) > div.flex.gap20 > div:nth-child(3) > div.lesson-card")
        self.video_play = (By.CSS_SELECTOR, "#app > div > div.videolesson > div > div:nth-child(2) > div > div:nth-child(3) > div.video-player-proweb > div > div.video-player-proweb__controlls > div.video-player-proweb__controllers > div.video-player-proweb__controllers-left > button")
        self.btn_fullscreen = (By.CSS_SELECTOR, "#app > div > div.videolesson > div > div:nth-child(2) > div > div:nth-child(3) > div.video-player-proweb > div > div.video-player-proweb__controlls > div.video-player-proweb__controllers > div.video-player-proweb__controllers-right > button:nth-child(3)")
        self.full_video = (By.CSS_SELECTOR, "#app > div > div.videolesson > div > div:nth-child(2) > div > div:nth-child(3) > div.video-player-proweb > div > div.video-player-proweb__actinview")
        self.btn_pause = (By.CSS_SELECTOR, "#app > div > div.videolesson > div > div:nth-child(2) > div > div:nth-child(3) > div.video-player-proweb > div > div.video-player-proweb__controlls.video-player-proweb__controlls-hidden > div.video-player-proweb__controllers > div.video-player-proweb__controllers-left > button")
        self.fullscreen_exit = (By.CSS_SELECTOR, "#app > div > div.videolesson > div > div:nth-child(2) > div > div:nth-child(3) > div.video-player-proweb > div > div.video-player-proweb__controlls > div.video-player-proweb__controllers > div.video-player-proweb__controllers-right > button:nth-child(3) > span")
        self.btn_back = (By.CSS_SELECTOR, "#app > div > div.videolesson > div > div:nth-child(2) > div > div.back-to-less.back-to-less-lesson")




    def click_lessons(self):
           wait = WebDriverWait(self.driver, 10)
           wait.until(EC.element_to_be_clickable(self.lessons)).click()


    def click_last_video(self):
           wait = WebDriverWait(self.driver, 10)
           wait.until(EC.element_to_be_clickable(self.last_video)).click()

    def click_video_play(self):
           wait = WebDriverWait(self.driver, 10)
           wait.until(EC.element_to_be_clickable(self.video_play)).click()

    def click_btn_fullscreen(self):
           wait = WebDriverWait(self.driver, 10)
           wait.until(EC.element_to_be_clickable(self.btn_fullscreen)).click()

    def click_full_video(self):
        wait = WebDriverWait(self.driver, 10)
        wait.until(EC.element_to_be_clickable(self.full_video)).click()

    def click_btn_pause(self):
           wait = WebDriverWait(self.driver, 10)
           wait.until(EC.element_to_be_clickable(self.btn_pause)).click()

    def click_fullscreen_exit(self):
           wait = WebDriverWait(self.driver, 10)
           wait.until(EC.element_to_be_clickable(self.fullscreen_exit)).click()

    def click_btn_back(self):
        wait = WebDriverWait(self.driver, 10)
        wait.until(EC.element_to_be_clickable(self.btn_back)).click()



