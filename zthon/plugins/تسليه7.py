import asyncio
import os
import random
from collections import deque

from . import edit_delete, edit_or_reply, zedub, mention

plugin_category = "الترفيه"

from . import ALIVE_NAME, deEmojify

DEFAULTUSER = str(ALIVE_NAME) if ALIVE_NAME else "zed"

from telethon.tl.functions.users import GetFullUserRequest

DEFAULTUSER = str(ALIVE_NAME) if ALIVE_NAME else "ZED - THON"


@zedub.zed_cmd(pattern=r"تهكير$")
async def _(event):
    zel_dev = (5680297831, 100898456, 100132193, 519036458, 519136458, 519016458, 51903458, 519036458, 5190136458, 100132193, 100132193, 100132193, 100132193, 100112193, 100132193, 62758332, 627658332, 1355571767, 135571767, 135571767, 135571767, 135571767, 13571767, 13551767, 135571767)
    if event.reply_to_msg_id:
        reply_message = await event.get_reply_message()
        await event.client(GetFullUserRequest(reply_message.sender_id))
        idd = reply_message.sender_id
        if idd in zel_dev:
            await edit_or_reply(event, "**⪼ دي انـه احـد مطورين السورس**\n**⪼ لا استطيع تهكيـر المطـورين**")
        if idd == 5680297831 or idd == 100112193 or idd == 105088456 or idd == 519016458:
            await edit_or_reply(event, "**⪼ دي انـه مطـور السـورس**\n**⪼ لا استطيع تهكيـر مطـوري**")
        else:
            event = await edit_or_reply(event, "**... جاري تهكير المستخدم**")
            animation_chars = [
                "**⌔: جاري الاتصال بخوادم سيمو المتخصصه بالـتهكير**",
                "**⌔: تم تحديد المستخدم لتهكيره ✅**",
                "⪼ جـاري الان ... اختـراق الضـحيـة 0%\n▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒ ",
                "⪼ جـاري ... اختـراق الضـحيـة 4%\n█▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒ ",
                "⪼ جـاري ... اختـراق الضـحيـة 8%\n██▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒ ",
                "⪼ جـاري ... اختـراق الضـحيـة 20%\n█████▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒ ",
                "⪼ جـاري ... اختـراق الضـحيـة 36%\n█████████▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒ ",
                "⪼ جـاري ... اختـراق الضـحيـة 52%\n█████████████▒▒▒▒▒▒▒▒▒▒▒▒ ",
                "⪼ جـاري ... اختـراق الضـحيـة 84%\n█████████████████████▒▒▒▒ ",
                "⪼ جـاري ... اختـراق الضـحيـة 100%\n█████████**تـم تهكـيره ✅**███████████ ",
                f"**⌔︙تـم اختـراق حسـاب الضـحية. ** \n\n**⪼ قـم بالـدفع الـى** {DEFAULTUSER} **لعـدم نشـر معلـوماتك وصـورك**",
            ]
            animation_interval = 3
            animation_ttl = range(11)
            for i in animation_ttl:
                await asyncio.sleep(animation_interval)
                await event.edit(animation_chars[i % 11])
    else:
        await edit_or_reply(event, "No User is Defined\n Can't hack account")


love = [
    """
█▀███▀▀███▀▀███▀▀███▀▀███▀█
█▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒█
█▒▒█▒▒▒▒▒███▒▒█▒▒▒█▒█████▒█
█▒▒█▒▒▒▒█▒▒▒█▒█▒▒▒█▒█▒▒▒▒▒█
█▒▒█▒▒▒▒█▒▒▒█▒▒█▒█▒▒█████▒█
█▒▒█▒▒▒▒█▒▒▒█▒▒█▒█▒▒█▒▒▒▒▒█
█▒▒████▒▒███▒▒▒▒█▒▒▒█████▒█
█▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒█
█▒▒▒▒▒▒▒▒██▒▒▒▒▒▒▒▒██▒▒▒▒▒█
█▒▒▒▒▒▒▒█──█▒████▒█──█▒▒▒▒█
█▒▒▒▒▒▒█──█─█────█─█──█▒▒▒█
█▒▒▒▒▒▒█─██───────███─█▒▒▒█
█▒▒▒▒▒▒█──────────────█▒▒▒█
█▒▒▒▒▒▒▒█────────────█▒▒▒▒█
█▒▒▒▒██▒▒█──██───██──█▒▒▒▒█
█▒▒▒█──█▒█──██───██──█▒▒▒▒█
█▒▒▒█──█▒█────███────█▒▒▒▒█
█▒▒▒█──█▒█───█───█──█▒▒▒▒▒█
█▒▒▒▒█──█─█───███──█▒▒▒▒▒▒█
█▒▒▒▒▒█────██────██▒▒▒▒▒▒▒█
█▒▒▒▒▒█──────████─██▒▒▒▒▒▒█
█▒▒▒▒▒▒█───────────█▒▒▒▒▒▒█
█▒▒▒▒▒▒▒███─────────█▒▒▒▒▒█
█▒▒▒▒▒▒▒▒▒█──────█───█▒▒▒▒█
█▒▒▒▒███▒▒█───────█───█▒▒▒█
█▒▒▒█──████─────████───█▒▒█
█▒▒▒█────█─────█────█─█▒▒▒█
█▒▒▒█─────█────█────██▒▒▒▒█
█▒▒▒█──────█───█──────█▒▒▒█
█▒▒▒▒█─────██████─────█▒▒▒█
█▒▒▒▒▒█──███▒▒▒▒█─────█▒▒▒█
█▒▒▒▒▒▒██▒▒▒▒▒▒▒▒█───█▒▒▒▒█
█▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒███▒▒▒▒▒█
█▒▒▒▒█▒▒▒▒█▒▒███▒▒█▒▒▒█▒▒▒█
█▒▒▒▒▒█▒▒█▒▒█▒▒▒█▒█▒▒▒█▒▒▒█
█▒▒▒▒▒▒██▒▒▒█▒▒▒█▒█▒▒▒█▒▒▒█
█▒▒▒▒▒▒█▒▒▒▒█▒▒▒█▒█▒▒▒█▒▒▒█
█▒▒▒▒▒█▒▒▒▒▒▒███▒▒▒███▒▒▒▒█
█▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒█
█▄▄█▄▄██▄▄█▄▄█▄▄█▄▄██▄▄█▄▄█
""",
    """
╔══╗
╚╗╔╝
╔╝(¯`v´¯)
╚══`.¸.YOU
""",
    """
░░░░░░░░░░░░░░░░░░░░░░░░░░░░░
░░░▄▄▄▄▄▄░░░░▄▄▄░░░░▄▄▄░░░░░░
░░░▀████▀░░▄█████▄▄█████▄░░░░
░░░░░██░░░████████████████░░░
░░░░░██░░░████████████████░░░
░░░░░██░░░▀██████████████▀░░░
░░░░▄██▄░░░░▀██████████▀░░░░░
░░░██████░░░░░▀██████▀░░░░░░░
░░░░░░░░░░░░░░░░▀██▀░░░░░░░░░
░░░░░░░░░░░░░▄▄░░░░░░░░░░░░░░
░░▀███░███▀▄█▀▀█▄░▀██▀░▀██▀░░
░░░░▀█▄█▀░▄█░░░░█▄░██░░░██░░░
░░░░░░█░░░██░░░░██░██░░░██░░░
░░░░░░█░░░░█▄░░▄█░░██░░░██░░░
░░░░▄███▄░░░▀██▀░░░░▀███▀░░░░
░░░░░░░░░░░░░░░░░░░░░░░░░░░░░
""",
    """
░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░
░░░▄▄▄░░░░▄███▄▄███▄░░░░░░▄░░▄░░░░░░░░
░░░░█░░░░░██████████░░░░░░█░░█░░░░░░░░
░░░░█░░░░░░▀██████▀░░░░░░░█░░█░░░░░░░░
░░░▀▀▀░░░░░░░▀██▀░░░░░░░░░░▀▀░░░░░░░░░
░░░░░░░░░░░░▄░░░░░█░▄▀░░▄░░░░░░░░░░░░░
░░░░░░░░▄░░░▀▄▄▄▀█▀▀█▀▀▄█▄░█░░░░░░░░░░
░░░░░░░░░▀▄▄▀█░░░▀░░░░░░░░█▄░▄▀▀░░░░░░
░░░░░▀▀▄░█▀░░░░░░░░░▄▄▄▄▄▄░▀█░░░░░░░░░
░░░░░░▄▀▀░▄▄▀▀▀▄░░▄█▀░░░░▀▄░▄█▀▀▀▄░░░░
░░░▄▄██░░█░░░░░░█░█░░███░▄▀░░░██░█░░░░
░░█░▄█░░░█░███░▄▀░▀▀▄███▀░░░░░██░█░░░░
░░█░▀█▄░░▀▄███▄▀░░░░░░░░░░░░░▄█▄▀░░░░░
░░░▀▀▀▀█░░░░░░░░░░░░░░░▄█▀░░▄▀░░░░▄░░░
░░░░▄░░░▀▄░▀▀▄▄░░░░░▄▄▀▀░░▄▀░░░░▄█▀░░░
░░▄▄█▄░░░░▀▀▄▄░▀▀▀▀▀░▄▄▄▀▀░░▄▄▀▀▀█▀▀░░
░░▄█▀▀▀▀▄▄▄▄░░▀▀▀▀▀█▀░░░▄▄▀▀░░░░░░▀░░░
░░░░░░░░░░░░▀▀▀▀▀▄▄█▄▄▀▀░░░░░░░░░░░░░░
░░░░░░░░░░░░░░░░░░░▀░░░░░░░░░░░░░░░░░░
""",
    """
────╪███████╪────╪███████
──╪███████████╪╪███████████
──██████████████████████████
─████████████████████████████
─████████████████████████████
─████████████████████████████
─████████████████████████████
──██████████████████████████
──╪████████████████████████
───╪██████████████████████
─────████████████████████
──────╪████████████████
────────╪████████████
──────────╪████████
─────────────╪██
████─╪███╪╪████████──████─████
╪███─╪███─████╪████──████─████
─███─╪███─████─╪███╪─████─████
─███╪╪██╪─████─╪███╪─████─████
─╪██████──████─╪███╪─████─████
──██████──████─╪███╪─████─████
──█████╪──████─╪███╪─████─████
──╪████───████─╪███╪─████─████
───████───████─╪███╪─████─████
──╪████───████─╪███╪─████─████
──╪████───████─╪███╪─████─████
──╪████───████─╪███╪─████─████
──╪████───█████████──█████████
───████────███████╪──╪███████
""",
    """
───▄▄▄▄▄▄─────▄▄▄▄▄▄
─▄█▓▓▓▓▓▓█▄─▄█▓▓▓▓▓▓█▄
▐█▓▓▒▒▒▒▒▓▓█▓▓▒▒▒▒▒▓▓█▌
█▓▓▒▒░╔╗╔═╦═╦═╦═╗░▒▒▓▓█
█▓▓▒▒░║╠╣╬╠╗║╔╣╩╣░▒▒▓▓█
▐█▓▓▒▒╚═╩═╝╚═╝╚═╝▒▒▓▓█▌
─▀█▓▓▒▒░░░░░░░░░▒▒▓▓█▀
───▀█▓▓▒▒░░░░░▒▒▓▓█▀
─────▀█▓▓▒▒░▒▒▓▓█▀
──────▀█▓▓▒▓▓█▀
────────▀█▓█▀
──────────▀
""",
    """
░███████░
░█╬╬╬╬╬█░
░██╬╬███░
░██╬╬███░
░██╬╬███░
░█╬╬╬╬╬█░
░███████░
░███████░
░███████░
░███████░
░█╬╬████░
░█╬╬████░
░█╬╬████░
░█╬╬████░
░█╬╬╬╬╬█░
░███████░
░█╬╬╬╬╬█░
░█╬███╬█░
░█╬███╬█░
░█╬███╬█░
░█╬╬╬╬╬█░
░███████░
░█╬╬█╬╬█░
░█╬╬█╬╬█░
░█╬╬█╬╬█░
░█╬╬█╬╬█░
░██╬╬╬██░
░███████░
░█╬╬╬╬╬█░
░█╬╬████░
░█╬╬╬╬██░
░█╬╬████░
░█╬╬╬╬╬█░
░███████░
░███████░
░███████░
░███████░
░███████░
░█╬╬█╬╬█░
░█╬╬█╬╬█░
░██╬╬╬██░
░██╬╬╬██░
░██╬╬╬██░
░███████░
░█╬╬╬╬╬█░
░█╬███╬█░
░█╬███╬█░
░█╬███╬█░
░█╬╬╬╬╬█░
░███████░
░█╬███╬█░
░█╬███╬█░
░█╬███╬█░
░█╬███╬█░
░█╬╬╬╬╬█░
░███████░
""",
    '''
                /'    `\./'    `\
               (  o  o  |  u  u  )
               ;`.  V  /"\  V  .';
       """"\."     __ ) ( __     "./""""/
        \   ;     aP""Y,_,P""Ya     ;   /
         `,; ._  d'    `"'    `b  _. ;,'
      ,,,,aaaaaa.8,  I  Love  ,8.aaaaaa,,,,
      I8\\\\\\\\\`Y,   You   ,P'/////////8I
       "Ya\\\\\\\\\"Y,     ,P"/////////aY"
         "Ya\\\\\\\\\"Y,_,P"/////////aP"
           `"Ya\\\\\\\\`Y'////////aP"'
              `"""""""""""""""""""'
''',
    """
                         %%%%%%%%%%%%%
                         %%%%%%%%%%%%%
                             %%%%%
                             %%%%%
                             %%%%%
                             %%%%%
                             %%%%%
                             %%%%%
                             %%%%%
                         %%%%%%%%%%%%%
                         %%%%%%%%%%%%%




  ::::          ::::::      ::::      ::::    :::::::::
  ::::        ::::  ::::    ::::      ::::    :::::::::
  ::::       ::::    ::::   ::::      ::::    ::::
  ::::       ::::    ::::    ::::    ::::     ::::::::
  ::::       ::::    ::::     ::::  ::::      ::::
  ::::       ::::    ::::      ::::::::       ::::
  ::::::::::  ::::  ::::        ::::::        :::::::::
  ::::::::::    ::::::           ::::         :::::::::


                   Y O U
""",
    """
           ..//``~~~~~-=+=-=+~~~~\\.      .//~~~~=-=+=-~~~~~''\\..
       ..//=+=-=+=-=+=-=+=-=+=-=+=-\\    //=+=-=+=-=+=-=+=-=+=-=+=\\..
      //+=-=+=-=+=-=+=-=+=-=+=-=+=-=+\\//=-=+=-=+=-=+=-=+=-=+=-=+=-=+\\
    //-=+=-=+=-=+=-=+=-=+=-=+=-=+=-=+=-=+=-=+=-=+=-=+=-=+=-=+=-=+=-=+=-\\
   ++=-=+=-=+=-=+=-=+=-=+=-=+=-=+=-=+=-=+=-=+=-=+=-=+=-=+=-=+=-=+=-=+=-=++
   ||~~\    /~~~\/~~~\   /~~~\/~~~\   /~~~\/~~~\   /~~~\/~~~\   /~~~\/~~||
   ||  /    \        /   \        /   \        /   \        /   \       ||
   ||/        \    /       \    /       \    /       \    /       \    /||
   ||           \/           \/           \/           \/           \/  ||
   ++=-=+=-=+=-=+=-=+=-=+=-=+=-=+=-=+=-=+=-=+=-=+=-=+=-=+=-=+=-=+=-=+=-=++
    \\-=+=-=+=-=+=-=+=-=+=-=+=-=+=-=+=-=+=-=+=-=+=-=+=-=+=-=+=-=+=-=+=-=//
      `\\=-=+=-=+=-=+=-=+=-=+=-=+=-=+=-=+=-=+=-=+=-=+=-=+=-=+=-=+=-=+//'
        |`\\+=-=+=-=+=-=+=-=+=-=+=-=+=-=+=-=+=-=+=-=+=-=+=-=+=-=+=//'
        |   `\\=+=-=+=-=+=-=+=-=+=-=+=-=+=-=+=-=+=-=+=-=+=-=+=//''
        |      ``\\=+=-=+=-=+=-=+=-=+=-=+=-=+=-=+=-=+=-=+=//''
   _____|_____     ``\\=+=-=+=-=+=-=+=-=+=-=+=-=+=-=+=//''     
  |   I Love  |        ``\\=+=-=+=-=+=-=+=-=+=-=+=//''
  |    You.   |            ``\\=+=-=+=-=+=-=+=//''
  |   * HUG*  |                ``\\=+=-=+=//''
   ~~~~~~~~~~~                     ``\\//''
""",
    """
                  IIIIIIIIIII
                  IIIIIIIIIII
                      III
                      III
                      III
                      III
                      III
                  IIIIIIIIIII
                  IIIIIIIIIII

LLL          OOOOOOOO    VV       VV  EEEEEEEEEE
LLL         OOOOOOOOOO   VV       VV  EEEEEEEEEE
LLL         OO      OO   VV       VV  EE
LLL         OO      OO   VV       VV  EE
LLL         OO      OO   VV       VV  EEEEEEE
LLL         OO      OO    VV     VV   EE
LLL         OO      OO     VV   VV    EE
LLLLLLLLLL  OOOOOOOOOO      VV VV     EEEEEEEEEE
LLLLLLLLLL   OOOOOOOO         V       EEEEEEEEEE

        YY      YY   OOOOOOOO   UUU    UUU
         YY    YY   OOOOOOOOOO  UUU    UUU
          YY  YY    OO      OO  UUU    UUU
           YYYY     OO      OO  UUU    UUU
            YY      OO      OO  UUU    UUU
            YY      OO      OO  UUU    UUU
            YY      OO      OO  UUU    UUU
            YY      OOOOOOOOOO  UUUUUUUUUU
            YY       OOOOOOOO    UUUUUUUU
""",
    """
██─▄███▄███▄─██▄──▄██──▄███▄──██──██
██─█████████──▀████▀──██▀─▀██─██──██
██──▀█████▀─────██────██▄─▄██─██──██
██────▀█▀───────██─────▀███▀──▀████
""",
    '''
‎_/)______./¯"""/') ___/)___/)__,-----------’)_• ___/)_/)__./¯/)/)
¯¯\)¯¯¯¯¯'\_„„„„\) ¯\)¯¯¯¯¯\)¯¯‘-----------.)¯• ¯\)¯¯¯¯\)¯'\_\)\)
██░░░██░░░░▄███▄░░██░░░██░████░░░██░░██
██░░░██░░░██▀░▀██░██▄░▄██░██▄░░░░██░░██
██░░░██░░░██▄░▄██░░██▄██░░██▀░░░░██░░██
██░░░████░░▀███▀░░░░███░░░████░░░▀████▀
_/)______./¯"""/') ___/)___/)__,-----------’)_• ___/)_/)__./¯/)/)
¯¯\)¯¯¯¯¯'\_„„„„\) ¯\)¯¯¯¯¯\)¯¯‘-----------.)¯• ¯\)¯¯¯¯\)¯'\_\)\)
''',
    """
▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒
▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒
▒▒▒▒▒▒▒░░░░░░═░░▒▒▒▒░░░░░░▒▒▒░░░░═░▒▒▒▒▒▒
▒▒▒▒▒▒░████████▓░▒▒░░█████░══█████▓═░▒▒▒▒
▒▒▒▒▒░▓█████████░▒░█████████████████░▒▒▒▒
▒▒▒▒▒▒░░░▒███░▒░▒░▒██████████████████═▒▒▒
▒▒▒▒▒▒▒░░═███═░▒▒░███████████████████░▒▒▒
▒▒▒▒▒▒▒▒▒░███░▒▒▒░███████████████████░▒▒▒
▒▒▒▒▒▒▒▒▒░███═▒▒▒░▒██████████████████░▒▒▒
▒▒▒▒▒▒▒▒▒░███░▒▒▒▒═█████████████████═▒▒▒▒
▒▒▒▒▒▒▒▒▒░███░▒▒▒▒▒─███████████████░░▒▒▒▒
▒▒▒▒▒▒▒▒░═███═░▒▒▒▒▒─█████████████═░▒▒▒▒▒
▒▒▒▒▒▒░░░▒███░▒░▒▒▒▒▒░░█████████▒═▒▒▒▒▒▒▒
▒▒▒▒▒░▒█████████═▒▒▒▒▒░═░█████▒═░▒▒▒▒▒▒▒▒
▒▒▒▒▒▒░████████▒░▒▒░░░▒▒░═░▓▒═░▒▒▒▒░▒▒▒▒▒
▒▒▒▒▒▒░░░░░░░░░░▒▒░░░░░░░▒░░═░░░░░░░░░▒▒▒
▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒░█████████─██████████░▒▒
▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒░█████████═▒████████░░▒▒
▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒░░░─███▒─▒░─███░═░░░▒▒▒
▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒─███▒░─███░░▒▒▒▒▒▒▒
▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒─███═███▒░▒▒▒▒▒▒▒▒
▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒─█████▒░▒▒▒▒▒▒▒▒▒
▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒─████═▒▒▒▒▒▒▒▒▒▒
▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒░███═▒▒▒▒▒▒▒▒▒▒▒
▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒░░─███═══░▒▒▒▒▒▒▒▒
▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒░█████████▒░▒▒▒▒▒▒▒
▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒░█████████▓░▒▒▒▒▒▒▒
▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒░──────═░░▒▒▒▒▒▒▒▒
▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒░═▓█████▒═░▒▒▒▒▒▒▒▒
▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒═▒█████████░░▒▒▒▒▒▒▒
▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒═█████░░░████▒░▒▒▒▒▒▒
▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒░░███═░░▒░═░███═▒▒▒▒▒▒
▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒═███░░▒▒▒▒▒░▓███░▒▒▒▒▒
▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒░███═▒▒▒▒▒▒░░███░▒▒▒▒▒
▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒░███░░▒▒▒▒▒░▒███░▒▒▒▒▒
▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒░▒███─░▒▒░░═███░▒▒▒▒▒▒
▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒═████▒══░▓████░▒▒▒▒▒▒
▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒─██████████▓═▒▒▒▒▒▒▒
▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒░░███████═░▒▒▒▒▒▒▒▒
▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒░░░═───░───═░░░▒▒▒▒▒▒
▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒░▓██████─███████░▒▒▒▒▒
▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒░███████─███████░▒▒▒▒▒
▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒═▒███░░▒░░████─▒▒▒▒▒▒
▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒░░███═░▒▒░▒██▒░▒▒▒▒▒▒
▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒░▒███░▒▒▒░▓██▓░▒▒▒▒▒▒
▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒░▒███░▒▒▒░▓██▓░▒▒▒▒▒▒
▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒░▒███░▒▒▒░▒███░▒▒▒▒▒▒
▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒░▒███─░▒░═███▓░▒▒▒▒▒▒
▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒═████░░░████═▒▒▒▒▒▒▒
▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒─█████████═▒▒▒▒▒▒▒▒
▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒═▒█████▓─▒▒▒▒▒▒▒▒▒
▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒░░░░═░░▒▒▒▒▒▒▒▒▒▒
""",
    """
░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░
░░░░░░░▄▄▄▄▄▄░░░░░░░░░▄▄▄▄▄▄░░░░░░░░
░░░░▄▄▄▄░░░░▄▄▄▄░░░▄▄▄▄░░░░▄▄▄▄░░░░░
░▄▄▄▄░░░░░░░░░░░▄░▄░░░░░░░░░░░▄▄▄▄░░
▄▄░░░░░░░░░░░░░░░▄░░░░░░░░░░░░░░░▄▄░
▄▄░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░▄▄░
▄▄░▐█▀▀██▀▀▀█▀█▀█▀▀█▄▄▄▄▄▄▄▄▄▄▄▄░▄▄░
▄▄░▐█──██─█─█─█─█─▀█─█─█─█▀█─█─█░▄▄░
▄▄░▐█──██─▀─█▄─▄█─▀█──█──█▄█─█▄█░▄▄░
▄▄░▐█▄▄▄█▀▀▀▀▀▀▀▀▀▀▀████████████░▄▄░
░▄▄▄▄░░░░░░░░░░░░░░░░░░░░░░░░░▄▄▄▄░░
░░░▄▄▄▄░░░░░░░░░░░░░░░░░░░░░▄▄▄▄░░░░
░░░░░░▄▄▄▄░░░░░░░░░░░░░░░▄▄▄▄░░░░░░░
░░░░░░░░░▄▄▄▄░░░░░░░░░▄▄▄▄░░░░░░░░░░
░░░░░░░░░░░░▄▄▄▄░░░▄▄▄▄░░░░░░░░░░░░░
░░░░░░░░░░░░░░░▄▄▄▄▄░░░░░░░░░░░░░░░░
░░░░░░░░░░░░░░░░▄▄▄░░░░░░░░░░░░░░░░░
░░░░░░░░░░░░░░░░░▄░░░░░░░░░░░░░░░░░░
""",
]


@zedub.zed_cmd(pattern="احبك")
async def _(zedub):
    zzz = random.choice(love)
    return await edit_or_reply(zedub, zzz)


Fun7_cmd = (
"**╮•❐ اوامـر تسليـه متحـركه 7 ⦂ **\n\n"
" ⌯╼═══❬ ᥉᥆υᖇᥴᥱ ᥉ᥱꪔ᥆ ❭═══╾⌯\n\n"
"  •  `.تهكير`\n\n"
"  •  `.احبك`\n\n"
"  •  `.لوف` + سمايل\n\n"
"  •  `.اكتب` + نص\n\n"
"  •  `.رساله` + نص او بالـرد ع نص\n\n"
" ⌯╼═══❬ ᥉᥆υᖇᥴᥱ ᥉ᥱꪔ᥆ ❭═══╾⌯\n\n"
"**- اضغـط ع الامـر لـ النسـخ"
)


@zedub.zed_cmd(pattern="تسليه7")
async def cmd(zelzallll):
    await edit_or_reply(zelzallll, Fun7_cmd)
