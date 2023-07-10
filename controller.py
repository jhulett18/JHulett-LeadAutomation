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
phoneNumberList = []
schoolNameList = []
addressList = []
data = pd.DataFrame()
readableList=[]

# Keywords Found
phoneNumberKeywords = ['Phone:','Phone']
schoolKeywords = ['Elementary', 'High', 'Middle', 'Academy', 'College', 'School']



# Start
driver.get(manateeDirectory)

def getTargetElement():
    try:
        target = WebDriverWait(driver, 3).until(
            EC.presence_of_element_located((By.CLASS_NAME, "flex-container"))
        )
        
    except:
        print("Locator for School Information was not found. Try making sure the spelling is correct.")
        driver.quit()
    finally:
        
        # update 
        count = 0
        
        # Unreadable code will be stored here, simply just finds css selector
        elementList = driver.find_elements(By.CLASS_NAME, "flex-container")
        
        # For every element in the target list append it to readableList
        for elements in elementList:
            count += 1    
            
            # Formatting into something we can read
            readableList.append(elements.text.split())

            
            # print("---------------- DEBUG LOG -----------------------------")
            # print("List #" + str(count))
            # print("\n")
            # print(readableList)
            # print(elements.text.split())
            # print("---------------- END -----------------------------------")
            # print("\n") 
        return readableList

def getPhoneNumber(List):
    
    # intialize
    counter = 0
    
    for unfilteredElement in List:
        
        # update
        counter += 1

        # Find and return the matching words
        matching_keywords = []
        for word in unfilteredElement:
            if word in phoneNumberKeywords:
                matching_keywords.append(word)
        
        # If keyword found, grab its POSITION
        if len(matching_keywords) == 1:
            result = matching_keywords[0]
        
        # No keyword is found, manually set to None
        elif len(matching_keywords) == 0:
            result = None

        # Everything to the right of the found keywords will be pulled and displayed, if found
        if result == None:
            elements_to_right = "No keyword found"
        else:
            keywordPosition = unfilteredElement.index(result)
            elements_to_right = unfilteredElement[keywordPosition:keywordPosition+3] 
        
        # Cleanup Phone Number List
            cleanPhoneNumberList = ' '.join(elements_to_right)
            phoneNumberList.append(cleanPhoneNumberList)

        
        # print("---------------- DEBUG LOG -----------------------------")
        # print("List #" + str(counter))
        # print("\n")
        # print(result)
        # print(unfilteredElement)
        # print(elements_to_right)
        # print("---------------- END -----------------------------------")
        # print("\n") 
        
    return phoneNumberList

def getNextSchool(List):
        
        # Initialize 
        counter = 0
        
        for unfilteredElements in List:
            
            # update
            counter += 1
            
            # Removes special characters and numbers
            filterNumbers = [x for x in unfilteredElements if x.isalpha()]
            
            
            # Find and return the matching words
            matching_keywords = []
            for word in filterNumbers:
                if word in schoolKeywords:
                    matching_keywords.append(word)
            
            
            # If keyword found, grab its POSITION
            if len(matching_keywords) == 1:
                result = matching_keywords[0]

            # No keyword is found, manually set to None
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
            # print("---------------- DEBUG LOG -----------------------------")
            # print("\n") # Empty Space
            # print("List #" + str(counter))
            # print("\n")
            # print(keywordPosition)
            # print(unfilteredList)
            # print(finalSchoolName)
            # print("\n") 
            # print("---------------- END -----------------------------------")
            # print("\n") 

        return schoolNameList

def getAddress(List):
    
    # intialize
    counter = 0

    for unfilteredElement in List:

        # update 
        counter += 1
    # Need to Find School keyword, this is out starting position
        school_matching_keywords = []
        for word in unfilteredElement:
            if word in schoolKeywords:
                school_matching_keywords.append(word)
    
        # If keyword found, grab its POSITION
        if len(school_matching_keywords) == 1:
            school_keyword_result = school_matching_keywords[0]
    
        # No keyword is found, manually set to None
        elif len(school_matching_keywords) == 0:
            school_keyword_result = None
    
    # Now we find Phone Number Keywords keyword Position
        phone_matching_keywords = []
        for word in unfilteredElement:
            if word in phoneNumberKeywords:
                phone_matching_keywords.append(word)
    
        # If keyword found, grab its POSITION
        if len(phone_matching_keywords) == 1:
            phone_keyword_result = phone_matching_keywords[0]

        # No keyword is found, manually set to None
        elif len(phone_matching_keywords) == 0:
            phone_keyword_result = None


    # Now we want to start at school name keyword and end with phone number position
        if phone_keyword_result  == None:
            elements_found = "No keyword found"
        elif school_keyword_result == None:
            elements_found = "No keyword found"
        else:
            schoolkeywordPosition = unfilteredElement.index(school_keyword_result)
            phonekeywordPosition = unfilteredElement.index(phone_keyword_result)
            elements_found = unfilteredElement[schoolkeywordPosition+1:phonekeywordPosition]


            # Cleanup Address List
            cleanAddressList = ' '.join(elements_found)
            addressList.append(cleanAddressList)
        
        
        # print("---------------- DEBUG LOG -----------------------------")
        # print("List #" + str(counter))
        # print("\n")
        # print(unfilteredElement)
        # print(elements_found)
        # print(schoolkeywordPosition)
        # print(phonekeywordPosition)
        # ("---------------- END -----------------------------------")
        # print("\n") 
    return addressList


list = getTargetElement()
numbers = getPhoneNumber(list)
names = getNextSchool(list)
address = getAddress(list)

# print(list)
print("\n")
print("Phone Numbers Found:")
print("\n")
print(numbers)
print("\n")
print("School Names Found:")
print(names)
print("\n")
print("School Address Found:")
print(address)

# Now that data is collected, it will be added to DataFrame and exported to CSV

# data = pd.DataFrame(schoolNameList, columns=['School Name'])
# print(data)
# print("\n")
# print("\n")
# data.info()
# data.to_csv('test.csv')

driver.quit()



