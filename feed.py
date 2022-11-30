import sqlite3
import time
import _feed
import serial
import sql
import tflite_runtime.interpreter as tflite

try:
    feeder = serial.Serial("/dev/ttyUSB1", 115200)
except:
    # feeder = serial.Serial('/dev/ttyUSB0', 115200)
    pass
interpreter = tflite.Interpreter(model_path="model.tflite")
interpreter.allocate_tensors()
tflife_input_details = interpreter.get_input_details()
tflife_output_details = interpreter.get_output_details()


def feed(weight: int) -> None:
    """
    Feed the pet with the given weight.

    :param weight: The weight of the food.
    :type weight: int
    :return: None
    :rtype: None
    """
    conn = sqlite3.Connection("./smartpet.db")
    cursor = sqlite3.Cursor(conn)
    interpreter.set_tensor(tflife_input_details[0]["index"], [[weight - 5]])
    interpreter.invoke()
    custom = interpreter.get_tensor(tflife_output_details[0]["index"])
    print(custom)
    # _feed.feed(int(custom[0][0]), feeder)
    now_time = time.localtime()
    hours = now_time.tm_hour
    minutes = now_time.tm_min
    year = now_time.tm_year
    month = now_time.tm_mon
    day = now_time.tm_mday
    sql.add_to_history(hours, minutes, weight, year, month, day, cursor)
    conn.commit()
    conn.close()
