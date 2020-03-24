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

    # 审批新闻
    def update_unreview_news(self, id):
        self.__news_dao.update_unreview_news(id)

    #查询新闻列表
    def search_list(self, page):
        result=self.__news_dao.search_list(page)
        return result

    # 查询新闻总页数
    def search_count_page(self):
        count_page=self.__news_dao.search_count_page()
        return count_page

    # 删除新闻
    def delete_by_id(self, id):
        self.__news_dao.delete_by_id(id)
