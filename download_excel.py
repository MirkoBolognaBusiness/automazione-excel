from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
import time
import shutil
import os

try:
    print("🚀 Avvio dello script...")

    # Configurazione di Selenium con Chrome
    options = webdriver.ChromeOptions()
    options.add_argument("--headless")  # Esegui senza interfaccia grafica
    options.add_argument("--no-sandbox")
    options.add_argument("--disable-dev-shm-usage")

    print("📌 Avvio del browser...")
    driver = webdriver.Chrome(options=options)

    # URL di login
    url_login = "https://pegasoflorencegroupsrl.krossbooking.com"
    username = "admin"
    password = "@Gemelli74"

    # Apriamo la pagina
    print(f"🌐 Apro la pagina di login: {url_login}")
    driver.get(url_login)
    time.sleep(2)

    # Troviamo i campi di login e inseriamo i dati
    print("🔑 Inserisco le credenziali...")
    driver.find_element(By.NAME, "username").send_keys(username)
    driver.find_element(By.NAME, "password").send_keys(password)
    driver.find_element(By.NAME, "password").send_keys(Keys.RETURN)

    time.sleep(3)  # Aspettiamo il caricamento

    # Andiamo direttamente alla pagina dell'export
    export_url = "https://pegasoflorencegroupsrl.krossbooking.com/admin/report/ricavi-prenotazioni?period=01/03/2025%20-%2031/03/2025&statuses=&cod_meal_plans=&netprices=0&gr=&scorpora_iva=&id_room_types="
    print(f"📂 Apro la pagina di export: {export_url}")
    driver.get(export_url)

    time.sleep(2)  # Aspettiamo il caricamento

    # Troviamo e clicchiamo il pulsante "Export Excel"
    print("📥 Cerco il pulsante 'Export Excel'...")
    export_button = driver.find_element(By.XPATH, "//button[contains(text(), 'Export Excel')]")
    export_button.click()

    print("✅ Download avviato!")
    time.sleep(5)  # Aspettiamo il download

    # Verifica dove viene salvato il file
    download_folder = "/home/runner/Downloads"  # Cartella predefinita di GitHub Actions
    files = os.listdir(download_folder)
    print("📂 File nella cartella Download:", files)

    # Trova il file Excel scaricato
    excel_file = None
    for file in files:
        if file.endswith(".xlsx"):
            excel_file = file
            break

    if excel_file:
        full_path = os.path.join(download_folder, excel_file)
        shutil.move(full_path, "downloaded_excel.xlsx")
        print("✅ File Excel spostato correttamente!")
    else:
        print("❌ Nessun file Excel trovato!")

    # Chiudiamo il browser
    driver.quit()
    print("🛑 Browser chiuso con successo!")

except Exception as e:
    print(f"❌ Errore durante l'esecuzione dello script: {str(e)}")
    exit(1)
