import logging

import utils
from Api.apifactory import Apifactory


class TestHomeApi:

    def test_home_api(self):
        """轮播图"""
        res = Apifactory.get_home_api().banner_api()
        logging.info("请求地址{}".format(res.url))
        logging.info("响应数据{}".format(res.json()))
        # 断言状态码
        utils.common_assert_code(res)

        # 断言items列表长度大于0
        assert len(res.json().get("items")) > 0

    def test_theme_api(self):
        """专题栏"""
        res = Apifactory.get_home_api().theme_api()
        logging.info("请求地址{}".format(res.url))
        logging.info("响应数据{}".format(res.json()))
        # 断言状态码
        utils.common_assert_code(res)
        # 断言id
        assert False not in [i in res.text for i in ['id":1', 'id":2', 'id":3']]
        # 断言关键字段name description topic_img head_img
        assert False not in [i in res.text for i in ["name", "description", "topic_img", "head_img"]]

    def test_product_api(self):
        """最近新品"""
        res = Apifactory.get_home_api().recent_product_api()
        logging.info("请求地址{}".format(res.url))
        logging.info("响应数据{}".format(res.json()))
        # 断言状态码
        utils.common_assert_code(res)
        # 断言新品数量大于0
        assert len(res.json()) > 0
        # 断言关键字段 id name price
        assert "id" in res.text and "name" in res.text and "price" in res.text
