import azure.functions as func
import logging
from .main import funcao_teste

app = func.FunctionApp()

@app.timer_trigger(schedule="0 */5 * * * *", arg_name="myTimer", run_on_startup=True)
def timer_trigger(myTimer: func.TimerRequest) -> None:
    logging.info('Executando função de teste...')
    funcao_teste()
