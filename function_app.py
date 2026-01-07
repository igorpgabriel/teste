import azure.functions as func
import datetime
import logging
from main import funcao_teste

app = func.FunctionApp()

@app.timer_trigger(schedule="0 */5 * * * *", arg_name="myTimer", run_on_startup=True, use_monitor=False)
def timer_trigger(myTimer: func.TimerRequest) -> None:
    if myTimer.past_due:
        logging.info('O agendamento está atrasado!')
    
    logging.info('Iniciando chamada da funcao_teste...')
    funcao_teste()
    logging.info('Script executado com sucesso.')
