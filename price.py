from holiday import m_type
from my_time import hourless20
def movieplan(day,m_class):
    """
    :param dayは入場者が入室した日付時間
    :return: 利用者の映画館に行った時間帯による開催されているプラン
    """
    hour_less = hourless20(day)
    hb ,day_num = m_type(day)
    if hb is True and day_num == "01" and m_class != "エムアイカード" and m_class == "シネマシティズン":
        plan = "holiday_movie_day_schi"
    elif day_num == "01" and m_class!= "エムアイカード" and m_class!= "シネマシティズン":
        plan = "movie_day"
    elif hb is None and hour_less is True:
        plan = "weekday_less_20"
    elif hb is None and hour_less is None:
        plan = "weekday_more_20"
    elif hb is True and hour_less is True:
        plan = "holiday_less_20"
    elif hb is True and hour_less is None:
        plan = "holiday_more_20"
    else:
        try:
            raise ValueError("指定された分類ではありません！")
        except ValueError as e:
            print(e)

    return plan
