

import time

from Navigating import *

depart_required_year = "2019"
depart_required_month = "FEBRUARY"
depart_required_day = "21"

return_required_year = "2019"
return_required_month = "APRIL"
return_required_day = "22"

orig = "Delhi"
dest = "Bangalore"

launch_mmt()

set_from(orig)
set_to(dest)

click_depart_date()
while depart_required_year not in get_curr_vis_year():
    time.sleep(5)
    select_depart_date_next()
while depart_required_month not in get_curr_vis_month():
    time.sleep(2)
    select_depart_date_next()
get_depart_all_dates(depart_required_month, depart_required_year, depart_required_day)

click_return_date()
while return_required_year not in get_curr_vis_year():
    time.sleep(5)
    select_return_date_next()
while return_required_month not in get_curr_vis_month():
    time.sleep(5)
    select_return_date_next()
get_return_all_dates(return_required_month, return_required_year, return_required_day)

click_flight_search()
time.sleep(5)
retrieve_trip_details()


time.sleep(10)
