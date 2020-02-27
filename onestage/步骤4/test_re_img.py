# -*- coding: utf-8 -*-
# __author__="jiajun.zhu"
# DATE:2020/2/27

import re

def test_re_img():
    """使用正则表达式找到图片地址"""
    # 读取文本内容
    with open("img.html","r") as f:
        html = f.read()
        p = re.compile(r"<img.+?src=\"(.+?)\".+?>")
        list_img = p.findall(html)
        print(len(list_img))
        for i in list_img:
            print(i.replace("&amp;","&"))
        #TODO 使用urllib，requests将图片保存




if __name__ == "__main__":
    test_re_img()