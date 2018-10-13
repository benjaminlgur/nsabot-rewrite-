#NSAbot using discord.py rewrite by Grunt67

import discord
import pymysql.cursors
import time
import datetime
import getpass
from discord.ext import commands
import nsahelp

pswd = getpass.getpass('Password:')

mydb = pymysql.connect(
  host="localhost",
  user="Admin",
  passwd=pswd
)
mycursor = mydb.cursor()

TOKEN = open('nsabottoken.txt', "rt")


client = discord.Client()

@client.event
async def on_ready():
    print("NSA Bot is ready.")
    print("Logged in as {0.user}".format(client))

@client.event
async def on_message(message):
    role_count = len(message.role_mentions)
    for x in range (0, role_count):
        game = message.role_mentions[x].name
        user = message.author.name
        server = message.guild.name
        weekday = nsahelp.out_week_day()
        date = nsahelp.out_date()
        time = nsahelp.out_time()
        sql = "INSERT INTO fsa.info(role, user, server, dayOfWeek, date, time) VALUES (%s, %s, %s, %s, %s, %s)"
        val = (game, user, server, weekday, date, time)
        try:
            mycursor.execute(sql, val)
            mydb.commit()
            print(mycursor.rowcount, "record inserted.")
        except:
            print("SQL server error")

client.run(TOKEN.read())