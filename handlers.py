from telethon import events
from Haron_Bot import bot

@bot.on(events.ChatAction()) #Hello-massage when bot is added in chat
async def on_join(event: events.ChatAction.Event):
    if event.is_group and event.user_added and event.user_id==bot.me.id:
        await bot.send_massage(event.chat_id, 'Еще работенка для старого Хорона')


