import app, logging
import requests


class UserApi:

    def __init__(self):
        # 获取token
        self.get_token_url = app.base_url + "/token/user"
        # token验证
        self.token_verify_url = app.base_url + "/token/verify"
        # 用户地址信息
        self.user_addr_url = app.base_url + "/address"

    def get_token_api(self):
        """验证token"""

        data = {"code": app.code}
        logging.info("获取token")
        return requests.post(self.get_token_url, json=data, headers=app.headers)

    def verify_token_api(self):
        data = {"token": app.headers.get("token")}
        logging.info("验证token")
        return requests.post(self.token_verify_url, json=data, headers=app.headers)

    def user_addr_api(self):
        logging.info("用户地址信息")
        return requests.get(self.user_addr_url, headers=app.headers)
