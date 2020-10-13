import app, logging
import requests


class HomeApi:
    """首页接口封装方法"""

    def __init__(self):
        # 轮播图地址
        self.banner_url = app.base_url + '/banner/{}'
        # 专题栏地址
        self.theme_url = app.base_url + '/theme'
        # 最近新品
        self.recent_url = app.base_url + '/product/recent'

    def banner_api(self, num=1):
        """
        请求轮播图
        :param num: 轮播同页面数
        :return: 响应对象
        """
        logging.info("请求首页——轮播图")
        return requests.get(self.banner_url.format(num))

    def theme_api(self, ids="1,2,3"):
        """
        专题栏
        :param ids:专题栏数据
        :return:
        """
        logging.info("请求首页--专题栏")
        data = {"ids": ids}
        return requests.get(self.theme_url, params=data)

    def recent_product_api(self):
        """最近新品"""
        logging.info("请求首页--最近新品")
        return requests.get(self.recent_url)

