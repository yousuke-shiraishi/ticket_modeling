import calendar
import datetime as dt
def m_type(day):
    """
    :param dayは入場者が入室した日付時間
    :return: 休日かどうかのbool値とmovie dayかどうかを判定するためにString型の日付を返す
    """
    year,month,day = day.split("T")[0].split("-")
    date = dt.date(int(year),int(month),int(day))
    day_index = date.weekday()
    weekday = calendar.day_name[day_index]
    if weekday == "Sunday" or weekday == "Saturday":
        holiday_bool = True
    else:
        holiday_bool = None

    return holiday_bool,day

