from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.common.by import By
from os import path
from selenium import webdriver
from selenium.webdriver.support.ui import Select
import pickle
import datetime

from time import sleep

totPages = 40
Ac = "Accepted"
arr = [ "Pupil" ,"Specialist" ,"Expert" , "Candidate Master" , "International Master"]
if __name__ == "__main__":
    driver = webdriver.Chrome(executable_path="./chromedriver")
    try:
        userId = input("Enter the UserName : ")
        clrId = int(input("Enter the color Id : \n 1. Pupil \n 2. Specialist \n 3. Expert \n 4. Candidate Master \n 5. International Master \n "))
        color = arr[clrId-1]
        driver.get("https://codeforces.com/submissions/" + userId)
        WebDriverWait(driver, 10).until(
            EC.presence_of_element_located((By.CLASS_NAME, "status-frame-datatable"))
        )
        driver.find_element_by_id("showUnofficial").click()
        WebDriverWait(driver, 10).until(
            EC.presence_of_element_located((By.CLASS_NAME, "status-frame-datatable"))
        )
        cur = 52
        while(cur >= totPages):
            driver.get("https://codeforces.com/submissions/" + userId + "/page/" + str(cur))
            WebDriverWait(driver, 10).until(
            EC.presence_of_element_located((By.CLASS_NAME, "status-frame-datatable"))
            )
            table = driver.find_element_by_css_selector('table.status-frame-datatable')
            for row in table.find_elements_by_css_selector("tr"):
                isAc = False
                isCol = False
                linkP = ""
                itr = 0
                for cell in row.find_elements_by_tag_name("td"):
                    if itr == 5:
                        theAc = cell.find_element_by_tag_name("span")
                        if Ac == theAc.text:
                            isAc = True
                    if itr == 2:
                        hr = cell.find_element_by_tag_name("a")
                        if hr.get_attribute("title") == color + " " + userId:
                            isCol = True
                    if itr == 3:
                        ll = cell.find_element_by_tag_name("a")
                        linkP = ll.get_attribute("href")
                    itr = itr + 1
                if isAc and isCol:
                    print(linkP)
            cur = cur - 1
    finally:
        driver.quit()
