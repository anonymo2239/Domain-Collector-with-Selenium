from selenium import webdriver
from selenium.webdriver.chrome.service import Service as ChromeService
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions
from selenium.webdriver.support.ui import Select
from datetime import datetime
from selenium.webdriver.common.keys import Keys
import time


def calculateValues():
    driver = webdriver.Chrome(service=ChromeService(ChromeDriverManager().install()))
    driver.maximize_window()
    driver.get("https://pc.domains")

    today_date = datetime.now().strftime("%Y-%m-%d")
    search_bar = driver.find_element(By.NAME, "vueInstant")
    check_button = driver.find_element(By.XPATH,
                                       "/html/body/div/div/div/div/div[1]/div[2]/section/div/div/div/div[2]/div[3]/div[2]/div[1]/div/form/div/button[1]")

    with open(f"domain_names_{today_date}.txt", "r") as file:
        domain_names = [line.strip() for line in file.readlines()]

    with open(f"domain_values_{today_date}.txt", "w") as file:
        i = 0
        for domain in domain_names:
            if i == 0:
                search_bar.send_keys(domain)
                check_button.click()
            else:
                check_button2 = driver.find_element(By.CLASS_NAME, "sbx-custom__submit")
                search_bar2 = driver.find_element(By.NAME, "vueInstant")
                time.sleep(1)
                WebDriverWait(driver, 4).until(expected_conditions.visibility_of_element_located(
                    (By.NAME, "vueInstant")))
                search_bar2.send_keys(Keys.CONTROL + "a")
                search_bar2.send_keys(Keys.DELETE)

                WebDriverWait(driver, 4).until(expected_conditions.visibility_of_element_located(
                    (By.NAME, "vueInstant")))
                search_bar2.send_keys(domain)
                WebDriverWait(driver, 4).until(expected_conditions.element_to_be_clickable(
                    (By.CLASS_NAME, "sbx-custom__submit")))
                check_button2.click()
            WebDriverWait(driver, 4).until(expected_conditions.element_to_be_clickable(
                (By.XPATH,
                 "/html/body/div/div/div/div/div[1]/div[2]/div[3]/div[1]/div/div/div/div/div[2]/div[1]/div[2]/div[2]/div/span[2]")))
            price_element = driver.find_element(By.XPATH,
                                                "/html/body/div/div/div/div/div[1]/div[2]/div[3]/div[1]/div/div/div/div/div[2]/div[1]/div[2]/div[2]/div/span[2]")
            WebDriverWait(driver, 4).until(expected_conditions.element_to_be_clickable(
                (By.XPATH,
                 "/html/body/div/div/div/div/div[1]/div[2]/div[3]/div[1]/div/div/div/div/div[2]/div[1]/div[2]/div[2]/div/span[2]")))
            price = price_element.text
            final_price = sayiyi_al(price)
            if final_price > 170:
                file.write(f"{domain}: {final_price}\n")
            i += 1
    sort_values(f"domain_values_{today_date}.txt")
    driver.quit()


def sort_values(file_path):
    with open(file_path, "r") as file:
        lines = file.readlines()
        # Sayıları alıp sıralamak için key parametresini kullanarak küçükten büyüğe sıralıyoruz
        lines.sort(key=lambda x: float(x.split(":")[1].strip()))

    with open(file_path, "w") as file:
        for line in lines:
            file.write(line)


def sayiyi_al(metin):
    sayi = ""
    for char in metin:
        if char.isdigit() or char == '.':
            sayi += char
    return float(sayi) if sayi else None


if __name__ == "__main__":
    calculateValues()
