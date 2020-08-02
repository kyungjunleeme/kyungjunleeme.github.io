import requests as rq
import pandas as pd
import urlib, json

BASE_URL = 'https://8oi9s0nnth.apigw.ntruss.com/corona19-masks/v1'
PATH = '/stores/json'
page = 1
perPage = 500 # max: 5000, min: 500, default: 500

result = {
    'addr': [],
    'code': [],
    'lat': [],
    'lng': [],
    'name': [],
    'type': [], # 0, 1, 2
}

while True:
    params = {
        'page': page,
        'perpage': perPage
    }

    res = rq.get(BASE_URL + PATH, params=params)
    
    json = res.json()
    cnt = json['count']
    stores = json['storeInfos']
    print(page)
    for store in stores:
        addr = store.get('addr', None)
        if addr:
            result['addr'].append(addr)
            result['code'].append(store['code'])
            result['lat'].append(store['lat'])
            result['lng'].append(store['lng'])
            result['name'].append(store['name'])
            result['type'].append(store['type'])
        
        if cnt != perPage:
            break

        page += 1
    
    df = pd.DataFrame(result)
    df.to_csv('stores_info.csv')
    print(page, '페이지 끝.')

    C:\\ProgramData\\Anaconda3\\Scripts\\activate.bat C:\\ProgramData\\Anaconda3