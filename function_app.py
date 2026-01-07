import azure.functions as func
import logging
import datetime

# Importação correta para o ambiente Linux do Azure
try:
    from .main import funcao_teste
except Exception as e:
    logging.error(f"Falha no import inicial: {e}")

app = func.FunctionApp()

@app.timer_trigger(schedule="0 */1 * * * *", arg_name="myTimer", run_on_startup=True, use_monitor=False)
def timer_trigger_teste(myTimer: func.TimerRequest) -> None:
    logging.info('O gatilho do timer foi disparado.')
    
    # Tentativa de importação local caso a global falhe
    try:
        from .main import funcao_teste
        funcao_teste()
        logging.info('funcao_teste executada com sucesso.')
    except Exception as e:
        logging.error(f"Erro na execucao da funcao_teste: {e}")
