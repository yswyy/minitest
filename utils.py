def common_assert_code(res, code=200):
    """
    对状态码进行断言
    :param res:
    :param code:
    :return:
    """

    assert res.status_code == code
