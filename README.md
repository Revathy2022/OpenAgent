# 1. Introduction
## 1.1. Web Scraper for PromptHero
This project contains a web scraper functionaly that navigates to prompthero.com and extracts data from the site. It also has the automated test suite that verifies the accuracy of the scrapper.  

# 2. Approach Followed:
There are multiptle ways to develop a webscraper. Here a simple pytest program is written using selenium web driver for web scraping. This project contains the webscraper and a test suite that verifies the extracted data. 

## 2.1. Web Scrapper Functionality
The web scraper performs the following actions:
- Navigates to prompthero.com.
- Clicks on a post.
- Once on the post’s page, the scraper extracts the following details:
	- Image links
	- Username
	- Prompt content
	- Generation parameters
	- Model Used

## 2.2. Test Suite:  

Following packages are imported Pyest,self,Selenium Web Diver, Service, ChromeDriverManager, By, time, random.
test_webscraper.py is a name of the python testsuite file here and it has following test functions 
def testlogin(): Performs Login function in the web page. 
def testsearch(): performs Search Operation to serach the required imge. 
def testextracturl(): Extracts url of the navigated page. 
def testextractusername(): Extracts the username.
deftestpromptdescription(): Extracts the prompt Description.
deftestgenerationparameters(): Extracts the generation parameters. 
def testmodelused():Extrcats the Model Used.

## 2.3. Testing with Pytest
This project includes a suite of tests written using the pytest framework to verify the accuracy and reliability of the web scraper. The tests check that the scraper is able to navigate to the site, click on a post, and extract the correct data.
To run the tests, use the *pytest* command.

# 3. How to run this project
## 3.1 Install Python and Libraries:
### 3.1.1. To get started with this project, you will need to have Python 3 installed on your computer. You will need an IDE to perform the testing process.Pycharm is a preferred one. You will also need to install the following libraries:

  	  ⦁  Selenium  
	  ⦁  pytest  
	  ⦁  pytest-html       
                                                                                                                                                  
### 3.1.2 How to Install:
You can install these libraries easily by running the following command:  

	⦁	pip install selenium  
	⦁	pip install -u pytest  
	⦁	pip install pytest-html  
 
	pip install pytest-html is used to genrate html report. Run the following command to generate the report in html.      
 		pytest --html=report.html --self-contained-html

## 3.2 Cloning the repository:
  ### 3.2.1 Run the following command to clone the repository
         git clone  https://github.com/Revathy/OpenAgent

## 3.3 Executing the project:
Naviagte to the directory where the repository is cloned and run the *pytest* command to execute the project.

# 4. Challenges faced & solution applied:
## 4.1. Challenge: No unique IDs
### 4.1.1 Challenges Description: 
For some web elements ID locator is available but its not unique and more than one web element with same ID is available.
### 4.1.2. Solution: 
As there is no unique ID's available and anyother preferred locators are available for many web elements I choose to write Xpath.

## 4.2. Challenge: Writing Xpath:
### 4.2.1. Challenges Description: 
Writing xpath was little challenging as the properties has no unique values and some tags text() function is not working in locating the web elements.
### 4.2.2 Solution: 
To write the xpath no unique values are available for the properties, so I traversed to the parent nodes and count on its siblings to write the unique xpath which was little time consuming.

## 4.3. Challenge: Page Scrolling:
### 4.3.1 Challenges Description: 
Page was scrolling to the top of the page when navigating to the new url or reloading after the search operation and which hinders the web element visibility.
### 4.3.2. Solution:
Implemented page scroll in between for the element to be visible on a page, which also helps the scraper to behave like human.

