# Retrive the room prices of interested hotels from website

import requests
import time
import datetime
import json
import csv
import numpy as np

def get_hotel_price(hotelID, cityID):
    addr = "https://hotels.ctrip.com/Domestic/tool/AjaxHote1RoomListForDetai1.aspx?psid=&MasterHotelID="+hotelID+"&hotel="+hotelID+"&EDM=F&roomId=&IncludeRoom=&city="+cityID+"&showspothotel=T&supplier=&IsDecoupleSpotHotelAndGroup=F&contrast=0&brand=0&cityId="+cityID+"&brand0&group0&startDate=2020-11-12&depDate=2020-11-13&IsFlash=F&RequestTravelMoney=F&hsids=&IsJustConfirm=&contyped=0&priceInfo=-1&equip=&filter=&filterJson={}&productcode=&couponList=&abForHuaZhu=&defaultLoad=F&esfiltertag=&estagid=&Currency=RMB&Exchange=1&minRoomId=921980585&maskDiscount=0&th=85&RoomGuestCount=1,1,0&RoomGuestCount=1,1,0&page_id_forlog=102003&suitcroud=&eleven=93a2~ADw9b1%C2%ACIKFRa544JB%3FJ9756f%3BBEf122df690994131f53dea011376a3555&twelve=hfmjQ9xs3e1De9nRAYGcYaSE9YkmiLHWSZWBYBTE50rXdKLow0YLnE3AKcovXFj3YchjOBj0ZK7DY0YXpIBPe9bxmsj7UePneBgyGHjcby0YaPv1nEkPyLPj6dizGeMqYzljkUyZY8YBDIzbe6LY3tK4heLrmaeZDj5HwgFYUcwoTE6YlFvZ0Y3peQ7Efkj49w6MeO8vGdePZj8GyPYOgyDfjf7xFleUmwXmjHGrXljN0RS7iAawmkI05Ys6v9OYzQyb0jMOvqUeXSYTBjtXy0YQXYk7iOQiLzi7zjbYMFvHhw7hYf5wnXjXTJ65Yg4wBYn6R3dwOFWgXEpbwhMJ6GJctwdmJboYGHRXgWTsjtYzQyDcYscepkJHzv8XJTNRBNE61ilojAAx5OvS3jLli3TJ77x3Ya4RoGwzSWdGEhHwFfi1sy5qygaJz3yGXi0HWTlYaY7OjGtwznvdsjLY4MRLSvfHY0hW7heN0RofWO4jqaWFYQURA8jZGEQSjB9eqzRa0WSDJHNilYmoRh1wHzW9oEflwctJMoJB5whdJaSY3NWOkYd8&UNSDS=&callback=CASFlRjdQwEVGKHWUFJ&_=1604655654441"
    header = {
        'Host': 'hotels.ctrip.com',
        'User-Agent': 'Mozilla/5.0 (X11; Ubuntu; Linux x86_64; rv:82.0) Gecko/20100101 Firefox/82.0',
        'Accept': '*/*',
        'Accept-Language': 'en-CA,en-US;q=0.7,en;q=0.3',
        'Accept-Encoding': 'gzip, deflate, br',
        'Content-Type': 'application/x-www-form-urlencoded; charset=utf-8',
        'If-Modified-Since': 'Thu, 01 Jan 1970 00:00:00 GMT',
        'Connection': 'keep-alive',
        'Referer': 'https://hotels.ctrip.com/hotel/757450.html?isFull=F&masterhotelid=757450&hcityid=1428',
        'Cookie': 'magicid=pLb/hpH6ffJtfao8kC1qxYL3J59g6Sb1BxRe2OoS42HBaLSQv4yIN4/TI76Mhhde; _bfa=1.1604637757302.o40kl.1.1604652351516.1604655213108.5.54; Union=AllianceID=4899&SID=135371&OUID=&createtime=1604655295&Expires=1605260095219; Session=smartlinkcode=U135371&smartlinklanguage=zh&SmartLinkKeyWord=&SmartLinkQuary=&SmartLinkHost=; MKT_OrderClick=ASID=48992611971&AID=4899&CSID=2611971&OUID=Canada&CT=1604637758985&CURL=https%3A%2F%2Fwww.ctrip.com%2F%3Fsid%3D2611971%26allianceid%3D4899%26ouid%3DCanada%26gclid%3DCjwKCAiA4o79BRBvEiwAjteoYD1iQhWai6FA7_vl08lLBDi4d4MqCwIF9wcLa9Wv4mvAEx6dxJBGqRoC0UcQAvD_BwE%26gclsrc%3Daw.ds%26keywordid%3D1358122705-101055166511&VAL={"pc_vid":"1604637757302.o40kl"}; MKT_CKID=1604637759017.1wt39.qyi2; MKT_CKID_LMT=1604637759017; _jzqco=%7C%7C%7C%7C1604637760944%7C1.808013776.1604637759022.1604655413757.1604655639808.1604655413757.1604655639808.undefined.0.0.32.32; __zpspc=9.5.1604655218.1604655639.6%233%7Cmail.google.com%7C%7C%7C%7C%23; _RF1=174.91.123.106; _RSG=zv4ek0sYvZBlm1N3hqf9a8; _RDG=28d7b93eb5da652458197547fddabbd208; _RGUID=b8f98b60-2ea0-4e7d-8909-a74ac35c1c2f; MKT_Pagesource=PC; _gcl_aw=GCL.1604637761.CjwKCAiA4o79BRBvEiwAjteoYD1iQhWai6FA7_vl08lLBDi4d4MqCwIF9wcLa9Wv4mvAEx6dxJBGqRoC0UcQAvD_BwE; _gcl_dc=GCL.1604637761.CjwKCAiA4o79BRBvEiwAjteoYD1iQhWai6FA7_vl08lLBDi4d4MqCwIF9wcLa9Wv4mvAEx6dxJBGqRoC0UcQAvD_BwE; _ga=GA1.2.1617066246.1604637761; _gid=GA1.2.1086628561.1604637761; _gac_UA-3748357-1=1.1604637761.CjwKCAiA4o79BRBvEiwAjteoYD1iQhWai6FA7_vl08lLBDi4d4MqCwIF9wcLa9Wv4mvAEx6dxJBGqRoC0UcQAvD_BwE; _bfi=p1%3D102003%26p2%3D102002%26v1%3D53%26v2%3D52; ibu_wws_c=1607229766601%7Czh-cn; HotelCityID=1428split%E6%81%A9%E5%B9%B3splitEnpingsplit2020-11-12split2020-11-13split5; ASP.NET_SessionId=dwfw5msox3crx0jzh1o1xm3k; librauuid=ZzdFVLzsdfdtCM1c; OID_ForOnlineHotel=1604637757302o40kl1604637994456102032; login_uid=0A018522261073AAD57BA39EF76C9A7F; login_type=0; UUID=288451D1F4D14C5AB9E10970DCD1D9D0; IsPersonalizedLogin=T; HotelDomesticVisitedHotels1=757450=0,0,4.4,2451,/20030v000000jzp545898.jpg,&28366175=0,0,4.4,706,/200k14000000w6qfx159E.jpg,&14249344=0,0,4.8,25434,/200s1900000169opw2822.jpg,&17892135=0,0,4.5,338,/2004180000014dnal905A.jpg,; _abtest_userid=0fedc4b7-74be-497c-8d0c-4dc6640fdae4; cticket=85F38A055A5BEDD507B4DB4814D2E52AEC5DBF7ABA36E75BEFAF5C78F0782505; AHeadUserInfo=VipGrade=10&VipGradeName=%BB%C6%BD%F0%B9%F3%B1%F6&UserName=&NoReadMessageCount=1; ticket_ctrip=bJ9RlCHVwlu1ZjyusRi+ypZ7X2r4+yoj7Qg58pKGqFqDsPTDmtuR1+DUXsqBhrtuYlMP+iLWl4Fc9XstSGgm1Fu9yZs15zVEibhXc4MDTWdrrjVbkrJTXlbRkMm3QkuMIT+wcxhgYqUyIDGenLZINgKWe+YRsd+ngnLdIkM1ZiWUNr8VdEZd9r/iZKz5nYmpbAbtBLHQtVhb0ISECMqgbO2FJCR8Zvxt84PaRuUwfjn3fOcNZOdF+dVTB7b78d7SQhc1HUb7l6fMm5BBVpVezXIC0G6RqqocMEaSQcPKAhg=; DUID=u=40B51B93B78F6DFA9B32231A3D52F7B7&v=0; IsNonUser=F; ibulanguage=CN; ibulocale=zh_cn; cookiePricesDisplayed=CNY; IBU_TRANCE_LOG_P=78119947423; _bfs=1.9; hotelhst=1164390341; _uetsid=235d8410201311eb86d30166f8d6f1c4; _uetvid=235d9450201311eb844a1520adcdefce; MjAxNS8wNi8yOSAgSE9URUwgIERFQlVH=OceanBall; _gat=1',
        'TE': 'Trailers'
    }
    try:
        hotel_price_html = requests.get(url = addr, headers=header)
    except:
        try:
            hotel_price_html = requests.get(url = addr, headers=header)
        except:
            print(hotelID)
            return
    hotel_price_html.encoding = 'utf-8-sig'
    hotel_data = hotel_price_html.text
    s_index = hotel_data.find('J_RoomListTbl') + len('J_RoomListTbl')
    hotel_data = hotel_data[s_index:]
    s_index = hotel_data.find('<\/dfn>') + len('<\/dfn>')
    hotel_data_list = hotel_data.split('<\/dfn>')
    price_list = []
    for element in (hotel_data_list):
        e_index = element.find('<\/span>')
        hotel_data_list.insert(hotel_data_list.index(element), element[:e_index])
        hotel_data_list.remove(element)
    for element in hotel_data_list:
        try:
            int_price = int(element)
            price_list.append(int_price)
        except:
            continue
    print(price_list)
    return price_list


def listToString(l):  
    str1 = ""    
    for ele in l:  
        str1 += (ele + ', ')   
    return str1  


if __name__ == "__main__":
    failed_hotelID = []
    with open('atlantis_with_room_info.csv', newline='') as csvfile:
        reader = csv.reader(csvfile, delimiter=' ', quotechar='|')
        row = reader.__next__()
        row[0] += ',avgPrice,minPrice,maxPrice'
        with_room_info_array = np.array((row[0].split(',')))
        print(with_room_info_array)
        row = reader.__next__()
        i = 0
        while(row != None):
            print(i)
            hotel_id = (row[0].split(','))[0]
            hotel_price = get_hotel_price(hotel_id, '43')
            if(hotel_price is None):
                failed_hotelID.append(hotel_id)
                continue
            print(row)
            hotel_price_str = []
            for price in hotel_price:
                hotel_price_str.append(str(price))
            hotel_price_list = []
            hotel_price_list.append(listToString(hotel_price_str))
            hotel_price_list.append(str(sum(hotel_price)/len(hotel_price)))
            hotel_price_list.append(str(min(hotel_price)))
            hotel_price_list.append(str(max(hotel_price)))
            new_row = [(row[0] + (',' + hotel_price_list[1]) + (',' + hotel_price_list[2]) + (',' + hotel_price_list[3])).split(',')]
            print(new_row)
            with_room_info_array = np.vstack((with_room_info_array, new_row))
            try:
                row = reader.__next__()
            except:
                print("end of the file")
                break
            i = i+1
        with open("atlantis_with_room_price.csv", 'w', encoding="utf-8-sig", newline="") as f:
            csvwriter = csv.writer(f, dialect='excel', delimiter=',')
            csvwriter.writerows(with_room_info_array)
    print(failed_hotelID)