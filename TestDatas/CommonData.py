import sys
path = str(sys.argv[0]).split('/')[-1]
if path == 'C_ptest.py':
    url = "https://test-item.intbee.com/customer/login"
    username = '13729542194'
    password = '123456'

elif path == 'C_ptestProduction.py':
    login_sesscus = [{'username': '13729542195', 'password': 'zckj123456', 'check': [{'personal_text': '个人中心'}]}]
    username = '13729542194'
    password = 'zckj123456'

else:
    url = "https://test-item.intbee.com/customer/login"
    username = '13729542194'
    password = '123456'