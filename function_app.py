import azure.functions as func
import logging
import datetime
import sys
import os

app = func.FunctionApp()

@app.timer_trigger(schedule="0 */1 * * * *", arg_name="myTimer", run_on_startup=True, use_monitor=False)
def timer_trigger_teste(myTimer: func.TimerRequest) -> None:
    logging.info('O gatilho do timer foi disparado.')
    
    try:
        # Tenta importar o arquivo main.py que está na mesma pasta
        import main
        main.funcao_teste()
        logging.info('funcao_teste executada com sucesso.')
    except ImportError:
        # Se falhar (comum no Linux da Azure), tenta o import relativo
        from .main import funcao_teste
        funcao_teste()
        logging.info('funcao_teste executada com sucesso via import relativo.')
    except Exception as e:
        logging.error(f"Erro na execucao da funcao_teste: {e}")
