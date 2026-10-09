import pytest
from selenium import webdriver
from selenium.webdriver.common.by import By

from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

def test_carrito():
    driver = webdriver.Chrome()
    
    driver.implicitly_wait(10)
    
    wait = WebDriverWait(driver, 10)
    
    
    try:
        #Login
        driver.get("https://www.saucedemo.com/")
        
        usuario = wait.until(EC.visibility_of_element_located((By.ID,"user-name"))).send_keys("standard_user")
        #usuario = driver.find_element(By.ID,"user-name")
        password = driver.find_element(By.ID,"password").send_keys("secret_sauce")
        boton_login = driver.find_element(By.ID,"login-button").click()
        
        #Que quiero hacer con estos elementos
        #usuario.send_keys("standard_user")
        #password.send_keys("secret_sauce")
        
        #boton_login.click()
        
        #validacion primer prducto
        primer_producto = wait.until(EC.visibility_of_element_located((By.CLASS_NAME,"inventory_item")))
        
        #validacion nombre/agregar producto
        nombre_producto = primer_producto.find_element(By.CLASS_NAME,"inventory_item_name").text
        boton_agregar = primer_producto.find_element(By.TAG_NAME,"button").click()
        
        #validacion contador carrito
        contador_carrito = wait.until(EC.visibility_of_element_located((By.CLASS_NAME, "shopping_cart_badge")))
        assert contador_carrito.text == "1"
        
        wait.until(EC.element_to_be_clickable((By.CLASS_NAME, "shopping_cart_link"))).click()
        
        #validacion producto agregado al carrito
        nombre_producto_carrito = wait.until(EC.visibility_of_element_located((By.CLASS_NAME, "inventory_item_name"))).text
        print(f"Producto agregado: {nombre_producto_carrito}")
        assert nombre_producto == nombre_producto_carrito
        
        
        #validacion agregar primer producto
        #add_primer_producto = driver.find_element(By.CSS_SELECTOR, "[data-test='add-to-cart-sauce-labs-backpack']").click()
        #add_primer_producto.click()
        
        
        #carrito_compras = driver.find_element(By.CLASS_NAME, "shopping_cart_link").click()
        
        #lista_carrito_compras = driver.find_elements(By.CLASS_NAME,"inventory_item_name")
        #print(f"Productos añadidos al carrito: {len(lista_carrito_compras)}")
        
        #validacion producto agregado
        #assert len(lista_carrito_compras) > 0
              
        #primer_producto = lista_carrito_compras[0]
       
        #primer_producto = driver.find_element(By.CLASS_NAME,"inventory_item_name")
        
        #validacion texto producto agregado
        #assert primer_producto.text == "Sauce Labs Backpack" 
        
    finally:
            driver.quit()