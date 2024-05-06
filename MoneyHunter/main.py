from selenium import webdriver
from selenium.webdriver.chrome.service import Service as ChromeService
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions
from selenium.webdriver.support.ui import Select
from datetime import datetime
from selenium.webdriver.support import expected_conditions as EC
import subprocess
import time


def start_to_gather():
    driver = webdriver.Chrome(service=ChromeService(ChromeDriverManager().install()))
    driver.maximize_window()
    driver.get("https://member.expireddomains.net/")

    # Login
    username_text = driver.find_element(By.NAME, "login")
    username_text.send_keys("anonymo2239")
    password_text = driver.find_element(By.NAME, "password")
    password_text.send_keys(".,Edirne2239alp165")
    login_button = driver.find_element(By.XPATH, "/html/body/div[1]/div/div/div[1]/div/div[2]/form/div[4]/div/button")
    WebDriverWait(driver, 4).until(expected_conditions.element_to_be_clickable(
        (By.XPATH, "/html/body/div[1]/div/div/div[1]/div/div[2]/form/div[4]/div/button")))
    login_button.click()

    # Deleted .com
    WebDriverWait(driver, 4).until(
        expected_conditions.element_to_be_clickable((By.XPATH, "/html/body/div/div[1]/div/div/div[1]/ul/li[2]/a")))
    deleted_com = driver.find_element(By.XPATH, "/html/body/div/div[1]/div/div/div[1]/ul/li[2]/a")
    WebDriverWait(driver, 4).until(
        expected_conditions.element_to_be_clickable((By.XPATH, "/html/body/div/div[1]/div/div/div[1]/ul/li[2]/a")))
    deleted_com.click()
    deleted_com_current = driver.find_element(By.XPATH, "/html/body/div/div[1]/div/div/div[1]/ul/li[2]/ul/li[1]/a")
    WebDriverWait(driver, 4).until(expected_conditions.element_to_be_clickable(
        (By.XPATH, "/html/body/div/div[1]/div/div/div[1]/ul/li[2]/ul/li[1]/a")))
    deleted_com_current.click()

    # filtering
    sorting_length = driver.find_element(By.XPATH, "/html/body/div/div[2]/div/div[2]/table/thead/tr/th[4]/a")
    WebDriverWait(driver, 4).until(expected_conditions.element_to_be_clickable((By.XPATH, "/html/body/div/div[2]/div/div[2]/table/thead/tr/th[4]/a")))
    sorting_length.click()

    show_filter = driver.find_element(By.CLASS_NAME, "showfilter")
    WebDriverWait(driver, 4).until(expected_conditions.element_to_be_clickable((By.CLASS_NAME, "showfilter")))
    show_filter.click()

    domains_per_page = driver.find_element(By.NAME, "flimit")
    WebDriverWait(driver, 4).until(expected_conditions.visibility_of_element_located((By.NAME, "flimit")))
    select = Select(domains_per_page)
    select.select_by_index(4)

    no_hypens = driver.find_element(By.NAME, "fsephost")
    WebDriverWait(driver, 4).until(expected_conditions.element_to_be_clickable((By.NAME, "fsephost")))
    no_hypens.click()

    # opsiyonel
    only_characters = driver.find_element(By.NAME, "fonlycharhost")
    WebDriverWait(driver, 4).until(expected_conditions.element_to_be_clickable((By.NAME, "fonlycharhost")))
    only_characters.click()

    # opsiyonel
    '''english = driver.find_element(By.NAME, "fworden")
    WebDriverWait(driver, 4).until(expected_conditions.element_to_be_clickable((By.NAME, "fworden")))
    english.click()'''

    # opsiyonel
    max_word = driver.find_element(By.NAME, "fwordcountmax")
    WebDriverWait(driver, 4).until(expected_conditions.element_to_be_clickable((By.NAME, "fwordcountmax")))
    max_word.send_keys("3")

    checkbox_last_hours = driver.find_element(By.NAME, "flast24")
    WebDriverWait(driver, 4).until(expected_conditions.element_to_be_clickable((By.NAME, "flast24")))
    checkbox_last_hours.click()

    with_useful_words = driver.find_element(By.XPATH, "/html/body/div/div[2]/div/div[1]/form/div[1]/div[1]/div/div[1]/div/div[1]/div[1]/div[2]/div[2]/div/input")
    WebDriverWait(driver, 4).until(expected_conditions.element_to_be_clickable((By.XPATH, "/html/body/div/div[2]/div/div[1]/form/div[1]/div[1]/div/div[1]/div/div[1]/div[1]/div[2]/div[2]/div/input")))
    with_useful_words.send_keys("green environment smart virtual robot meta virtual reality"
                                " Tech china japan india Online Shop Store Market Digital Media"
                                " Cloud Web Finance Health Travel News Blog Social Games Music"
                                " Fashion Education Career america england english american"
                                " education health economy space society bio international cyber"
                                " sustainable renewable climate agriculture global learn ecolog"
                                " personal medic artificial intelligence crypto fintech money"
                                " media equal gender culture satellite internet mobile book"
                                " pedia air plane europe migrate asia")

    #opsiyonel
    max_letter_length = driver.find_element(By.NAME, "fmaxhost")
    max_letter_length.send_keys("20")

    button_submit = driver.find_element(By.NAME, "button_submit")
    WebDriverWait(driver, 4).until(expected_conditions.element_to_be_clickable((By.NAME, "button_submit")))
    button_submit.click()

    today_date = datetime.now().strftime("%Y-%m-%d")
    WebDriverWait(driver, 10).until(EC.visibility_of_element_located((By.CLASS_NAME, "pageinfo")))
    page_info = driver.find_element(By.CLASS_NAME, "pageinfo")
    page_number = int(page_info.text.split()[-2])
    file_name = f"domain_names_{today_date}.txt"

    with open(file_name, "w") as file:
        for i in range(page_number):
            WebDriverWait(driver, 10).until(EC.element_to_be_clickable((By.CLASS_NAME, "namelinks")))
            domain_names = driver.find_elements(By.CLASS_NAME, "namelinks")
            for name in domain_names:
                file.write(name.text + "\n")
            if (i + 1) % 30 == 0:
                time.sleep(10)
            WebDriverWait(driver, 10).until(
                EC.element_to_be_clickable((By.XPATH, "/html/body/div/div[2]/div/div[2]/div[2]/div[2]/div[1]/a")))
            next_page = driver.find_element(By.XPATH, "/html/body/div/div[2]/div/div[2]/div[2]/div[2]/div[1]/a")
            WebDriverWait(driver, 10).until(
                EC.element_to_be_clickable((By.XPATH, "/html/body/div/div[2]/div/div[2]/div[2]/div[2]/div[1]/a")))
            next_page.click()


if __name__ == "__main__":
    start_to_gather()
