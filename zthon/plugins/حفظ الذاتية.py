from telethon import events

from zthon import zedub


tepthonself = False


@zedub.zed_cmd(pattern="الذاتية تشغيل")
async def start_datea(event):
    global tepthonself
    tepthonself = True
    await edit_or_reply(event, "تم بنجاح تفعيل حفظ الميديا الذاتية من الان")


@zedub.zed_cmd(pattern="الذاتية تعطيل")
async def stop_datea(event):
    global tepthonself
    tepthonself = False
    await edit_or_reply(event, "تم بنجاح تعطيل حفظ الميديا الذاتية من الان")


@zedub.on(
    events.NewMessage(
        func=lambda e: e.is_private and (e.photo or e.video) and e.media_unread
    )
)
async def tf3el(event):
    global tepthonself
    if tepthonself:
        result = await event.download_media()
        await zedub.send_file("me", result, caption="- تم بنجاح الحفظ بواسطة @FTTUTY")
