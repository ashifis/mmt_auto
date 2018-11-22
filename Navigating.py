from selenium import webdriver
from selenium.webdriver.common.by import By
import calendar
from selenium.webdriver.common.keys import  Keys
from selenium.webdriver.common.action_chains import ActionChains

import time

driver = webdriver.Chrome("C:\Program Files\Git\OptusEvent1\Selenium\Drivers\chromedriver.exe")
driver.maximize_window()


def launch_mmt():
    driver.get("https://www.makemytrip.com/")
    search_text_query = driver.find_element_by_id("header_tab_flights")


def set_from():
    Flight_from_search = driver.find_element_by_id("hp-widget__sfrom")
    Flight_from_search.clear()

    resultSet_from_City = driver.find_element_by_xpath("//*[@id=\"ui-id-1\"]")

    options_from_city = resultSet_from_City.find_elements_by_tag_name("li")

    print(len(options_from_city))
    for from_city in options_from_city:
        # print(from_city.text)
        if "Pune" in from_city.text:
            from_city.click()


def set_to():
    Flight_to_search = driver.find_element_by_id("hp-widget__sTo")
    Flight_to_search.clear()

    resultSet_to_City = driver.find_element_by_xpath("//*[@id=\"ui-id-2\"]")
    options_to_city = resultSet_to_City.find_elements_by_tag_name("li")

    print(len(options_to_city))
    for to_city in options_to_city:
        # print(to_city.text)
        if "Kolkata" in to_city.text:
            to_city.click()


def set_depart_date():
    depart_date_elem = driver.find_element_by_id('hp-widget__depart')
    depart_date_elem.click()


def get_curr_vis_month():
    depart_date_picker_month=""
    depart_date_picker_month = driver.find_elements_by_class_name("ui-datepicker-month")
    # print(list(set([a.text for a in depart_date_picker_month])))
    visible_months = []
    for vis_month in list(set(depart_date_picker_month)):
        if len(vis_month.text) > 0:
            if vis_month.text not in visible_months:
                visible_months.append(vis_month.text)
                # print(vis_month.text)
    print("Visible Depart Month/s ", end="")
    print([month_ for month_ in visible_months])
    return visible_months


def get_curr_vis_year():
    depart_date_picker_year=""
    depart_date_picker_year = driver.find_elements_by_class_name("ui-datepicker-year")
    # print(list(set([a.text for a in depart_date_picker_year])))
    visible_years = []
    for vis_year in list(set(depart_date_picker_year)):
        if len(vis_year.text) > 0:
            if vis_year.text not in visible_years:
                visible_years.append(vis_year.text)
                # print(vis_year.text)
    visible_years = sorted(visible_years)
    print("Visible Depart year/s ", end="")
    print([year_ for year_ in visible_years])
    return visible_years


def select_depart_date_next():
    '''

    select the depart date

    :param target_month:
    :param target_year:
    :return:
    '''
    target_month = "JANUARY"
    target_year = "2019"
    if str(target_year) in ["201855", ""]:
        print("hmmmm")
    else:
        '''
        click on prev
        '''

        date_picker_depart = driver.find_element_by_xpath("//div[@class='dateFilter hasDatepicker']")
        date_picker_depart.click()
        print("Desired year is not listed on the picker...\n Will click on Next...")
        #date_picker_next = driver.findElement(By.CLASS_NAME("ui-icon ui-icon-circle-triangle-e"))
        #date_picker_next = driver.find_element(By.CLASS_NAME(".ui-icon.ui-icon-circle-triangle-e"))
        search_form1 = ""
        search_form1 = driver.find_elements_by_xpath("//a[@class='ui-datepicker-next ui-corner-all']")
        # print(len(search_form1))
        for elem in search_form1:
            if elem.is_displayed():
                print("Element  visible, Clicked")
                elem.click()
                break
            else:
                #print("Element not visible")
                pass

#return_date_elem = driver.find_element_by_class_name('hp-widget__return')
#print(return_date_elem)


def get_all_dates(month, year):
    all_depart_dates = ""
    all_depart_dates = driver.find_element_by_xpath("//div[@class='ui-datepicker-group ui-datepicker-group-first']")
    if str(year) in all_depart_dates.text and str(month) in all_depart_dates.text:
        print(str(year) + " " + str(month)+" is first group")
    else:
        all_depart_dates = ""
        all_depart_dates = driver.find_element_by_xpath("//div[@class='ui-datepicker-group ui-datepicker-group-last']")
        if str(year) in all_depart_dates.text and str(month) in all_depart_dates.text:
            print(str(year) + " " + str(month) + " is last group")
    my_cal = {
        "JANUARY": 1,
        "FEBRUARY": 2,
        "MARCH": 3,
        "APRIL": 4,
        "MAY": 5,
        "JUNE": 6,
        "JULY": 7,
        "AUGUST": 8,
        "SEPTEMBER": 9,
        "OCTOBER": 10,
        "NOVEMBER": 11,
        "DECEMBER": 12
         }
    print(my_cal[month])
    "ui-state-default"
    all_Dates = driver.find_elements_by_xpath("//a[@class='ui-state-default']")
    print(len(all_Dates))
    for d in all_Dates:
        if d.is_displayed():
            #print(d.text)
            if d.text == "29":
                #"ui-state-default"
                to_be_selected_date = driver.find_elements_by_xpath("//a[@class='ui-state-default']")
                print(len(to_be_selected_date))
                for date_ in to_be_selected_date:
                    if date_.is_displayed:
                        if date_.text == "29":
                            time.sleep(5)
                            date_.click()
                            break


