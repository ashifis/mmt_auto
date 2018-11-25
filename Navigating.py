from selenium import webdriver

driver = webdriver.Chrome("C:\Program Files\Git\OptusEvent1\Selenium\Drivers\chromedriver.exe")
driver.maximize_window()


def launch_mmt():
    driver.get("https://www.makemytrip.com/")
    search_text_query = driver.find_element_by_id("header_tab_flights")
    search_text_query.click()


def set_from(from_city_):
    Flight_from_search = driver.find_element_by_id("hp-widget__sfrom")
    Flight_from_search.clear()

    resultSet_from_City = driver.find_element_by_xpath("//*[@id=\"ui-id-1\"]")
    options_from_city = resultSet_from_City.find_elements_by_tag_name("li")
    print(str(len(options_from_city)) + " cities listed...")
    for from_city in options_from_city:
        # print(from_city.text)
        if from_city_ in from_city.text:
            from_city.click()


def set_to(to_city_):
    Flight_to_search = driver.find_element_by_id("hp-widget__sTo")
    Flight_to_search.clear()
    resultSet_to_City = driver.find_element_by_xpath("//*[@id=\"ui-id-2\"]")
    options_to_city = resultSet_to_City.find_elements_by_tag_name("li")
    print(str(len(options_to_city)) + " cities listed...")
    for to_city in options_to_city:
        # print(to_city.text)
        if to_city_ in to_city.text:
            to_city.click()


def click_depart_date():
    depart_date_elem = driver.find_element_by_id('hp-widget__depart')
    depart_date_elem.click()


def click_return_date():
    return_date_elem = driver.find_element_by_id('hp-widget__return')
    return_date_elem.click()


def get_curr_vis_month():
    depart_date_picker_month = ""
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
    depart_date_picker_year = ""
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
    if 1 == 2:
        print("hmmmm")
    else:
        '''
        click on > Button/Link
        '''
        date_picker_depart = ""
        date_picker_depart = driver.find_element_by_xpath("//div[@class='dateFilter hasDatepicker']")
        date_picker_depart.click()
        print("Desired year is not listed on the picker...\n Will click on Next...")
        # date_picker_next = driver.findElement(By.CLASS_NAME("ui-icon ui-icon-circle-triangle-e"))
        # date_picker_next = driver.find_element(By.CLASS_NAME(".ui-icon.ui-icon-circle-triangle-e"))
        search_form1 = ""
        search_form1 = driver.find_elements_by_xpath("//a[@class='ui-datepicker-next ui-corner-all']")
        # print(len(search_form1))
        for elem in search_form1:
            if elem.is_displayed():
                print("Element  visible, Clicked")
                elem.click()
                break
            else:
                # print("Element not visible")
                pass


def get_depart_all_dates(m, y, d):
    all_depart_dates = ""
    date_in_sec = 0
    month = m
    year = y
    day = d

    all_depart_dates = driver.find_element_by_xpath("//div[@class='ui-datepicker-group ui-datepicker-group-first']")
    if str(year) in all_depart_dates.text and str(month) in all_depart_dates.text:
        print(str(year) + " " + str(month) + " is first group")
        date_in_sec = 1
    else:
        all_depart_dates = ""
        all_depart_dates = driver.find_element_by_xpath("//div[@class='ui-datepicker-group ui-datepicker-group-last']")
        if str(year) in all_depart_dates.text and str(month) in all_depart_dates.text:
            print(str(year) + " " + str(month) + " is last group")
            date_in_sec = 2
    all_Dates = driver.find_elements_by_xpath("//a[@class='ui-state-default']")
    date_Count = 0
    # print(len(all_Dates))
    for d in all_Dates:
        if d.is_displayed():
            # print(d.text)
            if d.text == str(day):
                date_Count += 1
                if d.text == str(day) and date_in_sec == date_Count:
                    if d.is_displayed:
                        d.click()
                        print(str(day) + " Date Selected")
                        break
                elif d.text == str(day) and date_in_sec == date_Count:
                    if d.is_displayed:
                        d.click()
                        print(str(day) + " Date Selected")
                        break


def get_visible_month_year_on_date_picker():
    "ui-datepicker-month"
    "ui-datepicker-year"
    vis_year_date_picker = driver.find_elements_by_xpath("//span[@class='ui-datepicker-year']")
    print(len(vis_year_date_picker))
    vis_month_date_picker = driver.find_elements_by_xpath("//span[@class='ui-datepicker-month']")
    print(len(vis_month_date_picker))

    for year_, month_ in zip(vis_year_date_picker, vis_month_date_picker):
        if year_.is_displayed and year_.text == "2019" and month_.is_displayed and month_.text == "NOVEMBER":
            print("Combination Found")
            break
        else:
            select_depart_date_next()
            get_visible_month_year_on_date_picker()


def select_return_date_next():
    '''

    select the depart date

    :param target_month:
    :param target_year:
    :return:
    '''
    if 1 == 2:
        print("hmmmm")
    else:
        '''
        click on > Button/Link
        '''
        date_picker_depart = ""
        date_picker_depart = driver.find_element_by_xpath("//div[@class='dateFilterReturn hasDatepicker']")
        date_picker_depart.click()
        print("Desired year is not listed on the picker...\n Will click on Next...")
        # date_picker_next = driver.findElement(By.CLASS_NAME("ui-icon ui-icon-circle-triangle-e"))
        # date_picker_next = driver.find_element(By.CLASS_NAME(".ui-icon.ui-icon-circle-triangle-e"))
        search_form1 = ""
        search_form1 = driver.find_elements_by_xpath("//a[@class='ui-datepicker-next ui-corner-all']")
        # print(len(search_form1))
        for elem in search_form1:
            if elem.is_displayed():
                print("Element  visible, Clicked")
                elem.click()
                break
            else:
                # print("Element not visible")
                pass


def get_return_all_dates(m, y, d):
    all_return_dates = ""
    date_in_sec = 0
    month = m
    year = y
    day = d
    # all_depart_dates = driver.find_element_by_xpath("//div[@class='ui-datepicker-group ui-datepicker-group-first']")

    all_return_dates = driver.find_elements_by_xpath("//div[@class='ui-datepicker-group ui-datepicker-group-first']")
    # print(len(all_return_dates))
    for return_dates in all_return_dates:
        if return_dates.is_displayed:
            # print("yes")
            # print(len(return_dates.text))
            # print(return_dates.text)
            if (len(return_dates.text)) > 0:
                if str(year) in return_dates.text and str(month) in return_dates.text:
                    print(str(year) + " " + str(month) + " is first group")
                    date_in_sec = 1

    all_return_dates = driver.find_elements_by_xpath("//div[@class='ui-datepicker-group ui-datepicker-group-last']")
    # print(len(all_return_dates))
    for return_dates in all_return_dates:
        if return_dates.is_displayed:
            # print("yes")
            # print(len(return_dates.text))
            # print(return_dates.text)
            if (len(return_dates.text)) > 0:
                if str(year) in return_dates.text and str(month) in return_dates.text:
                    print(str(year) + " " + str(month) + " is last group")
                    date_in_sec = 2
    all_Dates = driver.find_elements_by_xpath("//a[@class='ui-state-default']")
    date_Count = 0
    # print(len(all_Dates))
    for d in all_Dates:
        if d.is_displayed():
            # print(d.text)
            if d.text == str(day):
                date_Count += 1
                if d.text == str(day) and date_in_sec == date_Count:
                    if d.is_displayed:
                        d.click()
                        print(str(day) + " Date Selected")
                        break
                elif d.text == str(day) and date_in_sec == date_Count:
                    if d.is_displayed:
                        d.click()
                        print(str(day) + " Date Selected")
                        break


def click_flight_search():
    driver.find_element_by_xpath("//*[@id='searchBtn']").click()


def retrieve_trip_details():
    trip_type = driver.find_element_by_xpath(
        "//span[@class='rund_trip_txt modify_captions make_blockElm append_bottom8 ng-binding']")
    print("Trip type: " + trip_type.text)
    from_to = driver.find_element_by_xpath("//p[@class='modify_city_name modify_txt ng-binding']")
    print(from_to.text)

    dep_arv = driver.find_elements_by_xpath("//p[@class='modify_captions']")
    print(len(dep_arv))
    for d_a in dep_arv:
        print(d_a.text)

    dep_arv_date = driver.find_elements_by_xpath("//span[@class='date ng-binding']")
    # print(len(dep_arv_date))
    # for d_a_date in dep_arv_date:
    #     print(d_a_date.text)
    #
    dep_arv_month_year = driver.find_elements_by_xpath("//span[@class='month_day ng-binding']")
    # print(len(dep_arv_month_year))
    # for d_a_month_year in dep_arv_month_year:
    #     print(d_a_month_year.text)
    print("DEP/ARR")
    for j in range(0, 2):
        print(str(dep_arv_date[j].text), end=" ")
    for i in range(0, int(len(dep_arv_month_year)), 2):
        print(str(dep_arv_month_year[i].text) + "  " + str(dep_arv_month_year[i + 1].text))
