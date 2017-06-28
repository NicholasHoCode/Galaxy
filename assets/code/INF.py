from flask import Flask
from flask import g
from flask import Response
from flask import request
import json
import mysql.connector

from flask import Flask
from flask import g
from flask import Response
from flask import request

# REST SERVICES

app = Flask(__name__)

# enter your db credentiials

@app.before_request
def db_connect():
  g.conn  =  MySQLdb.connect(host='',
                              user='',
                              passwd='',
                              db='fb')
  g.cursor = g.conn.cursor()

@app.after_request
def db_disconnect(response):
  g.cursor.close()
  g.conn.close()
  return response

def query_db(query, args=(), one=False):
  g.cursor.execute(query, args)
  rv = [dict((g.cursor.description[idx][0], value)
  for idx, value in enumerate(row)) for row in g.cursor.fetchall()]
  return (rv[0] if rv else None) if one else rv

# HTTP request / REST call to get all the influencers
@app.route("/influencers", methods=['GET'])
def influencers():
    # get the value of the authenticated user's fb_id (i.e. ?fb_id =<some id>)
    fb_id = request.args.get('fb_id')

# HTTP request / REST call to get the most influential member from the database
@app.route("/influencers/most_influential", methods=['GET'])
def most_influential():
  result = query_db("SELECT influencerID FROM (SELECT influencerID, MAX(confidenceRATING) AS HighestRating FROM influencers)")
  data = json.dumps(result)
  resp = Response(data, status=200, mimetype='application/json')
  return resp

if __name__ == '__main__':
    app.run()



#install python facebook sdk library
import facebook

data = {'friends': [{'id': '876543', 'name': 'Sergey Rizhikov'}, {'id': '23456', 'name': 'Andrey Borisenko'}, {'id': '234117432', 'name': 'Shane Kimbrough'}, {'id': '3245683', 'name': 'Oleg Novitskiy'}, {'id': '13674321', 'name': 'Thomas Pesquet'}, {'id': '8752457775', 'name': 'Peggy Whitson'}], 'message': 'success', 'friends_no': 6}
# (1) iterate through the authenticated user's friend-list and retrieve their user id in json format and put them in a list
f_id = []

for y in range(0, data['friends_no']):
	f_id.append(data['friends'][y]['id'])

# iteratively retrieve the mututal number of friends for each of the authenticated user's friend with the user ids obtained from the previous step (1)

m_l = []

#for i in f_id:
    # response = getFriendNetwork(f_id)
    # data = response.json()
#    m_l.append(data['mutual_friend_number'])

# after iterating through the loop for each user id (friend 1 .... 6 .json files) we obtain the following list (please see the attached doc - sample_friends_json_format)

m_l = [5, 4, 2, 1, 5, 2]

# iteratively retrieve the total number of friends for each of the authenticated user's friend with the user ids obtained from the previous step (1)

t_l = []

t_l = [342, 736, 432, 125, 642, 1000]

# assign weight for component m (mutual friends)

weight_m = 0.8

# assign weight for component t (total number of friends)

weight_t = 0.2

# compute the weighted score for each of the authenticated user's friend

import numpy as np
w_l = [[m_l],[t_l]]
w_l = np.array(w_l)
w_l[0] = w_l[0] * weight_m
w_l[1]=w_l[1]*weight_t
w_l = w_l[0] + w_l[1]
w_l = w_l[0]

# compute the normalizing factor for the confidence rating

normalizing_factor = 1/sum(w_l)

# the normalized list consists of confidence ratings in the range of : 0 - 1

n_l = [x * normalizing_factor for x in w_l]

# set the threshold to be g.t 1/len(n_l) ensure that the "individual" is considered as "influential"

threshold = 1/len(n_l)

# find the position where the ratings are above the threshold

pos = [i for i in range(0,len(n_l)) if (n_l[i]>=threshold)]

# find the actual ratings that are above the threshold

cfr = [i for i in n_l if (i>threshold)]

cfr = np.array(cfr).tolist()

# this list consists of corresponding user that has ratings above the threshold

filtered = []

for x in range(0,len(f_id)):
	for i in pos:
		if (i == x):
			filtered.append(f_id[i])

# create a dictionary with key being the influencer's id and value being the influencer's confidence rating

in_dict = {}

for i in range(0,len(filtered)):
	in_dict[filtered[i]]=cfr[i]

# print user: confidence	

import operator
sorted_dict = sorted(in_dict, key=in_dict.get, reverse=True)
for r in sorted_dict :
    print('user_id', 'confidence')
    print(r+':', in_dict[r])

# first create schema 'fb' in MySQL db

# connect to SQL server
db = mysql.connector.connect(host='localhost', database = 'fb', user='root',password='')
cursor = db.cursor()
cursor.execute('''USE fb''')
db.commit()

# drop any pre-existing tables with the name "Influencer"
cursor.execute('''DROP TABLE IF EXISTS Influencer''')
db.commit()

#create the Influencer table
cursor.execute('''CREATE TABLE Influencer
             (influencerID decimal(20), confidenceRATING float(20))''')
db.commit()

# insert dictionary into MySQL
for i in in_dict.items():
        influencer_id = i[0]
        confidence_rating = i[1]
        sql = '''INSERT INTO Influencer (influencerID, confidenceRATING) VALUES (%s, %s)'''
        cursor.execute(sql, (influencer_id, confidence_rating))
        db.commit()


