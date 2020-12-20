def hourless20(day):
    """
    :param dayは入場者が入室した日付時間
    :return: 20時までに入室したかどうかのbool値
    """
    hour = day.split("T")[1].split(":")[0]

    if int(hour) < 20:
        hour_less_20 = True
    else:
        hour_less_20 = None

    return hour_less_20
