import azure.functions as func
import logging
import datetime

app = func.FunctionApp()

try:
    from .main import funcao_teste
except Exception as e:
    logging.error(f"Erro ao importar main.py: {e}")

@app.timer_trigger(schedule="0 */5 * * * *", arg_name="myTimer", run_on_startup=True, use_monitor=False)
def timer_trigger_teste(myTimer: func.TimerRequest) -> None:
    logging.info('O gatilho do timer foi disparado.')
    
    try:
        funcao_teste()
        logging.info('funcao_teste executada com sucesso.')
    except Exception as e:
        logging.error(f"Erro na execucao da funcao_teste: {e}")
