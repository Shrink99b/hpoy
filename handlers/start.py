import asyncio

from helpers.filters import command
from config import BOT_NAME as bn, BOT_USERNAME as bu, SUPPORT_GROUP, OWNER_USERNAME as me, START_IMG
from pyrogram import Client, filters
from pyrogram.types import Message, InlineKeyboardMarkup, InlineKeyboardButton


@Client.on_message(command("start") & filters.private & ~filters.group & ~filters.edited)
async def start_(client: Client, message: Message):
    
    await message.reply_photo(
        photo=f"{START_IMG}",
        caption=f"""**🌈 ʜɪᴇᴇ ᴊᴀᴀɴ {message.from_user.mention()} !

        ᴛʜɪs ɪs [{bn}](t.me/{bu}), Aɴ ᴀᴅᴠᴀɴᴄᴇ ᴍᴜsɪᴄ ʙᴏᴛ😍


┏━━━━━━━━━━━━━━━
┣Ⓒⓡⓔⓐⓣⓔⓓ ⓑⓨ: [@Dark_vs_soldier]
┣6𝘁𝗵-𝗚𝗲𝗻 𝗶𝗻𝗯𝘂𝗶𝗹𝘁 𝘀𝘆𝘀𝘁𝗲𝗺😍
┣༒︎𝗛𝗶𝘁𝗲𝗰𝗵 𝗘𝗻𝗴𝗶𝗻𝗲༒︎
┣💞𝐋𝐚𝐠 𝐟𝐫𝐞𝐞 & 𝐮𝐥𝐭𝐫𝐚 𝐪𝐮𝐚𝐥𝐢𝐭𝐲💞
┣𝗠𝗼𝗿𝗲 𝗳𝗲𝗮𝘂𝘁𝘂𝗿𝗲𝘀 𝘀𝗼𝗼𝗻
┣𝗕𝗲𝗰𝗼𝗺𝗲 𝗩𝗶𝗽 𝘂𝘀𝗲𝗿 & 𝘁𝗼 𝗴𝗲𝘁 𝗲𝘅𝗰𝗶𝘁𝗶𝗻𝗴 𝗳𝗲𝗮𝘂𝘁𝘂𝗿𝗲𝘀 
┗━━━━━━━━━━━━━━━

🌈 ꜰᴏʀ ᴀɴʏ ǫᴜᴇʀɪᴇs ᴅᴍ @Dark_vs_soldier 💦**""",
    reply_markup=InlineKeyboardMarkup(
            [
                [
                    InlineKeyboardButton(
                        "𝐀𝐝𝐝 𝐤𝐫𝐨𝐨 𝐧𝐚𝐚 𝐣𝐚𝐚𝐚𝐧 😘", url=f"https://t.me/{bu}?startgroup=true"
                       ),
                  ],[
                    InlineKeyboardButton(
                        "👑 ᴏᴡɴᴇʀ 👑", url="https://t.me/Dark_vs_soldier"
                    ),
                    InlineKeyboardButton(
                        "🍒 sᴜᴘᴘᴏʀᴛ 🍒", url="https://t.me/we_love_each"
                    )
                ],[
                    InlineKeyboardButton(
                        "💦 ᴛsʜ ᴄʟᴀɴ 💦", url= "https://t.me/TSH_CLA"
                    ),
                    InlineKeyboardButton(
                        "🍑 sᴏᴜʀᴄᴇ ᴄᴏᴅᴇ🍑", url="https://github.com/Pkginstalls"
                    )]
            ]
       ),
    )

