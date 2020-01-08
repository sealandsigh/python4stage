# -*- coding: utf-8 -*-
# __author__="jiajun.zhu"
# DATE:2020/1/7

# 序列传参
def calc(a,b,c):
    return (a+b) *c

l = [1,5,10]
print(calc(*l))

# 字典传参

def health_check(name,age,*,height,weight,hr,hbp,lbp,glu):
    print("您的身体健康")

param = {"name":'zhujiajun',"age":23,"height":23,"weight":23,"hr":23,"hbp":23,"lbp":23,"glu":23}
health_check(**param)
health_check(**param)