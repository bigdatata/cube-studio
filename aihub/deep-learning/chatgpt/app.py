import base64
import io,sys,os

import requests

from cubestudio.aihub.model import Model
from cubestudio.aihub.docker import Docker
from cubestudio.aihub.web.server import Server,Field,Field_type,Validator
import codecs, markdown
import pysnooper
import os

class Chatgpt_Model(Model):
    # 模型基础信息定义
    name='chatgpt'   # 该名称与目录名必须一样，小写
    label='全新的聊天机器人模型'
    describe="ChatGPT是OpenAI发布的聊天机器人模型，它的交互界面简洁，只有一个输入框，AI将根据输入内容进行回复，并允许在一个语境下持续聊天。"
    field="自然语言"
    scenes="聊天机器人"
    status='online'
    version='v20221001'
    doc='https://github.com/tencentmusic/cube-studio/tree/master/aihub' # 'https://帮助文档的链接地址'
    pic='example.jpg'  # https://应用描述的缩略图/可以直接使用应用内的图片文件地址

    inference_inputs = [
        Field(type=Field_type.text, name='question', label='您需要咨询的问题',
              describe='您需要咨询的问题，机器人将自动为您回复，答案将超乎你的想象',default='帮我写一段python代码，将时间类型转为字符串'),
    ]

    web_examples=[
        {
            "lable": "示例一描述",
            "input": {
                "question": '帮我写一段python代码，将时间类型转为字符串',

            }
        }
    ]
    # 加载模型
    def load_model(self):
        # self.model = load("/xxx/xx/a.pth")
        pass

    # 推理
    @pysnooper.snoop()
    def inference(self,question,**kwargs):
        req_data={
            "msgType": "text",
            "chatType": "group",
            "chatId": "wrkSFfCgAA1AxOagtYsQ5R******-iw",
            "userName": "zhang-san",
            "msgContent": question,
            "botName": "text",
            "botKey": "c1534e3f-****-4d21-****-484bc1a1307f",
            "hookUrl": "string",
            "msgId": "fCgAA1AxOagtYsQ5R",
            "chatInfoUrl": "string",
            "eventType": "add_to_chat"
        }
        res = requests.post('https://chatgpt.gometadata.xyz/api/v1/chat',timeout=120,headers={"x-token":"4fc6b7d6-8c07-41db-8161-7c6365ce5214"},json=req_data)
        result='系统出现问题'
        if res.status_code==200:
            result=res.json().get("msgContent",'')
            result_type = res.json().get("msgType",'')

        back=[
            {
                "markdown":result
            },
        ]
        return back

model=Chatgpt_Model()
# model.load_model()
# result = model.inference(question='帮我写一段python代码，将时间类型转为字符串')  # 测试
# print(result)
#
# # 启动服务
server = Server(model=model)
server.server(port=8080)
