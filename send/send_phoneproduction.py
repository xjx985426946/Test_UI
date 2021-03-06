from dingtalkchatbot.chatbot import DingtalkChatbot
from bs4 import BeautifulSoup
import time,os
class Message():
    # 解析文件获取结果数据
    now = time.strftime("%Y-%m-%d")
    report_file = now + '_phone_production_result.html'
    cur_path = os.path.dirname(os.path.dirname(os.path.dirname(os.path.dirname(os.path.dirname(os.path.realpath(__file__)))))) + '/web/autotest/ui/'

    def html_text(self):
        helloworld = open(self.cur_path + self.report_file, 'r', encoding="utf-8")
        soup = BeautifulSoup(helloworld, "html.parser")
        passed = soup.find('span', class_="passed")
        skipped = soup.find('span', class_="skipped")
        failed = soup.find('span', class_="failed")
        error = soup.find('span', class_="error")
        xfailed = soup.find('span', class_="xfailed")
        xpassed = soup.find('span', class_="xpassed")
        rerun = soup.find('span', class_="rerun")
        list = [passed, skipped, failed, error, xfailed, xpassed, rerun]
        result_list = []
        for i in list:
            result = str(i).split('>')[1].split(' ')[0]
            result_list.append(result)
        return result_list

    def messge(self):
        text = self.html_text()

        all_text = int(text[0]) + int(text[1]) + int(text[2]) + int(text[3]) + int(text[4]) + int(text[5])
        report_url = 'http://autotest.ebestore.com/ui/' + self.report_file
        msg = '线上环境phone端UI自动化测试报告\n 共执行%s个测试用例\n 通过用例: %s\n 跳过用例: %s \n 失败用例: %s\n 错误用例: %s \n 预期失败用例: %s\n' \
              '意外通过的用例: %s \n 用例重跑: %s次 \n 详情报告请点击跳转:\n %s' %(all_text,text[0],text[1],text[2],
                                                                     text[3],text[4],text[5],text[6],report_url)
        return msg
    def sends_text(self):
        # WebHook地址
        webhook = 'https://oapi.dingtalk.com/robot/send?access_token=03916cdbbd7566544302bdaba1a144f5c117b3ca8284bf9a9de9e74999c687f5d2a81f6'
        # 脚本的解析
        # 初始化机器人小丁
        xiaoding = DingtalkChatbot(webhook)
        # Text消息@所有人
        at_mobiles = ['13729542194', '13640993513', '18818655517', '13631233879', '15017589322']
        #to = '0289806f09dc2baaaf098555790a492e11c5711212e62ada4b25b88b17966d65'
        msg = self.messge()
        xiaoding.send_text(msg=msg, is_at_all=False,at_mobiles=at_mobiles)

Message().sends_text()
