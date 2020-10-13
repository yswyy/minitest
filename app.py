import logging.handlers
import os


def log_conf():
    logpath = './log'

    logger = logging.getLogger()

    logger.setLevel(logging.INFO)

    sh = logging.StreamHandler()
    trfh = logging.handlers.TimedRotatingFileHandler(filename=logpath + os.sep + 'mini.log', when='midnight',
                                                     interval=1, backupCount=7, encoding='utf-8')

    f = '%(asctime)s %(levelname)s [%(name)s] [%(filename)s(%(funcName)s:%(lineno)d)] - %(message)s'

    formatter = logging.Formatter(f)

    sh.setFormatter(formatter)
    trfh.setFormatter(formatter)

    logger.addHandler(sh)
    logger.addHandler(trfh)


#  请求通用接口地址
base_url = "http://e.cn/api/v1"

# 微信code
code = "081KuIFa1PrFMz0WQuHa1ARdyy1KuIFn"

# 请求头
headers = {
    "Content-Type": "application/json",
    "token": "583ef5059724fa8977abb9c86afaaac5"
}
