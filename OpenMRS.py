##
# Description : End to End OpenMRS
# Author :  Sunil Savale
# Date : 05-04-2024
#
import time
from selenium import webdriver
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.common.by import By
from selenium.webdriver import ActionChains
from selenium.webdriver.support import expected_conditions as ec
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support.ui import Select

# Launch the Browser
driver = webdriver.Chrome(executable_path=ChromeDriverManager().install())
driver.maximize_window()
driver.get("https://demo.openmrs.org/openmrs/login.htm")
wait = WebDriverWait(driver, 10)
action = ActionChains(driver)


# Login into OpenMRS
ele = driver.find_element(By.ID, "username")
print(ele.is_displayed())  # RETURN true/false based on element status
print(ele.is_enabled())  # Return true if element is enabled
print(ele.is_selected()) # Return true if element is checkbox/radiobutton selected
ele.send_keys("admin")
passfield = driver.find_element_by_id("password")
passfield.send_keys("Admin123")

# Click on Pharmacy
driver.find_element(By.ID, 'Pharmacy').click()


# Click on Login Button
parent_window = driver.current_window_handle
driver.find_element(By.XPATH, ".//input[@id = 'loginButton']").click()

# Register a Patient
patient_reg = driver.find_element(By.XPATH, "//a[contains(@id,'-registerPatient')]")
patient_reg.click()

# We have to switch the window
child_window = driver.window_handles
for window in child_window:
    if window != parent_window:
        driver.switch_to.window(window)

# What's Patient Name
given_name = wait.until(ec.presence_of_element_located((By.XPATH, "//input[starts-with(@id, 'fr')][1]")))
given_name.send_keys("Amol")
middle_name = wait.until(ec.presence_of_element_located((By.NAME, "middleName")))
middle_name.send_keys("Suresh")
family_name = wait.until(ec.presence_of_element_located((By.NAME, "familyName")))
family_name.send_keys("Patil")

# Click on gender
gender = wait.until(ec.presence_of_element_located((By.XPATH, "//span[.='Gender']")))
gender.click()

# Click the element by the select class
select_ele = driver.find_element(By.ID, "gender-field")
select = Select(select_ele)
select.select_by_visible_text("Male")

# Select the birth date of the patient
birth_date = wait.until(ec.presence_of_element_located((By.ID, 'birthdateLabel')))
birth_date.click()
"""Day"""
birthDay = wait.until(ec.presence_of_element_located((By.ID, "birthdateDay-field")))
birthDay.send_keys("01")
"""Month"""
monthBirth = wait.until(ec.presence_of_element_located((By.ID, 'birthdateMonth-field')))
MonthSelection = Select(monthBirth)
MonthSelection.select_by_visible_text("April")
"""Year"""
YearBirth = wait.until(ec.presence_of_element_located((By.ID, 'birthdateYear-field')))
YearBirth.send_keys("1993")

"""Address of the patient"""
address = driver.find_element(By.XPATH, "//span[.='Address']")
address.click()
address_1 = driver.find_element(By.ID, 'address1')
address_1.send_keys("At Ubharandi")
address_2 = driver.find_element(By.ID, 'address2')
address_2.send_keys("Post Vihirgaon")
city = driver.find_element(By.ID, "cityVillage")
city.send_keys("Dhule")
state_ele = driver.find_element(By.ID, 'stateProvince')
state_ele.send_keys("Maharashtra")
country = driver.find_element(By.ID, 'country')
country.send_keys("India")
postalcode = driver.find_element(By.ID, 'postalCode')
postalcode.send_keys("424303")

"""Phone Number"""
phoneNumber = driver.find_element(By.XPATH, "//span[.='Phone Number']")
phoneNumber.click()
number_ele = driver.find_element(By.NAME, 'phoneNumber')
number_ele.send_keys("9191919732")

"""Patient Relatives"""
relatives = driver.find_element(By.XPATH, "//span[.='Relatives']")
relatives.click()
relationType = driver.find_element(By.ID, 'relationship_type')
selectRelative = Select(relationType)
selectRelative.select_by_value("8d91a3dc-c2cc-11de-8d13-0010c6dffd0f-A")
personName = driver.find_element(By.XPATH, "//input[@placeholder='Person Name']")
personName.send_keys("Patil")

"""Confirm Page """
confirm_page = driver.find_element(By.XPATH, "//span[.='Confirm']")
confirm_page.click()
data = wait.until(ec.presence_of_all_elements_located((By.XPATH, "//div[@id='dataCanvas']//p")))
for patient_data in data:
    print(patient_data.text)

time.sleep(4)
confirm_button = driver.find_element(By.ID, "submit")
confirm_button.click()
print(driver.title)
driver.close()