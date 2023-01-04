import sqlite3
import time
from typing import Dict

import feed
import sql
from fastapi import FastAPI
from pydantic import BaseModel
from config import DB_PATH
import uvicorn

app = FastAPI()


class Feed(BaseModel):
    weight: int


class Plan(BaseModel):
    time_h: int
    time_m: int
    weight: int


class Plan_time(BaseModel):
    time_h: int
    time_m: int


class Get_food(BaseModel):
    range: str

@app.get("/")
async def greeting():
    return 200

@app.post("/api/food")
async def feed_func(feed_argument: Feed) -> Dict[str, int]:
    """
    Feeds the pet with the given weight.

    Args:
        feed_argument: The weight of the food to feed the pet.

    Returns:
        A JSON with the result of the feeding.
    """
    feed.feed(feed_argument.weight)
    print(feed_argument)
    print("[INFO] Sent feeding request to feeder")
    return {"result": 0}


@app.post("/api/plan")
async def add_plan_func(plan_argument: Plan) -> Dict[str, int]:
    """
    Add a plan to the database.

    Args:
        plan_argument: The plan to be added.

    Returns:
        A dict containing the result of the operation.
    """
    if ((plan_argument.time_h >= 24) or (plan_argument.time_m >= 60)) or ((plan_argument.time_h < 0) or (plan_argument.time_m < 0)):
        print("[WARN] Client sent invalid data")
        return {"result": 1, "reason": "Data invalid."}
    else:
        with sqlite3.Connection(DB_PATH) as conn:
            cursor = sqlite3.Cursor(conn)
            sql.add_plan(
                plan_argument.time_h, plan_argument.time_m, plan_argument.weight, cursor
            )
            conn.commit()
            # conn.close()
        return {"result": 0}


@app.delete("/api/plan")
async def del_plan_func(plan_argument: Plan_time) -> Dict[str, int]:
    """
    Delete a plan from the database.

    Args:
        plan_argument: The plan to be deleted.

    Returns:
        A dictionary containing the result of the operation.
    """
    if (plan_argument.time_h >= 24) or (plan_argument.time_m >= 60):
        print("[WARN] Client sent invalid data")
        return {"result": 1, "reason": "Data invalid."}
    else:
        with sqlite3.Connection(DB_PATH) as conn:
            cursor = sqlite3.Cursor(conn)
            sql.del_plan(plan_argument.time_h, plan_argument.time_m, cursor)
            conn.commit()
            conn.close()
        return {"result": 0}


@app.get("/api/food")
async def get_food_amount(food_range: Get_food) -> int:
    """
    Get the food weight from the database.

    Args:
        food_range: The range of the food weight.

    Returns:
        The food weight.
    """
    with sqlite3.Connection(DB_PATH) as conn:
        cursor = sqlite3.Cursor(conn)
        now_time = time.localtime()
        year = now_time.tm_year
        month = now_time.tm_mon
        day = now_time.tm_mday
        result: int
        switcher = {
            "today": sql.get_total_feed_amount_today,
            "month": sql.get_total_feed_amount_this_month,
            "avg_month": sql.get_average_feed_amount_last_month,
            "year": sql.get_total_feed_amount_this_year,
        }
        get_total_feed = switcher.get(food_range.range, None) # Use dict to simply switch the condition. If you can't know what's
        # it means, just ignore it. 
        if get_total_feed is not None:
            result = get_total_feed(year, month, day, cursor)
            result = result[0]
            if result is None: result = 0
            result_dict = {"result": 0, "weight": result}
        else:
            result_dict = {"result": 1, "reason": "Range invalid."}

    return result_dict

def main():
    uvicorn.run(app, host="0.0.0.0", port=80)