# -*- coding: utf-8 -*-
# __author__="jiajun.zhu"
# DATE:2020/1/7

# 混合传参，*号后面必须使用关键参数
def health_check(name,age,*,height,weight,hr,hbp,lbp,glu):
    print("您的身体健康")

health_check('zhujiajun',23,height=33,weight=180,hr=11,hbp=12,lbp=13,glu=14)

