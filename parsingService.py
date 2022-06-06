import re

CLEANDICT = {
  "<br>" : " ",
  "<sup>.<\/sup>.*?<\/i>" : "",
  "<sup class.*?</sup>" : ""
}
books = {
    "Genesis" : "Genesis",
    "Bereshit" : "Genesis",
    "Exodus" : "Exodus",
    "Shemot" : "Exodus",
    "Leviticus" : "Leviticus",
    "Vayikra" : "Leviticus",
    "Numbers" : "Numbers",
    "Bamidbar" : "Numbers",
    "Deuteronomy" : "Deuteronomy",
    "Devarim" : "Deuteronomy:",
    "Joshua" : "Joshua",
    "Yehoshua" : "Joshua",
    "Judges" : "Judges",
    "Shoftim" : "Judges",
    "I Samuel" : "1%20Samuel",
    "1 Samuel" : "1%20Samuel",
    "Samuel I" : "1%20Samuel",
    "Samuel 1" : "1%20Samuel",
    "Shmuel Aleph" : "1%20Samuel",
    "II Samuel" : "2%20Samuel",
    "2 Samuel" : "2%20Samuel",
    "Samuel II" : "2%20Samuel",
    "Samuel 2" : "2%20Samuel",
    "Shmuel Bet" : "2%20Samuel",
    "I Kings" : "1%20Kings",
    "1 Kings" : "1%20Kings",
    "Kings I" : "1%20Kings",
    "Kings 1" : "1%20Kings",
    "Melakhim Aleph" : "1%20Kings",
    "II Kings" : "2%20Kings",
    "2 Kings" : "2%20Kings",
    "Kings II" : "2%20Kings",
    "Kings 2" : "2%20Kings",
    "Melakhim Bet" : "2%20Kings",
    "Isaiah" : "Isaiah",
    "Yeshayahu" : "Isaiah",
    "Jeremiah" : "Jeremiah",
    "Jeremiah" : "Yirmiyahu",
    "Ezekiel" : "Ezekiel",
    "Yechezkel" : "Ezekiel",
    "Hosea" : "Hosea",
    "Hoshea" : "Hosea",
    "Joel" : "Joel",
    "Yoel" : "Joel",
    "Amos" : "Amos",
    "Obadiah" : "Obadiah",
    "Ovadiah" : "Obadiah",
    "Jonah" : "Jonah",
    "Yonah" : "Jonah",
    "Micah" : "Micah",
    "Micha" : "Micah",
    "Nahum" : "Nahum",
    "Habakkuk" : "Habakkuk",
    "Zephaniah" : "Zephaniah",
    "Haggai" : "Haggai",
    "Zechariah" : "Zechariah",
    "Malachi" : "Malachi",
    "Psalms" : "Psalms",
    "Psalm" : "Psalms",
    "Tehillim" : "Psalms",
    "Proverbs" : "Proverbs",
    "Proverb" : "Proverbs",
    "Mishlei" : "Proverbs",
    "Job" : "Job",
    "Iyov" : "Job",
    "Song of Songs" : "Song of Songs",
    "Song of Solomon" : "Song of Songs",
    "Shir Hashirim" : "Song of Songs",
    "Ruth" : "Ruth",
    "Lamentations" : "Lamentations",
    "Lamentation" : "Lamentations",
    "Eikhah" : "Lamentations",
    "Ecclesiastes" : "Ecclesiastes",
    "Kohelet" : "Ecclesiastes",
    "Esther" : "Esther",
    "Daniel" : "Daniel",
    "Ezra" : "Ezra",
    "Nehemiah" : "Nehemiah",
    "I Chronicles" : "1%20Chronicles",
    "1 Chronicles" : "1%20Chronicles",
    "Chronicles I" : "1%20Chronicles",
    "Chronicles 1" : "1%20Chronicles",
    "Divrei Hayamim Aleph" : "1%20Chronicles",
    "II Chronicles" : "2%20Chronicles",
    "2 Chronicles" : "2%20Chronicles",
    "Chronicles II" : "2%20Chronicles",
    "Chronicles 2" : "2%20Chronicles",
    "Divrei Hayamim Bet" : "2%20Chronicles",
  }
  
def checkBook(message: str):
  parsedData = ["",0,0,0] #Book name, chapter, start verse, end verse
  checkStr = ""
  parsedData[0] = ""
  parsedData[1] = 0
  index = 0
  maxNameLen = 21
  try:
    while index < min(len(message), maxNameLen) and parsedData[0] == "":
      checkStr = checkStr + message[index]
      if index+1 >= min(len(message), maxNameLen) or message[index+1] == " ":
        if checkStr in books:
          parsedData[0] = books[checkStr]
      index+=1
    
    if parsedData[0] == "":
      return False
    index+=1
    chTxt = ""
    while message[index] != ":":
      chTxt = chTxt + message[index]
      index+=1
    parsedData[1] = int(chTxt)
    index+=1
    versTxt = ""
    while index < len(message) and message[index].isnumeric():
      versTxt = versTxt + message[index]
      index+=1
    parsedData[2] = int(versTxt)
    parsedData[3] = parsedData[2]
    if index < len(message) and message[index] == "-":
      index+=1
      versTxt=""
      while index < len(message) and message[index].isnumeric():
        versTxt = versTxt + message[index]
        index+=1
      parsedData[3] = int(versTxt)
  except:
    print("error")
  else:
    print(parsedData[0], parsedData[1], parsedData[2],parsedData[3])
    if parsedData[0] != "" and parsedData[1] > 0 and parsedData[2] > 0 and parsedData[3] > 0:
      return [parsedData[0], parsedData[1], parsedData[2], parsedData[3]]
  return False


def textClean(message: str):
  cleantext = message
  for key, val in CLEANDICT.items():
    cleantext = re.sub(key, val, cleantext)
  return cleantext