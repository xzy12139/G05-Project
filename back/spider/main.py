import re
import urllib.error
import urllib.request
import xlwt

from bs4 import BeautifulSoup


def main():
    # 简单查一下灸法这个页面的相关信息
    baseurl = "http://www.pharmnet.com.cn/tcm/jf/"
    datalist = getData(baseurl)
    print(datalist)
    # savepath = "艾灸1.xls"
    # saveData(savepath, datalist)


# 全局变量，用于正则判断规则（字符串模式）
# r：忽视特殊符号
# ''：忽视双引号
findLink = re.compile(r'<a href="http://www.pharmnet.com.cn/tcm/jf/(.*?)/" title="(.*?)">.*?</a>', re.S)
findContext = re.compile(r'<div align="left">(.*?)</div>')
findName = re.compile(r'<strong>(.*?)</strong>')
findImgSrc = re.compile(r'<div align="left">.*', re.S)

findString = re.compile(r'<a href="(.*)>')


def getData(baseurl):
    datalist = []
    url = baseurl
    html = askURL(url)
    if html == "":
        return;
    # 一个写的屎一样的获取脚本
    soup = BeautifulSoup(html, "html.parser", fromEncoding="gb18030")
    list = soup.find_all('a')
    for item in list:
        data = []
        item = str(item)
        try:
            item = re.findall(findLink, item)[0]
        except IndexError:
            continue
        data.append(item[1])
        html = askURL(url + str(item[0]))
        if html == "":
            return;
        soup = BeautifulSoup(html, "html.parser", fromEncoding="gb18030")
        sublist = soup.find_all('div', align='left');
        for subItem in sublist:
            subItem = str(subItem)
            subItem = re.findall(findContext, subItem)[0]
            subItem = re.sub(r'\s', "", subItem)
            subItem = re.sub(r'<b></b>', "", subItem)
            subItem = re.sub(r'<br(\s+)?/>(\s+)?', "", subItem)
            data.append(subItem)
        # 这里得到了item[1]为name， subItem为内容
        datalist.append(data)
    return datalist


def saveData(savepath, datalist):
    workbook = xlwt.Workbook(encoding="utf-8", style_compression=0)
    worksheet = workbook.add_sheet('基本信息', cell_overwrite_ok=True)
    col = ("名称", "介绍")
    for i in range(0, 2):
        worksheet.write(0, i, col[i]);
    i = 0
    for data in datalist:
        i = i+1
        for j in range(0, 2):
            try:
                worksheet.write(i, j, data[j])
            except IndexError:
                continue


    workbook.save(savepath)
    return 0


def askURL(url):
    # 网站请求
    head = {
        "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/103.0.0.0 Safari/537.36"
    }
    request = urllib.request.Request(url, headers=head)
    html = ""
    try:
        response = urllib.request.urlopen(request)
        html = response.read()
    except urllib.error.URLError as e:
        if hasattr(e, "code"):
            return ""
        if hasattr(e, "reason"):
            return ""
    return html


if __name__ == "__main__":
    main()
