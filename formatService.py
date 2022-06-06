import discord
from parsingService import textClean

def formatEmbed(jsonReq, info):
  printTxt = ""
  for i in range(info[2]-1,info[3]):
    printTxt = printTxt + "<**" + str(i+1) + "**> " + textClean(jsonReq["text"][i]) + " "

  name = jsonReq["ref"] + ":" + str(info[2])
  if info[2] < info[3]:
    name = name + "-" + str(info[3])
  embed = discord.Embed(
    title = name,
    description = printTxt
  )
  return embed