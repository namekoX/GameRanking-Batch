from configparser import ConfigParser
import mysql.connector
import sys
import os
import datetime

class DbUtil(object):
    def __init__(self):
        self.app_home = os.path.abspath(os.path.join( os.path.dirname(os.path.abspath(__file__)) , ".." ))
        self.prog_name = os.path.splitext(os.path.basename(__file__))[0]
        self.config = ConfigParser()
        self.conf_path = os.path.join(self.app_home,"conf", self.prog_name + ".conf")
        self.config.read(self.conf_path)
        self.cnn = mysql.connector.connect(host=self.config.get("db","host"),
                                  port=self.config.get("db","port"),
                                  db=self.config.get("db","db"),
                                  user=self.config.get("db","user"),
                                  passwd=self.config.get("db","passwd"),
                                  charset=self.config.get("db","charset")
                                  )

    def select_entry(self):
        cur = self.cnn.cursor()

        from_id = 45
        to_id = 999

        cur.execute("""SELECT PREF_CD,PREF_NAME FROM t01prefecture
                    WHERE PREF_CD BETWEEN %s AND %s""" , (from_id, to_id, ))
        rows = cur.fetchall()
        for row in rows:
            print("%d %s" % (row[0], row[1]))
        cur.close()

        return self.config.get("db","host")

    def insert_entry(self, entry):
        cur = self.cnn.cursor()
        today = datetime.date.today().strftime('%Y-%m-%d')
        cur.execute("""INSERT INTO gameranking_entry(prat_form, game_name, ranking, description, link, image, create_at, update_at)
                    VALUES (%s, %s, %s, %s, %s, %s, %s, %s)""" , (entry.prat_form, entry.game_name, entry.rank, entry.description, entry.link, entry.image, today, today))
        cur.close()
        self.cnn.commit()

    def conClose(self):
        self.cnn.close()

class Entry:
    def __init__(self, prat_form, game_name, rank, description, link, image):
        self.prat_form = prat_form
        self.game_name = game_name
        self.rank = rank
        self.description = description
        self.link = link
        self.image = image
