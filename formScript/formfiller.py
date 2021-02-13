from selenium import webdriver

web = webdriver.Chrome()
web.get('https://patientconnect.bu.edu/CheckIn/Survey/Intro/21')



def site_login():
    web.find_element_by_id("j_username").send_keys("malbaker@bu.edu")
    web.find_element_by_id("j_password").send_keys("DSavage2700")
    web.find_element_by_css_selector("button.input-submit").click()

def do_survey():
    web.get('https://patientconnect.bu.edu/Mvc/Patients/QuarantineSurvey')
    web.get('https://patientconnect.bu.edu/CheckIn/Survey/ShowAll/21')
    web.find_elements_by_class_name("answer.button.p-3").click()

    
    

site_login()
do_survey()