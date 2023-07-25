from selenium import webdriver
from selenium.webdriver.common.by import By

# Inisialisasi driver
driver = webdriver.Chrome()

# Buka halaman web
driver.get("https://slidesgo.com/")

# Temukan tautan dengan teks tertentu dan klik
link_elem = driver.find_element(By.LINK_TEXT, "Selengkapnya")
link_elem.click()

# Tunggu beberapa detik sebelum menutup browser
driver.implicitly_wait(5)

# Tutup browser
driver.quit()
