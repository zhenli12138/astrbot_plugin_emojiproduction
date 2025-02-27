from astrbot.api.event import filter, AstrMessageEvent, MessageEventResult
from astrbot.api.star import Context, Star, register
from astrbot.api import logger
from astrbot.api.all import *

@register("astrbot_plugin_emojiproduction", "达莉娅",
          "gif表情包制作",
          "v0.0.0")
class MyPlugin(Star):
    def __init__(self, context: Context, config: dict):
        super().__init__(context)

    @filter.command("表情包制作")
    async def ddz_menu(self, event: AstrMessageEvent):
        yield event.make_result().message("本插件合并至moreapi，请下载moreapi插件！本插件不再使用\n")



