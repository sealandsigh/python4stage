# -*- coding: utf-8 -*-
# __author__="jiajun.zhu"
# DATE:2020/2/26

import re

def test_group():
    content = "hello,world!"
    p = re.compile(r"world")
    rest = p.search(content)
    print(rest)
    if rest:
        # group 的使用
        print(rest.group())
        # groups 的使用
        print(rest.groups())


def test_id_card():
    """身份证号码正则匹配"""
    p = re.compile(r"(\d{6})(?P<year>\d{4})((\d{2})(\d{2}))\d{2}\d{1}([0-9]|X)")
    # 准备两个正确的身份证号码
    id1 = "110105199909226451"
    id2 = "110105199909226452"
    rest1 = p.search(id1)
    print(rest1.group(1))

    # groups
    id1_rest = rest1.groups()
    print(id1_rest[1])
    print(rest1.groupdict())


if __name__ == "__main__":
    test_group()
    test_id_card()