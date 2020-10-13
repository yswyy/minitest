from Api.apifactory import Apifactory


# print("轮播图{}".format(Apifactory.get_home_api().banner_api().json()))
#
# print("专题栏{}".format(Apifactory.get_home_api().theme_api().json()))
#
# print("最近新品{}".format(Apifactory.get_home_api().recent_product_api().json()))

#
# print("商品分类{}".format(Apifactory.get_product_api().product_classify_api().json()))
#
# print("分类下商品{}".format(Apifactory.get_product_api().classify_product_api().json()))
#
# print("商品详情{}".format(Apifactory.get_product_api().product_datail_api().json()))

# print("token{}".format(Apifactory.get_user_api().get_token_api().json()))

print("订单列表{}".format(Apifactory.get_order_api().order_list_api().json()))
print("创建订单{}".format(Apifactory.get_order_api().create_order_api(19, 7).json()))
print("查看订单详情{}".format(Apifactory.get_order_api().query_order_api(71).json()))
