from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from openpyxl import Workbook

import pandas as pd
  

manateeDirectory = "https://www.manateeschools.net/schooldirectory"



# Webdriver Information
options = webdriver.ChromeOptions()
driver = webdriver.Chrome(options=options)

# Variable Initializing

schoolKeywords = ['Elementary', 'High', 'Middle', 'Academy', 'College', 'School']
phoneNumberKeywords = ['Phone']
schoolNameList = []
SchoolColumns = ['School Name']
data = pd.DataFrame()



# Start
driver.get(manateeDirectory)

def getPhoneNumber(filteredList):
    try:
        target = WebDriverWait(driver, 3).until(
            EC.presence_of_element_located((By.CLASS_NAME, "flex-container"))
            )
    
    except:
        print("Locator for School Information was not found. Try making sure the spelling is correct.")
        driver.quit()
    
    finally:

    # Find and return the matching words
        matching_keywords = []
        for word in filteredList:
            if word in keywords:
                matching_keywords.append(word)


def getNextSchool():
    
    try:
        target = WebDriverWait(driver, 3).until(
            EC.presence_of_element_located((By.CLASS_NAME, "flex-container"))
            )
        
    except:
        print("Locator for School Information was not found. Try making sure the spelling is correct.")
        driver.quit()
    finally:
        
        # Simple Counter
        counter = 0
        
        # Sorting through all instances of flex-container
        schoolsFound = driver.find_elements(By.CLASS_NAME, "flex-container")

        for list in schoolsFound :
            
            # update
            counter += 1
            
            # Formatting into list
            formattedList = list.text.split()
            
            # Removes special characters and numbers
            filterNumbers = [x for x in formattedList if x.isalpha()]
            
            
            # Find and return the matching words
            matching_keywords = []
            for word in filterNumbers:
                if word in schoolKeywords:
                    matching_keywords.append(word)
            
            
            # If keyword found, grab its POSITION
            if len(matching_keywords) == 1:
                result = matching_keywords[0]
            
            #  No keyword is found, manually set to None
            elif len(matching_keywords) == 0:
                result = None
            
                

            # Everything to the left of the found keywords will be pulled and displayed, if found
            if result == None:
                elements_to_left = "No keyword found"
            else:
                keywordPosition = filterNumbers.index(result)
                elements_to_left = filterNumbers[:keywordPosition + 1] # Plus 1 to add keyword that was found
            
            
            # Create a new list of joined final school names
            finalSchoolName = ' '.join(elements_to_left)
            schoolNameList.append(finalSchoolName)
            
            # Debug Log (Prints left in for demo purposes)
            print("---------------- DEBUG LOG -----------------------------")
            print("\n") # Empty Space
            print("List #" + str(counter))
            print("\n")
            # print(keywordPosition)
            print(formattedList)
            # print(filterNumbers)
            # print(elements_to_left) 
            # print(finalSchoolName)
            # print(sheet.cell(row=1, column=1).value)
            # print(sheet)
            print("\n") 
            print("---------------- END -----------------------------------")
            print("\n") 

getNextSchool()

# Now that data is collected, it will be added to DataFrame and exported to CSV

data = pd.DataFrame(schoolNameList, columns=['School Name'])
# print(data)
print("\n")
print("\n")
data.info()
# data.to_csv('test.csv')

driver.quit()



