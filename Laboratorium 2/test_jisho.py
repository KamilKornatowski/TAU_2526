from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import logging

service = Service()

logger = logging.getLogger('LOGGER')
logger.setLevel(logging.INFO)
ch = logging.StreamHandler()
ch.setLevel(logging.DEBUG)
formatter = logging.Formatter('%(asctime)s - %(name)s - %(levelname)s - %(message)s')
ch.setFormatter(formatter)
logger.addHandler(ch)


driver = webdriver.Chrome(service=service)

try:
    logger.info('Start testu - Chrome')
    logger.info('Otwieram słownik Jisho.org')
    driver.get("https://jisho.org")
    wait = WebDriverWait(driver, 10)

    logger.info("Wyszukuję słowo komputer")
    search_box = wait.until(EC.presence_of_element_located((By.ID, "keyword")))
    search_box.send_keys("computer")
    search_box.send_keys(Keys.RETURN)

    logger.info("Czekam na wyniki")
    first_result = wait.until(
        EC.presence_of_element_located((By.CSS_SELECTOR, ".concept_light.clearfix a"))
    )

   

    logger.info("Test zakonczony")
    print("Test zakończony – słowo wyszukane")

finally:
    pass


driver = webdriver.Firefox()
wait = WebDriverWait(driver, 10)

try:
    logger.info('Start testu - Firefox')
    logger.info('Otwieram słownik Jisho.org')
    driver.get("https://jisho.org")

    logger.info("Wyszukuję słowo komputer")
    search_box = wait.until(EC.presence_of_element_located((By.ID, "keyword")))
    search_box.send_keys("computer")
    search_box.send_keys(Keys.RETURN)

    logger.warning("Czekam na wyniki")
    first_result = wait.until(
        EC.presence_of_element_located((By.CSS_SELECTOR, ".concept_light.clearfix a"))
    )

    
    logger.info("Test zakonczony")


    print("Test zakończony – słowo wyszukane")
finally:
    pass  