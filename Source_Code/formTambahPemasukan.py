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

class FormTambahPemasukan(QWidget):
    def __init__(self, window):
        super().__init__()
        self.setWindowTitle("Form Tambah Catatan Keuangan")
        self.setGeometry(850, 200, 500, 350)

        self.window = window

        self.mydb = mc.connect(
                host="localhost",
                user="root",
                password="root",
                database="catatankeuangan"
            )

        # Menambah Widget
        self.comboBox1 = QComboBox(self)
        label1 = QLabel("Jenis Pemasukan")
        self.comboBox1.addItems(["Gaji", "Investasi", "Pengembalian Dana",
                                "Penjualan", "Penyewaan", "Tabungan", "Lain - lain"])
        label2 = QLabel("Nominal")
        self.text1 = QLineEdit(self)
        label3 = QLabel("Tanggal")
        self.tanggal = QDateEdit()
        self.tanggal.setDate(QDate.currentDate())
        label4 = QLabel("Keterangan")
        self.text2 = QLineEdit(self)
        button1 = QPushButton("Simpan")
        button1.clicked.connect(self.insert_data)

        # Membuat Layout
        mainLayout = QVBoxLayout()
        mainLayout.addWidget(label1)
        mainLayout.addWidget(self.comboBox1)
        mainLayout.addWidget(label2)
        mainLayout.addWidget(self.text1)
        mainLayout.addWidget(label3)
        mainLayout.addWidget(self.tanggal)
        mainLayout.addWidget(label4)
        mainLayout.addWidget(self.text2)
        mainLayout.addWidget(button1)

        self.setLayout(mainLayout)
        self.adjustSize()

    def insert_data(self):
        try:
            self.mydb._open_connection()
            mycursor = self.mydb.cursor()

            jenis = self.comboBox1.currentText()
            nominal = self.text1.text()
            selected_tanggal = self.tanggal.date()
            tanggal = selected_tanggal.toString("yyyy-MM-dd")
            text = self.text2.text()

            sql = "INSERT INTO pemasukan (jenis_pemasukan, nominal, tanggal, keterangan) VALUES (%s, %s, %s, %s)"
            val = (jenis, nominal, tanggal, text)

            mycursor.execute(sql, val)
            self.mydb.commit()

            mycursor.close()
            self.mydb.close()

            QMessageBox.information(self, 'Info', 'Catatan Pemasukan berhasil ditambahkan.')

        except Exception as e:
            # print(f"Exception Type: {type(e).__name__}")
            print(f"Gagal Menambahkan data pemasukan: {str(e)}")
            QMessageBox.warning(self, 'Peringatan', 'Gagal menambahkan catatan pemasukan.')
        self.close()

        self.window.load_catatan1()
        self.window.load_catatan2()
        self.window.load_catatan3()
        self.window.load_catatan4()
        self.window.load_catatan5()
        self.window.load_catatan6()
        self.window.load_catatan7()
        self.window.load_catatan8()
        self.window.total1()
        self.window.total2()
        self.window.total3()
        self.window.total4()
        self.window.total5()
        self.window.total6()
        self.window.total7()
        self.window.total8()
        self.window.saldo1()     
        self.window.saldo2()
        self.window.saldo3()
        self.window.saldo4()