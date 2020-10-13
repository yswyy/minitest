import logging

import utils
from Api.apifactory import Apifactory


class TestPorductApi:

    def test_product_classify_api(self):
        """商品分类"""
        res = Apifactory.get_product_api().product_classify_api()
        logging.info("请求地址{}".format(res.url))
        logging.info("响应数据{}".format(res.json()))
        utils.common_assert_code(res)

        assert len(res.json()) > 0

        assert "id" in res.text and "name" in res.text and "topic_img_id" in res.text

    def test_classify_product_api(self):
        """分类下商品"""
        res = Apifactory.get_product_api().classify_product_api()
        logging.info("请求地址{}".format(res.url))
        logging.info("响应数据{}".format(res.json()))
        utils.common_assert_code(res)

        assert len(res.json()) > 0
        assert False not in [i in res.text for i in ["id", "name", "price", "stock"]]

    def test_product_datail_api(self):
        """商品信息"""
        res = Apifactory.get_product_api().product_datail_api()
        logging.info("请求地址{}".format(res.url))
        logging.info("响应数据{}".format(res.json()))
        utils.common_assert_code(res)
        assert res.json().get("id") == 2
        assert res.json().get("price") == '0.01'
        assert res.json().get("name") == '梨花带雨 3个'
