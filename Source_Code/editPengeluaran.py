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

class EditPengeluaran(QDialog):
    def __init__(self, nominal, tanggal, keterangan, parent=None):
        super().__init__(parent)

        self.setWindowTitle("Edit Data")
        self.setGeometry(850, 200, 400, 200)

        self.jenis_edit = QComboBox(self)
        self.jenis_edit.addItems(["Pajak", "Makanan", "Pulsa atau Paket Data", "Pendidikan", 
                                "Kebutuhan Rumah Tangga", "Tagihan", "Cicilan Kredit", "Lain - Lain"])
        self.nominal_edit = QLineEdit(str(nominal))
        self.tanggal_edit = QDateEdit(tanggal)  
        self.keterangan_edit = QLineEdit(keterangan)

        form_layout = QFormLayout()
        form_layout.addRow("Jenis Pemasukan:", self.jenis_edit)
        form_layout.addRow("Nominal:", self.nominal_edit)
        form_layout.addRow("Tanggal:", self.tanggal_edit)
        form_layout.addRow("Keterangan:", self.keterangan_edit)

        save_button = QPushButton("Simpan")
        save_button.clicked.connect(self.accept)

        layout = QVBoxLayout()
        layout.addLayout(form_layout)
        layout.addWidget(save_button)

        self.setLayout(layout)
        self.adjustSize()

    def get_data(self):
        return (
            self.jenis_edit.currentText(),
            float(self.nominal_edit.text()),
            self.tanggal_edit.date().toPyDate(),  
            self.keterangan_edit.text()
        )