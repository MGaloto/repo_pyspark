class DatePython():

    def generateMonthlyPathList(year: str, month: str, day: str):
        list_urls = []
        try:
            if len(str(year)) == 4 and len(str(month)) == 2 and len(str(day)) == 2:
                for i in range(1, int(day) + 1):
                    if len(str(i)) == 1:
                        day = '0'+ str(i)
                    else:
                        day = i
                    url = f"https://importantdata@location/{year}/{month}/{day}/"
                    list_urls.append(url)
                return list_urls
            else:
                raise ValueError(f"\nError: Verificar los datos ingresados.\n\nEl formato tiene que ser YYYY-MM-DD.\n\nYear: {year}  Month: {month} Day: {day}")
        except Exception as e:
            print(e)
        

    
    
    def generateLastDaysPaths(date: str, days: int):
        list_urls = []
        try:
            if len(date) == 8 and type(date) == str:
                date_total = date[:4]+date[4:6]+date[6:8]
                date = datetime.strptime(date_total, "%Y%m%d").date()
                date_list = [date - timedelta(days=x) for x in range(days)][::-1]
                for d in date_list:
                    if len(str(d.month)) == 1:
                        month = '0' + str(d.month)
                    else:
                        month = str(d.month)
                    if len(str(d.day)) == 1:
                        day = '0' + str(d.day)
                    else:
                        day = str(d.day)
                    year = str(d.year)
                    url = "https://importantdata@location/"+year+"/"+month+"/"+day+"/"
                    list_urls.append(url)
                return list_urls
            else:
               raise ValueError(f"\nError: Verificar los datos ingresados.\n\nEl formato tiene que ser YYYYMMDD.\n\nInputs: date: {date} and days: {days}") 
        except Exception as e:
            print(e)
    
    










