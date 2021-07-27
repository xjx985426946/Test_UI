from PageLocators.F_web import product_locator
from Common.basepage import BasePage
import time
from selenium import webdriver
class ProductPage(BasePage):
    name = '商品管理页面'

    #添加商品
    def create_product(self,product_name,product_descript,product_code,address,price,stock,wenan):
        #点击添加商品按钮
        self.click_element(product_locator.createproduct,model=self.name)
        #点击实体商品按钮
        self.click_element(product_locator.normal_product,model=self.name)
        #输入商品名称
        self.input_text(product_name,product_locator.productname,model=self.name)
        #输入商品描述
        self.input_text(product_descript,product_locator.product_description,model=self.name)
        #输入商品编码
        self.input_text(product_code,product_locator.product_code,model=self.name)
        #点击商品类别
        self.click_element(product_locator.category,model=self.name)
        #选择一级品类
        self.click_element(product_locator.category1,model=self.name)
        #选择二级品类
        self.click_element(product_locator.category2,model=self.name)
        #选择三级品类
        self.click_element(product_locator.category3,model=self.name)
        #输入发货地址
        self.input_text(address,product_locator.addresslimit,model=self.name)

        #选择规格
        self.click_element(product_locator.sdandarname1,model=self.name)
        self.click_element(product_locator.sdandarname1_1,model=self.name)
        self.click_element(product_locator.sdandarname2,model=self.name)
        self.click_element(product_locator.sdandarname2_1,model=self.name)
        #批量输入价格
        self.input_text(price,product_locator.price,self.name)
        #输入库存
        self.input_text(stock,product_locator.stock,self.name)
        #点击库存确定按钮
        self.click_element(product_locator.stockbutton,self.name)
        #下一步按钮
        self.click_element(product_locator.next_button,self.name)
        #输入商品默认文案
        self.input_text(wenan,product_locator.wenan,model=self.name)

        '''文件上传
            未写
        '''

        #点击保存按钮
        self.click_element(product_locator.save_button,model=self.name)


    #发布蜂卡
    def create_card(self,search_spreader,commom_service,vip_servicer):

        #点击新建蜂卡按钮
        self.click_element(product_locator.createcard,model=self.name)
        #点击定向蜂卡按钮
        self.click_element(product_locator.card,model=self.name)
        #输入智蜂客名称
        self.input_text(search_spreader,product_locator.search_spreader,model=self.name)
        #点击搜索按钮
        self.click_element(product_locator.search_button,model=self.name)
        #选择智蜂客
        self.click_element(product_locator.select_preader,model=self.name)
        #点击下一步按钮
        self.click_element(product_locator.next_submit,model=self.name)
        #选择商品
        self.click_element(product_locator.select_product,model=self.name)
        #点击下一步按钮
        self.click_element(product_locator.button,model=self.name)
        #输入服务费
        self.input_text(commom_service,product_locator.commom_service,model=self.name)
        self.input_text(vip_servicer,product_locator.vip_servicer,model=self.name)
        #点击下一步按钮
        self.click_element(product_locator.but,model=self.name)
        #点击阅读协议
        self.click_element(product_locator.Agreement,model=self.name)
        #点击发布蜂卡
        self.click_element(product_locator.publish_card,model=self.name)

