import datetime
import re
ld_curr_dt = datetime.date(2020,4,1)
ld_end_dt = datetime.date(2020,4,1)
#var_date = var_date + 1
while  ld_curr_dt <= ld_end_dt :
    print (ld_curr_dt.isocalendar())
    ld_curr_dow=ld_curr_dt.isocalendar()[2]
    if ld_curr_dow in (1,3) :
        print (ld_curr_dow)
        print (ld_curr_dt)
    ld_curr_dt = ld_curr_dt + datetime.timedelta(days=1)

exec("print (10)")
ls_str_dt="2020-01-01"
la_str_dt=ls_str_dt.split("-")
print (la_str_dt[0])
print (datetime.date.today())
if type(ls_str_dt) == str :
    print ("true")
if re.search(r"^\d{4}-\d{2}-\d{2}$","202001-01") :
    print (1)