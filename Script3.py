from selenium import webdriver
from selenium.webdriver.common.by import By

# Inisialisasi driver
driver = webdriver.Chrome()

# Buka halaman web dengan formulir
driver.get("https://ecourse.del.ac.id/form")

# Temukan elemen input dan masukkan teks
input_elem = driver.find_element(By.NAME, "email")
input_elem.send_keys("https://ecourse.del.ac.id")

# Temukan elemen textarea dan masukkan teks
textarea_elem = driver.find_element(By.NAME, "message")
textarea_elem.send_keys("Ini adalah pesan contoh.")

# Kirim formulir dengan metode submit()
textarea_elem.submit()

# Tunggu beberapa detik sebelum menutup browser
driver.implicitly_wait(5)

# Tutup browser
driver.quit()
