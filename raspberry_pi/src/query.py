import sqlite3
import time
import feed
import sql
from config import DB_PATH

conn = sqlite3.Connection(DB_PATH)


def start_query() -> None:
    """
    This function is used to start the query.
    """
    global conn
    history = [] # Use for avoid duplicate feeding.
    while True:
        now_time = time.localtime()
        plans = sql.get_plan(conn.cursor())
        now_hours = now_time.tm_hour
        now_minutes = now_time.tm_min
        if (now_hours == 0) and (now_minutes == 0):
            history = []
        for plan in plans:
            # Check for feeding time.
            
            hours = plan[0]
            minutes = plan[1]
            weight = plan[2]
            if (now_hours == hours) and (now_minutes == minutes):
                feeded = 0
                for plan in history:
                    if (hours == plan[0]) and (minutes == plan[1]):
                        feeded = 1
                if feeded == 0:
                    feed.feed(weight)
                    history.append((hours, minutes))


if __name__ == "__main__":
    start_query()
