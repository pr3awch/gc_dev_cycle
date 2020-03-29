import datetime
import re
class date_udf :
    def __init__(self) :
        self.ld_start_dt = datetime.date.today()
    def date_add (self,*args) :
        if len(args) == 1 and isinstance(args[0],int) :
            return self.ld_start_dt + datetime.timedelta(days=args[0])
        elif len(args) == 2 and isinstance(args[0],str)  and re.search(r"^\d{4}-\d{2}-\d{2}$",args[0]):
            la_split_start_dt = args[0].split('-')
            ld_add_dt = datetime.date(int(la_split_start_dt[0]),int(la_split_start_dt[1]),int(la_split_start_dt[2]))
            ld_add_dt += datetime.timedelta(days=args[1])
        else :
            return None
        return ld_add_dt
    def next_day (self,ps_start_dt,ps_interval_dt) :
        la_split_start_dt = ps_start_dt.split('-')
        ld_start_dt= datetime.date(int(la_split_start_dt[0]),int(la_split_start_dt[1]),int(la_split_start_dt[2]))
        return ld_start_dt
if __name__ == "__main__":
    c_date = date_udf()
    c_date.next_day("2020-01-01","")
    print (c_date.date_add(3))
    print (c_date.date_add("2020-01-01",3))
    print (c_date.date_add("20200101",3))