import requests,re,json
from bs4 import BeautifulSoup

# 1. 发送请求，获取疫情首页
response = requests.get('https://ncov.dxy.cn/ncovh5/view/pneumonia')
home_page = response.content.decode()

# 2. 从疫情首页中提取最近一日各国疫情字符串
soup = BeautifulSoup(home_page,'lxml')
script = soup.find(id = 'getListByCountryTypeService2true')
text = script.string

# 3. 从最近一日各国疫情字符串中提取json格式字符串
json_str = re.findall(r'\[.+\]',text)[0]
# 4. 把json格式字符串，转换为python类型
last_day_corona_virus = json.loads(json_str)
# 5. 把python类型的数据，以json格式存入文件中
with open('./data/last_day_corona_virus.json','w',encoding='utf8') as fp:
    json.dump(last_day_corona_virus,fp,ensure_ascii=False)           # ensure_ascii=False 不使用asci