import time
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.ui import WebDriverWait
import unittest
from selenium import webdriver
from POM.elementLocatorCart import cartPage
from POM.dataCart import inputanCart

class demoBlazeTest(unittest.TestCase):
    def setUp(self):
        self.driver = webdriver.Chrome()
        self.url=inputanCart.url
    
    def test_cart_with_logins(self):
        driver = self.driver #buka web browser
        driver.get(self.url) # buka situs
        driver.maximize_window()
        login=driver.find_element(*cartPage.idLoginPage)
        WebDriverWait(driver,5).until(EC.element_to_be_clickable(login))
        login.click()
        username=driver.find_element(*cartPage.idUsername)
        WebDriverWait(driver,5).until(EC.visibility_of(username))
        username.send_keys(inputanCart.username)
        password=driver.find_element(*cartPage.idPassword)
        WebDriverWait(driver,5).until(EC.visibility_of(password))
        password.send_keys(inputanCart.password)
        driver.find_element(*cartPage.buttonLogin).click()
        WebDriverWait(driver, 10).until(EC.presence_of_element_located((cartPage.linkLogout)))#untuk bantuan,tidak ada fungsi click
        WebDriverWait(driver, 10).until(EC.presence_of_element_located((cartPage.linkCartPage))).click()

    def test_cart_without_login(self):
        driver=self.driver
        driver.get(self.url)
        driver.maximize_window()
        WebDriverWait(driver, 10).until(EC.presence_of_element_located((cartPage.linkCartPage))).click()

    def test_add_to_cart_with_login(self):
        driver = self.driver #buka web browser
        driver.get(self.url) # buka situs
        driver.maximize_window()
        login=driver.find_element(*cartPage.idLoginPage)
        WebDriverWait(driver,5).until(EC.element_to_be_clickable(login))
        login.click()
        username=driver.find_element(*cartPage.idUsername)
        WebDriverWait(driver,5).until(EC.visibility_of(username))
        username.send_keys(inputanCart.username)
        password=driver.find_element(*cartPage.idPassword)
        WebDriverWait(driver,5).until(EC.visibility_of(password))
        password.send_keys(inputanCart.password)
        driver.find_element(*cartPage.buttonLogin).click()
        WebDriverWait(driver, 10).until(EC.presence_of_element_located((cartPage.linkLogout)))#untuk bantuan,tidak ada fungsi click
        WebDriverWait(driver, 10).until(EC.presence_of_element_located((cartPage.linkSamsung))).click()
        WebDriverWait(driver, 10).until(EC.presence_of_element_located((cartPage.linkAddToCart))).click()
        WebDriverWait(driver, 5).until(EC.alert_is_present())
        alert = driver.switch_to.alert
        successMessage=alert.text
        print(alert.text)
        alert.accept()
        self.assertEqual(inputanCart.productAddWithLogin, successMessage)

    def test_add_to_cart_without_login(self):
        driver = self.driver #buka web browser
        driver.get(self.url) # buka situs
        driver.maximize_window()
        WebDriverWait(driver, 10).until(EC.presence_of_element_located((cartPage.linkSamsung))).click()
        WebDriverWait(driver, 10).until(EC.presence_of_element_located((cartPage.linkAddToCart))).click()
        WebDriverWait(driver, 5).until(EC.alert_is_present())
        alert = driver.switch_to.alert
        successMessage=alert.text
        print(alert.text)
        alert.accept()
        self.assertEqual(inputanCart.productAddWithoutLoign, successMessage)
    
    def test_add_more_than_one_with_login(self):
        driver = self.driver #buka web browser
        driver.get(self.url) # buka situs
        driver.maximize_window()
        login=driver.find_element(*cartPage.idLoginPage)
        WebDriverWait(driver,5).until(EC.element_to_be_clickable(login))
        login.click()
        username=driver.find_element(*cartPage.idUsername)
        WebDriverWait(driver,5).until(EC.visibility_of(username))
        username.send_keys(inputanCart.username)
        password=driver.find_element(*cartPage.idPassword)
        WebDriverWait(driver,5).until(EC.visibility_of(password))
        password.send_keys(inputanCart.password)
        driver.find_element(*cartPage.buttonLogin).click()
        WebDriverWait(driver, 10).until(EC.presence_of_element_located((cartPage.linkLogout)))#untuk bantuan,tidak ada fungsi click
        WebDriverWait(driver, 10).until(EC.presence_of_element_located((cartPage.linkSamsung))).click()
        WebDriverWait(driver, 10).until(EC.presence_of_element_located((cartPage.linkAddToCart))).click()
        WebDriverWait(driver, 5).until(EC.alert_is_present())
        alert = driver.switch_to.alert
        successMessage=alert.text
        print(alert.text)
        alert.accept()
        self.assertEqual(inputanCart.productAddWithLogin, successMessage)
        driver.find_element(*cartPage.linkHome).click()
        WebDriverWait(driver,10).until(EC.presence_of_element_located((cartPage.linkNokia))).click()
        WebDriverWait(driver, 10).until(EC.presence_of_element_located((cartPage.linkAddToCart))).click()
        WebDriverWait(driver, 5).until(EC.alert_is_present())
        alert2 = driver.switch_to.alert
        message = alert2.text
        print(alert2.text)
        alert.accept()
        self.assertEqual(inputanCart.productAddWithLogin, message)
        WebDriverWait(driver, 10).until(EC.presence_of_element_located((cartPage.linkCartPage))).click()

    def test_add_more_than_one_without_login(self):
        driver = self.driver #buka web browser
        driver.get(self.url) # buka situs
        driver.maximize_window()
        WebDriverWait(driver, 10).until(EC.presence_of_element_located((cartPage.linkSamsung))).click()
        WebDriverWait(driver, 10).until(EC.presence_of_element_located((cartPage.linkAddToCart))).click()
        WebDriverWait(driver, 5).until(EC.alert_is_present())
        alert = driver.switch_to.alert
        successMessage=alert.text
        print(alert.text)
        alert.accept()
        self.assertEqual(inputanCart.productAddWithoutLoign, successMessage)
        driver.find_element(*cartPage.linkHome).click()
        WebDriverWait(driver,10).until(EC.presence_of_element_located((cartPage.linkNokia))).click()
        WebDriverWait(driver, 10).until(EC.presence_of_element_located((cartPage.linkAddToCart))).click()
        WebDriverWait(driver, 5).until(EC.alert_is_present())
        alert2 = driver.switch_to.alert
        message = alert2.text
        print(alert2.text)
        alert.accept()
        self.assertEqual(inputanCart.productAddWithoutLoign, message)
        WebDriverWait(driver, 10).until(EC.presence_of_element_located((cartPage.linkCartPage))).click()

    def test_delete_one_with_login(self):
        driver = self.driver #buka web browser
        driver.get(self.url) # buka situs
        driver.maximize_window()
        login=driver.find_element(*cartPage.idLoginPage)
        WebDriverWait(driver,5).until(EC.element_to_be_clickable(login))
        login.click()
        username=driver.find_element(*cartPage.idUsername)
        WebDriverWait(driver,5).until(EC.visibility_of(username))
        username.send_keys(inputanCart.username)
        password=driver.find_element(*cartPage.idPassword)
        WebDriverWait(driver,5).until(EC.visibility_of(password))
        password.send_keys(inputanCart.password)
        driver.find_element(*cartPage.buttonLogin).click()
        WebDriverWait(driver, 10).until(EC.presence_of_element_located((cartPage.linkLogout)))#untuk bantuan,tidak ada fungsi click
        WebDriverWait(driver, 10).until(EC.presence_of_element_located((cartPage.linkSamsung))).click()
        WebDriverWait(driver, 10).until(EC.presence_of_element_located((cartPage.linkAddToCart))).click()
        WebDriverWait(driver, 5).until(EC.alert_is_present())
        alert = driver.switch_to.alert
        successMessage=alert.text
        print(alert.text)
        alert.accept()
        self.assertEqual(inputanCart.productAddWithLogin, successMessage)
        WebDriverWait(driver, 10).until(EC.presence_of_element_located((cartPage.linkCartPage))).click()
        time.sleep(2)
        driver.find_element(*cartPage.linkDelete).click()

    def test_delete_one_without_login(self):
        driver = self.driver #buka web browser
        driver.get(self.url) # buka situs
        driver.maximize_window()
        WebDriverWait(driver, 10).until(EC.presence_of_element_located((cartPage.linkSamsung))).click()
        WebDriverWait(driver, 10).until(EC.presence_of_element_located((cartPage.linkAddToCart))).click()
        WebDriverWait(driver, 5).until(EC.alert_is_present())
        alert = driver.switch_to.alert
        successMessage=alert.text
        print(alert.text)
        alert.accept()
        self.assertEqual(inputanCart.productAddWithoutLoign, successMessage)
        WebDriverWait(driver, 10).until(EC.presence_of_element_located((cartPage.linkCartPage))).click()
        time.sleep(2)
        driver.find_element(*cartPage.linkDelete).click()

    def test_delete_more_than_one_without_login(self):
        driver = self.driver #buka web browser
        driver.get(self.url) # buka situs
        driver.maximize_window()
        WebDriverWait(driver, 10).until(EC.presence_of_element_located((cartPage.linkSamsung))).click()
        WebDriverWait(driver, 10).until(EC.presence_of_element_located((cartPage.linkAddToCart))).click()
        WebDriverWait(driver, 5).until(EC.alert_is_present())
        alert = driver.switch_to.alert
        successMessage=alert.text
        print(alert.text)
        alert.accept()
        self.assertEqual(inputanCart.productAddWithoutLoign, successMessage)
        driver.find_element(*cartPage.linkHome).click()
        WebDriverWait(driver,10).until(EC.presence_of_element_located((cartPage.linkNokia))).click()
        WebDriverWait(driver, 10).until(EC.presence_of_element_located((cartPage.linkAddToCart))).click()
        WebDriverWait(driver, 5).until(EC.alert_is_present())
        alert2 = driver.switch_to.alert
        message = alert2.text
        print(alert2.text)
        alert.accept()
        self.assertEqual(inputanCart.productAddWithoutLoign, message)
        driver.find_element(*cartPage.linkHome).click()
        WebDriverWait(driver,10).until(EC.presence_of_element_located((cartPage.linkNexus))).click()
        WebDriverWait(driver, 10).until(EC.presence_of_element_located((cartPage.linkAddToCart))).click()
        WebDriverWait(driver, 5).until(EC.alert_is_present())
        alert3 = driver.switch_to.alert
        message3 = alert3.text
        print(alert3.text)
        alert.accept()
        self.assertEqual(inputanCart.productAddWithoutLoign, message3)
        WebDriverWait(driver, 10).until(EC.presence_of_element_located((cartPage.linkCartPage))).click()
        time.sleep(2)
        driver.find_element(*cartPage.linkDelete).click()
        time.sleep(2)
        driver.find_element(*cartPage.linkHome).click()
        WebDriverWait(driver, 10).until(EC.presence_of_element_located((cartPage.linkCartPage))).click()
        time.sleep(2)
        driver.find_element(*cartPage.linkDelete).click()
        time.sleep(2)
        driver.find_element(*cartPage.linkHome).click()
        WebDriverWait(driver, 10).until(EC.presence_of_element_located((cartPage.linkCartPage))).click()
        time.sleep(2)
        driver.find_element(*cartPage.linkDelete).click()
        time.sleep(2)
        aftercountofcart = driver.find_elements(*cartPage.linkDelete)
        print(inputanCart.sisaProduk, len(aftercountofcart))

    def test_delete_more_than_one_with_login(self):
        driver = self.driver #buka web browser
        driver.get(self.url) # buka situs
        driver.maximize_window()
        login=driver.find_element(*cartPage.idLoginPage)
        WebDriverWait(driver,5).until(EC.element_to_be_clickable(login))
        login.click()
        username=driver.find_element(*cartPage.idUsername)
        WebDriverWait(driver,5).until(EC.visibility_of(username))
        username.send_keys(inputanCart.username)
        password=driver.find_element(*cartPage.idPassword)
        WebDriverWait(driver,5).until(EC.visibility_of(password))
        password.send_keys(inputanCart.password)
        driver.find_element(*cartPage.buttonLogin).click()
        WebDriverWait(driver, 10).until(EC.presence_of_element_located((cartPage.linkLogout)))#untuk bantuan,tidak ada fungsi click
        WebDriverWait(driver, 10).until(EC.presence_of_element_located((cartPage.linkSamsung))).click()
        WebDriverWait(driver, 10).until(EC.presence_of_element_located((cartPage.linkAddToCart))).click()
        WebDriverWait(driver, 5).until(EC.alert_is_present())
        alert = driver.switch_to.alert
        successMessage=alert.text
        print(alert.text)
        alert.accept()
        self.assertEqual(inputanCart.productAddWithLogin, successMessage)
        driver.find_element(*cartPage.linkHome).click()
        WebDriverWait(driver,10).until(EC.presence_of_element_located((cartPage.linkNokia))).click()
        WebDriverWait(driver, 10).until(EC.presence_of_element_located((cartPage.linkAddToCart))).click()
        WebDriverWait(driver, 5).until(EC.alert_is_present())
        alert2 = driver.switch_to.alert
        message = alert2.text
        print(alert2.text)
        alert.accept()
        self.assertEqual(inputanCart.productAddWithLogin, message)
        WebDriverWait(driver, 10).until(EC.presence_of_element_located((cartPage.linkCartPage))).click()
        time.sleep(2)
        driver.find_element(*cartPage.linkDelete).click()
        time.sleep(2)
        driver.find_element(*cartPage.linkHome).click()
        WebDriverWait(driver, 10).until(EC.presence_of_element_located((cartPage.linkCartPage))).click()
        time.sleep(2)
        driver.find_element(*cartPage.linkDelete).click()
        time.sleep(2)

    def test_delete_more_than_one_with_login_without_add_product(self):
        driver = self.driver #buka web browser
        driver.get(self.url) # buka situs
        driver.maximize_window()
        login=driver.find_element(*cartPage.idLoginPage)
        WebDriverWait(driver,5).until(EC.element_to_be_clickable(login))
        login.click()
        username=driver.find_element(*cartPage.idUsername)
        WebDriverWait(driver,5).until(EC.visibility_of(username))
        username.send_keys(inputanCart.username)
        password=driver.find_element(*cartPage.idPassword)
        WebDriverWait(driver,5).until(EC.visibility_of(password))
        password.send_keys(inputanCart.password)
        driver.find_element(*cartPage.buttonLogin).click()
        WebDriverWait(driver, 10).until(EC.presence_of_element_located((cartPage.linkLogout)))#untuk bantuan,tidak ada fungsi click
        WebDriverWait(driver, 10).until(EC.presence_of_element_located((cartPage.linkCartPage))).click()
        time.sleep(2)
        driver.find_element(*cartPage.linkDelete).click()
        time.sleep(2)
        driver.find_element(*cartPage.linkHome).click()
        WebDriverWait(driver, 10).until(EC.presence_of_element_located((cartPage.linkCartPage))).click()
        time.sleep(2)
        driver.find_element(*cartPage.linkDelete).click()
        time.sleep(2)

    def test_delete_one_with_login_without_add_product(self):
        driver = self.driver #buka web browser
        driver.get(self.url) # buka situs
        driver.maximize_window()
        login=driver.find_element(*cartPage.idLoginPage)
        WebDriverWait(driver,5).until(EC.element_to_be_clickable(login))
        login.click()
        username=driver.find_element(*cartPage.idUsername)
        WebDriverWait(driver,5).until(EC.visibility_of(username))
        username.send_keys(inputanCart.username)
        password=driver.find_element(*cartPage.idPassword)
        WebDriverWait(driver,5).until(EC.visibility_of(password))
        password.send_keys(inputanCart.password)
        driver.find_element(*cartPage.buttonLogin).click()
        WebDriverWait(driver, 10).until(EC.presence_of_element_located((cartPage.linkLogout)))#untuk bantuan,tidak ada fungsi click
        WebDriverWait(driver, 10).until(EC.presence_of_element_located((cartPage.linkCartPage))).click()
        time.sleep(2)
        driver.find_element(*cartPage.linkDelete).click()
        time.sleep(2)

    def tearDown(self):
        self.driver.close()

if __name__ == "__main__":
    unittest.main()