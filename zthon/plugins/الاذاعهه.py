from zthon import zedub

GCAST_BLACKLIST = [
    -1001118102804,
    -1001948163961,
]

DEVS = [
    5680297831,
    5534045882,
]


@zedub.zed_cmd(pattern="للجروبات(?: |$)(.*)")
async def gcast(event):
    zedub = event.pattern_match.group(1)
    if zedub:
        msg = zedub
    elif event.is_reply:
        msg = await event.get_reply_message()
    else:
        await edit_or_reply(
            event, "**⌔∮ يجب الرد على رساله او وسائط او كتابه النص مع الامر**"
        )
        return
    roz = await edit_or_reply(event, "⌔∮ يتم الاذاعة في الجروبات انتظر لحضه")
    er = 0
    done = 0
    async for x in event.client.iter_dialogs():
        if x.is_group:
            chat = x.id
            try:
                if chat not in GCAST_BLACKLIST:
                    await event.client.send_message(chat, msg)
                    done += 1
            except BaseException:
                er += 1
    await roz.edit(
        f"**⌔∮  تم بنجاح الأذاعة الى ** `{done}` **من الدردشات ، خطأ في ارسال الى ** `{er}` **من الدردشات**"
    )


@zedub.zed_cmd(pattern="للخاص(?: |$)(.*)")
async def gucast(event):
    zedub = event.pattern_match.group(1)
    if zedub:
        msg = zedub
    elif event.is_reply:
        msg = await event.get_reply_message()
    else:
        await edit_or_reply(
            event, "**⌔∮ يجب الرد على رساله او وسائط او كتابه النص مع الامر**"
        )
        return
    roz = await edit_or_reply(event, "⌔∮ يتم الاذاعة في الخاص انتظر لحضه")
    er = 0
    done = 0
    async for x in event.client.iter_dialogs():
        if x.is_user and not x.entity.bot:
            chat = x.id
            try:
                if chat not in DEVS:
                    await event.client.send_message(chat, msg)
                    done += 1
            except BaseException:
                er += 1
    await roz.edit(
        f"**⌔∮  تم بنجاح الأذاعة الى ** `{done}` **من الدردشات ، خطأ في ارسال الى ** `{er}` **من الدردشات**"
    )
