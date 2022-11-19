import requests
headers = {
    "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64; rv:99.0) Gecko/20100101 Firefox/99.0",
    "Accept-Language": "ru-RU,ru;q=0.8,en-US;q=0.5,en;q=0.3"
}
names=['Hulk','Captain America','Thanos']
result = {}
max_iq=0
name_genius=''
for surname in names:
    url='https://www.superheroapi.com/api/2619421814940190/search/'+surname
    resp = requests.get(url, headers=headers)
    d=resp.json()
    if int(d['results'][0]['powerstats']['intelligence'])>max_iq:
        max_iq=int(d['results'][0]['powerstats']['intelligence'])
        name_genius=d['results'][0]['name']
print(f'Самый умный, прости господи, супергерой - {name_genius} обладатель интеллекта в {max_iq} попугаев')
