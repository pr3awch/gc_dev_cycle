import datetime

var_date = datetime.date(2020,1,1)
#var_date = var_date + 1
while  var_date <= datetime.date(2020,1,31) :
    var_date = var_date + datetime.timedelta(days=1)
    print (var_date)