#NSAbot using discord.py rewrite by Grunt67 made for python 3.7

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
    #code for role mentions.
    role_count = len(message.role_mentions)
    for x in range (0, role_count):
        game = message.role_mentions[x].name
        user = message.author.display_name
        server = message.guild.name
        channel = message.channel.name
        weekday = nsahelp.out_week_day()
        date = nsahelp.out_date()
        time = nsahelp.out_time()
        sql = "INSERT INTO fsa.roleinfo(role, user, server, channel, dayOfWeek, date, time) VALUES (%s, %s, %s, %s, %s, %s, %s)"
        val = (game, user, server, channel, weekday, date, time)
        try:
            mycursor.execute(sql, val)
            mydb.commit()
            print(mycursor.rowcount, "record inserted.")
        except:
            print("SQL server error")
    #code for user mentions
    member_count = len(message.mentions)
    for x in range (0, member_count):
        ping = message.mentions[x].display_name
        user = message.author.display_name
        server = message.guild.name
        channel = message.channel.name
        weekday = nsahelp.out_week_day()
        date = nsahelp.out_date()
        time = nsahelp.out_time()
        sql = "INSERT INTO fsa.pinginfo(ping, user, server, channel, dayOfWeek, date, time) VALUES (%s, %s, %s, %s, %s, %s, %s)"
        val = (ping, user, server, channel, weekday, date, time)
        try:
            mycursor.execute(sql, val)
            mydb.commit()
            print(mycursor.rowcount, "record inserted.")
        except:
            print("SQL server error")

client.run(TOKEN.read())