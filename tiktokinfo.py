
import requests
from bs4 import BeautifulSoup
from datetime import datetime
import telebot
from telebot import types
import os

BOT_TOKEN = os.getenv('BOT_TOKEN')
ADMIN = os.getenv('ADMIN')
CHANNEL = os.getenv('CHANNEL')
CHANNELS = os.getenv('CHANNELS')

bot = telebot.TeleBot(BOT_TOKEN)

def  check_file():
    try:
        open("member.txt","r")
    except:
        open("member.txt","a").close()
check_file()

def Inline_admin():
    Mains=types.InlineKeyboardMarkup()
    Mains.add(
    types.InlineKeyboardButton(text="إذاعة",callback_data="callmember")    ,
    types.InlineKeyboardButton(text="الإحصائيات",callback_data="member")
    )

    return Mains

def Inline():
    Mains = types.InlineKeyboardMarkup()
    Mains.row_width = 2
    Mains.add(
   types.InlineKeyboardButton("Developer", url=f"https://t.me/Z_0_G")
    )
    return Mains

def admin(IdAdmin):
    admin=ADMIN
    if str(IdAdmin)==(admin):
        result=True
    else:
        result=False
    return result


def check_join(id_member):

        read_file=open("member.txt","r").readlines()

        if str(id_member)+"\n" in (read_file):
            result=True
        else:
            result=False
        return result
def join(id,msg):
    sudo_id=ADMIN
    url = f"https://api.telegram.org/bot{BOT_TOKEN}/getchatmember?chat_id={CHANNEKS}&user_id={id}"
    req = requests.get(url)
    if id == sudo_id or 'member' in req.text or 'creator' in req.text or 'administartor' in req.text:
        result=True
    else:
        A = types.InlineKeyboardMarkup(row_width = 1)
        B = types.InlineKeyboardButton(text = f''' {CHANNEL} ''',url=f"https://t.me/{CHANNEL}")
        A.add(B)
        bot.send_message(msg, """*🚸| عذرا عزيزي
🔰| عليك الاشتراك بقناة البوت لتتمكن من استخدامه

- مــعرف القـناة : {}

‼️| اشترك ثم ارسل /start*""".format(ch),parse_mode="markdown",reply_markup=A)
        result=A
    return result

@bot.message_handler(commands=["start"])
def welcom(message):
    admins=ADMIN
    send=message.chat.id
    id=message.from_user.id
    first_name = message.from_user.first_name
    username = message.from_user.username

    if join(id,message.chat.id) == True:
        if admin(id) == True:
            bot.send_message(send,text="لوحة ادمن",reply_markup=Inline_admin())


        if (check_join(id))== False:
                numb=len(open("member.txt","r").readlines())

                bot.send_message(admins, text=f'''
⌯ New member entry to your bot ⌯
⌯⌯⌯⌯⌯⌯⌯⌯⌯⌯⌯⌯⌯⌯⌯⌯⌯⌯⌯⌯⌯⌯⌯⌯⌯⌯⌯
⌯ name: {first_name}
⌯ username: @{username}
⌯ id: {id}
⌯ The number of total members: {numb}
⌯⌯⌯⌯⌯⌯⌯⌯⌯⌯⌯⌯⌯⌯⌯⌯⌯⌯⌯⌯⌯⌯⌯⌯⌯⌯⌯⌯
''', parse_mode="html", disable_web_page_preview=True)
                saeve=open("member.txt","a").write(str(id)+"\n")

        bot.send_message(send,text='''
Welcome in bot information of TikTok send your username
اهلا بك في بوت معلومات التيك توك ارسل يوزرك
''',reply_markup=Inline())


@bot.message_handler(func=lambda m: True)
def info(message):
    if message.chat.type == "private":
        you_ch = f"{CHANNEL}"
        idu = message.chat.id
        A = types.InlineKeyboardMarkup(row_width=1)
        B = types.InlineKeyboardButton(text=f''' {CHANNEL} ''', url=f"https://t.me/{CHANNEL}")
        A.add(B)
        join = requests.get(f"https://api.telegram.org/bot{BOT_TOKEN}/getChatMember?chat_id=@{you_ch}&user_id={idu}").text
        if '"status":"left"' in join:
            bot.send_message(message.chat.id, """
*🚸| عذرا عزيزي
🔰| عليك الاشتراك بقناة البوت لتتمكن من استخدامه

- مــعرف القـناة : {}

‼️| اشترك ثم ارسل /start*
""".format(ch), parse_mode="markdown", reply_markup=A)
        else:
            try:
                msg = message.text
                bot.reply_to(message, "wait...")
                username = f"{msg}"
                headers = {
                    "user-agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/110.0.0.0 Safari/537.36"
                }
                r = requests.get(f"https://www.tiktok.com/@{username}", headers=headers)
                server_log = str(r.text)
                soup = BeautifulSoup(server_log, 'html.parser')
                script = soup.find(id='SIGI_STATE')
                if script is None:
                    bot.send_message(message.chat.id, "Unable to find user information. Please check the username and try again.")
                    return
                data = str(script.contents).split('},"UserModule":{"users":{')[1]
                data_json = data
                userID = data.split('"id":"')[1].split('",')[0]
                name = data.split(',"nickname":"')[1].split('",')[0]
                secID = data.split(',"secUid":"')[1].split('"')[0]
                followers = data.split('"followerCount":')[1].split(',')[0]
                following = data.split('"followingCount":')[1].split(',')[0]
                likes = data.split('"heartCount":')[1].split(',')[0]
                videoCount = data.split('"videoCount":')[1].split(',')[0]
                signature = data.split('"signature":')[1].split(',')[0].strip('"\n')
                signature = signature.replace('\\n', ' ').replace('\n', ' ').replace('\\', ' ')
                flags = {
'AD': ' - 🇦🇩',
'AE': ' - 🇦🇪',
'AF': ' - 🇦🇫',
'AG': ' - 🇦🇬',
'AI': ' - 🇦🇮',
'AL': ' - 🇦🇱',
'AM': ' - 🇦🇲',
'AO': ' - 🇦🇴',
'AQ': ' - 🇦🇶',
'AR': ' - 🇦🇷',
'AS': ' - 🇦🇸',
'AT': ' - 🇦🇹',
'AU': ' - 🇦🇺',
'AW': ' - 🇦🇼',
'AX': ' - 🇦🇽',
'AZ': ' - 🇦🇿',
'BA': ' - 🇧🇦',
'BB': ' - 🇧🇧',
'BD': ' - 🇧🇩',
'BE': ' - 🇧🇪',
'BF': ' - 🇧🇫',
'BG': ' - 🇧🇬',
'BH': ' - 🇧🇭',
'BI': ' - 🇧🇮',
'BJ': ' - 🇧🇯',
'BL': ' - 🇧🇱',
'BM': ' - 🇧🇲',
'BN': ' - 🇧🇳',
'BO': ' - 🇧🇴',
'BQ': ' - 🇧🇶',
'BR': ' - 🇧🇷',
'BS': ' - 🇧🇸',
'BT': ' - 🇧🇹',
'BV': ' - 🇧🇻',
'BW': ' - 🇧🇼',
'BY': ' - 🇧🇾',
'BZ': ' - 🇧🇿',
'CA': ' - 🇨🇦',
'CC': ' - 🇨🇨',
'CD': ' - 🇨🇩',
'CF': ' - 🇨🇫',
'CG': ' - 🇨🇬',
'CH': ' - 🇨🇭',
'CI': ' - 🇨🇮',
'CK': ' - 🇨🇰',
'CL': ' - 🇨🇱',
'CM': ' - 🇨🇲',
'CN': ' - 🇨🇳',
'CO': ' - 🇨🇴',
'CR': ' - 🇨🇷',
'CU': ' - 🇨🇺',
'CV': ' - 🇨🇻',
'CW': ' - 🇨🇼',
'CX': ' - 🇨🇽',
'CY': ' - 🇨🇾',
'CZ': ' - 🇨🇿',
'DE': ' - 🇩🇪',
'DJ': ' - 🇩🇯',
'DK': ' - 🇩🇰',
'DM': ' - 🇩🇲',
'DO': ' - 🇩🇴',
'DZ': ' - 🇩🇿',
'EC': ' - 🇪🇨',
'EE': ' - 🇪🇪',
'EG': ' - 🇪🇬',
'EH': ' - 🇪🇭',
'ER': ' - 🇪🇷',
'ES': ' - 🇪🇸',
'ET': ' - 🇪🇹',
'FI': ' - 🇫🇮',
'FJ': ' - 🇫🇯',
'FK': ' - 🇫🇰',
'FM': ' - 🇫🇲',
'FO': ' - 🇫🇴',
'FR': ' - 🇫🇷',
'GA': ' - 🇬🇦',
'GB': ' - 🇬🇧',
'GD': ' - 🇬🇩',
'GE': ' - 🇬🇪',
'GF': ' - 🇬🇫',
'GG': ' - 🇬🇬',
'GH': ' - 🇬🇭',
'GI': ' - 🇬🇮',
'GL': ' - 🇬🇱',
'GM': ' - 🇬🇲',
'GN': ' - 🇬🇳',
'GP': ' - 🇬🇵',
'GQ': ' - 🇬🇶',
'GR': ' - 🇬🇷',
'GS': ' - 🇬🇸',
'GT': ' - 🇬🇹',
'GU': ' - 🇬🇺',
'GW': ' - 🇬🇼',
'GY': ' - 🇬🇾',
'HK': ' - 🇭🇰',
'HM': ' - 🇭🇲',
'HN': ' - 🇭🇳',
'HR': ' - 🇭🇷',
'HT': ' - 🇭🇹',
'HU': ' - 🇭🇺',
'ID': ' - 🇮🇩',
'IE': ' - 🇮🇪',
'IL': ' - 🇮🇱',
'IM': ' - 🇮🇲',
'IN': ' - 🇮🇳',
'IO': ' - 🇮🇴',
'IQ': ' - 🇮🇶',
'IR': ' - 🇮🇷',
'IS': ' - 🇮🇸',
'IT': ' - 🇮🇹',
'JE': ' - 🇯🇪',
'JM': ' - 🇯🇲',
'JO': ' - 🇯🇴',
'JP': ' - 🇯🇵',
'KE': ' - 🇰🇪',
'KG': ' - 🇰🇬',
'KH': ' - 🇰🇭',
'KI': ' - 🇰🇮',
'KM': ' - 🇰🇲',
'KN': ' - 🇰🇳',
'KP': ' - 🇰🇵',
'KR': ' - 🇰🇷',
'KW': ' - 🇰🇼',
'KY': ' - 🇰🇾',
'KZ': ' - 🇰🇿',
'LA': ' - 🇱🇦',
'LB': ' - 🇱🇧',
'LC': ' - 🇱🇨',
'LI': ' - 🇱🇮',
'LK': ' - 🇱🇰',
'LR': ' - 🇱🇷',
'LS': ' - 🇱🇸',
'LT': ' - 🇱🇹',
'LU': ' - 🇱🇺',
'LV': ' - 🇱🇻',
'LY': ' - 🇱🇾',
'MA': ' - 🇲🇦',
'MC': ' - 🇲🇨',
'MD': ' - 🇲🇩',
'ME': ' - 🇲🇪',
'MF': ' - 🇲🇫',
'MG': ' - 🇲🇬',
'MH': ' - 🇲🇭',
'MK': ' - 🇲🇰',
'ML': ' - 🇲🇱',
'MM': ' - 🇲🇲',
'MN': ' - 🇲🇳',
'MO': ' - 🇲🇴',
'MP': ' - 🇲🇵',
'MQ': ' - 🇲🇶',
'MR': ' - 🇲🇷',
'MS': ' - 🇲🇸',
'MT': ' - 🇲🇹',
'MU': ' - 🇲🇺',
'MV': ' - 🇲🇻',
'MW': ' - 🇲🇼',
'MX': ' - 🇲🇽',
'MY': ' - 🇲🇾',
'MZ': ' - 🇲🇿',
'NA': ' - 🇳🇦',
'NC': ' - 🇳🇨',
'NE': ' - 🇳🇪',
'NF': ' - 🇳🇫',
'NG': ' - 🇳🇬',
'NI': ' - 🇳🇮',
'NL': ' - 🇳🇱',
'NO': ' - 🇳🇴',
'NP': ' - 🇳🇵',
'NR': ' - 🇳🇷',
'NU': ' - 🇳🇺',
'NZ': ' - 🇳🇿',
'OM': ' - 🇴🇲',
'PA': ' - 🇵🇦',
'PE': ' - 🇵🇪',
'PF': ' - 🇵🇫',
'PG': ' - 🇵??',
'PH': ' - 🇵🇭',
'PK': ' - 🇵🇰',
'PL': ' - 🇵🇱',
'PM': ' - 🇵🇲',
'PN': ' - 🇵🇳',
'PR': ' - 🇵🇷',
'PS': ' - 🇵🇸',
'PT': ' - 🇵🇹',
'PW': ' - 🇵🇼',
'PY': ' - 🇵🇾',
'QA': ' - 🇶🇦',
'RE': ' - 🇷🇪',
'RO': ' - 🇷🇴',
'RS': ' - 🇷🇸',
'RU': ' - 🇷🇺',
'RW': ' - 🇷🇼',
'SA': ' - 🇸🇦',
'SB': ' - 🇸🇧',
'SC': ' - 🇸🇨',
'SD': ' - 🇸🇩',
'SE': ' - 🇸🇪',
'SG': ' - 🇸🇬',
'SH': ' - 🇸🇭',
'SI': ' - 🇸🇮',
'SJ': ' - 🇸🇯',
'SK': ' - 🇸🇰',
'SL': ' - 🇸🇱',
'SM': ' - 🇸🇲',
'SN': ' - 🇸🇳',
'SO': ' - 🇸🇴',
'SR': ' - 🇸🇷',
'SS': ' - 🇸🇸',
'ST': ' - 🇸🇹',
'SV': ' - 🇸🇻',
'SX': ' - 🇸🇽',
'SY': ' - 🇸🇾',
'SZ': ' - 🇸🇿',
'TC': ' - 🇹🇨',
'TD': ' - 🇹🇩',
'TF': ' - 🇹🇫',
'TG': ' - 🇹🇬',
'TH': ' - 🇹🇭',
'TJ': ' - 🇹🇯',
'TK': ' - 🇹🇰',
'TL': ' - 🇹🇱',
'TM': ' - 🇹🇲',
'TN': ' - 🇹🇳',
'TO': ' - 🇹🇴',
'TR': ' - 🇹🇷',
'TT': ' - 🇹🇹',
'TV': ' - 🇹🇻',
'TW': ' - 🇹🇼',
'TZ': ' - 🇹🇿',
'UA': ' - 🇺🇦',
'UG': ' - 🇺🇬',
'UM': ' - 🇺🇲',
'US': ' - 🇺🇸',
'UY': ' - 🇺🇾',
'UZ': ' - 🇺🇿',
'VA': ' - 🇻🇦',
'VC': ' - 🇻🇨',
'VE': ' - 🇻🇪',
'VG': ' - 🇻🇬',
'VI': ' - 🇻🇮',
'VN': ' - 🇻🇳',
'VU': ' - 🇻🇺',
'WF': ' - 🇼🇫',
'WS': ' - 🇼🇸',
'XK': ' - 🇽🇰',
'YE': ' - 🇾🇪',
'YT': ' - 🇾🇹',
'ZA': ' - 🇿🇦',
'ZM': ' - 🇿🇲',
    }
                region = data.split('"region":"')[1].split('"')[0]
                if region in flags:
                    region += flags[region]
                checkverified = data.split('"verified":')[1].split(',')[0]

                checkprivate = data.split('"privateAccount":')[1].split(',')[0]
                is_verified = "Yes ✅" if checkverified == "true" else "No ❌"
                is_private = "Yes ✅" if checkprivate == "true" else "No ❌"
                time = data.split('"nickNameModifyTime":')[1].split(',')[0]
                lastchangeuser = datetime.fromtimestamp(int(time))

                url_id = int(userID)
                binary = "{0:b}".format(url_id)
                bits = ""
                for i in range(min(len(binary), 31)):
                    bits += binary[i]
                    timestamp = int(bits, 2)
                    dt_object = datetime.fromtimestamp(timestamp)
                    meta_tags = soup.find_all('meta', {'property': 'og:image'})
                    profile = None
                    for tag in meta_tags:
                        if 'content' in tag.attrs:
                            profile = tag['content']
                            break
                if profile:
#                    reply_message = f'''𖡋 username » @{username}
#'''
                    bot.send_photo(message.chat.id, profile, caption=f'''𖡋 username » @{username}

𖡋 name » {name}

𖡋 Followers » {followers}

𖡋 Following » {following}

𖡋 Likes » {likes}

𖡋 change name » {lastchangeuser}

𖡋 Bio » {signature}

𖡋 User create time » {dt_object}

𖡋 Account region » {region}

𖡋 UserID » {userID}

𖡋 Verified » {is_verified}

𖡋 Private » {is_private}''', parse_mode='html', reply_to_message_id=message.message_id)
                else:
                    bot.send_message(message.chat.id, "Profile picture not found.")

            except Exception as e:
                bot.send_message(message.chat.id, f"ERROR!")
#An error occurred: {str(e)}


@bot.callback_query_handler(func=lambda call:True)
def callback(call):
    if call.data == "member":
        member=len(open("member.txt","r").readlines())
        result=f"عدد اعضاء {member}"
        bot.edit_message_text(text=result,chat_id=int(ADMIN), message_id=call.message.message_id)

    if call.data == "callmember":
        welcom=bot.reply_to(call.message,text="- Send Text .")
        bot.register_next_step_handler(welcom,Call)
def Call(message):
    admins=ADMIN
    msg=message.text
    starting=bot.send_message(admins,"Starting...")
    read_file=open("member.txt","r")
    lins=0
    for line in read_file.readlines():
        bot.send_message(line,text=msg)
        lins+=1
        result=f"جاري إذاعة الى الاعضاء\n تم إذاعة الى : {lins}"
    bot.edit_message_text(text=result,chat_id=int(admins), message_id=starting.message_id)

print("bot is running..")
bot.polling()
