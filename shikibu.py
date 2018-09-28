import os
import tweepy
from credentials import *
import time

file_direction = "/home/cirulinas/Documentos/SCRIPTING/REPOS/Bot/quotes.txt"
auth = tweepy.OAuthHandler("kX06DzKmjUVISgqgYMo4LUQOj",
                           "NUCNwsMhmZO5z47sl4u4SV3dMGtO3unMyUMlMxKUnIGdesgfT8")
auth.set_access_token("1045141160082182144-XFUVY48LRsGDNkt4fdluAWvss8XDhN",
                      "rm7bRdEknOja8ZjcYffDk4pb1LwfGVjSkkVRTEVr1kFPs")
api = tweepy.API(auth)

try:
    os.mknod("saves.txt")
except FileExistsError:
    pass

with open(file_direction) as file:
    for line in file:
        saves = open('saves.txt', 'r+')

        if line not in saves.readlines():

            api.update_status(status=line)
            saves.write(line)
            print("twitteado")
            time.sleep(30)

    saves.close()
