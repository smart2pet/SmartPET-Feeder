import sqlite3
import log

def add_plan(
    hours: int, minutes: int, amount: int, cursor: sqlite3.Cursor
):
    """
    Add a plan to the database.
    :param hours: The number of hours to run the plan.
    :param minutes: The number of minutes to run the plan.
    :param amount: The amount of the food (in gram).
    :param cursor: The cursor to the database.
    """
    print(
        f"INSERT INTO plan (hours, minutes, weights) VALUES ({hours}, {minutes}, {amount});"
    )
    cursor.execute(
        "INSERT INTO plan (hours, minutes, weights) VALUES (?, ?, ?);",
        (hours, minutes, amount)
    )
    log.add_plan(hours, minutes, amount)
    


def del_plan(
    hours: int, minutes: int, cursor: sqlite3.Cursor
) -> None:
    """
    Delete a plan from the database.
    :param hours: The hours of the plan.
    :param minutes: The minutes of the plan.
    :param cursor: The cursor of the database.
    """
    print(f"DELETE FROM plan WHERE hours = {hours} and minutes = {minutes};")
    cursor.execute("DELETE FROM plan WHERE hours = ? and minutes = ?;", (hours, minutes))
    log.del_plan(hours, minutes)


def get_plan(cursor: sqlite3.Cursor) -> list[tuple]:
    """
    Get the plan from the database.
    :param cursor: The cursor to the database.
    :return: The plan.
    """
    cursor.execute("SELECT * FROM plan;")
    return cursor.fetchall()


def add_to_history(
    hours: int,
    minutes: int,
    weight: float,
    year: int,
    month: int,
    day: int,
    cursor: sqlite3.Cursor,
):
    """
    Add a new entry to the history table.
    Args:
        hours: The hours.
        minutes: The minutes.
        weight: The weight of the food.
        year: The year of the entry.
        month: The month of the entry.
        day: The day of the entry.
        cursor: The cursor to the database.
    """
    print(
        f"INSERT INTO history (hours, minutes, weight, year, month, day) VALUES ({hours}, {minutes}, {weight}, {year}, {month}, {day});"
    )
    cursor.execute(
        "INSERT INTO history (hours, minutes, weight, year, month, day) VALUES (?, ?, ?, ?, ?, ?);",
        (hours, minutes, weight, year, month, day),
    )
    cursor.close()


def get_total_feed_amount_today(
    year: int,
    month: int,
    day: int,
    cursor: sqlite3.Cursor,
) -> int:
    """
    Get the total feed today.
    :param year: The year.
    :param month: The month.
    :param day: The day.
    :param cursor: The cursor.
    :return: The total feed today.
    """
    cursor.execute(
        "SELECT SUM(weight) FROM history WHERE year = ? and month = ? and day = ?;", 
        (year, month, day)
    )
    return cursor.fetchone()


def get_total_feed_amount_this_month(year, month, day, cursor: sqlite3.Cursor):
    """
    Get the total feed this month.
    Args:
        year (int): The year.
        month (int): The month.
        day (None): Ignored but for compat with web_api.py.
        cursor (sqlite3.Cursor): The cursor.
    Returns:
        int: The total feed this month.
    """
    cursor.execute(
        "SELECT SUM(weight) FROM history WHERE year = ? and month = ?;",
        (year, month)
    )
    return cursor.fetchone()


def get_average_feed_amount_last_month(year, month, day, cursor: sqlite3.Cursor):
    """
    Get the average feed weight for the last month.

    Args:
        year (int): The year.
        month (int): The month.
        day (int): Look at get_total_feed_this_month(year, month, day, cursor: sqlite3.Cursor). 
        cursor (sqlite3.Cursor): The database cursor.

    Returns:
        float: The average feed weight for the last month.
    """
    if month > 1:
        cursor.execute(
            "SELECT AVG(weight) FROM history WHERE year = ? and month = ?;",
            (year, month - 1),
        )
        return cursor.fetchone()
    return 0


def get_total_feed_amount_this_year(year, month, day, cursor: sqlite3.Cursor):
    """
    Get the total feed this year.
    Args:
        year (int): The year to get the total feed for.
        cursor (sqlite3.Cursor): The cursor to use to execute the query.
    Returns:
        int: The total feed this year.
    """
    cursor.execute("SELECT SUM(weight) FROM history WHERE year = ?;", (year,))
    return cursor.fetchone()
