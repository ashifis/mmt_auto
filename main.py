from Navigating import *
import time


click = 0
launch_mmt()

set_from()
set_to()
set_depart_date()

required_year = "2019"
required_month = "OCTOBER"

while required_year not in get_curr_vis_year():
    time.sleep(5)
    select_depart_date_next()

while required_month not in get_curr_vis_month():
    time.sleep(2)
    select_depart_date_next()


get_all_dates(required_month, required_year)