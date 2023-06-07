import requests
print ("ПРОГРАММА ПО ПОГОДЕ ЗАПУЩЕНА!ПОЛЬЗУЙТЕСЬ НА ЗДОРОВЬЕ!")
params = {
    "Mmn" : "",
    "lang": "ru"

}
gorod=input('ВВЕДИТЕ ВАШ ГОРОД ')
url = f"https://wttr.in/{gorod}"
response = requests.get(url, params=params)

response.raise_for_status()
saratovy=["саратов","САРАТОВ","Саратов"]
if gorod in saratovy :
    print ("чел. из него нельзя выбраться.....")
else:
    print(response.text)






