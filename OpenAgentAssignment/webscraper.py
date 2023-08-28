from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.common.by import By
import time
import random

# Random Delay
min_delay = 3
max_delay = 10

options = webdriver.ChromeOptions()
options.add_experimental_option("detach", True)
driver = webdriver.Chrome(options=options, service=Service(ChromeDriverManager().install()))

with open('extracted_data.txt', 'w') as f:
    f.write('***********Open Agent WebScraper for Prompthero!!********\n\n')
    f.write('***********The Extracted Details as per the given Assignment are*********\n\n')

def base():
    # Initilaizing the url
    url = 'https://prompthero.com/'
    driver.get(url)
    driver.implicitly_wait(10)
    driver.maximize_window()

    # Random Delay for the scraper to behave like human
    delay = random.uniform(min_delay, max_delay)
    time.sleep(delay)

    # Scrolled the page for the scraper to behave like human
    driver.execute_script("window.scrollBy(0, 100);")


def login():
    # Logging in Function
    login_button = driver.find_element(By.XPATH, "//div/a[@href = '/users/sign_in']")
    login_button.click()
    time.sleep(5)
    email_id = driver.find_element(By.ID, "user_email")
    email_id.send_keys("rvthym89@gmail.com")
    password = driver.find_element(By.ID, "user_password")
    password.send_keys("WebScraper")
    submit = driver.find_element(By.NAME, "commit")
    submit.click()
    print("The Title of the page is " + driver.title)
    delay = random.uniform(min_delay, max_delay)
    time.sleep(delay)


def search():
    # Searching the given prompt page
    # search_box = driver.find_element(By.NAME, "q")
    search_box = driver.find_element(By.XPATH, "//div[@class='input-group mb-3']/input[@name='q']")
    search_box.send_keys("darkness, scary, atmospheric")
    search_btn = driver.find_element(By.ID, "search-button")
    search_btn.click()

    # Scrolled the page for the scraper to behave like human
    driver.execute_script("window.scrollBy(0, 300);")
    time.sleep(5)   # wait
    model = driver.find_element(By.XPATH, "//label[text()='Openjourney']")
    model.click()
    time.sleep(2)   # wait
    driver.execute_script("window.scrollBy(0, 500);")
    time.sleep(5)   # wait
    driver.find_element(By.XPATH, '//div[@id="prompt-card-image-backdrop-4ae9caa7ad7"]').click()

    # Random Delay for the scraper to behave like human
    delay = random.uniform(min_delay, max_delay)
    time.sleep(delay)
    # Printing the Statements and Titles
    print(" **********The Extracted Details as per given Assignment********* ")


def extracturl():
    # Extracting URL  of the Navigated page
    current_url = driver.current_url
    print('The Current URL is: ' + current_url)
    with open('extracted_data.txt', 'a') as f:
        # Write data to the end of the file
        f.write(f'Current Link is: {current_url}\n\n')
    return current_url



def extractusername():
    # Extracting the Account Name
    name = driver.find_element(By.XPATH,
    "//div[@class='d-inline-flex align-items-center']/a[@href = 'https://prompthero.com/DameVee']")
    print('Account Name is: ' + name.text)
    with open('extracted_data.txt', 'a') as f:
        # Write data to the end of the file
        f.write(f'Username : {name.text}\n\n')

    return name.text



def extractpromptdescription():
    # Extracting the prompt Description
    prompt_description1 = driver.find_element(By.XPATH, '//b/a[1]')
    prompt_description2 = driver.find_element(By.XPATH, '//b/a[2]')
    prompt_description3 = driver.find_element(By.XPATH, '//b/a[3]')
    prompt_description = prompt_description1.text + prompt_description2.text + prompt_description3.text
    print('Prompt Description is:' + prompt_description)
    with open('extracted_data.txt', 'a') as f:
        # Write data to the end of the file
        f.write(f'Prompt Content: {prompt_description}\n\n')
    return prompt_description



def extractgenerationparameters():
    # Scrolled the Page for web element visibility
    driver.execute_script("window.scrollBy(0, 500);")

    # Extracting the Generation Parameters
    gen_parm1 = driver.find_element(By.XPATH, '//div[@class="metadata small"]/span[1]')
    gen_parm2 = driver.find_element(By.XPATH, '//div[@class="metadata small"]/span[2]')
    gen_parm3 = driver.find_element(By.XPATH, '//div[@class="metadata small"]/span[3]')
    gen_parm4 = driver.find_element(By.XPATH, '//div[@class="metadata small"]/span[4]')
    gen_parm5 = driver.find_element(By.XPATH, '//div[@class="metadata small"]/span[5]')
    gen_parm = gen_parm1.text + "  " + gen_parm2.text + "  " + gen_parm3.text + "  " + gen_parm4.text + "  " + gen_parm5.text
    print("The Generation Parameters are:" + gen_parm)
    with open('extracted_data.txt', 'a') as f:
        # Write data to the end of the file
        f.write(f'Generation Parameter: {gen_parm}\n\n')

    return gen_parm


def extractmodelused():

    # Random Delay for the scraper to behave like human
    delay = random.uniform(min_delay, max_delay)
    time.sleep(delay)
    # Extracting the Model Used
    model_used = driver.find_element(By.XPATH, "//a[@class='d-inline']/span")
    print('Model used is: ' + model_used.text)
    with open('extracted_data.txt', 'a') as f:
        # Write data to the end of the file
        f.write(f'Model Used: {model_used.text}\n\n')

    return model_used.text

"""
base()
login()
search()
url = extracturl()
username = extractusername()
prompt_content = extractpromptdescription()
generation_parameter = extractgenerationparameters()
model_used = extractmodelused()
"""
"""
def data_file():
    with open('extracteddata.txt', 'w') as f:
        f.write('***********Open Agent WebScraper for Prompthero!!********\n\n')
        f.write('***********The Extracted Details as per the given Assignment are*********\n\n')
        f.write(f'URL: {url}\n\n')
        f.write(f'Username: {username}\n\n')
        f.write(f'Prompt content: {prompt_content}\n\n')
        f.write(f'Generation parameter: {generation_parameter}\n\n')
        f.write(f'Model used: {model_used}\n\n')
"""
# data_file()
#driver.quit()