from .database_connect import DbCon
#from sqlalchemy_utils import database_exists, create_database
import sqlalchemy

def create_tables_from_df(df_reservations):
    db = DbCon()
    db.Connect()
    if not sqlalchemy.inspect(db.m_engine).has_table("Guest"):
        (df_guests,df_reservations) = split_df_reservations(df_reservations)
        db.insert_df(df_reservations, "Reservation")
        db.insert_df(df_guests, "Guest")

        db.Disconnect()
    
def split_df_reservations(df_reservations):
    df_reservations.insert(0, 'ReservationId', range(0, 0 + len(df_reservations)))
    #first arg len(df_reservations) instead of 0 untested. did this so GuestId is at end instead of beg.
    df_reservations.insert(len(df_reservations.axes[1]), 'GuestId', range(0, 0 + len(df_reservations)))
    df_guests = df_reservations[['GuestId', 'adults','children', 'babies', 'country']]
    df_reservations = df_reservations.drop(columns=['adults','children', 'babies', 'country'])
    return (df_guests,df_reservations)

def query(sql):
    db = DbCon()
    db.Connect()
    df_result = db.ReadSqlQuery(sql)
    return df_result
