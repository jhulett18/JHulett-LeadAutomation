from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

manateeDirectory = "https://www.manateeschools.net/schooldirectory"


options = webdriver.ChromeOptions()
driver = webdriver.Chrome(options=options)

keywords = ['Elementary', 'High', 'Middle', 'Academy', 'College', 'School']
schoolNameList = []
AddressList = []
PhoneList = []



driver.get(manateeDirectory)



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
        
        # Printing the length of the list     
        # listLength = len(schoolsFound)
        # print("Length: " + str(listLength))

        for element in schoolsFound :
            
            # Formatting the Elements received and putting them in lists
            formattedList = element.text.split()
            counter += 1
            
            # Removes special characters and numbers
            filterNumbers = [x for x in formattedList if x.isalpha()]
            
            
            # Find and return the matching words
            matching_keywords = []
            for word in filterNumbers:
                if word in keywords:
                    matching_keywords.append(word)
            
            
            # Test Case to see if one or multiple keywords were found & then transforms it into a string value to be used as input
            
            # If keyword found, grab its POSITION
            if len(matching_keywords) == 1:
                result = matching_keywords[0]
            
            # Used if no keyword is found, manually set to None
            elif len(matching_keywords) == 0:
                result = None
            
                

            # Everything to the left of the found keywords will be pulled and displayed
            
            if result == None:
                elements_to_left = "No keyword was found for this school list"

            else:
                keywordPosition = filterNumbers.index(result)
                elements_to_left = filterNumbers[:keywordPosition + 1] # Plus 1 to add keyword that was found
            
            
            # Present Final Title
            finalSchoolName = ' '.join(elements_to_left)

            # Debug Log (Prints left in for demo purposes)
            print("---------------- DEBUG LOG -----------------------------")
            print(" ") # Empty Space
            print("List #" + str(counter))
            print(" ")
            # print(keywordPosition)
            # print(formattedList)
            # print(filterNumbers)
            # print(elements_to_left) 
            print(finalSchoolName)
            print(" ") 
            print("---------------- END -----------------------------------")
            print(" ") 
            print(" ") 

            schoolNameList.append(finalSchoolName)
getNextSchool()

print(schoolNameList)

driver.quit()

