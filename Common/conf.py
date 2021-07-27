#测试环境域名
import sys
path = str(sys.argv[0]).split('/')[-1]
if path == 'C_ptest.py':

    url = 'https://test-item.intbee.com/'
    url_f ='https://test-www.intbee.com/'
    url_v = "https://test-api.intbee.com/"
    url_c = "https://test-item.intbee.com/"


if path == 'C_ptestProduction.py':

    url = 'https://item.intbee.com/'
    url_f = 'https://test-www.intbee.com/'
    url_v = "https://test-api.intbee.com/"
    url_c = "https://item.intbee.com/"

else:
    url = 'https://test-item.intbee.com/'
    url_f = 'https://test-www.intbee.com/'
    url_v = "https://test-api.intbee.com/"
    url_c = "https://test-item.intbee.com/"
    url_zc = "http://test-zc-thirdparty.intbee.com/"

#c端手机端登录地址
m_lg_url = url + 'customer/mobile/login'
#web端登录地址
w_lg_url = url + 'customer/login'