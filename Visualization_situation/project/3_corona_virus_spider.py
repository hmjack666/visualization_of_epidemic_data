import requests,re,json
from bs4 import BeautifulSoup
from tqdm import tqdm          #一个实现进度条的包

class CoronaVirusSpider(object):
    def __init__(self):
        self.home_url = 'https://ncov.dxy.cn/ncovh5/view/pneumonia'

    def get_content_from_url(self,url):
        '''
        根据url,获取相应的字符串数据
        :param url:      #请求的url
        :return: 相应内容的字符串
        '''
        response = requests.get(url)
        return response.content.decode()

    def parse_home_page(self,home_page,tag_id):
        '''
        解析首页内容，获取解析后的Python数据
        :param home_page: 首页的内容
        :return: 解析后的Python数据
        '''
        # 2. 从疫情首页中提取最近一日各国疫情字符串
        soup = BeautifulSoup(home_page, 'lxml')
        script = soup.find(id=tag_id)
        text = script.string
        # 3. 从最近一日各国疫情字符串中提取json格式字符串
        json_str = re.findall(r'\[.+\]', text)[0]
        # 4. 把json格式字符串，转换为python类型
        data = json.loads(json_str)
        return data

    def save(self,data,path):
        # 5. 把python类型的数据，以json格式存入文件中
        with open(path, 'w',encoding='utf8') as fp:
            json.dump(data, fp, ensure_ascii=False)  # ensure_ascii=False 不使用asci

    def crawl_last_day_corona_virus(self):
        '''
        采集最近一天的各国疫情细腻些
        :return:
        '''
        # 1. 发送请求， 获取首页内容
        home_page = self.get_content_from_url(self.home_url)
        # 2. 解析首页内容，获取最近一天的各国疫情信息
        last_day_corona_virus = self.parse_home_page(home_page,'getListByCountryTypeService2true')
        # 3. 保存数据
        self.save(last_day_corona_virus,'./data/last_day_corona_virus.json')

    def crawl_corona_virus(self):
        '''
        采集从01月23号以来各国疫情数据
        :return:
        '''
        # 1- 加载最近一日各国疫情数据
        with open('./data/last_day_corona_virus.json',encoding='utf8') as fp:
            last_day_corona_virus = json.load(fp)
        #定义列表，用于存储各国从1月23日以来疫情数据
        corona_virus = []
        # 2- 遍历各国疫情数据，获取从01月23日以来的各个国家疫情的URL
        for country in tqdm(last_day_corona_virus, '采集1月23日以来各国疫情信息'):  # tqdm是一个进度条
            # 3- 发送请求，获取从01月23日以来的各个国家疫情的json字符串
            statistics_data_url = country['statisticsData']
            statics_data_json_str = self.get_content_from_url(statistics_data_url)
            # 4- 解析各个国检疫情的json字符串，添加到列表
            # print(statics_data_json_str)
            statistics_data = json.loads(statics_data_json_str)["data"]  # 一个国家的每天的疫情信息
            for one_day in statistics_data:
                one_day['provinceName'] = country['provinceName']
                one_day['countryShortCode'] = country['countryShortCode']

            corona_virus.extend(statistics_data)  # 把元素存入列表
            # 5- 以json格式保存从01月23日以来的各个国家疫情数据
            self.save(corona_virus, './data/corona_virus.json')

    def crawl_last_day_corona_virus_of_china(self):
        '''
        采集最近一日各省疫情数据
        :return:
        '''
        # 1. 发送请求，获取疫情首页
        home_page = self.get_content_from_url(self.home_url)
        # 2. 解析疫情首页，获取最近一日各省疫情数据
        last_day_corona_virus_of_china = self.parse_home_page(home_page,tag_id='getAreaStat')
        # 3. 保存疫情数据
        self.save(last_day_corona_virus_of_china, './data/last_day_corona_virus_of_china.json')
        

    def run(self):
        self.crawl_last_day_corona_virus()
        # self.crawl_corona_virus()
        self.crawl_last_day_corona_virus_of_china()

if __name__ == '__main__':
    spider = CoronaVirusSpider()
    spider.run()





