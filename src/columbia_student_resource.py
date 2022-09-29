import pymysql

import os


class ColumbiaStudentResource:

    def __int__(self):
        pass

    @staticmethod
    def _get_connection():

        #usr = os.environ.get("root")
        #pw = os.environ.get("dbuserbdbuser")
        #h = os.environ.get("hw06156.cmm5ba669nkr.us-east-1.rds.amazonaws.com")

        conn = pymysql.connect(
            host="hw06156.cmm5ba669nkr.us-east-1.rds.amazonaws.com",
            port=3306,
            user="root",
            password="dbuserbdbuser",
            cursorclass=pymysql.cursors.DictCursor,
            autocommit=True)
        return conn

    @staticmethod
    def get_by_key(key):

        sql = "SELECT * FROM f22_databases.columbia_students where guid=%s";
        conn = ColumbiaStudentResource._get_connection()
        cur = conn.cursor()
        res = cur.execute(sql, args=key)
        result = cur.fetchone()

        return result

