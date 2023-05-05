from zthon import zedub
from zthon.sql_helper.MOrakb import *

from ..Config import Config

# from zedub.sql_helper.mo5zn import *


@zedub.zed_cmd(incoming=True, func=lambda e: e.is_group, edited=False, forword=None)
async def forward_to_saved_messages(event):
    if event.is_private:
        return
    if event.sender_id == event.chat_id:
        return
    if event.is_group:
        if is_morakb(event.sender_id) and not event.forward:
            await event.client.forward_messages(
                Config.PM_LOGGER_GROUP_ID, event.message
            )


"""
@zedub.zed_cmd(incoming=True, func=lambda e: e.is_private, edited=False, forword=None)
async def forward_to_saved_messages(event):
    if event.sender_id == event.chat_id:
        return
    if is_mo5zn(event.sender_id):
        await event.forward_to(Config.PM_LOGGER_GROUP_ID)
        

@zedub.zed_cmd(pattern=r"تخزين")
async def add_morakb_handler(event):
    msg = event.text.split()
    username = msg[1]
    user = await zedub.get_entity(username)
    replied_user = user.id
    if is_mo5zn(replied_user):
        await event.reply("هذا المستخدم في قائمة التخزين في الاصل.")
    else:
        addmo5zn(replied_user)
        await event.reply("تم بنجاح اضافة المستخدمالى قائمة التخزين بنجاح.")


@zedub.zed_cmd(pattern=r"الغاء تخزين")
async def remove_morakb_handler(event):
    msg = event.text.split()
    username = msg[2]
    user = await zedub.get_entity(username)
    replied_user = user.id
    if not is_mo5zn(replied_user):
        await event.reply("هذا المستخدم ليس في قائمة التخزين في الاصل.")
    else:
        unmo5zn(replied_user)
        await event.reply("تم بنجاح الغاء تخزين المستخدم.")


"""


@zedub.zed_cmd(pattern=r"بحبك")
async def add_morakb_handler(event):
    msg = event.text.split()
    username = msg[1]
    user = await zedub.get_entity(username)
    replied_user = user.id
    if is_morakb(replied_user):
        await event.reply("علفكره انت قولتله انك بتحبو مش موضوع هوا 🙄")
    else:
        addmorakb(replied_user)
        await event.reply("ابسط يعم انا بحبك اهو 😹♥")


@zedub.zed_cmd(pattern=r"الغاء الحب")
async def remove_morakb_handler(event):
    msg = event.text.split()
    username = msg[2]
    user = await zedub.get_entity(username)
    replied_user = user.id
    if not is_morakb(replied_user):
        await event.reply("تم مسح المستخدم من قائمة الاحباء 🥲")
    else:
        unmorakb(replied_user)
        await event.reply("انت مش بتحبو اصلا 🙄😹")
