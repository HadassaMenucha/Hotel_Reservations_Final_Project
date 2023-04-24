import sqlalchemy
import pandas as pd
import logging
from sqlalchemy.orm import sessionmaker

import sql.db_info as db_info #this file has the dbinfo:server,db,etc.
#This class is to connect to the database
class DbCon:
    def __init__(self):
            self.m_sServer = db_info.server
            self.m_sDriver = db_info.driver
            self.m_sDb = db_info.database
            self.m_bConnected = False
    def Connect(self):
        self.create_engine()
        #engine = sqlalchemy.create_engine('mssql+pyodbc://{}/{}?driver={}'.format(self.m_sServer, self.m_sDb, driver))
        self.m_oConn = self.m_engine.raw_connection()
        #self.m_oSession = Session(sessionmaker(bind=self.m_engine,autocommit=False))
        Session = sessionmaker(bind=self.m_engine,autocommit=False)
        self.m_oSession = Session()
        self.m_bConnected = True

    def create_engine(self):
        s = 'mssql+pyodbc://@' + self.m_sServer + '/' + self.m_sDb + '?trusted_connection=yes&driver='+self.m_sDriver
        self.m_engine = sqlalchemy.create_engine(s)
    def Disconnect(self):
        if self.m_bConnected:
            self.m_oConn.cursor().close()
            self.m_oSession.close_all()
            self.m_engine.dispose()
            self.m_oConn.close()
            self.m_bConnected = False
    def ReadSqlQuery(self, sQuery):
        if (self.m_bConnected == False):
            print('Error: db found disconnected and will try to connect again while tryng to run a query')
            self.Connect()
            if (self.m_bConnected == False):
                print('Error: db disconnected while tryng to run a query')
        df = pd.read_sql_query(sQuery,self.m_engine)
        return df
    def insert_df(self, df_to_insert, s_table_name):
        #__init__() got multiple values for argument 'schema'
        df_to_insert.to_sql(s_table_name, con=self.m_engine, if_exists='append', index=False, chunksize=1000) #,
        self.m_oConn.cursor().commit()
   