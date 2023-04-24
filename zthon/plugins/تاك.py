from telethon import functions
from telethon.tl import functions
from telethon.tl.functions.channels import InviteToChannelRequest

from zthon import zedub

from ..core.managers import edit_delete, edit_or_reply

@zedub.on(admin_cmd(pattern="تاك 200(?: |$)(.*)"))
async def iq(zedub):
    mentions = zedub.text[8:]
    chat = await zedub.get_input_chat()
    async for x in zedub.client.iter_participants(chat, 200):
        mentions += f" \n◉  ⦙ ⵧ〈[{x.first_name}](tg://user?id={x.id})〉"
    await zedub.client.send_message(zedub.chat_id, mentions)
    await zedub.delete()
from telethon import functions
from telethon.tl import functions
from telethon.tl.functions.channels import InviteToChannelRequest

from zthon import zedub

from ..core.managers import edit_delete, edit_or_reply

@zedub.on(admin_cmd(pattern="تاك(?: |$)(.*)"))
async def iq(zedub):
    mentions = zedub.text[8:]
    chat = await zedub.get_input_chat()
    async for x in zedub.client.iter_participants(chat, 200):
        mentions += f" \n◉  ⦙ ⵧ〈[{x.first_name}](tg://user?id={x.id})〉"
    await zedub.client.send_message(zedub.chat_id, mentions)
    await zedub.delete()
@zedub.on(admin_cmd(pattern="تاك 150(?: |$)(.*)"))
async def iq(zedub):
    mentions = zedub.text[8:]
    chat = await zedub.get_input_chat()
    async for x in zedub.client.iter_participants(chat, 150):
        mentions += f" \n◉  ⦙ ⵧ〈[{x.first_name}](tg://user?id={x.id})〉 \n"
    await zedub.client.send_message(zedub.chat_id, mentions)
    await zedub.delete()
@zedub.on(admin_cmd(pattern="تاك 100(?: |$)(.*)"))
async def iq(zedub):
    mentions = zedub.text[8:]
    chat = await zedub.get_input_chat()
    async for x in zedub.client.iter_participants(chat, 100):
        mentions += f" \n◉  ⦙ ⵧ〈[{x.first_name}](tg://user?id={x.id})〉 \n"
    await zedub.client.send_message(zedub.chat_id, mentions)
    await zedub.delete()
@zedub.on(admin_cmd(pattern="تاك 50(?: |$)(.*)"))
async def iq(zedub):
    mentions = zedub.text[8:]
    chat = await zedub.get_input_chat()
    async for x in zedub.client.iter_participants(chat, 50):
        mentions += f" \n◉  ⦙ ⵧ〈[{x.first_name}](tg://user?id={x.id})〉 \n"
    await zedub.client.send_message(zedub.chat_id, mentions)
    await zedub.delete()
@zedub.on(admin_cmd(pattern="تاك 10(?: |$)(.*)"))
async def iq(zedub):
    mentions = zedub.text[8:]
    chat = await zedub.get_input_chat()
    async for x in zedub.client.iter_participants(chat, 10):
        mentions += f" \n◉  ⦙ ⵧ〈[{x.first_name}](tg://user?id={x.id})〉 \n"
    await zedub.client.send_message(zedub.chat_id, mentions)
    await zedub.delete()
