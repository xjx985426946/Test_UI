import time
import pytest
from Common import common
from TestDatas.C_web import product_detail_data
import logging
# from PageObject.C_phone.pcenter_page import PcenterPage
from PageObject.C_web.product_detail_page import ProductDetailPage

@pytest.mark.usefixtures("web_page")
@pytest.mark.domes
@pytest.mark.production
class TestProductDetail:

    # 成功登录
    @pytest.mark.smoke
    @pytest.mark.parametrize("data", product_detail_data.login_success)
    def test_login_success(self, data, web_page):
        '''登录页面-商品详情跳转'''
        time.sleep(2)
        # 步骤 跳转商品详情
        ProductDetailPage(web_page).login_product_detail(data['username'], data['code'])

        logging.info("开始断言")
        time.sleep(3)

        # 验证-检查点
        try:
            assert ProductDetailPage(web_page).check_product_detail() == data['check']
            logging.info("登录成功-商品详情跳转成功")
        except:
            print("登录成功-商品详情跳转失败")
            common.save_screenShot(web_page, model_name="登录页面-商品详情跳转")
            raise

    @pytest.mark.smoke
    @pytest.mark.parametrize("data", product_detail_data.product_like_success)
    def test_product_like(self, data, web_page):
        '''商品详情-我的喜欢'''
        # 步骤 跳转商品详情
        ProductDetailPage(web_page).login_product_detail(data['username'], data['code'])
        # 商品详情-点击我的喜欢
        time.sleep(2)
        ProductDetailPage(web_page).my_like()

        logging.info("开始断言")
        time.sleep(2)

        try:
            assert ProductDetailPage(web_page).check_msg() == data['check']
            logging.info("断言成功")

        except:
            print("断言失败")
            print("商品详情-我的喜欢失败")
            common.save_screenShot(web_page, model_name="商品详情-我的喜欢")
            raise

    @pytest.mark.smoke
    @pytest.mark.parametrize("data", product_detail_data.product_unlike_success)
    def test_product_unlike(self, data, web_page):
        '''商品详情-我的喜欢-二次点击'''
        # 步骤 跳转商品详情
        ProductDetailPage(web_page).login_product_detail(data['username'], data['code'])
        # 商品详情-点击我的喜欢
        time.sleep(2)
        ProductDetailPage(web_page).my_like()

        logging.info("开始断言")
        time.sleep(2)

        try:
            assert ProductDetailPage(web_page).check_msg() == data['check']
            logging.info("断言成功")

        except:
            print("断言失败")
            print("商品详情-我的喜欢-二次点击失败")
            common.save_screenShot(web_page, model_name="商品详情-我的喜欢-二次点击")
            raise

    @pytest.mark.smoke
    @pytest.mark.parametrize("data", product_detail_data.product_coupon_success)
    def test_product_coupon(self, data, web_page):
        '''商品详情-立即领取-领取优惠券'''
        # 步骤 跳转商品详情
        ProductDetailPage(web_page).login_product_detail(data['username'], data['code'])
        # 商品详情-点击立即领取-领取优惠券
        time.sleep(2)
        ProductDetailPage(web_page).get_coupon()

        logging.info("开始断言")
        time.sleep(2)

        try:
            assert ProductDetailPage(web_page).check_msg() == data['check']
            logging.info("断言成功")

        except:
            print("断言失败")
            print("商品详情-立即领取-领取优惠券")
            common.save_screenShot(web_page, model_name="商品详情-立即领取-领取优惠券")
            raise

    @pytest.mark.smoke
    @pytest.mark.parametrize("data", product_detail_data.report)
    def test_product_report(self, data, web_page):
        '''商品详情-举报页面跳转'''
        # 步骤 跳转商品详情
        ProductDetailPage(web_page).login_product_detail(data['username'], data['code'])
        # 商品详情-点击举报
        time.sleep(2)
        ProductDetailPage(web_page).report()

        logging.info("开始断言")
        time.sleep(2)

        try:
            assert ProductDetailPage(web_page).check_report() == data['check']
            logging.info("断言成功")

        except:
            print("断言失败")
            print("商品详情-举报页面跳转失败")
            common.save_screenShot(web_page, model_name="商品详情-举报页面跳转")
            raise

    @pytest.mark.smoke
    @pytest.mark.parametrize("data", product_detail_data.report_help)
    def test_product_report_help(self, data, web_page):
        '''商品详情-举报帮助页面跳转'''
        # 步骤 跳转商品详情
        ProductDetailPage(web_page).login_product_detail(data['username'], data['code'])
        # 商品详情-点击举报
        time.sleep(2)
        ProductDetailPage(web_page).report()
        # 商品详情-点击举报
        time.sleep(2)
        ProductDetailPage(web_page).report_help()

        logging.info("开始断言")
        time.sleep(2)

        try:
            assert ProductDetailPage(web_page).check_report_help() == data['check']
            logging.info("断言成功")

        except:
            print("断言失败")
            print("商品详情-举报帮助页面跳转失败")
            common.save_screenShot(web_page, model_name="商品详情-举报帮助页面跳转")
            raise

    @pytest.mark.smoke
    @pytest.mark.parametrize("data", product_detail_data.report_err)
    def test_product_report_err(self, data, web_page):
        '''商品详情-举报错误-请选择举报类型'''
        # 步骤 跳转商品详情
        ProductDetailPage(web_page).login_product_detail(data['username'], data['code'])
        # 商品详情-点击举报
        time.sleep(2)
        ProductDetailPage(web_page).report()
        # 点击提交
        time.sleep(2)
        ProductDetailPage(web_page).report_success(data['report_msg'])

        logging.info("开始断言")
        time.sleep(2)

        try:
            assert ProductDetailPage(web_page).check_toast() == data['check']
            logging.info("断言成功")

        except:
            print("断言失败")
            print("商品详情-举报失败")
            common.save_screenShot(web_page, model_name="商品详情-举报跳转")
            raise

    @pytest.mark.smoke
    @pytest.mark.parametrize("data", product_detail_data.report_msg)
    def test_product_report_success(self, data, web_page):
        '''商品详情-举报-错误：举报内容不少于20字/举报成功'''
        # 步骤 跳转商品详情
        ProductDetailPage(web_page).login_product_detail(data['username'], data['code'])
        # 商品详情-点击举报
        time.sleep(2)
        ProductDetailPage(web_page).report()
        # 选择举报类型
        time.sleep(2)
        ProductDetailPage(web_page).report_type()
        # 点击提交
        time.sleep(1)
        ProductDetailPage(web_page).report_success(data['report_msg'])

        logging.info("开始断言")
        time.sleep(2)

        try:
            assert ProductDetailPage(web_page).check_toast() == data['check']
            logging.info("断言成功")

        except:
            print("断言失败")
            print("商品详情-举报失败")
            common.save_screenShot(web_page, model_name="商品详情-举报")
            raise

    @pytest.mark.smoke
    @pytest.mark.parametrize("data", product_detail_data.product_buying_err)
    def test_product_buying(self, data, web_page):
        '''商品详情-无规格-立即购买'''
        # 步骤 跳转商品详情
        ProductDetailPage(web_page).login_product_detail(data['username'], data['code'])
        # 商品详情-无规格-立即购买
        time.sleep(2)
        ProductDetailPage(web_page).buying()

        logging.info("开始断言")
        time.sleep(2)

        try:
            assert ProductDetailPage(web_page).check_msg() == data['check']
            logging.info("断言成功")

        except:
            print("断言失败")
            print("商品详情-无规格-立即购买失败")
            common.save_screenShot(web_page, model_name="商品详情-无规格-立即购买")
            raise

    @pytest.mark.smoke
    @pytest.mark.parametrize("data", product_detail_data.product_settle)
    def test_product_settle(self, data, web_page):
        '''商品详情-立即购买-确认订单页面跳转'''
        # 步骤 跳转商品详情
        ProductDetailPage(web_page).login_product_detail(data['username'], data['code'])
        # 商品详情-选择规格
        time.sleep(3)
        ProductDetailPage(web_page).standards()
        # 商品详情-立即购买
        time.sleep(1)
        ProductDetailPage(web_page).buying()
        # 商品详情-去结算
        time.sleep(1)
        ProductDetailPage(web_page).settle()

        logging.info("开始断言")
        time.sleep(2)

        try:
            assert ProductDetailPage(web_page).check_settle() == data['check']
            logging.info("断言成功")

        except:
            print("断言失败")
            print("商品详情-确认订单页面跳转失败")
            common.save_screenShot(web_page, model_name="商品详情-确认订单页面跳转")
            raise

    @pytest.mark.smoke
    @pytest.mark.parametrize("data", product_detail_data.add_address_err)
    def test_product_address_err(self, data, web_page):
        '''确认订单页面-新增收货地址_错误（收货人、手机号、详细地址）'''
        # 步骤 跳转商品详情
        ProductDetailPage(web_page).login_product_detail(data['username'], data['code'])
        # 商品详情-选择规格
        time.sleep(3)
        ProductDetailPage(web_page).standards()
        # 商品详情-立即购买
        time.sleep(1)
        ProductDetailPage(web_page).buying()
        # 商品详情-去结算
        time.sleep(1)
        ProductDetailPage(web_page).settle()
        # 商品详情-新增收货地址
        time.sleep(3)
        ProductDetailPage(web_page).order_commit_address_success(data['receiver_name'], data['receiver_mobile'], data['detail_address'])

        logging.info("开始断言")
        time.sleep(2)

        try:
            assert ProductDetailPage(web_page).check_msg() == data['check']
            logging.info("断言成功")

        except:
            print("断言失败")
            print("确认订单页面-新增收货地址")
            common.save_screenShot(web_page, model_name="确认订单页面-新增收货地址")
            raise

    @pytest.mark.smoke
    @pytest.mark.parametrize("data", product_detail_data.add_address_err2)
    def test_product_address_err2(self, data, web_page):
        '''确认订单页面-新增收货地址_无地区'''
        # 步骤 跳转商品详情
        ProductDetailPage(web_page).login_product_detail(data['username'], data['code'])
        # 商品详情-选择规格
        time.sleep(3)
        ProductDetailPage(web_page).standards()
        # 商品详情-立即购买
        time.sleep(1)
        ProductDetailPage(web_page).buying()
        # 商品详情-去结算
        time.sleep(1)
        ProductDetailPage(web_page).settle()
        # 商品详情-新增收货地址
        time.sleep(3)
        ProductDetailPage(web_page).order_commit_address_err(data['receiver_name'], data['receiver_mobile'])

        logging.info("开始断言")
        time.sleep(2)

        try:
            assert ProductDetailPage(web_page).check_msg() == data['check']
            logging.info("断言成功")

        except:
            print("断言失败")
            print("确认订单页面-新增收货地址失败")
            common.save_screenShot(web_page, model_name="确认订单页面-新增收货地址_无地区")
            raise

    @pytest.mark.smoke
    @pytest.mark.parametrize("data", product_detail_data.add_address_success)
    def test_product_address_success(self, data, web_page):
        '''确认订单页面-新增收货地址-成功'''
        # 步骤 跳转商品详情
        ProductDetailPage(web_page).login_product_detail(data['username'], data['code'])
        # 商品详情-选择规格
        time.sleep(3)
        ProductDetailPage(web_page).standards()
        # 商品详情-立即购买
        time.sleep(1)
        ProductDetailPage(web_page).buying()
        # 商品详情-去结算
        time.sleep(1)
        ProductDetailPage(web_page).settle()
        # 商品详情-新增收货地址
        time.sleep(3)
        ProductDetailPage(web_page).order_commit_address_success(data['receiver_name'], data['receiver_mobile'], data['detail_address'])

        logging.info("开始断言")
        time.sleep(2)

        try:
            assert ProductDetailPage(web_page).check_address_success() == data['check']
            logging.info("断言成功")

        except:
            print("断言失败")
            print("确认订单页面-新增收货地址失败")
            common.save_screenShot(web_page, model_name="确认订单页面-新增收货地址")
            raise

    @pytest.mark.smoke
    @pytest.mark.parametrize("data", product_detail_data.paper_invoice)
    def test_product_paper_invoice(self, data, web_page):
        '''确认订单页面-新增纸质发票'''
        # 步骤 跳转商品详情
        ProductDetailPage(web_page).login_product_detail(data['username'], data['code'])
        # 商品详情-选择规格
        time.sleep(3)
        ProductDetailPage(web_page).standards()
        # 商品详情-立即购买
        time.sleep(1)
        ProductDetailPage(web_page).buying()
        # 商品详情-去结算
        time.sleep(1)
        ProductDetailPage(web_page).settle()
        # 商品详情-新增纸质发票
        time.sleep(3)
        ProductDetailPage(web_page).order_commit_paper_invoice(data['invoice_name'], data['invoice_no'])

        logging.info("开始断言")
        time.sleep(2)

        try:
            assert ProductDetailPage(web_page).check_paper_invoice() == data['check']
            logging.info("断言成功")

        except:
            print("断言失败")
            print("确认订单页面-纸质发票失败")
            common.save_screenShot(web_page, model_name="确认订单页面-纸质发票")
            raise

    @pytest.mark.smoke
    @pytest.mark.parametrize("data", product_detail_data.electronic_invoice)
    def test_product_electronic_invoice(self, data, web_page):
        '''确认订单页面-新增电子发票'''
        # 步骤 跳转商品详情
        ProductDetailPage(web_page).login_product_detail(data['username'], data['code'])
        # 商品详情-选择规格
        time.sleep(3)
        ProductDetailPage(web_page).standards()
        # 商品详情-立即购买
        time.sleep(1)
        ProductDetailPage(web_page).buying()
        # 商品详情-去结算
        time.sleep(1)
        ProductDetailPage(web_page).settle()
        # 商品详情-新增电子发票
        time.sleep(3)
        ProductDetailPage(web_page).order_commit_electronic_invoice(data['invoice_name'], data['invoice_no'], data['invoice_email'])

        logging.info("开始断言")
        time.sleep(2)

        try:
            assert ProductDetailPage(web_page).check_electronic_invoice() == data['check']
            logging.info("断言成功")

        except:
            print("断言失败")
            print("确认订单页面-新增电子发票失败")
            common.save_screenShot(web_page, model_name="确认订单页面-新增电子发票")
            raise

    @pytest.mark.smoke
    @pytest.mark.parametrize("data", product_detail_data.remarks)
    def test_product_remarks(self, data, web_page):
        '''确认订单页面-提交订单'''
        # 步骤 跳转商品详情
        ProductDetailPage(web_page).login_product_detail(data['username'], data['code'])
        # 商品详情-选择规格
        time.sleep(3)
        ProductDetailPage(web_page).standards()
        # 商品详情-立即购买
        time.sleep(2)
        ProductDetailPage(web_page).buying()
        # 商品详情-去结算
        time.sleep(2)
        ProductDetailPage(web_page).settle()
        # 商品详情-新增留言
        time.sleep(3)
        ProductDetailPage(web_page).order_commit_remarks(data['remarks'])

        logging.info("开始断言")
        time.sleep(2)

        try:
            assert ProductDetailPage(web_page).check_order_commit() == data['check']
            logging.info("断言成功")

        except:
            print("断言失败")
            print("确认订单页面-提交订单失败")
            common.save_screenShot(web_page, model_name="确认订单页面-提交订单")
            raise

if __name__ == '__main__':
    pass