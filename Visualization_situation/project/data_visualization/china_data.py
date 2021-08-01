import pandas as pd
import requests
headers={
    'user-agent':'Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/88.0.4324.182 Safari/537.36'
}
url='https://c.m.163.com/ug/api/wuhan/app/data/list-total?'
res=requests.get(url,headers=headers)
import json
data_json=json.loads(res.text)
data=data_json['data']
data_province=data['areaTree'][2]['children']
print(data_province)
free_data=pd.DataFrame(data_province)[['id','lastUpdateTime','name']]
today_data=pd.DataFrame([province['today'] for province in data_province])
total_data=pd.DataFrame([province['total'] for province in data_province])
today_data.columns=("today_"+i for i in today_data.columns)
total_data.columns=("total_"+i for i in total_data.columns)
China_data=pd.concat([free_data,today_data,total_data],axis=1)

print(China_data)
file_name='../data/china_data'+'.csv'
China_data.to_csv(file_name,index=None,encoding='utf_8_sig')
print("中国的各省疫情数据保存成功啦！")