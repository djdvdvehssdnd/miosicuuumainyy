import asyncio

import os
import time
import requests
from config import START_IMG_URL
from pyrogram import filters
import random
from pyrogram import Client
from pyrogram.types import Message, InlineKeyboardMarkup, InlineKeyboardButton, ReplyKeyboardMarkup
from strings.filters import command
from AnonX import (Apple, Resso, SoundCloud, Spotify, Telegram, YouTube, app)
from AnonX import app
from random import  choice, randint

                
@app.on_message(
    command(["مطورين سي ار","المطورين","مطورين","مطورين cr"])
    & ~filters.edited
)
async def huhh(client: Client, message: Message):
    await message.reply_photo(
        photo=f"https://f.top4top.io/p_3320c0elg1.jpg",
        caption=f"""**⩹━★⊷━⌞ 𓏺 V!a . ⌝━⊶★━⩺**\nمرحبا بك عزيزي {message.from_user.mention} في قسم مطورين cr ميوزك\nللتحدث مع مطورين اضغط علي الازرار بالاسفل👇\n**⩹━★⊷━⌞ 𓏺 V!a . ⌝━⊶★━⩺**""",
        reply_markup=InlineKeyboardMarkup(
            [
                [
                    InlineKeyboardButton(
                        "᳒𝙏َِ𝙊َِ𝙈َِّّ ", url=f"https://t.me/Ss_sQS"), 
                 ],[
                    InlineKeyboardButton(
                        "ρ᥆kᥱꪔ᥆ꪀ", url=f"https://t.me/devpokemon"),
                ],[
                    InlineKeyboardButton(
                        "𝐶𝑅𝐼𝑆𝑇𝐼𝑁", url=f"https://t.me/dr_criss"),
                    InlineKeyboardButton(
                        "ꪔᥲ️ꪀ᥆᥆", url=f"https://t.me/C1_I_I"),
                ],[
                
                    InlineKeyboardButton(
                        "★⌞ 𓏺 V!a . ⌝⚡", url=f"https://t.me/nissv"),
                ],

            ]

        ),

    )








@app.on_message(
    command(["توم انجم","احمد","توم","مبرمج","TOM","tom"])
    & filters.group
    & ~filters.edited
)
async def yas(client, message):
    usr = await client.get_chat("Ss_sQS")
    name = usr.first_name
    photo = await app.download_media(usr.photo.big_file_id)
    await message.reply_photo(photo,       caption=f"**⩹━★⊷━⌞ 𓏺 V!a . ⌝━⊶★━⩺\n\n‍ ¦ᦔꫀꪜ :{name}\n ¦ꪊ𝘴ꫀ𝘳 :@{usr.username}\n ¦Ꭵժ :`{usr.id}`\n ¦ႦᎥ᥆ :{usr.bio}\n\n**⩹━★⊷━⌞ 𓏺 V!a . ⌝━⊶★━⩺**", 
    reply_markup=InlineKeyboardMarkup(
            [
                [
                    InlineKeyboardButton(
                        name, url=f"https://t.me/{usr.username}")
                ],
            ]
        ),
    )


@app.on_message(
    command(["زين انجم","زين","زين","بوكمان","pokmon","pokman"])
    & filters.group
    & ~filters.edited
)
async def yas(client, message):
    usr = await client.get_chat("devpokemon")
    name = usr.first_name
    photo = await app.download_media(usr.photo.big_file_id)
    await message.reply_photo(photo,       caption=f"**⩹━★⊷━⌞ 𓏺 V!a . ⌝━⊶★━⩺\n\n¦ᦔꫀꪜ :{name}\n ¦ꪊ𝘴ꫀ𝘳 :@{usr.username}\n ¦Ꭵժ :`{usr.id}`\n ¦ႦᎥ᥆ :{usr.bio}\n\n**⩹━★⊷━⌞ 𓏺 V!a . ⌝━⊶★━⩺**", 
    reply_markup=InlineKeyboardMarkup(
            [
                [
                    InlineKeyboardButton(
                        name, url=f"https://t.me/{usr.username}")
                ],
            ]
        ),
    )


@app.on_message(
    command(["كريستين انجم","كريستين","كرستين","الدكتوره","cristin","كرستينه"])
    & filters.group
    & ~filters.edited
)
async def yas(client, message):
    usr = await client.get_chat("dr_criss")
    name = usr.first_name
    photo = await app.download_media(usr.photo.big_file_id)
    await message.reply_photo(photo,       caption=f"**⩹━★⊷━⌞ 𓏺 V!a . ⌝━⊶★━⩺\n\n‍ ¦ᦔꫀꪜ :{name}\n ¦ꪊ𝘴ꫀ𝘳 :@{usr.username}\n ¦Ꭵժ :`{usr.id}`\n ¦ႦᎥ᥆ :{usr.bio}\n\n**⩹━★⊷━⌞ 𓏺 V!a . ⌝━⊶★━⩺**", 
    reply_markup=InlineKeyboardMarkup(
            [
                [
                    InlineKeyboardButton(
                        name, url=f"https://t.me/{usr.username}")
                ],
            ]
        ),
    )
    

@app.on_message(
    command(["مانو انجم","مانو","الممول","mano","Mano"])
    & filters.group
    & ~filters.edited
)
async def yas(client, message):
    usr = await client.get_chat("C1_I_I")
    name = usr.first_name
    photo = await app.download_media(usr.photo.big_file_id)
    await message.reply_photo(photo,       caption=f"**⩹━★⊷━⌞ 𓏺 V!a . ⌝━⊶★━⩺\n\n ¦ᦔꫀꪜ :{name}\n ¦ꪊ𝘴ꫀ𝘳 :@{usr.username}\n ¦Ꭵժ :`{usr.id}`\n ¦ႦᎥ᥆ :{usr.bio}\n\n**⩹━★⊷━⌞ 𓏺 V!a . ⌝━⊶★━⩺**", 
    reply_markup=InlineKeyboardMarkup(
            [
                [
                    InlineKeyboardButton(
                        name, url=f"https://t.me/{usr.username}")
                ],
            ]
        ),
    )
    


@app.on_message(
    command(["/api"])
    & ~filters.edited
    
)
async def huhh(client: Client, message: Message):
    await message.reply_photo(
        photo=f"https://f.top4top.io/p_3320c0elg1.jpg",
        caption=f"""**⩹⊷━⌞ 𓏺 V!a . ⌝━━⩺**\nمرحبا بك عزيزي {message.from_user.mention} في قسم الذكاء الاصتناعي الخاص بسورس cr\nلتتمكن من استخدام اوامر الذكاء الاصتناعي اكتب \n /gpt + السؤال بالاسفل👇\n**⩹━━⌞ 𓏺 V!a . ⌝━━⩺**""",
        reply_markup=InlineKeyboardMarkup(
            [
                [
                    InlineKeyboardButton(
                        "᳒𝙏َِ𝙊َِ𝙈َِّّ", url=f"https://t.me/Ss_sQS"), 
                 ],[
                
                    InlineKeyboardButton(
                        "★⌞ 𓏺 V!a . ⌝⚡", url=f"https://t.me/nissv"),
                ],

            ]

        ),

    )



@app.on_message(
    command(["قرأن"])
    & ~filters.edited
    
)
async def huhh(client: Client, message: Message):
    await message.reply_photo(
        photo=f"https://f.top4top.io/p_3320c0elg1.jpg",
        caption=f"""**⩹⊷━⌞ 𓏺 V!a . ⌝━━⩺**\nمرحبا بك عزيزي {message.from_user.mention} في قسم تشغيل القرأن الخاص بسورس cr\nلتتمكن من استخدام اوامر القرأن اكتب \n سورة + اسم السورة بالاسفل👇\n**⩹━━⌞ 𓏺 V!a . ⌝━━⩺**""",
        reply_markup=InlineKeyboardMarkup(
            [
                [
                    InlineKeyboardButton(
                        "᳒aSaL", url=f"https://t.me/Ss_sQS"), 
                 ],[
                
                    InlineKeyboardButton(
                        "★⌞ 𓏺 V!a . ⌝⚡", url=f"https://t.me/nissv"),
                ],

            ]

        ),

    )



    
