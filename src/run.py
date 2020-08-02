from PySide2 import QtWidgets
import sys
from view.mainwin import MainWin

print(sys.path)

if __name__ == "__main__":
    # TODO: Wrap in try catch block
    # TODO: Send argv to the _run() function
    app = QtWidgets.QApplication([])
    window = MainWin()
    window.resize(800, 600)
    window.show()
    sys.exit(app.exec_())
