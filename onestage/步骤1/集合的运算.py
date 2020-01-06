# -*- coding: utf-8 -*-
# __author__="jiajun.zhu"
# DATE:2020/1/6

college1 = {'哲学','经济学','法学','教育学'}
college2 = set(['金融学','哲学','经济学','历史学','文学'])

# 交集
c3 = college1.intersection(college2)
print(c3)
# 把交集的结果赋给college1
college1.intersection_update(college2)
print(college1)

# 并集
college1 = {'哲学','经济学','法学','教育学'}
college2 = set(['金融学','哲学','经济学','历史学','文学'])

c4 = college1.union(college2)
print(c4)

# 差集 是指两个集合之间差异的部分
# difference 代表得到A在B集合中不存在的部分

c5 = college1.difference(college2)
print(c5)
c6 = college2.difference(college1)
print(c6)
c7 = college1.symmetric_difference(college2)
print(c7)

