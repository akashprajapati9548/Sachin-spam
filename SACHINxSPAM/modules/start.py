# ©️ @WTF_NoHope || @WTF_NoHope
from telethon import __version__, events, Button
from config import X1, X2, X3, X4, X5, X6, X7, X8, X9, X10

START_OP = [
    [
        Button.url("🍁 AKASH", "https://t.me/Akash_Daksh1c"),
        Button.url("MUSIC BOT 🕸️", "https://t.me/AD_Creation_Chatzone")
    ],
    [
        Button.inline("🥀 ʜᴇʟᴘ ᴀɴᴅ ᴄᴏᴍᴍᴀɴᴅs 🥀", data="help_back")
    ],
    [
        Button.url("✨ ᴜᴘᴅᴀᴛᴇ", "https://t.me/Sanatani_Network"),
        Button.url("sᴜᴘᴘᴏʀᴛ ❄️", "https://t.me/AD_Creation_Chatzone")
    ],
    [
        Button.url("🌸 ᴊᴏɪɴ ғᴏʀ sᴜᴅᴏ 🌸", "https://t.me/AD_Creation_Chatzone")
    ],
]

@X1.on(events.NewMessage(pattern="/start"))
@X2.on(events.NewMessage(pattern="/start"))
@X3.on(events.NewMessage(pattern="/start"))
@X4.on(events.NewMessage(pattern="/start"))
@X5.on(events.NewMessage(pattern="/start"))
@X6.on(events.NewMessage(pattern="/start"))
@X7.on(events.NewMessage(pattern="/start"))
@X8.on(events.NewMessage(pattern="/start"))
@X9.on(events.NewMessage(pattern="/start"))
@X10.on(events.NewMessage(pattern="/start"))
async def start(event):
    if event.is_private:
        KEX = await event.client.get_me()
        bot_name = KEX.first_name
        bot_id = KEX.id
        TEXT = f"**╭────── ˹ ɪɴғᴏʀᴍᴀᴛɪᴏɴ ˼ ⏤͟͟͞͞‌‌‌‌★**\n**┆**\n**┊◍ ʜᴇʏ : [{event.sender.first_name}] **\n**┆◍ ɪ ᴀᴍ : [{bot_name}](tg://user?id={bot_id}) **\n**┊**\n**┆● sᴀɴᴀᴛᴀɴɪ NETWORK :** `0.2`\n**┊● ᴛᴇʟᴇᴛʜᴏɴ ᴠᴇʀsɪᴏɴ :** `8.2.5.1.01`\n**╰─────────────────────────**\n**──────────────────────────**\n**⦿ Oᴡɴᴇʀ - [🦋⃟‌AKASH 🌸](https://t.me/Akash_Daksh1c) | [🦋⃟‌AKASH 🌸](https://t.me/AD_Creation_Chatzone) **\n**──────────────────────────**\n**    ❖ Uᴘᴅᴀᴛᴇ's ⏤͟͟͞͞‌‌‌‌ [❖ ∣ Sᴀɴᴀᴛᴀɴɪ Network ∣ ❖](https://t.me/Sanatani_Network) **\n**──────────────────────────**"
        await event.client.send_Full
                    event.chat_id,  
                    "https://telegra.ph//file/7cfeff721589b61a2f634.jpg",
                    caption=TEXT, 
                    buttons=START_OP
                )
