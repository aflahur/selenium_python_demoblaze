import time
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.ui import WebDriverWait

import unittest
from selenium import webdriver

class demoBlazeTest(unittest.TestCase):
    def setUp(self):
        self.driver = webdriver.Chrome()
        self.url="https://www.demoblaze.com/"
    
    def test_cart_with_logins(self):
        driver = self.driver #buka web browser
        driver.get(self.url) # buka situs
        driver.maximize_window()
        # driver.find_element(By.ID,"login2").click()
        # driver.find_element(By.XPATH("//input[@id='loginusername']")).send_keys("cek12345@gmail.com")
        # driver.find_element(By.ID,"loginpassword").send_keys("cek12345")
        # driver.find_element(By.CLASS_NAME,"btn btn-primary").click()
        login=driver.find_element(By.ID,"login2")
        WebDriverWait(driver,5).until(EC.element_to_be_clickable(login))
        login.click()
        username=driver.find_element(By.ID,"loginusername")
        WebDriverWait(driver,5).until(EC.visibility_of(username))
        username.send_keys("cek12345@gmail.com")
        password=driver.find_element(By.ID,"loginpassword")
        WebDriverWait(driver,5).until(EC.visibility_of(password))
        password.send_keys("cek12345")
        driver.find_element("xpath", "//button[contains(text(),'Log in')]").click()
        WebDriverWait(driver, 10).until(EC.presence_of_element_located((By.LINK_TEXT, "Log out")))#untuk bantuan,tidak ada fungsi click
        WebDriverWait(driver, 10).until(EC.presence_of_element_located((By.LINK_TEXT, "Cart"))).click()
        # cart=driver.find_element(By.ID,"cartur")
        # WebDriverWait(driver, 10).until(EC.element_to_be_clickable(cart))
        # cart.click()

    def test_cart_without_login(self):
        driver=self.driver
        driver.get(self.url)
        driver.maximize_window()
        WebDriverWait(driver, 10).until(EC.presence_of_element_located((By.LINK_TEXT, "Cart"))).click()

    def test_add_to_cart_with_login(self):
        driver = self.driver #buka web browser
        driver.get(self.url) # buka situs
        driver.maximize_window()
        login=driver.find_element(By.ID,"login2")
        WebDriverWait(driver,5).until(EC.element_to_be_clickable(login))
        login.click()
        username=driver.find_element(By.ID,"loginusername")
        WebDriverWait(driver,5).until(EC.visibility_of(username))
        username.send_keys("cek12345@gmail.com")
        password=driver.find_element(By.ID,"loginpassword")
        WebDriverWait(driver,5).until(EC.visibility_of(password))
        password.send_keys("cek12345")
        driver.find_element("xpath", "//button[contains(text(),'Log in')]").click()
        WebDriverWait(driver, 10).until(EC.presence_of_element_located((By.LINK_TEXT, "Log out")))#untuk bantuan,tidak ada fungsi click
        # WebDriverWait(driver, 10).until(EC.presence_of_element_located((By.LINK_TEXT, "Phones"))).click()
        WebDriverWait(driver, 10).until(EC.presence_of_element_located((By.LINK_TEXT, "Samsung galaxy s6"))).click()
        WebDriverWait(driver, 10).until(EC.presence_of_element_located((By.LINK_TEXT, "Add to cart"))).click()
        WebDriverWait(driver, 5).until(EC.alert_is_present())
        alert = driver.switch_to.alert
        successMessage=alert.text
        print(alert.text)
        alert.accept()
        self.assertEqual("Product added.", successMessage)

    def test_add_to_cart_without_login(self):
        driver = self.driver #buka web browser
        driver.get(self.url) # buka situs
        driver.maximize_window()
        # WebDriverWait(driver, 10).until(EC.presence_of_element_located((By.LINK_TEXT, "Phones"))).click()
        WebDriverWait(driver, 10).until(EC.presence_of_element_located((By.LINK_TEXT, "Samsung galaxy s6"))).click()
        WebDriverWait(driver, 10).until(EC.presence_of_element_located((By.LINK_TEXT, "Add to cart"))).click()
        WebDriverWait(driver, 5).until(EC.alert_is_present())
        alert = driver.switch_to.alert
        successMessage=alert.text
        print(alert.text)
        alert.accept()
        self.assertEqual("Product added", successMessage)
    
    def test_add_more_than_one_with_login(self):
        driver = self.driver #buka web browser
        driver.get(self.url) # buka situs
        driver.maximize_window()
        login=driver.find_element(By.ID,"login2")
        WebDriverWait(driver,5).until(EC.element_to_be_clickable(login))
        login.click()
        username=driver.find_element(By.ID,"loginusername")
        WebDriverWait(driver,5).until(EC.visibility_of(username))
        username.send_keys("cek12345@gmail.com")
        password=driver.find_element(By.ID,"loginpassword")
        WebDriverWait(driver,5).until(EC.visibility_of(password))
        password.send_keys("cek12345")
        driver.find_element("xpath", "//button[contains(text(),'Log in')]").click()
        WebDriverWait(driver, 10).until(EC.presence_of_element_located((By.LINK_TEXT, "Log out")))#untuk bantuan,tidak ada fungsi click
        WebDriverWait(driver, 10).until(EC.presence_of_element_located((By.LINK_TEXT, "Samsung galaxy s6"))).click()
        WebDriverWait(driver, 10).until(EC.presence_of_element_located((By.LINK_TEXT, "Add to cart"))).click()
        WebDriverWait(driver, 5).until(EC.alert_is_present())
        alert = driver.switch_to.alert
        successMessage=alert.text
        print(alert.text)
        alert.accept()
        self.assertEqual("Product added.", successMessage)
        driver.find_element(By.XPATH, "//a[contains(text(),'Home')]").click()
        WebDriverWait(driver,10).until(EC.presence_of_element_located((By.LINK_TEXT,"Nokia lumia 1520"))).click()
        WebDriverWait(driver, 10).until(EC.presence_of_element_located((By.LINK_TEXT, "Add to cart"))).click()
        WebDriverWait(driver, 5).until(EC.alert_is_present())
        alert2 = driver.switch_to.alert
        message = alert2.text
        print(alert2.text)
        alert.accept()
        self.assertEqual("Product added.", message)
        WebDriverWait(driver, 10).until(EC.presence_of_element_located((By.LINK_TEXT, "Cart"))).click()

    def test_add_more_than_one_without_login(self):
        driver = self.driver #buka web browser
        driver.get(self.url) # buka situs
        driver.maximize_window()
        WebDriverWait(driver, 10).until(EC.presence_of_element_located((By.LINK_TEXT, "Samsung galaxy s6"))).click()
        WebDriverWait(driver, 10).until(EC.presence_of_element_located((By.LINK_TEXT, "Add to cart"))).click()
        WebDriverWait(driver, 5).until(EC.alert_is_present())
        alert = driver.switch_to.alert
        successMessage=alert.text
        print(alert.text)
        alert.accept()
        self.assertEqual("Product added", successMessage)
        driver.find_element(By.XPATH, "//a[contains(text(),'Home')]").click()
        WebDriverWait(driver,10).until(EC.presence_of_element_located((By.LINK_TEXT,"Nokia lumia 1520"))).click()
        WebDriverWait(driver, 10).until(EC.presence_of_element_located((By.LINK_TEXT, "Add to cart"))).click()
        WebDriverWait(driver, 5).until(EC.alert_is_present())
        alert2 = driver.switch_to.alert
        message = alert2.text
        print(alert2.text)
        alert.accept()
        self.assertEqual("Product added", message)
        WebDriverWait(driver, 10).until(EC.presence_of_element_located((By.LINK_TEXT, "Cart"))).click()

    def test_delete_one_with_login(self):
        driver = self.driver #buka web browser
        driver.get(self.url) # buka situs
        driver.maximize_window()
        login=driver.find_element(By.ID,"login2")
        WebDriverWait(driver,5).until(EC.element_to_be_clickable(login))
        login.click()
        username=driver.find_element(By.ID,"loginusername")
        WebDriverWait(driver,5).until(EC.visibility_of(username))
        username.send_keys("cek12345@gmail.com")
        password=driver.find_element(By.ID,"loginpassword")
        WebDriverWait(driver,5).until(EC.visibility_of(password))
        password.send_keys("cek12345")
        driver.find_element("xpath", "//button[contains(text(),'Log in')]").click()
        WebDriverWait(driver, 10).until(EC.presence_of_element_located((By.LINK_TEXT, "Log out")))#untuk bantuan,tidak ada fungsi click
        WebDriverWait(driver, 10).until(EC.presence_of_element_located((By.LINK_TEXT, "Samsung galaxy s6"))).click()
        WebDriverWait(driver, 10).until(EC.presence_of_element_located((By.LINK_TEXT, "Add to cart"))).click()
        WebDriverWait(driver, 5).until(EC.alert_is_present())
        alert = driver.switch_to.alert
        successMessage=alert.text
        print(alert.text)
        alert.accept()
        self.assertEqual("Product added.", successMessage)
        WebDriverWait(driver, 10).until(EC.presence_of_element_located((By.LINK_TEXT, "Cart"))).click()
        time.sleep(2)
        driver.find_element(By.LINK_TEXT,"Delete").click()

    def test_delete_one_without_login(self):
        driver = self.driver #buka web browser
        driver.get(self.url) # buka situs
        driver.maximize_window()
        WebDriverWait(driver, 10).until(EC.presence_of_element_located((By.LINK_TEXT, "Samsung galaxy s6"))).click()
        WebDriverWait(driver, 10).until(EC.presence_of_element_located((By.LINK_TEXT, "Add to cart"))).click()
        WebDriverWait(driver, 5).until(EC.alert_is_present())
        alert = driver.switch_to.alert
        successMessage=alert.text
        print(alert.text)
        alert.accept()
        self.assertEqual("Product added", successMessage)
        WebDriverWait(driver, 10).until(EC.presence_of_element_located((By.LINK_TEXT, "Cart"))).click()
        time.sleep(2)
        driver.find_element(By.LINK_TEXT,"Delete").click()

    def test_delete_more_than_one_without_login(self):
        driver = self.driver #buka web browser
        driver.get(self.url) # buka situs
        driver.maximize_window()
        WebDriverWait(driver, 10).until(EC.presence_of_element_located((By.LINK_TEXT, "Samsung galaxy s6"))).click()
        WebDriverWait(driver, 10).until(EC.presence_of_element_located((By.LINK_TEXT, "Add to cart"))).click()
        WebDriverWait(driver, 5).until(EC.alert_is_present())
        alert = driver.switch_to.alert
        successMessage=alert.text
        print(alert.text)
        alert.accept()
        self.assertEqual("Product added", successMessage)
        driver.find_element(By.XPATH, "//a[contains(text(),'Home')]").click()
        WebDriverWait(driver,10).until(EC.presence_of_element_located((By.LINK_TEXT,"Nokia lumia 1520"))).click()
        WebDriverWait(driver, 10).until(EC.presence_of_element_located((By.LINK_TEXT, "Add to cart"))).click()
        WebDriverWait(driver, 5).until(EC.alert_is_present())
        alert2 = driver.switch_to.alert
        message = alert2.text
        print(alert2.text)
        alert.accept()
        self.assertEqual("Product added", message)
        driver.find_element(By.XPATH, "//a[contains(text(),'Home')]").click()
        WebDriverWait(driver,10).until(EC.presence_of_element_located((By.LINK_TEXT,"Nexus 6"))).click()
        WebDriverWait(driver, 10).until(EC.presence_of_element_located((By.LINK_TEXT, "Add to cart"))).click()
        WebDriverWait(driver, 5).until(EC.alert_is_present())
        alert3 = driver.switch_to.alert
        message3 = alert3.text
        print(alert3.text)
        alert.accept()
        self.assertEqual("Product added", message3)
        WebDriverWait(driver, 10).until(EC.presence_of_element_located((By.LINK_TEXT, "Cart"))).click()
        time.sleep(2)
        driver.find_element(By.LINK_TEXT,"Delete").click()
        time.sleep(2)
        driver.find_element(By.XPATH, "//a[contains(text(),'Home')]").click()
        WebDriverWait(driver, 10).until(EC.presence_of_element_located((By.LINK_TEXT, "Cart"))).click()
        time.sleep(2)
        driver.find_element(By.LINK_TEXT,"Delete").click()
        time.sleep(2)
        driver.find_element(By.XPATH, "//a[contains(text(),'Home')]").click()
        WebDriverWait(driver, 10).until(EC.presence_of_element_located((By.LINK_TEXT, "Cart"))).click()
        time.sleep(2)
        driver.find_element(By.LINK_TEXT,"Delete").click()
        time.sleep(2)
        aftercountofcart = driver.find_elements(By.LINK_TEXT, "Delete")
        print("sisa produk: ", len(aftercountofcart))

    def test_delete_more_than_one_with_login(self):
        driver = self.driver #buka web browser
        driver.get(self.url) # buka situs
        driver.maximize_window()
        login=driver.find_element(By.ID,"login2")
        WebDriverWait(driver,5).until(EC.element_to_be_clickable(login))
        login.click()
        username=driver.find_element(By.ID,"loginusername")
        WebDriverWait(driver,5).until(EC.visibility_of(username))
        username.send_keys("cek12345@gmail.com")
        password=driver.find_element(By.ID,"loginpassword")
        WebDriverWait(driver,5).until(EC.visibility_of(password))
        password.send_keys("cek12345")
        driver.find_element("xpath", "//button[contains(text(),'Log in')]").click()
        WebDriverWait(driver, 10).until(EC.presence_of_element_located((By.LINK_TEXT, "Log out")))#untuk bantuan,tidak ada fungsi click
        WebDriverWait(driver, 10).until(EC.presence_of_element_located((By.LINK_TEXT, "Samsung galaxy s6"))).click()
        WebDriverWait(driver, 10).until(EC.presence_of_element_located((By.LINK_TEXT, "Add to cart"))).click()
        WebDriverWait(driver, 5).until(EC.alert_is_present())
        alert = driver.switch_to.alert
        successMessage=alert.text
        print(alert.text)
        alert.accept()
        self.assertEqual("Product added.", successMessage)
        driver.find_element(By.XPATH, "//a[contains(text(),'Home')]").click()
        WebDriverWait(driver,10).until(EC.presence_of_element_located((By.LINK_TEXT,"Nokia lumia 1520"))).click()
        WebDriverWait(driver, 10).until(EC.presence_of_element_located((By.LINK_TEXT, "Add to cart"))).click()
        WebDriverWait(driver, 5).until(EC.alert_is_present())
        alert2 = driver.switch_to.alert
        message = alert2.text
        print(alert2.text)
        alert.accept()
        self.assertEqual("Product added.", message)
        WebDriverWait(driver, 10).until(EC.presence_of_element_located((By.LINK_TEXT, "Cart"))).click()
        time.sleep(2)
        driver.find_element(By.LINK_TEXT,"Delete").click()
        time.sleep(2)
        driver.find_element(By.XPATH, "//a[contains(text(),'Home')]").click()
        WebDriverWait(driver, 10).until(EC.presence_of_element_located((By.LINK_TEXT, "Cart"))).click()
        time.sleep(2)
        driver.find_element(By.LINK_TEXT,"Delete").click()
        time.sleep(2)

    def tearDown(self):
        self.driver.close()

if __name__ == "__main__":
    unittest.main()