import requests
import datetime as DT
import pprint

archive_depth = DT.datetime.today() - DT.timedelta(days=2)
# print(archive_depth)
base_host = 'https://api.stackexchange.com/'

uri_requests = '/search'
requests_url = base_host + uri_requests
params = {'tagged': 'Python', 'sort': 'creation', 'order': 'desc', 'pagesize': 20,
          'fromdate': archive_depth.strftime(''), 'todate': DT.datetime.today().strftime(''), 'site': 'stackoverflow'}
response = requests.get(requests_url, params=params)
print(response.status_code)
dict_my = response.json()
# from pprint import pprint
# pprint(dict_my)
count = 0
list_my = dict_my['items']
# pprint(list_my)
for item in list_my:
    print(item['title'])
    count += 1
print(count)
