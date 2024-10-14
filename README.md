# SZTU-getLabQbank
深技大实验室测试题库爬取Python小脚本
### 0.前言 💭（图片显示不出来的请使用VPN）
《关于两次模拟考试把试题都喂给ChatGPT-4o但是连80分都没有这件事》
![对称加密算法使用同一个密钥进行加解密](https://github.com/MessyMidi/SZTU-getLabQbank/blob/main/img/%E5%B1%8F%E5%B9%95%E6%88%AA%E5%9B%BE%202024-10-13%20101517.png)
对称加密算法使用同一个密钥进行加解密

![哦 贵校每人配发一台有公网ip的服务器](https://github.com/MessyMidi/SZTU-getLabQbank/blob/main/img/%E5%B1%8F%E5%B9%95%E6%88%AA%E5%9B%BE%202024-10-13%20102228.png)
哦 贵校每人配发一台有公网ip的服务器

![](https://github.com/MessyMidi/SZTU-getLabQbank/blob/main/img/%E5%B1%8F%E5%B9%95%E6%88%AA%E5%9B%BE%202024-10-13%20102029.png)
![](https://github.com/MessyMidi/SZTU-getLabQbank/blob/main/img/%E5%B1%8F%E5%B9%95%E6%88%AA%E5%9B%BE%202024-10-13%20102047.png)



以上并非个别现象 而且贵校似乎并不打算更新题库 要通过考试似乎就只能死记（甚至错误答案也要记）故出此下策

### 1.环境配置 🛠️
需要安装Selenium库以及ChromeDriver

①安装Selenium库
```
pip install selenium
```
②下载ChromeDriver
https://developer.chrome.com/docs/chromedriver/downloads?hl=zh-cn

### 2.使用前✏️
替换/pathtochromedriver为你的ChromeDriver路径
爬取到的题目默认输出到脚本所在目录 如有需要 可在`output_file =`中手动指定输出目录

### 3.使用😉
爬取前需要自行输入题库id 找到你要爬取的题库页面 复制地址栏中`tikubh=`后面的数字（比如1111）粘贴回车即可
由于~~时效性以及~~某些因素 我不能直接给出已经爬取的题库 但`你应该会用吧？`


### 4.画饼🥞
- 批量爬取
- GUI界面
