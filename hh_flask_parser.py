import multiprocessing as ml
from hh_parser.parser_app import main as pr

from hh_parser import create_app

if __name__ == "__main__":
    # Создать приложение Flask
    app = create_app()

    par_service = ml.Process(name="HH API Parser", target=pr.main)
    par_service.start()

    # Запустить Flask приложение
    app.run()
