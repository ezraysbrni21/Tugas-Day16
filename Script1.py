from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys

# Inisialisasi driver
driver = webdriver.Chrome()

# Buka halaman web
driver.get("https://www.teepublic.com")

# Temukan elemen input dan masukkan teks
input_elem = driver.find_element(By.NAME, "username")
input_elem.send_keys("pengguna123")

# Temukan elemen password dan masukkan kata sandi
password_elem = driver.find_element(By.NAME, "password")
password_elem.send_keys("password123")

# Kirim formulir dengan menekan tombol Enter
password_elem.send_keys(Keys.ENTER)

# Tunggu beberapa detik sebelum menutup browser
driver.implicitly_wait(5)

# Tutup browser
driver.quit()
