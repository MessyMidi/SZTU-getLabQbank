# SZTU-getLabQbank
深技大实验室测试题库爬取Python小脚本
### 0.前言 💭
《关于两次模拟考试把试题都喂给ChatGPT-4o但是连80分都没有这件事》

↑参考答案错误

↑题目定义不明导致两个答案均可
并非个别现象 而且贵校似乎并不打算更新题库 要通过考试似乎就只能死记（甚至错误答案也要记）故出此下策

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

### 3.使用😉
爬取前需要自行输入题库id 找到你要爬取的题库页面 复制地址栏中`tikubh=`后面的数字（比如1111）粘贴进命令行回车即可
由于~~时效性以及~~某些因素 我不能直接给出已经爬取的题库 但`你应该会用吧？`

题库会直接输出到命令行 自行复制粘贴即可

### 4.画饼🥞
- 爬取完成后自动输出到txt
- 批量爬取
- GUI界面
