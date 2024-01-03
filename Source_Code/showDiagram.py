import sys
from PyQt5 import QtGui
from PyQt5.QtWidgets import (
    QApplication,
    QMainWindow,
    QWidget,
    QPushButton,
    QLabel,
    QListWidget,
    QVBoxLayout,
    QGridLayout,
    QComboBox,
    QLineEdit,
    QDateEdit,
    QTabWidget,
    QHBoxLayout,
    QMessageBox,
    QDialog, 
    QListWidgetItem,
    QFormLayout,
)
from PyQt5.QtCore import QDate, Qt
import mysql.connector as mc
from datetime import datetime, timedelta
from matplotlib.backends.backend_qt5agg import FigureCanvasQTAgg as FigureCanvas
import matplotlib.pyplot as plt
import pandas as pd
from tkinter import filedialog
import os

class ShowDiagram(QWidget):
    def __init__(self, judul, sizes, labels):
        super().__init__()

        self.judul = judul
        self.sizes = sizes
        self.labels = labels
        
        self.setWindowTitle('Grafik Pemasukan dan Pengeluaran')
        self.setGeometry(850, 200, 400, 200)

        self.figure, self.axes = plt.subplots()
        self.canvas = FigureCanvas(self.figure)

        button_keluar = QPushButton("Keluar")
        button_keluar.clicked.connect(self.close)

        layout = QVBoxLayout()
        layout.addWidget(self.canvas)
        layout.addWidget(button_keluar)

        self.setLayout(layout)
        self.adjustSize()

        self.drawChart()

    def drawChart(self):
        self.axes.clear()
        bars = self.axes.bar(self.labels, self.sizes, color=['green', 'red'])
        self.axes.set_title(self.judul)
        self.axes.set_xlabel('Kategori')
        self.axes.set_ylabel('Jumlah (Rp)')

        for bar in bars:
            yval = bar.get_height()
            self.axes.text(bar.get_x() + bar.get_width()/2, yval + 10, round(yval, 2), ha='center', va='bottom')

        self.canvas.draw()