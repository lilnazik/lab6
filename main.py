import sys
import matplotlib.pyplot as plt
from PySide6.QtWidgets import QApplication, QMainWindow
from PySide6.QtGui import QPixmap, QIcon
from UI.main_window import Ui_MainWindow

from services.calculations import euler_method, runge_kutta_method

class MainWindow(QMainWindow):
    def __init__(self):
        super(MainWindow, self).__init__()
        self.ui = Ui_MainWindow()
        self.ui.setupUi(self)
        self.setWindowTitle("Чисельне розв'язування звичайних диференціальних рівнянь")
        self.setWindowIcon(QIcon("ico.png"))
        
        self.ui.calc_btn.clicked.connect(self.calculate)
    
    def calculate(self):
        func_str = self.ui.function_input.text()
        y0 = self.ui.Y0SpinBox.value()
        x0 = self.ui.X0SpinBox.value()
        xn = self.ui.XnspinBox.value()
        step = self.ui.AccuracySpinBox.value()
        
        euler, runge = None, None
        
        if self.ui.radio_euler.isChecked():
            euler = euler_method(func_str, y0, x0, xn, step)
        elif self.ui.radio_runge_kutta.isChecked():
            runge = runge_kutta_method(func_str, y0, x0, xn, step)
        else:
            euler = euler_method(func_str, y0, x0, xn, step)
            runge = runge_kutta_method(func_str, y0, x0, xn, step)
        
        self.plot_chart(euler, runge)
    
    def plot_chart(self, euler, runge):
        plt.figure(figsize=(6, 4.5), dpi=100)
        
        if euler:
            plt.plot(euler[0], euler[1], label="Метод Ейлера", color="green")
            
        if runge:
            plt.plot(runge[0], runge[1], label="Метод Рунге-Кутта", color="blue")
            
        plt.xlabel("x")
        plt.ylabel("y")
        plt.title("Чисельне розв'язування звичайних диференціальних рівнянь")
        plt.legend()
        plt.grid(True)
        plt.savefig('plot.png')
        self.ui.img_place.setPixmap(QPixmap("plot.png"))


if __name__ == "__main__":
    app = QApplication(sys.argv)
    window = MainWindow()
    window.show()
    sys.exit(app.exec())