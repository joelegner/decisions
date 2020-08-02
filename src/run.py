from PySide2 import QtWidgets
import sys
from view.mainwin import MainWin
import logging

if __name__ == "__main__":
    # TODO: Wrap in try catch block
    # TODO: Send argv to the _run() function
    logging.basicConfig(filename="decisions.log",
                        filemode='a',
                        format='%(asctime)s.%(msecs)d %(filename)s:%(lineno)s %(levelname)s %(message)s',
                        datefmt='%H:%M:%S',
                        level=logging.DEBUG)
    logging.info("Starting Qt application")
    app = QtWidgets.QApplication([])
    window = MainWin()
    window.resize(800, 600)
    logging.info("Show window")
    window.show()
    sys.exit(app.exec_())
