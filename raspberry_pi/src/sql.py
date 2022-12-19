import sqlite3


def add_plan(hours: int, minutes: int, weight: int, cursor: sqlite3.Cursor) -> None:
    """
    Add a plan to the database.
    :param hours: The number of hours to run the plan.
    :param minutes: The number of minutes to run the plan.
    :param weight: The weight of the plan.
    :param cursor: The cursor to the database.
    """
    print(
        f"INSERT INTO plan (hours, minutes, weights) VALUES ({hours}, {minutes}, {weight});"
    )
    cursor.execute(
        f"INSERT INTO plan (hours, minutes, weights) VALUES ({hours}, {minutes}, {weight});"
    )
    cursor.close()


def del_plan(hours: int, minutes: int, cursor: sqlite3.Cursor) -> None:
    """
    Delete a plan from the database.
    :param hours: The hours of the plan.
    :param minutes: The minutes of the plan.
    :param cursor: The cursor of the database.
    """
    print(f"DELETE FROM plan WHERE hours = {hours} and minutes = {minutes};")
    cursor.execute(f"DELETE FROM plan WHERE hours = {hours} and minutes = {minutes};")


def get_plan(cursor: sqlite3.Cursor) -> list:
    """
    Get the plan from the database.
    :param cursor: The cursor to the database.
    :return: The plan.
    """
    cursor.execute(f"SELECT * FROM plan;")
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
        f"INSERT INTO history (hours, minutes, weight, year, month, day) VALUES ({hours}, {minutes}, {weight}, {year}, {month}, {day});"
    )
    cursor.close()


def get_total_feed_today(
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
        f"SELECT SUM(weight) FROM history WHERE year = {year} and month = {month} and day = {day};"
    )
    return cursor.fetchone()


def get_total_feed_this_month(year, month, cursor: sqlite3.Cursor):
    """
    Get the total feed this month.

    Args:
        year (int): The year.
        month (int): The month.
        cursor (sqlite3.Cursor): The cursor.

    Returns:
        int: The total feed this month.
    """
    cursor.execute(
        f"SELECT SUM(weight) FROM history WHERE year = {year} and month = {month};"
    )
    return cursor.fetchone()


def get_average_feed_last_month(year, month, cursor: sqlite3.Cursor):
    if month > 1:
        cursor.execute(
            f"SELECT AVG(weight) FROM history WHERE year = {year} and month = {month - 1};"
        )
        return cursor.fetchone()
    return 0


def get_total_feed_this_year(year, cursor: sqlite3.Cursor):
    """
    Get the total feed this year.

    Args:
        year (int): The year to get the total feed for.
        cursor (sqlite3.Cursor): The cursor to use to execute the query.

    Returns:
        int: The total feed this year.
    """
    cursor.execute(f"SELECT SUM(weight) FROM history WHERE year = {year};")
    return cursor.fetchone()