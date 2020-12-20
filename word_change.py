def word_change(pre_word):
    """
    :param pre_wordはシネマプランの名前
    :return: 日本語なので英文字数字に変換
    """
    if "シネマシティズン(60才以上)" == pre_word:
        return "sc60"
    elif "シネマシティズン" == pre_word:
        return "sc"
    elif "一般" == pre_word:
        return "gene"
    elif "シニア(70才以上)" == pre_word:
        return "sni70"
    elif "学生(大・専)" == pre_word:
        return "histudent"
    elif "中・高校生" == pre_word:
        return "midstudent"
    elif "幼児(3才以上)・小学生" == pre_word:
        return "lowstudent"
    elif "障がい者(学生以上)" == pre_word:
        return "hhstudent"
    elif "障がい者(高校以下)" == pre_word:
        return "hlstudent"
    elif "夫婦50割引" == pre_word:
        return "couple"
    else:
        try:
            raise ValueError("指定された分類ではありません！")
        except ValueError as e:
            print(e)


def reverse_word_change(pre_word):
    """
    :param pre_wordはシネマプランの変換後の名前
    :return: 英文字数字を日本語に変換
    """
    if "sc60" == pre_word:
        return "シネマシティズン(60才以上)"
    elif "sc" == pre_word:
        return "シネマシティズン"
    elif "gene" == pre_word:
        return "一般"
    elif "sni70" == pre_word:
        return "シニア(70才以上)"
    elif "histudent" == pre_word:
        return "学生(大・専)"
    elif "midstudent" == pre_word:
        return "中・高校生"
    elif "lowstudent" == pre_word:
        return "幼児(3才以上)・小学生"
    elif "hhstudent" == pre_word:
        return "障がい者(学生以上)"
    elif "hlstudent" == pre_word:
        return "障がい者(高校以下)"
    elif "couple" == pre_word:
        return "夫婦50割引"
    else:
        try:
            raise ValueError("指定された分類ではありません！")
        except ValueError as e:
            print(e)