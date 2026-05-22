from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait

class CoworkingPage:
    def __init__(self, driver):
        self.driver = driver
        self.enroll = (By.CSS_SELECTOR, "#app > div > div.coworking > div > button > span")
        self.branch_page = (By.CSS_SELECTOR, "#dialog > div > div > div.material-dialog__window-container > div.material-dialog__window-body > div > div.container.coworking__page-dialog-follow-container > div.coworking__page-dialog-follow-branch > div:nth-child(2) > div.list-tile.coworking__page-dialog-follow-branch-item-list > div.list-tile__trailing")
        self.btn_choose = (By.CSS_SELECTOR, "#dialog > div.material-dialog.coworking__branch-dialog > div > div.material-dialog__window-actions > button:nth-child(2) > span > span")
        self.btn_date = (By.CSS_SELECTOR, "#dialog > div > div > div.material-dialog__window-container > div.material-dialog__window-body > div > div.container.coworking__page-dialog-follow-container > div.coworking__page-dialog-follow-date > div > div:nth-child(4) > button")
        self.group = (By.CSS_SELECTOR, "#dialog > div > div > div.material-dialog__window-container > div.material-dialog__window-body > div > div.container.coworking__page-dialog-follow-container > div.list-tile.coworking__page-dialog-follow-list")
        self.btn_radio = (By.CSS_SELECTOR, "#dialog > div:nth-child(2) > div > div.material-dialog__window-container > div.material-dialog__window-body > div > div > div > div.list-tile__trailing > button")
        self.btn_choose = (By.CSS_SELECTOR, "#dialog > div:nth-child(2) > div > div.material-dialog__window-actions > button:nth-child(2) > span > span")
        self.time_choose = (By.CSS_SELECTOR, "#dialog > div > div > div.material-dialog__window-container > div.material-dialog__window-body > div > div.container.coworking__page-dialog-follow-container > div.coworking__page-dialog-follow-timeseat > div:nth-child(1) > label > input")
        self.btn_time = (By.CSS_SELECTOR, "#dialog > div.material-dialog.timepicker > div > div.material-dialog__window-actions > button:nth-child(2)")
        self.place_choose = (By.CSS_SELECTOR, "#dialog > div > div > div.material-dialog__window-container > div.material-dialog__window-body > div > div.container.coworking__page-dialog-follow-container > div.coworking__page-dialog-follow-timeseat > div:nth-child(2) > div")
        self.btn_radio_place = (By.CSS_SELECTOR, "#dialog > div:nth-child(2) > div > div.material-dialog__window-container > div.material-dialog__window-body > div.coworking__page-dialog-time-seats > div:nth-child(1) > div.list-tile__trailing > button")
        self.select_place = (By.CSS_SELECTOR, "#dialog > div:nth-child(2) > div > div.material-dialog__window-actions > button:nth-child(2)")
        self.send = (By.CSS_SELECTOR, "#dialog > div > div > div.material-dialog__window-actions > button:nth-child(2)")
        self.cancel_coworking = (By.CSS_SELECTOR, "#app > div > div.coworking > div > div.lazyscroll > div > div > div:nth-child(9) > div > div.flex.aic.jcsb.width100.gap5 > button")
        self.btn_confirm_cancel = (By.CSS_SELECTOR, "#dialog > div > div > div.material-dialog__window-actions > button:nth-child(2)")


    def click_enroll(self):
        wait = WebDriverWait(self.driver, 10)
        wait.until(EC.element_to_be_clickable(self.enroll)).click()

    def click_branch_page(self):
        wait = WebDriverWait(self.driver, 10)
        wait.until(EC.element_to_be_clickable(self.branch_page)).click()

    def click_btn_choose(self):
        wait = WebDriverWait(self.driver, 10)
        wait.until(EC.element_to_be_clickable(self.btn_choose)).click()

    def click_btn_date(self):
        wait = WebDriverWait(self.driver, 10)
        wait.until(EC.element_to_be_clickable(self.btn_date)).click()

    def click_group(self):
        wait = WebDriverWait(self.driver, 10)
        wait.until(EC.element_to_be_clickable(self.group)).click()

    def click_btn_radio(self):
        wait = WebDriverWait(self.driver, 10)
        wait.until(EC.element_to_be_clickable(self.btn_radio)).click()

    def click_btn_choose(self):
        wait = WebDriverWait(self.driver, 10)
        wait.until(EC.element_to_be_clickable(self.btn_choose)).click()

    def click_time_choose(self):
        wait = WebDriverWait(self.driver, 10)
        wait.until(EC.element_to_be_clickable(self.time_choose)).click()

    def click_btn_time(self):
        wait = WebDriverWait(self.driver, 10)
        wait.until(EC.element_to_be_clickable(self.btn_time)).click()

    def click_place_choose(self):
        wait = WebDriverWait(self.driver, 10)
        wait.until(EC.element_to_be_clickable(self.place_choose)).click()

    def click_btn_radio_place(self):
        wait = WebDriverWait(self.driver, 10)
        wait.until(EC.element_to_be_clickable(self.btn_radio_place)).click()

    def click_select_place(self):
        wait = WebDriverWait(self.driver, 10)
        wait.until(EC.element_to_be_clickable(self.select_place)).click()

    def click_send(self):
        wait = WebDriverWait(self.driver, 10)
        wait.until(EC.element_to_be_clickable(self.send)).click()

    def click_cancel_coworking(self):
        wait = WebDriverWait(self.driver, 10)
        wait.until(EC.element_to_be_clickable(self.cancel_coworking)).click()

    def click_btn_confirm_cancel(self):
        wait = WebDriverWait(self.driver, 10)
        wait.until(EC.element_to_be_clickable(self.btn_confirm_cancel)).click()

