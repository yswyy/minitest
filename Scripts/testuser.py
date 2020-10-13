import logging

from Api.apifactory import Apifactory
import app
import utils
import pytest


@pytest.mark.run(order=0)
class TestUserApi:

    def test_get_token(self):
        """获取token"""
        res = Apifactory.get_user_api().get_token_api()
        logging.info("请求地址{}".format(res.url))
        logging.info("响应数据{}".format(res.json()))
        utils.common_assert_code(res)

        assert len(res.json().get("token")) > 0
        app.headers["token"] = res.json().get("token")
        print("headers", app.headers)

    def test_verify_token_api(self):
        """验证token"""
        res = Apifactory.get_user_api().verify_token_api()
        logging.info("请求地址{}".format(res.url))
        logging.info("响应数据{}".format(res.json()))
        utils.common_assert_code(res)

        assert res.json().get("isValid") is True

    def test_user_addr_api(self):
        res = Apifactory.get_user_api().user_addr_api()
        logging.info("请求地址{}".format(res.url))
        logging.info("响应数据{}".format(res.json()))
        utils.common_assert_code(res)
        assert False not in [i in res.text for i in ["司马狗剩", "13866666666", "上海市", "浦东新区", "110号"]]
