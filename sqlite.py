# -*- coding: utf-8 -*-
"""
Created on Sun Oct 23 17:20:20 2022

@author: user
"""

import sqlite3

connection = sqlite3.connect('hotel.db')
cursor = connection.cursor()

sql = """ SELECT * FROM Hotel; """

cursor.execute(sql)

sql2 = """ SELECT guestName, guestAddress FROM Guest ORDER BY guestName ASC;"""
            
cursor.execute(sql2)

sql3 = """SELECT Room.price, Room.roomtype FROM Room, Hotel WHERE room.hotelno=Hotel.hotelNo AND Hotel.hotelName='Grosvenor Hotel' GROUP BY Room.roomtype; """

cursor.execute(sql3)

sql4 = """SELECT MAX(price), MIN(price), AVG(price) FROM Room;"""