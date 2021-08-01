from flask import Flask, render_template
import csv
import codecs

web = Flask(__name__)

# 首页
@web.route('/')
def index():
    return render_template('index.html')

# 疫情可视化动画展示模块
@web.route('/movie')
def movie_list():
    movies = [{'file':'top10省现有确诊病例对比.mp4','title':'Top10省现有确诊病例对比'},
              {'file':'Top15国现有确诊病例对比.mp4','title':'Top15国现有确诊病例对比'}]
    return render_template('movie.html',movies=movies)

# 中国新冠疫情实时数据地图模块
@web.route('/map')
def map():
    return render_template('map.html')

# 今日发生疫情省份统计模块
@web.route('/pie')
def pie():
    with codecs.open(filename='../data/china_data.csv', mode='r', encoding='utf-8') as f:
        reader = csv.reader(f)
        head = next(reader)

        today_confirm1 = {}
        today_confirm2 = []
        for item in reader:
            args = tuple(item)
            today_confirm1.update({args[2]: args[3]})

        for key, value in today_confirm1.items():
            if (value != '0'):
                # today_confirm2.append({key: value})
                today_confirm2.append({'name': key, 'value': value})

        print(today_confirm2)

    return render_template('pie.html',today_confirm=today_confirm2)

# 各省累计确诊排名模块
@web.route('/rank')
def	rank():
    with codecs.open('../data/china_data.csv', mode='r', encoding='utf-8') as f:
        reader = csv.reader(f)
        head = next(reader)

        province_name = []
        province_confirm = []
        for item in reader:
            args = tuple(item)
            # print(args)
            province_name.append(args[2])
            province_confirm.append(args[9])
        print(province_name)
        print(province_confirm)

    return render_template('rank.html', province_name=province_name,province_confirm=province_confirm)

web.run(debug=True)
