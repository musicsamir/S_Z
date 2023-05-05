from telethon import events

from zthon import zedub

from ..utils import is_admin


@zedub.zed_cmd(pattern="تعطيل الميديا")
async def cleanup_command(event):
    if await is_admin(event.client, event.chat_id, event.sender_id):
        global handler

        @zedub.on(events.MessageEdited(incoming=True, chats=event.chat_id))
        async def handler(event):
            if event.media:
                await event.client.delete_messages(event.chat_id, event.id)

        await event.edit("- تم تفعيل نظام حذف الميديا المعدلة")
    else:
        await event.edit("- ليس لديك الصلاحيات الكافية لأستخدام هذا الامر.")


@zedub.zed_cmd(pattern="فتح الميديا")
async def stop_cleanup_command(event):
    if await is_admin(event.client, event.chat_id, event.sender_id):
        zedub.remove_event_handler(handler)
        await event.edit("- تم تعطيل نظام حذف الميديا المعدلة.")
    else:
        await event.edit("- ليس لديك الصلاحيات الكافية لأستخدام هذا الامر.")
