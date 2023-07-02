from selenium.webdriver.common.by import By

class cartPage():
    idLoginPage = (By.ID,"login2")
    idUsername = (By.ID,"loginusername")
    idPassword = (By.ID,"loginpassword")
    buttonLogin = ("xpath", "//button[contains(text(),'Log in')]")
    linkCartPage = (By.LINK_TEXT, "Cart")
    linkSamsung = (By.LINK_TEXT, "Samsung galaxy s6")
    linkAddToCart = (By.LINK_TEXT, "Add to cart")
    linkHome = (By.XPATH, "//a[contains(text(),'Home')]")
    linkNokia = (By.LINK_TEXT,"Nokia lumia 1520")
    linkDelete = (By.LINK_TEXT,"Delete")
    linkLogout = (By.LINK_TEXT, "Log out")
    linkNexus = (By.LINK_TEXT,"Nexus 6")


