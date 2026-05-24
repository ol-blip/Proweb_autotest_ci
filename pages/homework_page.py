from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait


class HomeworkPage:
    def __init__(self, driver):
        self.driver = driver
        self.homework = (By.XPATH,"//span[contains(text(),'Домашние задания')]")
        self.last_done_homework = (By.CSS_SELECTOR, "#app > div > div.container.container_mobile > div > div > div.tab-content.group-homeworks-tab-content > div > div > div > div:nth-child(2) > div.work-dropdown.homework-card_drop.grow > div")
        self.press_to_hw = (By.XPATH, "//span[contains(text(), 'К заданию')]")
        self.btn_message = (By.CSS_SELECTOR, "#app > div > div.container.homework-page-container > div > div > div > div.solved-homework__materials > div.message-input.relative.solved-homework-input > div > div > label > textarea")
        self.enter_message = (By.CSS_SELECTOR, "#app > div > div.container.homework-page-container > div > div > div > div.solved-homework__materials > div.message-input.relative.solved-homework-input > div > div > label")
        self.btn_send = (By.CSS_SELECTOR, "#app > div > div.container.homework-page-container > div > div > div > div.solved-homework__materials > div.message-input.relative.solved-homework-input > button")
        self.back = (By.CSS_SELECTOR, "#app > div > div.container.homework-page-container > div > div > div > div.global-wrapper.group-homeworks_works-submit-info > div > div > div.group-homeworks_works-submit-info-block > div.group-homeworks_works-submit-info-block-titles.p10 > div")

    def click_homework(self):
        wait = WebDriverWait(self.driver, 10)
        wait.until(EC.element_to_be_clickable(self.homework)).click()

    def click_last_done_homework(self):
        wait = WebDriverWait(self.driver, 10)
        wait.until(EC.element_to_be_clickable(self.last_done_homework)).click()

    def click_press_to_hw(self):
        wait = WebDriverWait(self.driver, 20)
        wait.until(EC.element_to_be_clickable(self.press_to_hw)).click()

    def click_btn_message(self):
        wait = WebDriverWait(self.driver, 10)
        wait.until(EC.element_to_be_clickable(self.btn_message)).click()

    def enter_enter_message(self, enter_message):
        wait = WebDriverWait(self.driver, 10)
        wait.until(EC.presence_of_element_located(self.enter_message)).send_keys(enter_message)

    def click_btn_send(self):
        wait = WebDriverWait(self.driver, 10)
        wait.until(EC.element_to_be_clickable(self.btn_send)).click()

    def click_back (self):
        wait = WebDriverWait(self.driver, 10)
        wait.until(EC.element_to_be_clickable(self.back )).click()







