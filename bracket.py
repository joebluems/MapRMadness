#!/usr/bin/python
import csv
import random
import re
import math
import sys

#################
## read args ####
#################
weights=[0.5]
if len(sys.argv)>1: weights.append(float(sys.argv[1]))
else: weights.append(0.5)

#####################################
## read season data and load stats ##
#####################################
season="cbb2015_noheader.csv"
id={}
names={}
with open(season, 'rb') as csvfile:
  lines = csv.reader(csvfile)
  for row in lines:
	id[row[0]]=row
	names[row[1]]=row[0]

###########################################
### determine winner of individual game ###
###########################################
def playgame(details):
  team1=details[1]
  team2=details[3]
  if details[4] in seeds[details[2]]: prob1=float(re.sub(r'%','',seeds[details[2]][details[4]]))/100
  elif details[2] in seeds[details[4]]: prob1=1-float(re.sub(r'%','',seeds[details[4]][details[2]]))/100
  else: prob1=0.5
  prob0=0.5
  prob = (weights[0]*prob0+weights[1]*prob1)/sum(weights)
  if random.random()<prob1: return team1,details[2]
  else: return team2,details[4]

#####################################
### read historical seed matchups ###
#####################################
seedfile="seeds.csv"
seeds={}
with open(seedfile, 'rb') as csvfile:
  lines = csv.reader(csvfile)
  for row in lines:
    if row[0] not in seeds: seeds[row[0]]={}
    if row[1] not in seeds[row[0]]: seeds[row[0]][row[1]]=row[2]
	

#######################################################
## ROUND 0 (play-in round) requires special handling ##
#######################################################
round0={}
bracket0 = "bracket2015_round0.csv"
with open(bracket0, 'rb') as csvfile:
  lines = csv.reader(csvfile)
  for row in lines:
     winner,rank = playgame(row)
     print row[0],": ",winner,id[winner][1] 
     round0[row[5]]=winner+","+rank

#####################################
## ROUND 1 also requires handling ###
#####################################
bracket = "bracket2015.csv"
games={}
with open(bracket, 'rb') as csvfile:
  lines = csv.reader(csvfile)
  for row in lines:
     ### complete bracket from round1 ###
     if row[0] in round0: 
	for a in round0[row[0]].split(','):
	  row.append(a)
     winner,rank = playgame(row)
     print row[0],": ",winner,id[winner][1]
     ### move winner to the next round ###
     rnum,gnum = re.sub(r'g','',row[0]).split('_')
     rnew = int(rnum)+1
     gnew = int(math.ceil(float(gnum)/2))
     if rnew not in games: games[rnew]={}
     if gnew not in games[rnew]: 
	games[rnew][gnew]=[]
	games[rnew][gnew].append("g"+str(rnew)+"_"+str(gnew))
     games[rnew][gnew].append(winner)
     games[rnew][gnew].append(rank)

################
## ROUNDS 2-6 ##
################
for r in 2,3,4,5,6:
  for a in games[r]:
    winner,rank = playgame(games[r][a])
    print games[r][a][0],": ",winner,id[winner][1]
    rnum,gnum = re.sub(r'g','',games[r][a][0]).split('_')
    rnew = int(rnum)+1
    gnew = int(math.ceil(float(gnum)/2))
    if rnew not in games: games[rnew]={}
    if gnew not in games[rnew]:
      games[rnew][gnew]=[]
      games[rnew][gnew].append("g"+str(rnew)+"_"+str(gnew))
    games[rnew][gnew].append(winner)
    games[rnew][gnew].append(rank)

