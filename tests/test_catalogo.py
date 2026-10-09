import pytest
from selenium import webdriver
from selenium.webdriver.common.by import By

from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

def test_catalogo():
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
        
        #Validacion del titulo pagina
        assert driver.title == "Swag Labs"
        
        #validacion catalogo de productos
        productos = driver.find_elements(By.CLASS_NAME,"inventory_item")
        print(f"Cantidad de Productos: {len(productos)}")
        assert len(productos) > 0
        
        primer_producto = productos[0]
        
        nombre_producto = primer_producto.find_element(By.CLASS_NAME, "inventory_item_name ").text
        precio_producto = primer_producto.find_element(By.CLASS_NAME, "inventory_item_price").text
        
        #validacion primer producto
        assert nombre_producto == "Sauce Labs Backpack"
        assert precio_producto == "$29.99"
        
        #Verificar menu hamburguesa
        menu = driver.find_element(By.ID, "react-burger-menu-btn")
        
        #elemento visible en la pagina
        assert menu.is_displayed()
    
        #verificar filtro
        filtro = driver.find_element(By.CLASS_NAME, "product_sort_container")
        
        assert filtro.is_displayed()
        
    finally:
        driver.quit()
