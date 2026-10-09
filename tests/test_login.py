import pytest
from selenium import webdriver
from selenium.webdriver.common.by import By

from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

def test_login_exitoso():
    driver = webdriver.Chrome()
    
    driver.implicitly_wait(10)
    
    wait = WebDriverWait(driver,10)
    
    try:
        #Login
        driver.get("https://www.saucedemo.com/")
        
        usuario = wait.until(EC.presence_of_element_located((By.ID,"user-name" ))).send_keys("standard_user")
        #driver.find_element(By.ID,"user-name")
        password = wait.until(EC.presence_of_element_located((By.ID,"password" ))).send_keys("secret_sauce")
        #driver.find_element(By.ID,"password")
        
        boton_login = wait.until(EC.element_to_be_clickable((By.ID,"login-button"))).click()
        
        #boton_login = driver.find_element(By.ID,"login-button")
        
        #Que quiero hacer con estos elementos
        #usuario.send_keys("standard_user")
        #password.send_keys("secret_sauce")
        
        #boton_login.click()
        
        #Validacion URL
        assert "/inventory.html" in driver.current_url
        
        #Validacion titulo pagina
        logo = driver.find_element(By.CLASS_NAME, "app_logo")
        print(f"Titulo de página: {(logo.text) }")
        assert logo.text == "Swag Labs"
        
        #validacion titulo inventario
        titulo = driver.find_element(By.CSS_SELECTOR, "[data-test='title']")
        assert titulo.text == "Products"
    finally:
        driver.quit()
        
        