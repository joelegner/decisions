from PySide2 import QtWidgets
import sys
from view.startwin import StartWin
import logging
import linecache
import settings


def log_error():
    exc_type, exc_obj, tb = sys.exc_info()
    f = tb.tb_frame
    lineno = tb.tb_lineno
    filename = f.f_code.co_filename
    linecache.checkcache(filename)
    line = linecache.getline(filename, lineno, f.f_globals)
    msg = '{}:{} "{}"): {}'.format(filename, lineno, line.strip(), exc_obj)
    logging.error(msg)


if __name__ == "__main__":
    # TODO: Wrap in try catch block
    # TODO: Send argv to the _run() function
    logging.basicConfig(filename=settings.LOGFILENAME,
                        filemode='a',
                        format='%(asctime)s.%(msecs)d %(filename)s:%(lineno)s %(levelname)s %(message)s',
                        datefmt='%H:%M:%S',
                        level=logging.DEBUG)
    logging.info("Starting Qt application")

    try:
        app = QtWidgets.QApplication(sys.argv)
        main_window = StartWin()
        main_window.resize(
            settings.MAIN_WIN_SIZE[0], settings.MAIN_WIN_SIZE[1])
        logging.info("Show main_window")
        main_window.show()
        sys.exit(app.exec_())
    except Exception as e:
        log_error()
        raise
