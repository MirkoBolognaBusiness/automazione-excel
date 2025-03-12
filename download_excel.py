from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
import time

# Impostiamo il driver di Chrome
options = webdriver.ChromeOptions()
options.add_argument("--headless")  # Esegui senza interfaccia grafica
options.add_argument("--no-sandbox")
options.add_argument("--disable-dev-shm-usage")

# Inizializza il browser
driver = webdriver.Chrome(options=options)

# URL di login
url_login = "https://pegasoflorencegroupsrl.krossbooking.com"
username = "admin"
password = "@Gemelli74"

# Apriamo la pagina
driver.get(url_login)
time.sleep(2)

# Troviamo i campi di login e inseriamo i dati
driver.find_element(By.NAME, "username").send_keys(username)
driver.find_element(By.NAME, "password").send_keys(password)
driver.find_element(By.NAME, "password").send_keys(Keys.RETURN)

time.sleep(3)  # Aspettiamo il caricamento

# Andiamo direttamente alla pagina dell'export
export_url = "https://pegasoflorencegroupsrl.krossbooking.com/admin/report/ricavi-prenotazioni?period=01/03/2025%20-%2031/03/2025&statuses=&cod_meal_plans=&netprices=0&gr=&scorpora_iva=&id_room_types="
driver.get(export_url)

time.sleep(2)  # Aspettiamo il caricamento

# Troviamo e clicchiamo il pulsante "Export Excel"
export_button = driver.find_element(By.XPATH, "//button[contains(text(), 'Export Excel')]")
export_button.click()

time.sleep(5)  # Aspettiamo il download

# Chiudiamo il browser
driver.quit()
