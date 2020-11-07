# Retrive the information of interested hotels from Ctrip.

import requests
import csv
import json
import time
import numpy as np

def get_quanlin():
    quanlin_url = "https://hotels.ctrip.com/Domestic/Tool/AjaxHotelList.aspx"
    quanlin_header = {
        'Host': 'hotels.ctrip.com',
        'User-Agent': 'Mozilla/5.0 (X11; Ubuntu; Linux x86_64; rv:82.0) Gecko/20100101 Firefox/82.0',
        'Accept': '*/*',
        'Accept-Language': 'en-CA,en-US;q=0.7,en;q=0.3',
        'Accept-Encoding': 'gzip, deflate, br',
        'Content-Type': 'application/x-www-form-urlencoded; charset=utf-8',
        'If-Modified-Since': 'Thu, 01 Jan 1970 00:00:00 GMT',
        'Content-Length': '2435',
        'Origin': 'https://hotels.ctrip.com',
        'Connection': 'keep-alive',
        'Referer': 'https://hotels.ctrip.com/hotel/enping1428',
        'Cookie': 'magicid=pLb/hpH6ffJtfao8kC1qxYL3J59g6Sb1BxRe2OoS42HBaLSQv4yIN4/TI76Mhhde; MjAxNS8wNi8yOSAgSE9URUwgIERFQlVH=OceanBall; _bfa=1.1604637757302.o40kl.1.1604637757302.1604637757302.1.12; _bfs=1.12; Union=OUID=Canada&AllianceID=4899&SID=2611971&SourceID=&createtime=1604637759&Expires=1605242558982; Session=SmartLinkCode=U2611971&SmartLinkKeyWord=&SmartLinkQuary=&SmartLinkHost=&SmartLinkLanguage=zh; MKT_OrderClick=ASID=48992611971&AID=4899&CSID=2611971&OUID=Canada&CT=1604637758985&CURL=https%3A%2F%2Fwww.ctrip.com%2F%3Fsid%3D2611971%26allianceid%3D4899%26ouid%3DCanada%26gclid%3DCjwKCAiA4o79BRBvEiwAjteoYD1iQhWai6FA7_vl08lLBDi4d4MqCwIF9wcLa9Wv4mvAEx6dxJBGqRoC0UcQAvD_BwE%26gclsrc%3Daw.ds%26keywordid%3D1358122705-101055166511&VAL={"pc_vid":"1604637757302.o40kl"}; MKT_CKID=1604637759017.1wt39.qyi2; MKT_CKID_LMT=1604637759017; _jzqco=%7C%7C%7C%7C1604637760944%7C1.808013776.1604637759022.1604638070558.1604638151522.1604638070558.1604638151522.undefined.0.0.6.6; __zpspc=9.1.1604637759.1604638151.6%233%7Cwww.google.com%7C%7C%7C%7C%23; _RF1=174.91.123.106; _RSG=zv4ek0sYvZBlm1N3hqf9a8; _RDG=28d7b93eb5da652458197547fddabbd208; _RGUID=b8f98b60-2ea0-4e7d-8909-a74ac35c1c2f; MKT_Pagesource=PC; _gcl_aw=GCL.1604637761.CjwKCAiA4o79BRBvEiwAjteoYD1iQhWai6FA7_vl08lLBDi4d4MqCwIF9wcLa9Wv4mvAEx6dxJBGqRoC0UcQAvD_BwE; _gcl_dc=GCL.1604637761.CjwKCAiA4o79BRBvEiwAjteoYD1iQhWai6FA7_vl08lLBDi4d4MqCwIF9wcLa9Wv4mvAEx6dxJBGqRoC0UcQAvD_BwE; _ga=GA1.2.1617066246.1604637761; _gid=GA1.2.1086628561.1604637761; _gac_UA-3748357-1=1.1604637761.CjwKCAiA4o79BRBvEiwAjteoYD1iQhWai6FA7_vl08lLBDi4d4MqCwIF9wcLa9Wv4mvAEx6dxJBGqRoC0UcQAvD_BwE; _bfi=p1%3D102002%26p2%3D102002%26v1%3D12%26v2%3D11; ibu_wws_c=1607229766601%7Czh-cn; HotelCityID=1428split%E6%81%A9%E5%B9%B3splitEnpingsplit2020-11-5split2020-11-06split5; ASP.NET_SessionId=dwfw5msox3crx0jzh1o1xm3k; hotelhst=1164390341; librauuid=sAZDuSma38X9VQbX; OID_ForOnlineHotel=1604637757302o40kl1604637994456102032; login_uid=E388EFA775EE478A54F20FE346101CA9; login_type=0; cticket=85F38A055A5BEDD507B4DB4814D2E52A7AE9F58E514C181743B2A00998561395; AHeadUserInfo=VipGrade=10&VipGradeName=%BB%C6%BD%F0%B9%F3%B1%F6&UserName=&NoReadMessageCount=1; ticket_ctrip=bJ9RlCHVwlu1ZjyusRi+ypZ7X2r4+yoj7Qg58pKGqFqDsPTDmtuR1+DUXsqBhrtuYlMP+iLWl4Fc9XstSGgm1Fu9yZs15zVE6pPixpG+L+oHt9hlTI12Yqo+RGkohL+3kEwXaHDVBXbIUnkp5Usf00xVhhcdt8s3fREvSRhqgr6ZsngdJGb4RRMCeZtNJ71G/DY2Zs8yBo5n5Mwpyf2sO4z2z48xpvIguy7VWbvez8QEUCAoGOwYbBq2XLRvsp7WsKwxoVZo8lX6ZHfs0No7w7yyr87IkyMhOcKMbovfEF4=; DUID=u=40B51B93B78F6DFA9B32231A3D52F7B7&v=0; IsNonUser=F; UUID=288451D1F4D14C5AB9E10970DCD1D9D0; IsPersonalizedLogin=T; _gat=1',
        'TE': 'Trailers'
    }
    quanlin_request = {
        '__VIEWSTATEGENERATOR':	"DB1FBB6D",
        'cityName':	"%E6%81%A9%E5%B9%B3",
        'StartTime':	"2020-11-12",
        'DepTime':	"2020-11-13",
        'RoomGuestCount':	"1,1,0",
        'operationtype':	"NEWHOTELORDER",
        'IsOnlyAirHotel':	"F",
        'cityId':	"1428",
        'cityPY':	"enping",
        'cityCode':	"0750",
        'cityLat':	"22.1894430514",
        'cityLng':	"112.3115824719",
        'hotelposition':	"0%2C0",
        'htlPageView':	"0",
        'hotelType':	"F",
        'hasPKGHotel':	"F",
        'requestTravelMoney':	"F",
        'isusergiftcard':	"F",
        'useFG':	"F",
        'priceRange':	"-2",
        'promotion':	"F",
        'prepay':	"F",
        'IsCanReserve':	"F",
        'OrderBy':	"99",
        'checkIn':	"2020-11-12",
        'checkOut':	"2020-11-13",
        'hidTestLat':	"0%7C0",
        'isfromlist':	"T",
        'ubt_price_key':	"htl_search_noresult_promotion",
        'isHuaZhu':	"False",
        'allianceid':	"0",
        'sid':	"0",
        'markType':	"4",
        'a':	"0",
        'contrast':	"0",
        'page_id_forlog':	"102002",
        'contyped':	"0",
        'eleven':	"cc888ed5e0f6e33¦441bcefd27d7d26c5fa62b419f3d11414d8f93797e84f0bf",
        'twelve':	"DTLrS8jM5ez9E9nRAYpNY1oEzYUzia6WXlWUYn6jZ8yQ7ic3jXYpOjAPeFlvd5jUYZMWMoxa3vsUjdYtFvlqYQcyASYZnvSteDoJO3jQ4y3Y1ceh5YBnyUDjX5vs4eLpYQkjhBygY0YBNIcbeQTYSbv9ZyqrGzeDajLZw1lYbXwplEmY4PWn6YU0ydUE5Xj9Owg7edtvqzeMDjPay8Y6SyfojHqxM9eXPwDTjTorDojd5R0nioZwkMIq4YkTvGMYMny9tjmXvTqe05YNSj4HyUYtTY9hizpiOLitojnYBcvM0w1GY0Xwq8j0oJ1QYA0waYN8RHlwMGWO9EAhwasilAjQ6R7zEPdjHdJ6XwDhvlYknytzYT4eScJOQvOFJMzR9GEFAic9jBBxANvOoj1Hi7dJkkxoYNoRM4wp7WmhEckw9ZipzyD1ytsJO3yPgihDWqoYSYgHjHpwQqvMOjdYHORsXv0bYMlWUNeUGRZMW8ojbHW9YcSRgPjbDEN0jcQeZlR9cW3ZJtpiBY3QRDawM4W03EPFw7oiQMjsMRfgEnBjlTESUvN6",
        'filterJson':	"{\"zone\":\"\",\"location\":\"\",\"type\":\"\",\"brand\":\"\",\"group\":\"\",\"feature\":\"\",\"equip\":\"\",\"bed\":\"\",\"breakfast\":\"\",\"other\":\"\",\"sl\":\"\",\"s\":\"\",\"l\":\"\",\"price\":\"\",\"a\":\"0\",\"contrast\":\"0\",\"PaymentType\":\"\",\"CtripService\":\"\",\"promotionf\":\"\",\"allpoint\":\"\",\"star\":\"4,5\"}",
        'attachDistance':	"0",
        'star':	"4,5",
        'page':	"1",
    }
    quanlin_html = requests.post(url = quanlin_url, headers = quanlin_header, data = quanlin_request)
    quanlin_list = quanlin_html.json()["hotelPositionJSON"]
    print(quanlin_list)
    id = []
    name = []
    lat = []
    lon = []
    hotel_url = []
    img = []
    address = []
    score = []
    dpscore = []
    dpcount = []
    star = []
    stardesc = []
    shortName = []
    isSingleRec = []
    for item in quanlin_list:
            id.append(item['id'])
            name.append(item['name'])
            lat.append(item['lat'])
            lon.append(item['lon'])
            hotel_url.append(item['url'])
            img.append(item['img'])
            address.append(item['address'])
            score.append(item['score'])
            dpscore.append(item['dpscore'])
            dpcount.append(item['dpcount'])
            star.append(item['star'])
            stardesc.append(item['stardesc'])
            shortName.append(item['shortName'])
            isSingleRec.append(item['isSingleRec'])

    hotel_array = np.array((id, name, lat, lon, hotel_url, img, address, score, dpscore, dpcount, star, stardesc, shortName, isSingleRec)).T
    list_header = ['id', 'name', 'lat', 'lon', 'url', 'img', 'address', 'score', 'dpscore', 'dpcount', 'star', 'stardesc', 'shortName', 'isSingleRec']
    array_header = np.array((list_header))
    quanlin_hotellists = np.vstack((array_header, hotel_array))
    with open("quanlin.csv", 'w', encoding="utf-8-sig", newline="") as f:
        csvwriter = csv.writer(f, dialect='excel')
        csvwriter.writerows(quanlin_hotellists)
    time.sleep(5)
    return


def get_atlantis():
    id = []
    name = []
    lat = []
    lon = []
    hotel_url = []
    img = []
    address = []
    score = []
    dpscore = []
    dpcount = []
    star = []
    stardesc = []
    shortName = []
    isSingleRec = []
    #fatlantis = open("atlantis.csv", 'w', encoding="utf-8-sig", newline="")
    #fatlantis.close()
    atlantis_url = "https://hotels.ctrip.com/Domestic/Tool/AjaxHotelList.aspx"
    atlantis_header = {
        'Host': 'hotels.ctrip.com',
        'User-Agent': 'Mozilla/5.0 (X11; Ubuntu; Linux x86_64; rv:82.0) Gecko/20100101 Firefox/82.0',
        'Accept': '*/*',
        'Accept-Language': 'en-CA,en-US;q=0.7,en;q=0.3',
        'Accept-Encoding': 'gzip, deflate, br',
        'Content-Type': 'application/x-www-form-urlencoded; charset=utf-8',
        'If-Modified-Since': 'Thu, 01 Jan 1970 00:00:00 GMT',
        'Content-Length': '2490',
        'Origin': 'https://hotels.ctrip.com',
        'Connection': 'keep-alive',
        'Referer': 'https://hotels.ctrip.com/hotel/sanya43/sl4324798star5',
        'Cookie': 'magicid=pLb/hpH6ffJtfao8kC1qxYL3J59g6Sb1BxRe2OoS42HBaLSQv4yIN4/TI76Mhhde; MjAxNS8wNi8yOSAgSE9URUwgIERFQlVH=OceanBall; _bfa=1.1604637757302.o40kl.1.1604637757302.1604637757302.1.16; _bfs=1.16; Union=OUID=Canada&AllianceID=4899&SID=2611971&SourceID=&createtime=1604637759&Expires=1605242558982; Session=SmartLinkCode=U2611971&SmartLinkKeyWord=&SmartLinkQuary=&SmartLinkHost=&SmartLinkLanguage=zh; MKT_OrderClick=ASID=48992611971&AID=4899&CSID=2611971&OUID=Canada&CT=1604637758985&CURL=https%3A%2F%2Fwww.ctrip.com%2F%3Fsid%3D2611971%26allianceid%3D4899%26ouid%3DCanada%26gclid%3DCjwKCAiA4o79BRBvEiwAjteoYD1iQhWai6FA7_vl08lLBDi4d4MqCwIF9wcLa9Wv4mvAEx6dxJBGqRoC0UcQAvD_BwE%26gclsrc%3Daw.ds%26keywordid%3D1358122705-101055166511&VAL={"pc_vid":"1604637757302.o40kl"}; MKT_CKID=1604637759017.1wt39.qyi2; MKT_CKID_LMT=1604637759017; _jzqco=%7C%7C%7C%7C1604637760944%7C1.808013776.1604637759022.1604638215983.1604638251434.1604638215983.1604638251434.undefined.0.0.8.8; __zpspc=9.1.1604637759.1604638251.8%233%7Cwww.google.com%7C%7C%7C%7C%23; _RF1=174.91.123.106; _RSG=zv4ek0sYvZBlm1N3hqf9a8; _RDG=28d7b93eb5da652458197547fddabbd208; _RGUID=b8f98b60-2ea0-4e7d-8909-a74ac35c1c2f; MKT_Pagesource=PC; _gcl_aw=GCL.1604637761.CjwKCAiA4o79BRBvEiwAjteoYD1iQhWai6FA7_vl08lLBDi4d4MqCwIF9wcLa9Wv4mvAEx6dxJBGqRoC0UcQAvD_BwE; _gcl_dc=GCL.1604637761.CjwKCAiA4o79BRBvEiwAjteoYD1iQhWai6FA7_vl08lLBDi4d4MqCwIF9wcLa9Wv4mvAEx6dxJBGqRoC0UcQAvD_BwE; _ga=GA1.2.1617066246.1604637761; _gid=GA1.2.1086628561.1604637761; _gac_UA-3748357-1=1.1604637761.CjwKCAiA4o79BRBvEiwAjteoYD1iQhWai6FA7_vl08lLBDi4d4MqCwIF9wcLa9Wv4mvAEx6dxJBGqRoC0UcQAvD_BwE; _bfi=p1%3D102002%26p2%3D102002%26v1%3D16%26v2%3D15; ibu_wws_c=1607229766601%7Czh-cn; HotelCityID=43split%E4%B8%89%E4%BA%9AsplitSanyasplit2020-11-12split2020-11-13split5; ASP.NET_SessionId=dwfw5msox3crx0jzh1o1xm3k; librauuid=sAZDuSma38X9VQbX; OID_ForOnlineHotel=1604637757302o40kl1604637994456102032; login_uid=E388EFA775EE478A54F20FE346101CA9; login_type=0; cticket=85F38A055A5BEDD507B4DB4814D2E52A7AE9F58E514C181743B2A00998561395; AHeadUserInfo=VipGrade=10&VipGradeName=%BB%C6%BD%F0%B9%F3%B1%F6&UserName=&NoReadMessageCount=1; ticket_ctrip=bJ9RlCHVwlu1ZjyusRi+ypZ7X2r4+yoj7Qg58pKGqFqDsPTDmtuR1+DUXsqBhrtuYlMP+iLWl4Fc9XstSGgm1Fu9yZs15zVE6pPixpG+L+oHt9hlTI12Yqo+RGkohL+3kEwXaHDVBXbIUnkp5Usf00xVhhcdt8s3fREvSRhqgr6ZsngdJGb4RRMCeZtNJ71G/DY2Zs8yBo5n5Mwpyf2sO4z2z48xpvIguy7VWbvez8QEUCAoGOwYbBq2XLRvsp7WsKwxoVZo8lX6ZHfs0No7w7yyr87IkyMhOcKMbovfEF4=; DUID=u=40B51B93B78F6DFA9B32231A3D52F7B7&v=0; IsNonUser=F; UUID=288451D1F4D14C5AB9E10970DCD1D9D0; IsPersonalizedLogin=T; hotelhst=1164390341',
        'TE': 'Trailers',
    }
    for i in range(9, 10):
        atlantis_request = {
            '__VIEWSTATEGENERATOR':	"DB1FBB6D",
            'cityName':	"%E4%B8%89%E4%BA%9A",
            'StartTime':	"2020-11-12",
            'DepTime':	"2020-11-13",
            'RoomGuestCount':	"1,1,0",
            'operationtype':	"NEWHOTELORDER",
            'IsOnlyAirHotel':	"F",
            'cityId': "43",
            'cityPY':	"sanya",
            'cityCode':	"0899",
            'cityLat':	"18.2585823406",
            'cityLng':	"109.5184657451",
            'positionArea':	"RailwayStation",
            'positionId':	"4324798",
            'htlPageView':	"0",
            'hotelType':	"F",
            'hasPKGHotel':	"F",
            'requestTravelMoney': "F",
            'isusergiftcard':	"F",
            'useFG':	"F",
            'priceRange': "-2",
            'promotion':	"F",
            'prepay':	"F",
            'IsCanReserve':	"F",
            'OrderBy':	"99",
            'checkIn':	"2020-11-12",
            'checkOut':	"2020-11-13",
            'hidTestLat':	"18.3603382110596%7C109.750579833984",
            'isfromlist':	"T",
            'ubt_price_key':	"htl_search_noresult_promotion",
            'isHuaZhu':	"False",
            'allianceid':	"0",
            'sid':	"0",
            'markType':	"4",
            'sl':	"4324798",
            'a':	"0",
            'contrast':	"0",
            'page_id_forlog':	"102002",
            'contyped':	"0",
            'eleven':	"73§efe3e32a4fgcb311f0f715ffa02bc3190f11876b5c340d88a83417b96651a",
            'twelve':	"N1fWbFjgTeUNE4owsYMAYq4ELYdfi09WQgWSYABJFheblRsMjXYSAeo9wLfig0jAYOqKUzYA0vFDYOYdtvXLYGDy9DxMAvh8es5YocjBzyfYQPv5GWNmyGgjDfvMdeQ9YdtjFSykYlYMkI9QeQaYh5vZ4ekrk7etajphw0TYLUwOzEPYNtvkQYMmy3kE9bj5QwpqelFv0ceftja7yNYG3yqPjn4xh3etdwaljtdr31jkDROMiAXwLmIoOYnpvmfYqOyz1jmSv4pesUYcTjkdybYPSYXzidSipUiZUjcYUMvsPwDgYpaw7Ajh4JmlYpfwFYgZR8XwTOWAqEtdwFkiU5vqOY69vTHw3lR0pjflw3Ybmy48YktegzJ7Xv3pJokRNZE6sigNjZZx6ovULjOniAQJaaxZYmHRUswNDWfkEolwODic9y4fyBhJStycfiBmWQTYZYd1j6OwGBvapjOYtLRsPv5nYTQWoNedsRG9WqajgHWzYmoRLUjqmEM5jU9ehkR4tW5dJdSiAYgkR14wOBWgSE5SwdXiQ8jNsYBaE0kjlgwpXE4a",
            'filterJson':	"{\"zone\":\"\",\"location\":\"\",\"type\":\"\",\"brand\":\"\",\"group\":\"\",\"feature\":\"\",\"equip\":\"\",\"bed\":\"\",\"breakfast\":\"\",\"other\":\"\",\"sl\":\"4324798\",\"s\":\"\",\"l\":\"\",\"price\":\"\",\"a\":\"0\",\"contrast\":\"0\",\"PaymentType\":\"\",\"CtripService\":\"\",\"promotionf\":\"\",\"allpoint\":\"\",\"star\":\"5,4\"}",
            'star':	"5,4",
            'attachDistance':	"0",
            'page':	i
        }
        atlantis_html = requests.post(url = atlantis_url, headers = atlantis_header, data = atlantis_request)
        atlantis_list = atlantis_html.json()["hotelPositionJSON"]
        for item in atlantis_list:
                id.append(item['id'])
                name.append(item['name'])
                lat.append(item['lat'])
                lon.append(item['lon'])
                hotel_url.append(item['url'])
                img.append(item['img'])
                address.append(item['address'])
                score.append(item['score'])
                dpscore.append(item['dpscore'])
                dpcount.append(item['dpcount'])
                star.append(item['star'])
                stardesc.append(item['stardesc'])
                shortName.append(item['shortName'])
                isSingleRec.append(item['isSingleRec'])

        hotel_array = np.array((id, name, lat, lon, hotel_url, img, address, score, dpscore, dpcount, star, stardesc, shortName, isSingleRec)).T
        list_header = ['id', 'name', 'lat', 'lon', 'url', 'img', 'address', 'score', 'dpscore', 'dpcount', 'star', 'stardesc', 'shortName', 'isSingleRec']
        array_header = np.array((list_header))
        quanlin_hotellists = np.vstack((hotel_array))
        with open("atlantis.csv", 'a', encoding="utf-8-sig", newline="") as f:
            csvwriter = csv.writer(f, dialect='excel')
            csvwriter.writerows(quanlin_hotellists)
        time.sleep(5)
    return

if __name__ == "__main__":
    get_quanlin()
    get_atlantis()