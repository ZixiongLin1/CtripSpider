# Retrive the hotels' information(opening, renovation, size of the hotel) from website

import requests
import time
import datetime
import json
import csv
import numpy as np
import random

def get_hotel_info(hotelID):
    addr = "https://hotels.ctrip.com/hotel/" + hotelID + '.html'
    header = {
        'Host': 'hotels.ctrip.com',
        'User-Agent': 'Mozilla/5.0 (X11; Ubuntu; Linux x86_64; rv:82.0) Gecko/20100101 Firefox/82.0',
        'Accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,*/*;q=0.8',
        'Accept-Language': 'en-CA,en-US;q=0.7,en;q=0.3',
        'Accept-Encoding': 'gzip, deflate, br',
        'Connection': 'keep-alive',
        'Cookie': 'magicid=pLb/hpH6ffJtfao8kC1qxYL3J59g6Sb1BxRe2OoS42HBaLSQv4yIN4/TI76Mhhde; MjAxNS8wNi8yOSAgSE9URUwgIERFQlVH=OceanBall; _bfa=1.1604637757302.o40kl.1.1604645851593.1604648214650.3.40; Union=OUID=Canada&AllianceID=4899&SID=2611971&SourceID=&createtime=1604637759&Expires=1605242558982; Session=SmartLinkCode=U2611971&SmartLinkKeyWord=&SmartLinkQuary=&SmartLinkHost=&SmartLinkLanguage=zh; MKT_OrderClick=ASID=48992611971&AID=4899&CSID=2611971&OUID=Canada&CT=1604637758985&CURL=https%3A%2F%2Fwww.ctrip.com%2F%3Fsid%3D2611971%26allianceid%3D4899%26ouid%3DCanada%26gclid%3DCjwKCAiA4o79BRBvEiwAjteoYD1iQhWai6FA7_vl08lLBDi4d4MqCwIF9wcLa9Wv4mvAEx6dxJBGqRoC0UcQAvD_BwE%26gclsrc%3Daw.ds%26keywordid%3D1358122705-101055166511&VAL={"pc_vid":"1604637757302.o40kl"}; MKT_CKID=1604637759017.1wt39.qyi2; MKT_CKID_LMT=1604637759017; _jzqco=%7C%7C%7C%7C1604637760944%7C1.808013776.1604637759022.1604649063249.1604649318556.1604649063249.1604649318556.undefined.0.0.25.25; __zpspc=9.4.1604648218.1604649318.10%233%7Cwww.google.com%7C%7C%7C%7C%23; _RF1=174.91.123.106; _RSG=zv4ek0sYvZBlm1N3hqf9a8; _RDG=28d7b93eb5da652458197547fddabbd208; _RGUID=b8f98b60-2ea0-4e7d-8909-a74ac35c1c2f; MKT_Pagesource=PC; _gcl_aw=GCL.1604637761.CjwKCAiA4o79BRBvEiwAjteoYD1iQhWai6FA7_vl08lLBDi4d4MqCwIF9wcLa9Wv4mvAEx6dxJBGqRoC0UcQAvD_BwE; _gcl_dc=GCL.1604637761.CjwKCAiA4o79BRBvEiwAjteoYD1iQhWai6FA7_vl08lLBDi4d4MqCwIF9wcLa9Wv4mvAEx6dxJBGqRoC0UcQAvD_BwE; _ga=GA1.2.1617066246.1604637761; _gid=GA1.2.1086628561.1604637761; _gac_UA-3748357-1=1.1604637761.CjwKCAiA4o79BRBvEiwAjteoYD1iQhWai6FA7_vl08lLBDi4d4MqCwIF9wcLa9Wv4mvAEx6dxJBGqRoC0UcQAvD_BwE; _bfi=p1%3D102003%26p2%3D102003%26v1%3D40%26v2%3D39; ibu_wws_c=1607229766601%7Czh-cn; HotelCityID=1428split%E6%81%A9%E5%B9%B3splitEnpingsplit2020-11-12split2020-11-13split5; ASP.NET_SessionId=dwfw5msox3crx0jzh1o1xm3k; librauuid=sAZDuSma38X9VQbX; OID_ForOnlineHotel=1604637757302o40kl1604637994456102032; login_uid=E388EFA775EE478A54F20FE346101CA9; login_type=0; cticket=85F38A055A5BEDD507B4DB4814D2E52A7AE9F58E514C181743B2A00998561395; AHeadUserInfo=VipGrade=10&VipGradeName=%BB%C6%BD%F0%B9%F3%B1%F6&UserName=&NoReadMessageCount=1; ticket_ctrip=bJ9RlCHVwlu1ZjyusRi+ypZ7X2r4+yoj7Qg58pKGqFqDsPTDmtuR1+DUXsqBhrtuYlMP+iLWl4Fc9XstSGgm1Fu9yZs15zVE6pPixpG+L+oHt9hlTI12Yqo+RGkohL+3kEwXaHDVBXbIUnkp5Usf00xVhhcdt8s3fREvSRhqgr6ZsngdJGb4RRMCeZtNJ71G/DY2Zs8yBo5n5Mwpyf2sO4z2z48xpvIguy7VWbvez8QEUCAoGOwYbBq2XLRvsp7WsKwxoVZo8lX6ZHfs0No7w7yyr87IkyMhOcKMbovfEF4=; DUID=u=40B51B93B78F6DFA9B32231A3D52F7B7&v=0; IsNonUser=F; UUID=288451D1F4D14C5AB9E10970DCD1D9D0; IsPersonalizedLogin=T; HotelDomesticVisitedHotels1=28366175=0,0,4.4,706,/200k14000000w6qfx159E.jpg,&14249344=0,0,4.8,25434,/200s1900000169opw2822.jpg,&17892135=0,0,4.5,338,/2004180000014dnal905A.jpg,; _abtest_userid=0fedc4b7-74be-497c-8d0c-4dc6640fdae4; _bfs=1.10',
        'Upgrade-Insecure-Requests': '1',
        'Cache-Control': 'max-age=0'
    }
    hotel_html = requests.get(url = addr, headers=header)
    hotel_html.encoding = 'utf-8-sig'
    hotel_data = hotel_html.text
    s_index = hotel_data.find('<div class="htl_room_txt text_3l" id="htlDes">') + len('<div class="htl_room_txt text_3l" id="htlDes">')
    e_index = hotel_data.find('<span id="ctl00_MainContentPlaceHolder_hotelDetailInfo_lbDesc" itemprop="description">')
    hotel_data = hotel_data[s_index:e_index]
    s_index = hotel_data.find('<p>\n') + len('<p>\n')
    e_index = hotel_data.find('\n<span id="J_realContact"')
    hotel_data = hotel_data[s_index:e_index]
    hotel_info_list = hotel_data.split('&nbsp;&nbsp;')[:-1]
    print(hotel_info_list)
    f = open('hotel.html', 'w', encoding='utf-8-sig')
    f.write(hotel_data)
    f.close()
    #time.sleep(random.randint(7,13))
    return hotel_info_list


if __name__ == "__main__":
    with open('atlantis_with_distance.csv', newline='') as csvfile:
        reader = csv.reader(csvfile, delimiter=' ', quotechar='|')
        row = reader.__next__()
        row[0] += ',opening,renovation,size'
        with_room_info_array = np.array((row[0].split(',')))
        print(with_room_info_array)
        row = reader.__next__()
        while(row != None):
            hotel_id = (row[0].split(','))[0]
            hotel_info = get_hotel_info(hotel_id)
            if (len(hotel_info) == 2):
                hotel_info.insert(1, '')
            new_row = [(row[0] + (',' + hotel_info[0]) + (',' + hotel_info[1]) + (',' + hotel_info[2])).split(',')]
            print(new_row)
            with_room_info_array = np.vstack((with_room_info_array, new_row))
            try:
                row = reader.__next__()
            except:
                print("end of the file")
                break
        with open("atlantis_with_room_info.csv", 'w', encoding="utf-8-sig", newline="") as f:
            csvwriter = csv.writer(f, dialect='excel', delimiter=',')
            csvwriter.writerows(with_room_info_array)