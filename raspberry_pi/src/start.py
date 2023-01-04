from multiprocessing import Process
import query
import ui
import web_api

if __name__ == "__main__":
    query_process = Process(target=query.main)
    ui_process = Process(target=ui.main)
    web_api_process = Process(target=web_api.main)
    query_process.start()
    ui_process.start()
    web_api_process.start()
