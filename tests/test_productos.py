import pytest
from selenium import webdriver
from selenium.webdriver.common.by import By


def test_productos():
    driver = webdriver.Chrome()
    
    
    try:
        #Login
        driver.get("https://www.saucedemo.com/")
        
        usuario = driver.find_element(By.ID,"user-name")
        password = driver.find_element(By.ID,"password")
        boton_login = driver.find_element(By.ID,"login-button")
        
        #Que quiero hacer con estos elementos
        usuario.send_keys("standard_user")
        password.send_keys("secret_sauce")
        
        boton_login.click()
        
        
        #validacion agregar primer producto
        add_primer_producto = driver.find_element(By.CSS_SELECTOR, "[data-test='add-to-cart-sauce-labs-backpack']").click()
        #add_primer_producto.click()
        
        
        carrito_compras = driver.find_element(By.CLASS_NAME, "shopping_cart_link").click()
        
        
        lista_carrito_compras = driver.find_elements(By.CLASS_NAME,"inventory_item_name")
        
        #print(f"elementos: {len(carrito_compras)}")
        
        
        assert len(lista_carrito_compras) > 0
              
        primer_producto = lista_carrito_compras[0]
       
        primer_producto = driver.find_element(By.CLASS_NAME,"inventory_item_name")
        
        assert primer_producto.text == "Sauce Labs Backpack" 
        
        
        
        
    finally:
            driver.quit()