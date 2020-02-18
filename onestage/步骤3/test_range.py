# -*- coding: utf-8 -*-
# __author__="jiajun.zhu"
# DATE:2020/2/18

def use_range():
    for i in range(5,10):
        print(i)


class IterRange(object):
    """使用迭代器来模拟range函数"""

    def __init__(self,start,end):
        self.start = start - 1
        self.end = end

    def __next__(self):
        self.start += 1
        if self.start >= self.end:
            raise StopIteration
        return self.start

    def __iter__(self):
        return self


class GenRange(object):
    def __init__(self,start,end):
        self.start = start - 1
        self.end = end

    def get_num(self):
        while True:
            if self.start >= 9:
                break
            self.start += 1
            yield self.start



if __name__ == "__main__":
    use_range()
    print("---------------------")
    iter = IterRange(5,10)
    # print(next(iter))
    # print(next(iter))
    # print(next(iter))
    # print(next(iter))
    # print(next(iter))
    l = list(iter)
    print(l)
    print("========================")
    gen = GenRange(5,10).get_num()
    # print(next(gen))
    # print(next(gen))
    # print(next(gen))
    # print(next(gen))
    # print(next(gen))
    l = list(gen)
    print(l)
