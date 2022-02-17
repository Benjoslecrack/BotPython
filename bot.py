from selenium import webdriver
from selenium.common.exceptions import ElementClickInterceptedException
from selenium.webdriver.common.by import By

# Constante
PATH = "C:\Program Files (x86)\chromedriver.exe"
CLASS_PRICE = "uqkIZw ka2E9k uMhVZi FxZV-M _6yVObe pVrzNP"
CLASS_ADD_CART = "DJxzzA u9KIT8 uEg2FS U_OhzR ZkIJC- Vn-7c- FCIprz heWLCX JIgPn9 LyRfpJ pxpHHp Md_Vex NN8L-8 GTG2H9 MfX1a0 WCjo-q EKabf7 aX2-iv r9BRio mo6ZnF E6Km4r"
CLASS_CART = "z-navicat-header_navToolItemLink"
CLASS_SIZE = "piG9a1 _1IcNq Uxq3DH QylWsg JCuRr_ _6yVObe _7Cm1F9 ka2E9k uMhVZi FxZV-M"
SELECT_SIZE = "size-picker-NI111A0ZB-A110105000" # 42

# Initialisation
driver = webdriver.Chrome(PATH)

# Chargement de la page
driver.get("https://www.zalando.fr/nike-sportswear-dunk-baskets-basses-whitemulticolor-ni111a0zb-a11.html")

# PRIX
price_div = driver.find_element(By.XPATH, "//span[@class='"+CLASS_PRICE+"']")
price = price_div.text
print(price)

# SIZE
size_div = driver.find_element(By.XPATH, "//span[@class='"+CLASS_SIZE+"']")
size_div.click()

# SELECT SIZE
select_size_div = driver.find_element(By.XPATH, "//label[@for='"+SELECT_SIZE+"']")
select_size_div.click()

    
# AJOUTER AU PANIER
add_cart_div = driver.find_element(By.XPATH, "//button[@class='"+CLASS_ADD_CART+"']")

try:
   add_cart_div.click()
except ElementClickInterceptedException:
    print("Article indisponible, Impossible d'ajouter au panier")

# Quitter le programme
driver.quit()

print("Yo la team !")