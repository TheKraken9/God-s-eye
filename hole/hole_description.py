from database import database as database
from django.db import models
from django.contrib.gis.db import models


def cost(pk):
    conn = database.connect()
    cur1 = conn.cursor()
    # cur1.execute("select * from holedescri where nationalroute LIKE'%{}%'".format(pk))
    cur1.execute("select * from holedescri where beginroute LIKE'%{}%'".format(pk))
    rows = cur1.fetchall()
    sentence = []
    for row in rows:
        lv = level(row[5])
        levels = (lv/1000)
        height = ((row[3] - row[2])*1000) #longueur
        width = row[4] #largeur
        prices = price()
        new_title = f" pk{row[2]} <> pk{row[3]}"
        print(new_title)
        sentence.append(new_title)
        for pr in prices:
            mcube = ((height * width * levels))
            hour = ((mcube * pr[3]))
            result = ((mcube * pr[1]))
            new_sentence = f" => {mcube} m3 / fait en {hour} H / {pr[2]} : {result} Ar"
            sentence.append(new_sentence)
        cur1.close()
        conn.close()
    return sentence


def all_cost(pk):
    conn = database.connect()
    cur1 = conn.cursor()
    cur1.execute("select * from holedescri where nationalroute = '{}'".format(pk))
    # cur1.execute("select * from holedescri where beginroute LIKE'%{}%'".format(pk))
    rows = cur1.fetchall()
    sentence = []
    for row in rows:
        lv = level(row[5])
        levels = (lv/1000)
        print(levels)
        height = ((row[3] - row[2])*1000)
        print(height)
        width = row[4]
        print(width)
        prices = price()
        new_title = f" PK{row[2]} <> PK{row[3]} | {row[6]} - {row[7]}"
        print(new_title)
        sentence.append(new_title)
        for pr in prices:
            mcube = ((height * width * levels))
            hour = ((mcube * pr[3]))
            result = ((mcube * pr[1]))
            new_sentence = f" => {mcube} m3 / fait en {hour} H / {pr[2]} : {result} Ar"
            sentence.append(new_sentence)
        cur1.close()
        conn.close()
    return sentence


def all_all_cost(pk):
    conn = database.connect()
    cur1 = conn.cursor()
    cur1.execute("select * from holedescri where nationalroute LIKE'%{}%'".format(pk))
    # cur1.execute("select * from holedescri where beginroute LIKE'%{}%'".format(pk))
    rows = cur1.fetchall()
    sentence = []
    for row in rows:
        lv = level(row[5])
        levels = (lv/1000)
        height = ((row[3] - row[2])*1000)
        width = row[4]
        prices = price()
        new_title = f" PK{row[2]} <> PK{row[3]} | {row[6]} - {row[7]}"
        print(new_title)
        sentence.append(new_title)
        for pr in prices:
            mcube = ((height * width * levels))
            hour = ((mcube * pr[3]))
            result = ((mcube * pr[1]))
            new_sentence = f" => {mcube} m3 / fait en {hour} H / {pr[2]} : {result} Ar"
            sentence.append(new_sentence)
        cur1.close()
        conn.close()
    return sentence


def my_cost(pk):
    conn = database.connect()
    cur1 = conn.cursor()
    cur1.execute(pk)
    # cur1.execute("select * from holedescri where beginroute LIKE'%{}%'".format(pk))
    rows = cur1.fetchall()
    sentence = []
    for row in rows:
        lv = level(row[5])
        levels = (lv/1000)
        height = ((row[3] - row[2])*1000)
        width = row[4]
        prices = price()
        new_title = f" PK{row[2]} <> PK{row[3]} | {row[6]} - {row[7]}"
        print(new_title)
        sentence.append(new_title)
        for pr in prices:
            mcube = ((height * width * levels))
            hour = ((mcube * pr[3]))
            result = ((mcube * pr[1]))
            new_sentence = f" => {mcube} m3 / fait en {hour} H / {pr[2]} : {result} Ar"
            sentence.append(new_sentence)
        cur1.close()
        conn.close()
    return sentence


def price():
    conn = database.connect()
    cur = conn.cursor()
    cur.execute("select * from workmanship")
    rows = cur.fetchall()
    return rows


def level(lv):
    conn = database.connect()
    cur = conn.cursor()
    cur.execute("select * from holelevel where level = {}".format(lv))
    lvl = cur.fetchone()
    return lvl[2]


def mada():
    conn = database.connect()
    cur = conn.cursor()
    cur.execute("select * from madagascar_road")
    res = cur.fetchall()
    return res


def specified(rn):
    conn = database.connect()
    cur = conn.cursor()
    cur.execute(
        "select roadno, start_km, end_km, startdesc, enddesc from routes where roadno like '%{}%' order by roadno".format(
            rn))
    res = cur.fetchall()
    return res


def allSpecifiedRoad(rd):
    conn = database.connect()
    cur = conn.cursor()
    cur.execute("select roadno from route_fusion where roadno like '%{}%' group by roadno".format(rd))
    res = cur.fetchall()
    return res


def execute_request(req):
    conn = database.connect()
    cur = conn.cursor()
    cur.execute(req)
    res = cur.fetchall()
    return res


def decide(param):
    conn = database.connect()
    cur = conn.cursor()


def getAllRn():
    conn = database.connect()
    cur = conn.cursor()
    cur.execute("select roadno from route_fusion")
    res = cur.fetchall()
    return res


def getHoleDescription(rn):
    conn = database.connect()
    cur = conn.cursor()
    cur.execute("select * from holedescription where idroad = '{}'".format(rn))
    res = cur.fetchall()
    return res


def getGeomHoleDescription(id):
    conn = database.connect()
    cur = conn.cursor()
    cur.execute("SELECT ST_M(ST_LineLocatePoint(ST_LineMerge(geom), ST_StartPoint(ST_LineMerge(geom)))) AS pkbegin, ST_M( ST_LineLocatePoint(geom, ST_EndPoint(geom)) ) AS pkend FROM holedescription WHERE id = {}".format(id))
    res = cur.fetchall()
    return res


def getCalcul(geom, desc):
    conn = database.connect()
    cur = conn.cursor()
    cur.execute("SELECT distinct count(h.gid) as gid FROM environment h join description on h.id = description.id WHERE ST_DWithin(h.geom, {} , 1000) and idroad = {}".format(geom, desc))
    res = cur.fetchall()
    return res


def getGeomInternalHoleDescription(id):# atoooo
    conn = database.connect()
    cur = conn.cursor()
    cur.execute(
        "SELECT distinct h.gid as gid, h.name as name, h.geom as geom FROM environment h, holeintern r WHERE ST_DWithin(h.geom, r.geom, 1000) AND r.id = {}".format(id))
    res = cur.fetchall()
    return res