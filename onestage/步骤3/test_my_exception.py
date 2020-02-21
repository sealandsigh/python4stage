# -*- coding: utf-8 -*-
# __author__="jiajun.zhu"
# DATE:2020/2/21

class ApiException(Exception):
    """我的自定义异常"""
    err_code = ''
    err_msg = ''

    def __init__(self,err_code=None, err_msg=None):
        """

        :param err_code:
        :param err_msg:
        """
        self.err_code = self.err_code if self.err_code else err_code
        self.err_msg = self.err_msg if self.err_msg else err_msg

    def __str__(self):
        return "Error: {0} - {1}".format(self.err_code,self.err_msg)


class InvalidCtrExec(ApiException):
    """当参数不合法时候触发
    40001 invalid credentinal 不合法的地阿偶欧诺个凭证
    """
    err_code = '40001'
    err_msg = '不合法的参数'


def div(num1,num2):
    """除法的实现"""
    if not isinstance(num2,int) or not isinstance(num1,int):
        raise InvalidCtrExec()
    # 除数不能为0
    if num2 == 0:
        raise ApiException("4000000","整数不能为0")


if __name__ == "__main__":

    try:
        rest = div(5,"s")
        print(rest)
    except InvalidCtrExec as err:
        print("test")
        print(err)
    except ApiException as err:
        print("出错了")
        print(err)