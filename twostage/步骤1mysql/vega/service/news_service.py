# -*- coding: utf-8 -*-
# __author__="jiajun.zhu"
# DATE:2020/3/24

from db.news_dao import NewsDao

class NewsService(object):
    __news_dao=NewsDao()

    def search_unreview_list(self,page):
        result = self.__news_dao.search_unreview_list(page)
        return result

    # 查询待审批的总页数
    def search_unreview_count_page(self):
        count_page = self.__news_dao.search_unreview_count_page()
        return  count_page