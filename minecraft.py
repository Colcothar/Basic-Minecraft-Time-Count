from mcstatus import MinecraftServer

import time
from datetime import datetime
import csv

server = MinecraftServer.lookup("51.195.188.94:25585")
#server = MinecraftServer.lookup("play.mishkacraft.co")

status = server.status()


print("The server has {0} players and replied in {1} ms".format(status.players.online, status.latency))

players =[["",0]]

with open('/home/pi/Documents/data2.csv', 'r') as file:
    reader = csv.reader(file, delimiter = ',')
    for row in reader:
        sub=[]
        for i in range(len(row)-1):
            if i == 0:
                sub.append(str(row[i]))
            else:
                sub.append(int(row[i]))
        players.append(sub)

 
print(players)

while True:
    try:
        status = server.status()
    except:
        time.sleep(300)
        status = server.status()
        
    print(status.players.sample)
    if status.players.sample != None:
        now = datetime.now()
        print(now.strftime("%H:%M:%S") )
        
        
        for player in status.players.sample:
            print(player.name)
            
            index =-1
            
            for i in range (len(players)):
                if players[i][0] == player.name:
                    index =1
                    players[i][int(now.strftime("%d"))+6] = players[i][int(now.strftime("%d"))+6] + int(5)
            if index ==-1:
                players.append([player.name,0,0,0,0,0,0,0,0,0,0])
                

       
    print(players)
    with open("/home/pi/Documents/data2.csv", "w") as f:
        for x in range (len(players)-1):
            line=""
            for y in range (len(players[x+1])):
                line  = line + str(players[x+1][y]) + ","
            f.write(line +"\n")
            
    time.sleep(300)
    
            
#print(dir(status.Players))


