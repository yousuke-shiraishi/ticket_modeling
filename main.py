import csv
from price import movieplan
from my_time import hourless20
from word_change import word_change,reverse_word_change
from holiday import m_type

planandprice = {"weekday_less_20":{"シネマシティズン(60才以上)":1000, "シネマシティズン":1000, "一般":1800, "シニア(70才以上)":1100, "学生(大・専)":1500, "中・高校生":1000, "幼児(3才以上)・小学生":1000, "障がい者(学生以上)":1000, "障がい者(高校以下)":900, "夫婦50割引":2200  },
                "weekday_more_20":{"シネマシティズン(60才以上)":1000, "シネマシティズン":1000, "一般":1300, "シニア(70才以上)":1100, "学生(大・専)":1300, "中・高校生":1000, "幼児(3才以上)・小学生":1000, "障がい者(学生以上)":1000, "障がい者(高校以下)":900, "夫婦50割引":2200  },
                "holiday_less_20":{"シネマシティズン(60才以上)":1000, "シネマシティズン":1300, "一般":1800, "シニア(70才以上)":1100, "学生(大・専)":1500, "中・高校生":1000, "幼児(3才以上)・小学生":1000, "障がい者(学生以上)":1000, "障がい者(高校以下)":900, "夫婦50割引":2200  },
                "holiday_more_20":{"シネマシティズン(60才以上)":1000, "シネマシティズン":1000, "一般":1300, "シニア(70才以上)":1100, "学生(大・専)":1300, "中・高校生":1000, "幼児(3才以上)・小学生":1000, "障がい者(学生以上)":1000, "障がい者(高校以下)":900, "夫婦50割引":2200  },
                      "movie_day":{"シネマシティズン(60才以上)":1000, "シネマシティズン":1100, "一般":1100, "シニア(70才以上)":1100, "学生(大・専)":1100, "中・高校生":1000, "幼児(3才以上)・小学生":1000, "障がい者(学生以上)":1000, "障がい者(高校以下)":900, "夫婦50割引":9999  },
         "holiday_movie_day_schi":{"シネマシティズン(60才以上)":1000, "シネマシティズン":1100, "一般":1100, "シニア(70才以上)":1100, "学生(大・専)":1100, "中・高校生":1000, "幼児(3才以上)・小学生":1000, "障がい者(学生以上)":1000, "障がい者(高校以下)":900, "夫婦50割引":9999  }}



def main():
    with open("plan.csv", mode="r", encoding="utf-8") as rf:
        reader = csv.reader(rf)
        result =[]
        result_pair ={}
        prices = 0
        for row in reader:
            row[2]=row[2].replace('（', '(')
            row[2]=row[2].replace('）', ')')
            price = int(planandprice[movieplan(row[0],row[2])][row[2]])
            prices += price

    print("▼サマリー")
    print("")
    print("")
    print("{:,}".format(prices) + "円")
    print("")
    print("")
    print("")

    with open("plan.csv", mode="r", encoding="utf-8") as rf:
        reader = csv.reader(rf)
        result =[]
        result_pair ={}
        for row in reader:
            row[2]=row[2].replace('（', '(')
            row[2]=row[2].replace('）', ')')
            row[1]=row[1].replace('・','')
            price = int(planandprice[movieplan(row[0],row[2])][row[2]])
            if row[1] not in result:
                result.append(row[1])
                exec('{} = {}'.format(row[1], 0))
            exec('{} += {}'.format(row[1], price))
            exec('result_pair[row[1]] = {}'.format(row[1]))

    print("▼作品別売上")
    print("")
    print("")
    score_sorted = sorted(result_pair.items(), key=lambda x:x[1], reverse=True)
    for key,val in score_sorted:
        print(key + ":" + "{:,}".format(val) + "円")
    print("")
    print("")
    print("")
    with open("plan.csv", mode="r", encoding="utf-8") as rf:
        reader = csv.reader(rf)
        result =[]
        result_pair ={}
        for row in reader:
            row[2]=row[2].replace('（', '(')
            row[2]=row[2].replace('）', ')')
            price = int(planandprice[movieplan(row[0],row[2])][row[2]])
            mo_type = word_change(row[2])
            if mo_type not in result:
                result.append(mo_type)
                exec('{} = {}'.format(mo_type, 0))
            exec('{} += {}'.format(mo_type, price))
            exec('result_pair[mo_type] = {}'.format(mo_type))

    print("▼料金タイプ別売上")
    print("")
    print("")
    score_sorted = sorted(result_pair.items(), key=lambda x:x[1], reverse=True)
    for key,val in score_sorted:
        print(reverse_word_change(key)+ ":" + "{:,}".format(val) + "円")

main()