from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import time
import logging


expected_address = "ul. Koszykowa 86, 02-008 Warszawa"

driver = webdriver.Chrome()
wait = WebDriverWait(driver, 15)

logger = logging.getLogger('LOGGER')
logger.setLevel(logging.INFO)
ch = logging.StreamHandler()
ch.setLevel(logging.DEBUG)
formatter = logging.Formatter('%(asctime)s - %(name)s - %(levelname)s - %(message)s')
ch.setFormatter(formatter)
logger.addHandler(ch)



try:
    logger.info('Start testu - Chrome')
    logger.info('Otwieram stronę PJATK')
    driver.get("https://pja.edu.pl")

    logger.warning('Próba akceptacji cookies')
    
    try:
        cookie_buttons = driver.find_elements(By.TAG_NAME, "button")
        for btn in cookie_buttons:
            if "zaakceptuj" in (btn.text or "").lower():
                btn.click()
                logger.info('Cookies zaakceptowane')
                break
        else:
           logger.warning('Brak przycisku')
    except Exception as e:
        logger.error('Nie udało się zaakceptować cookies')


    
    kontakt_link = wait.until(
    EC.presence_of_element_located((By.LINK_TEXT, "Kontakt"))
)
    driver.execute_script("arguments[0].scrollIntoView(true); arguments[0].click();", kontakt_link)

    try:
        cookie_buttons = driver.find_elements(By.TAG_NAME, "button")
        for btn in cookie_buttons:
            if "zaakceptuj" in (btn.text or "").lower():
                btn.click()
                logger.info('Cookies zaakceptowane')
                break
        else:
           logger.warning('Brak przycisku')
    except Exception as e:
        logger.error('Nie udało się zaakceptować cookies')
    
    time.sleep(1) 

    body_text = driver.find_element(By.TAG_NAME, "body").text

    logger.info('Test adresu')
    if expected_address in body_text:
        logger.info('Adres poprawny')
    else:
        logger.info('Adres niepoprawny')
 
finally:
    pass

