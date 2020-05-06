from selenium import webdriver
def location(list_of_locations):
    driver=webdriver.Firefox(executable_path="./geckodriver")
    for i in list_of_locations:
        driver.get("https://www.google.com/search?client=ubuntu&channel=fs&q="+i+" latitude+and+logitude&ie=utf-8&oe=utf-8")
        text=driver.find_element_by_class_name('Z0LcW').text
        print(text)
        driver.quit()