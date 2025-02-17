from astrbot.api.event import filter, AstrMessageEvent, MessageEventResult
from astrbot.api.star import Context, Star, register
from astrbot.api import logger
from astrbot.api.all import *
import inspect
from pathlib import Path
from openai import OpenAI
import base64
import os
from queue import Queue
import requests
from astrbot.core.provider.entites import LLMResponse
import re
from PIL import Image, ImageDraw, ImageFont, ImageOps
import random

@register("astrbot_plugin_emojiproduction", "达莉娅",
          "gif表情包制作",
          "v1.0.0")
class MyPlugin(Star):
    def __init__(self, context: Context, config: dict):
        super().__init__(context)
        self.data = {}
        self.enabled = True
        self.config = config
        #self.api_name = config.get('name', 'FunAudioLLM/CosyVoice2-0.5B')

    '''---------------------------------------------------'''
    '''---------------------------------------------------'''
    @filter.command("表情包制作")
    async def ddz_menu(self, event: AstrMessageEvent):
        img = self.generate_menu()
        yield event.make_result().message("表情包制作菜单：\n").file_image(img)

    @filter.command("摸头")
    async def trap1(self, event: AstrMessageEvent):
        '''【摸头@xx】指令'''
        message_chain = event.get_messages()  # 用户所发的消息的消息链
        logger.info(message_chain)
        id = self.parse_target(event)
        data = self.fetch_image(id, "摸头")
        user_id = event.get_sender_id()
        if not data:
            yield event.plain_result("请求失败，该api已失效")
        else:
            yield event.image_result(data)

    @filter.command("感动哭了")
    async def trap2(self, event: AstrMessageEvent):
        ''''''
        message_chain = event.get_messages()  # 用户所发的消息的消息链
        logger.info(message_chain)
        id = self.parse_target(event)
        data = self.fetch_image(id, "感动哭了")
        user_id = event.get_sender_id()
        if not data:
            yield event.plain_result("请求失败，该api已失效")
        else:
            yield event.image_result(data)



    @filter.command("膜拜")
    async def trap3(self, event: AstrMessageEvent):
        ''''''
        message_chain = event.get_messages()  # 用户所发的消息的消息链
        logger.info(message_chain)
        id = self.parse_target(event)
        data = self.fetch_image(id, "膜拜")
        user_id = event.get_sender_id()
        if not data:
            yield event.plain_result("请求失败，该api已失效")
        else:
            yield event.image_result(data)

    @filter.command("咬")
    async def trap4(self, event: AstrMessageEvent):
        ''''''
        message_chain = event.get_messages()  # 用户所发的消息的消息链
        logger.info(message_chain)
        id = self.parse_target(event)
        data = self.fetch_image(id, "咬")
        user_id = event.get_sender_id()
        if not data:
            yield event.plain_result("请求失败，该api已失效")
        else:
            yield event.image_result(data)

    @filter.command("可莉吃")
    async def trap5(self, event: AstrMessageEvent):
        ''''''
        message_chain = event.get_messages()  # 用户所发的消息的消息链
        logger.info(message_chain)
        id = self.parse_target(event)
        data = self.fetch_image(id, "可莉吃")
        user_id = event.get_sender_id()
        if not data:
            yield event.plain_result("请求失败，该api已失效")
        else:
            yield event.image_result(data)


    @filter.command("吃掉")
    async def trap6(self, event: AstrMessageEvent):
        ''''''
        message_chain = event.get_messages()  # 用户所发的消息的消息链
        logger.info(message_chain)
        id = self.parse_target(event)
        data = self.fetch_image(id, "吃掉")
        user_id = event.get_sender_id()
        if not data:
            yield event.plain_result("请求失败，该api已失效")
        else:
            yield event.image_result(data)


    @filter.command("捣")
    async def trap7(self, event: AstrMessageEvent):
        ''''''
        message_chain = event.get_messages()  # 用户所发的消息的消息链
        logger.info(message_chain)
        id = self.parse_target(event)
        data = self.fetch_image(id, "捣")
        user_id = event.get_sender_id()
        if not data:
            yield event.plain_result("请求失败，该api已失效")
        else:
            yield event.image_result(data)

    @filter.command("咸鱼")
    async def trap8(self, event: AstrMessageEvent):
        ''''''
        message_chain = event.get_messages()  # 用户所发的消息的消息链
        logger.info(message_chain)
        id = self.parse_target(event)
        data = self.fetch_image(id, "咸鱼")
        user_id = event.get_sender_id()
        if not data:
            yield event.plain_result("请求失败，该api已失效")
        else:
            yield event.image_result(data)

    @filter.command("玩")
    async def trap9(self, event: AstrMessageEvent):
        ''''''
        message_chain = event.get_messages()  # 用户所发的消息的消息链
        logger.info(message_chain)
        id = self.parse_target(event)
        data = self.fetch_image(id, "玩")
        user_id = event.get_sender_id()
        if not data:
            yield event.plain_result("请求失败，该api已失效")
        else:
            yield event.image_result(data)

    @filter.command("舔")
    async def trap10(self, event: AstrMessageEvent):
        ''''''
        message_chain = event.get_messages()  # 用户所发的消息的消息链
        logger.info(message_chain)
        id = self.parse_target(event)
        data = self.fetch_image(id, "舔")
        user_id = event.get_sender_id()
        if not data:
            yield event.plain_result("请求失败，该api已失效")
        else:
            yield event.image_result(data)


    @filter.command("拍")
    async def trap11(self, event: AstrMessageEvent):
        ''''''
        message_chain = event.get_messages()  # 用户所发的消息的消息链
        logger.info(message_chain)
        id = self.parse_target(event)
        data = self.fetch_image(id, "拍")
        user_id = event.get_sender_id()
        if not data:
            yield event.plain_result("请求失败，该api已失效")
        else:
            yield event.image_result(data)


    @filter.command("丢")
    async def trap12(self, event: AstrMessageEvent):
        ''''''
        message_chain = event.get_messages()  # 用户所发的消息的消息链
        logger.info(message_chain)
        id = self.parse_target(event)
        data = self.fetch_image(id, "丢")
        user_id = event.get_sender_id()
        if not data:
            yield event.plain_result("请求失败，该api已失效")
        else:
            yield event.image_result(data)


    @filter.command("撕")
    async def trap13(self, event: AstrMessageEvent):
        ''''''
        message_chain = event.get_messages()  # 用户所发的消息的消息链
        logger.info(message_chain)
        id = self.parse_target(event)
        data = self.fetch_image(id, "撕")
        user_id = event.get_sender_id()
        if not data:
            yield event.plain_result("请求失败，该api已失效")
        else:
            yield event.image_result(data)


    @filter.command("求婚")
    async def trap14(self, event: AstrMessageEvent):
        ''''''
        message_chain = event.get_messages()  # 用户所发的消息的消息链
        logger.info(message_chain)
        id = self.parse_target(event)
        data = self.fetch_image(id, "求婚")
        user_id = event.get_sender_id()
        if not data:
            yield event.plain_result("请求失败，该api已失效")
        else:
            yield event.image_result(data)


    @filter.command("爬")
    async def trap15(self, event: AstrMessageEvent):
        ''''''
        message_chain = event.get_messages()  # 用户所发的消息的消息链
        logger.info(message_chain)
        id = self.parse_target(event)
        data = self.fetch_image(id, "爬")
        user_id = event.get_sender_id()
        if not data:
            yield event.plain_result("请求失败，该api已失效")
        else:
            yield event.image_result(data)


    @filter.command("你可能需要他")
    async def trap16(self, event: AstrMessageEvent):
        ''''''
        message_chain = event.get_messages()  # 用户所发的消息的消息链
        logger.info(message_chain)
        id = self.parse_target(event)
        data = self.fetch_image(id, "你可能需要他")
        user_id = event.get_sender_id()
        if not data:
            yield event.plain_result("请求失败，该api已失效")
        else:
            yield event.image_result(data)
    @filter.command("想看")
    async def trap17(self, event: AstrMessageEvent):
        ''''''
        message_chain = event.get_messages()  # 用户所发的消息的消息链
        logger.info(message_chain)
        id = self.parse_target(event)
        data = self.fetch_image(id, "想看")
        user_id = event.get_sender_id()
        if not data:
            yield event.plain_result("请求失败，该api已失效")
        else:
            yield event.image_result(data)
    @filter.command("点赞")
    async def trap18(self, event: AstrMessageEvent):
        ''''''
        message_chain = event.get_messages()  # 用户所发的消息的消息链
        logger.info(message_chain)
        id = self.parse_target(event)
        data = self.fetch_image(id, "点赞")
        if not data:
            yield event.plain_result("请求失败，该api已失效")
        else:
            yield event.image_result(data)
    @filter.command("随机制作")
    async def trap19(self, event: AstrMessageEvent,msg:str,msg2:str):
        ''''''
        message_chain = event.get_messages()  # 用户所发的消息的消息链
        logger.info(message_chain)
        id = self.parse_target(event)
        id2 = self.parse_target2(event,id)
        data = self.fetch_image2(id,id2,msg,msg2)
        if not data:
            yield event.plain_result("请求失败，该api已失效")
        else:
            yield event.image_result(data)

    def fetch_image(self, qq_number, flag):
        # 摸头
        # 定义字典映射
        switch_dict = {
            "摸头": "https://api.lolimi.cn/API/face_petpet/api.php",
            "感动哭了": "https://api.lolimi.cn/API/face_touch/api.php",
            "膜拜": "https://api.lolimi.cn/API/face_worship/api.php",
            "咬": "https://api.lolimi.cn/API/face_suck/api.php",
            "可莉吃": "https://api.lolimi.cn/API/chi/api.php",
            "吃掉": "https://api.lolimi.cn/API/face_bite/api.php",
            "捣": "https://api.lolimi.cn/API/face_pound/api.php",
            "咸鱼": "https://api.lolimi.cn/API/face_yu/api.php",
            "玩": "https://api.lolimi.cn/API/face_play/api.php",
            "舔": "https://api.lolimi.cn/API/tian/api.php",
            "拍": "https://api.lolimi.cn/API/face_pat/api.php",
            "丢": "https://api.lolimi.cn/API/diu/api.php",
            "撕": "https://api.lolimi.cn/API/si/api.php",
            "求婚": "https://api.lolimi.cn/API/face_propose/api.php",
            "爬": "https://api.lolimi.cn/API/pa/api.php",
            "你可能需要他": "https://api.lolimi.cn/API/face_need/api.php",
            "想看":"https://api.lolimi.cn/API/face_thsee/api.php",
            "点赞":"https://api.lolimi.cn/API/zan/api.php",
        }
        # 获取对应的函数并执行
        url = switch_dict.get(flag, '')
        params = {
            'QQ': qq_number
        }
        response = requests.get(url, params=params)
        if response.status_code == 200:
            image_data = response.content
            with open(f"./data/plugins/astrbot_plugin_emojiproduction/pet_{qq_number}.gif", "wb") as file:
                file.write(image_data)
            return f"./data/plugins/astrbot_plugin_emojiproduction/pet_{qq_number}.gif"
        else:
            print(f"请求失败，状态码: {response.status_code}")

    def fetch_image2(self, qq_number, qq_number2,msg,msg2):
        url = "https://api.lolimi.cn/API/preview/api.php"
        # 生成 1 到 10 之间的随机整数
        type = random.randint(1, 166)
        params = {
            'qq': qq_number,
            'qq2': qq_number2,
            'msg':msg,
            'msg2':msg2,
            'type': type,
        }
        response = requests.get(url, params=params)
        if response.status_code == 200:
            image_data = response.content
            with open(f"./data/plugins/astrbot_plugin_emojiproduction/p.gif", "wb") as file:
                file.write(image_data)
            return f"./data/plugins/astrbot_plugin_emojiproduction/p.gif"
        else:
            print(f"请求失败，状态码: {response.status_code}")
    def parse_target(self, event):
        """解析@目标或用户名"""
        for comp in event.message_obj.message:
            if isinstance(comp, At) and event.get_self_id() != str(comp.qq):
                return str(comp.qq)
    def parse_target2(self, event,id):
        """解析@目标或用户名"""
        for comp in event.message_obj.message:
            if isinstance(comp, At) and event.get_self_id() != str(comp.qq) and id!= str(comp.qq):
                return str(comp.qq)

    def generate_menu(self):
        img = Image.new('RGB', (800, 900), (73, 109, 137))
        d = ImageDraw.Draw(img)
        font = ImageFont.truetype('msyh.ttc', 24)
        menu = [
        "【表情包制作菜单】",
        "摸头@xx",
        "感动哭了@xx",
        "膜拜@xx",
        "咬@xx",
        "可莉吃@xx",
        "吃掉@xx",
        "捣@xx",
        "咸鱼@xx",
        "玩@xx",
        "舔@xx",
        "拍@xx",
        "丢@xx",
        "撕@xx",
        "求婚@xx",
        "爬@xx",
        "你可能需要他@xx",
        "想看@xx",
        "点赞@xx",
        "@xx@xx随机制作 【内容1】 【内容2】",
        ]
        y = 50
        for line in menu:
            d.text((100, y), line, fill=(255, 255, 0), font=font)
            y += 40

        output_path = f"./data/plugins/astrbot_plugin_emojiproduction/pet.png"
        img.save(output_path, format='PNG')
        return output_path