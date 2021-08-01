 项目已发布博客于CSDN上，博客中涵盖了更多内容，若需要了解得更多，可以访问博客链接: [基于flask框架的新冠疫情数据可视化系统](https://blog.csdn.net/m0_46991388/article/details/119301870)。

# 基于flask框架的新冠疫情数据可视化系统

新冠疫情数据可视化系统是本学期大数据可视化这门课的结课作业，本系统有四个模块的功能，涵盖有视频播放、疫情情况中国地图分布、Echarts饼状图和树状图等，应用Python爬虫、Flask框架、Echarts等技术实现 。

#### 一、系统概述
系统开发环境：

1) 关键技术:1、Python爬虫；Flask框架；Echarts。

2) 实验平台:1、Window 10；2、PyCharm (2019.1)；3、Jupyter。

功能模块设计：

共五个模块:1、导航栏；2、疫情可视化动画展示模块；3、中国新冠疫情实时数据地图模块；4、各省累计确诊排名模块；5、今日发生疫情省份统计模块。

##### 项目结构说明
<img src="https://img-blog.csdnimg.cn/26213c0534e74e90b5a9c91a2dda85a1.png?x-oss-process=image/watermark,type_ZmFuZ3poZW5naGVpdGk,shadow_10,text_aHR0cHM6Ly9ibG9nLmNzZG4ubmV0L20wXzQ2OTkxMzg4,size_16,color_FFFFFF,t_70#pic_center" alt="项目结构说明" style="zoom: 67%;" />

#### 二、项目启动方法：
##### 1、启动项目前需要导入的依赖
<img src="https://img-blog.csdnimg.cn/4702c9c08ce0413a88e66f075e4fe204.png#pic_center" alt="启动项目前需要导入的依赖" style="zoom: 80%;" />
安装 Flask

```
pip install Flask
```
报错:
Could not find a version that satisfies the requirement Flask (from versions: )
No matching distribution found for Flask
这是因为网络的问题，需要使用国内的镜像源来加速,比如豆瓣源
```
pip install flask -i http://pypi.douban.com/simple/ --trusted-host pypi.douban.com
```
##### 2、进入到启动类所在目录
<img src="https://img-blog.csdnimg.cn/cf5b08183f204ed3b7ba6ccbcaa05001.png?x-oss-process=image/watermark,type_ZmFuZ3poZW5naGVpdGk,shadow_10,text_aHR0cHM6Ly9ibG9nLmNzZG4ubmV0L20wXzQ2OTkxMzg4,size_16,color_FFFFFF,t_70#pic_center" alt="进入到启动类所在目录" style="zoom:67%;" />

##### 3、在启动类所在目录启动cmd
<img src="https://img-blog.csdnimg.cn/16ca772d4068449e99209e4230049168.png?x-oss-process=image/watermark,type_ZmFuZ3poZW5naGVpdGk,shadow_10,text_aHR0cHM6Ly9ibG9nLmNzZG4ubmV0L20wXzQ2OTkxMzg4,size_16,color_FFFFFF,t_70#pic_center" alt="在启动类所在目录启动cmd" style="zoom: 67%;" />

##### 4、进入cmd中
![进入cmd中](https://img-blog.csdnimg.cn/c1ae0e6dee37411191664e2cb0cb66c8.png?x-oss-process=image/watermark,type_ZmFuZ3poZW5naGVpdGk,shadow_10,text_aHR0cHM6Ly9ibG9nLmNzZG4ubmV0L20wXzQ2OTkxMzg4,size_16,color_FFFFFF,t_70#pic_center)
##### 接下来是启动flask框架
##### 1、启动flask框架步骤1
![启动flask框架步骤1](https://img-blog.csdnimg.cn/48cd455d5c9e485fbae79be8901074eb.png?x-oss-process=image/watermark,type_ZmFuZ3poZW5naGVpdGk,shadow_10,text_aHR0cHM6Ly9ibG9nLmNzZG4ubmV0L20wXzQ2OTkxMzg4,size_16,color_FFFFFF,t_70#pic_center)

```
set FLASK_APP=app.py
```

##### 2、启动flask框架步骤2
![启动flask框架步骤2](https://img-blog.csdnimg.cn/ad4761409b264c7e935ecdcda58bc290.png?x-oss-process=image/watermark,type_ZmFuZ3poZW5naGVpdGk,shadow_10,text_aHR0cHM6Ly9ibG9nLmNzZG4ubmV0L20wXzQ2OTkxMzg4,size_16,color_FFFFFF,t_70#pic_center)

```
python -m flask run
```

##### 启动flask后看到的项目效果
![启动flask后看到的项目效果](https://img-blog.csdnimg.cn/bd802bb52fd84fcca46ab92e8b545637.png?x-oss-process=image/watermark,type_ZmFuZ3poZW5naGVpdGk,shadow_10,text_aHR0cHM6Ly9ibG9nLmNzZG4ubmV0L20wXzQ2OTkxMzg4,size_16,color_FFFFFF,t_70#pic_center)

#### 三、系统实现的效果：

疫情可视化动画展示模块
![疫情可视化动画展示模块](https://img-blog.csdnimg.cn/de454f76db854b2fa653f092d8678bb7.png?x-oss-process=image/watermark,type_ZmFuZ3poZW5naGVpdGk,shadow_10,text_aHR0cHM6Ly9ibG9nLmNzZG4ubmV0L20wXzQ2OTkxMzg4,size_16,color_FFFFFF,t_70#pic_center)
![视频播放](https://img-blog.csdnimg.cn/90e42e25ca404ceea678ee752fed6318.png?x-oss-process=image/watermark,type_ZmFuZ3poZW5naGVpdGk,shadow_10,text_aHR0cHM6Ly9ibG9nLmNzZG4ubmV0L20wXzQ2OTkxMzg4,size_16,color_FFFFFF,t_70#pic_center)
中国新冠疫情实时数据地图模块
![中国新冠疫情实时数据地图模块](https://img-blog.csdnimg.cn/9ed4838461ff4ff3b5f832b47504907e.png?x-oss-process=image/watermark,type_ZmFuZ3poZW5naGVpdGk,shadow_10,text_aHR0cHM6Ly9ibG9nLmNzZG4ubmV0L20wXzQ2OTkxMzg4,size_16,color_FFFFFF,t_70#pic_center)
![新冠疫情数据地图](https://img-blog.csdnimg.cn/9aadfc18d14848d084f2598042c63ff6.png?x-oss-process=image/watermark,type_ZmFuZ3poZW5naGVpdGk,shadow_10,text_aHR0cHM6Ly9ibG9nLmNzZG4ubmV0L20wXzQ2OTkxMzg4,size_16,color_FFFFFF,t_70#pic_center)
各省累计确诊排名模块
![各省累计确诊排名模块](https://img-blog.csdnimg.cn/36e1884cefb54d32986dea37f076397a.png?x-oss-process=image/watermark,type_ZmFuZ3poZW5naGVpdGk,shadow_10,text_aHR0cHM6Ly9ibG9nLmNzZG4ubmV0L20wXzQ2OTkxMzg4,size_16,color_FFFFFF,t_70#pic_center)
![各省累计确诊排名](https://img-blog.csdnimg.cn/b78f2b1dca8a4f8ca37bee81d7db6067.png?x-oss-process=image/watermark,type_ZmFuZ3poZW5naGVpdGk,shadow_10,text_aHR0cHM6Ly9ibG9nLmNzZG4ubmV0L20wXzQ2OTkxMzg4,size_16,color_FFFFFF,t_70#pic_center)
今日发生疫情省份统计模块
![今日发生疫情省份统计模块](https://img-blog.csdnimg.cn/9c7898e5af5d4faf8a5452d47c844ddc.png?x-oss-process=image/watermark,type_ZmFuZ3poZW5naGVpdGk,shadow_10,text_aHR0cHM6Ly9ibG9nLmNzZG4ubmV0L20wXzQ2OTkxMzg4,size_16,color_FFFFFF,t_70#pic_center)
![今日发生疫情省份统计](https://img-blog.csdnimg.cn/655d1a231bd04132bd6e878037485b90.png?x-oss-process=image/watermark,type_ZmFuZ3poZW5naGVpdGk,shadow_10,text_aHR0cHM6Ly9ibG9nLmNzZG4ubmV0L20wXzQ2OTkxMzg4,size_16,color_FFFFFF,t_70#pic_center)