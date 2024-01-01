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

class CatatanKeuanganApp(QMainWindow):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("Catatan Keuangan Pribadi")
        self.setGeometry(200, 200, 500, 540)

        font = QtGui.QFont()
        font.setFamily("Times New Roman")
        font.setPointSize(12)

        font1 = QtGui.QFont()
        font1.setFamily("Times New Roman")
        font1.setPointSize(12)
        font1.setBold(True)

        self.font2 = QtGui.QFont()
        self.font2.setFamily("Times New Roman")
        self.font2.setPointSize(8)

        # Membuat Widget
        button1 = QPushButton("Tambah Pemasukan")
        button2 = QPushButton("Tambah Pengeluaran")
        button1.clicked.connect(self.tambahCatatanPemasukan)
        button2.clicked.connect(self.tambahCatatanPengeluaran)
        label9 = QLabel("Total")
        label1 = QLabel("Pemasukan")
        label1.setAlignment(Qt.AlignCenter)
        label1.setFont(font1)
        label2 = QLabel("Pengeluaran")
        label2.setAlignment(Qt.AlignCenter)
        label2.setFont(font1)
        label3 = QLabel("Pemasukan")
        label3.setAlignment(Qt.AlignCenter)
        label3.setFont(font1)
        label4 = QLabel("Pengeluaran")
        label4.setAlignment(Qt.AlignCenter)
        label4.setFont(font1)
        label5 = QLabel("Pemasukan")
        label5.setAlignment(Qt.AlignCenter)
        label5.setFont(font1)
        label6 = QLabel("Pengeluaran")
        label6.setAlignment(Qt.AlignCenter)
        label6.setFont(font1)
        label7 = QLabel("Pemasukan")
        label7.setAlignment(Qt.AlignCenter)
        label7.setFont(font1)
        label8 = QLabel("Pengeluaran")
        label8.setAlignment(Qt.AlignCenter)
        label8.setFont(font1)
        self.list1 = QListWidget()
        self.list1.itemDoubleClicked.connect(self.show_catatan)
        self.list1.setStyleSheet("QListWidget::item { margin: 5px; }")
        self.list1.setFont(QtGui.QFont("Times New Roman", 11))
        self.list1.setFixedSize(250, 400)
        self.list2 = QListWidget()
        self.list2.itemDoubleClicked.connect(self.show_catatan)
        self.list2.setStyleSheet("QListWidget::item { margin: 5px; }")
        self.list2.setFont(QtGui.QFont("Times New Roman", 11))
        self.list2.setFixedSize(250, 400)
        self.list3 = QListWidget()
        self.list3.itemDoubleClicked.connect(self.show_catatan)
        self.list3.setStyleSheet("QListWidget::item { margin: 5px; }")
        self.list3.setFont(QtGui.QFont("Times New Roman", 11))
        self.list3.setFixedSize(250, 400)
        self.list4 = QListWidget()
        self.list4.itemDoubleClicked.connect(self.show_catatan)
        self.list4.setStyleSheet("QListWidget::item { margin: 5px; }")
        self.list4.setFont(QtGui.QFont("Times New Roman", 11))
        self.list4.setFixedSize(250, 400)
        self.list5 = QListWidget()
        self.list5.itemDoubleClicked.connect(self.show_catatan)
        self.list5.setStyleSheet("QListWidget::item { margin: 5px; }")
        self.list5.setFont(QtGui.QFont("Times New Roman", 11))
        self.list5.setFixedSize(250, 400)
        self.list6 = QListWidget()
        self.list6.itemDoubleClicked.connect(self.show_catatan)
        self.list6.setStyleSheet("QListWidget::item { margin: 5px; }")
        self.list6.setFont(QtGui.QFont("Times New Roman", 11))
        self.list6.setFixedSize(250, 400)
        self.list7 = QListWidget()
        self.list7.itemDoubleClicked.connect(self.show_catatan)
        self.list7.setStyleSheet("QListWidget::item { margin: 5px; }")
        self.list7.setFont(QtGui.QFont("Times New Roman", 11))
        self.list7.setFixedSize(250, 400)
        self.list8 = QListWidget()
        self.list8.itemDoubleClicked.connect(self.show_catatan)
        self.list8.setStyleSheet("QListWidget::item { margin: 5px; }")
        self.list8.setFont(QtGui.QFont("Times New Roman", 11))
        self.list8.setFixedSize(250, 400)
        label9.setFont(font1)
        label10 = QLabel("Total")
        label10.setFont(font1)
        label11 = QLabel("Total")
        label11.setFont(font1)
        label12 = QLabel("Total")
        label12.setFont(font1)
        label13 = QLabel("Total")
        label13.setFont(font1)
        label14 = QLabel("Total")
        label14.setFont(font1)
        label15 = QLabel("Total")
        label15.setFont(font1)
        label16 = QLabel("Total")
        label16.setFont(font1)
        self.label17 = QLabel()
        self.label17.setAlignment(Qt.AlignCenter)
        self.label17.setFont(font1)
        self.label18 = QLabel()
        self.label18.setAlignment(Qt.AlignCenter)
        self.label18.setFont(font1)
        self.label19 = QLabel()
        self.label19.setAlignment(Qt.AlignCenter)
        self.label19.setFont(font1)
        self.label20 = QLabel()
        self.label20.setAlignment(Qt.AlignCenter)
        self.label20.setFont(font1)
        self.labeltotal1 = QLabel()
        self.labeltotal1.setStyleSheet("border: 1px solid gray; padding: 5px;")
        self.labeltotal2 = QLabel()
        self.labeltotal2.setStyleSheet("border: 1px solid gray; padding: 5px;")
        self.labeltotal3 = QLabel()
        self.labeltotal3.setStyleSheet("border: 1px solid gray; padding: 5px;")
        self.labeltotal4 = QLabel()
        self.labeltotal4.setStyleSheet("border: 1px solid gray; padding: 5px;")
        self.labeltotal5 = QLabel()
        self.labeltotal5.setStyleSheet("border: 1px solid gray; padding: 5px;")
        self.labeltotal6 = QLabel()
        self.labeltotal6.setStyleSheet("border: 1px solid gray; padding: 5px;")
        self.labeltotal7 = QLabel()
        self.labeltotal7.setStyleSheet("border: 1px solid gray; padding: 5px;")
        self.labeltotal8 = QLabel()
        self.labeltotal8.setStyleSheet("border: 1px solid gray; padding: 5px;")
        button_ekspor1 = QPushButton("Ekspor data ke Excel")
        button_ekspor1.clicked.connect(self.ekspor_excel1)
        button_ekspor2 = QPushButton("Ekspor data ke Excel")
        button_ekspor2.clicked.connect(self.ekspor_excel2)
        button_ekspor3 = QPushButton("Ekspor data ke Excel")
        button_ekspor3.clicked.connect(self.ekspor_excel3)
        button_ekspor4 = QPushButton("Ekspor data ke Excel")
        button_ekspor4.clicked.connect(self.ekspor_excel4)
        button_diagram1 = QPushButton("Tampilkan Diagram")
        button_diagram1.clicked.connect(self.show_diagram1)
        button_diagram2 = QPushButton("Tampilkan Diagram")
        button_diagram2.clicked.connect(self.show_diagram2)
        button_diagram3 = QPushButton("Tampilkan Diagram")
        button_diagram3.clicked.connect(self.show_diagram3)
        button_diagram4 = QPushButton("Tampilkan Diagram")
        button_diagram4.clicked.connect(self.show_diagram4)

        layoutH1 = QHBoxLayout()
        layoutH1.addWidget(label9)
        layoutH1.addWidget(self.labeltotal1)
        layoutH1.setSpacing(0)

        layoutH2 = QHBoxLayout()
        layoutH2.addWidget(label10)
        layoutH2.addWidget(self.labeltotal2)
        layoutH2.setSpacing(0)

        layoutH3 = QHBoxLayout()
        layoutH3.addWidget(label11)
        layoutH3.addWidget(self.labeltotal3)
        layoutH3.setSpacing(0)

        layoutH4 = QHBoxLayout()
        layoutH4.addWidget(label12)
        layoutH4.addWidget(self.labeltotal4)
        layoutH4.setSpacing(0)

        layoutH5 = QHBoxLayout()
        layoutH5.addWidget(label13)
        layoutH5.addWidget(self.labeltotal5)
        layoutH5.setSpacing(0)

        layoutH6 = QHBoxLayout()
        layoutH6.addWidget(label14)
        layoutH6.addWidget(self.labeltotal6)
        layoutH6.setSpacing(0)

        layoutH7 = QHBoxLayout()
        layoutH7.addWidget(label15)
        layoutH7.addWidget(self.labeltotal7)
        layoutH7.setSpacing(0)

        layoutH8 = QHBoxLayout()
        layoutH8.addWidget(label16)
        layoutH8.addWidget(self.labeltotal8)
        layoutH8.setSpacing(0)

        layouttab1 = QGridLayout()
        layouttab1.addWidget(label1, 0, 0)
        layouttab1.addWidget(label2, 0, 1)
        layouttab1.addWidget(self.list1, 1, 0)
        layouttab1.addWidget(self.list2, 1, 1)
        layouttab1.addLayout(layoutH1, 2, 0)
        layouttab1.addLayout(layoutH2, 2, 1)
        layouttab1.addWidget(self.label17, 3, 0, 1, 2)
        layouttab1.addWidget(button_ekspor1, 4, 0, 1, 2)
        layouttab1.addWidget(button_diagram1, 5, 0, 1, 2)

        layouttab2 = QGridLayout()
        layouttab2.addWidget(label3, 0, 0)
        layouttab2.addWidget(label4, 0, 1)
        layouttab2.addWidget(self.list3, 1, 0)
        layouttab2.addWidget(self.list4, 1, 1)
        layouttab2.addLayout(layoutH3, 2, 0)
        layouttab2.addLayout(layoutH4, 2, 1)
        layouttab2.addWidget(self.label18, 3, 0, 1, 2)
        layouttab2.addWidget(button_ekspor2, 4, 0, 1, 2)
        layouttab2.addWidget(button_diagram2, 5, 0, 1, 2)

        layouttab3 = QGridLayout()
        layouttab3.addWidget(label5, 0, 0)
        layouttab3.addWidget(label6, 0, 1)
        layouttab3.addWidget(self.list5, 1, 0)
        layouttab3.addWidget(self.list6, 1, 1)
        layouttab3.addLayout(layoutH5, 2, 0)
        layouttab3.addLayout(layoutH6, 2, 1)
        layouttab3.addWidget(self.label19, 3, 0, 1, 2)
        layouttab3.addWidget(button_ekspor3, 4, 0, 1, 2)
        layouttab3.addWidget(button_diagram3, 5, 0, 1, 2)

        layouttab4 = QGridLayout()
        layouttab4.addWidget(label7, 0, 0)
        layouttab4.addWidget(label8, 0, 1)
        layouttab4.addWidget(self.list7, 1, 0)
        layouttab4.addWidget(self.list8, 1, 1)
        layouttab4.addLayout(layoutH7, 2, 0)
        layouttab4.addLayout(layoutH8, 2, 1)
        layouttab4.addWidget(self.label20, 3, 0, 1, 2)
        layouttab4.addWidget(button_ekspor4, 4, 0, 1, 2)
        layouttab4.addWidget(button_diagram4, 5, 0, 1, 2)

        tab1 = QWidget()
        tab1.setObjectName("Harian")
        tab1.setFont(font)
        tab1.setLayout(layouttab1)
        tab2 = QWidget()
        tab2.setObjectName("Mingguan")
        tab2.setFont(font)
        tab2.setLayout(layouttab2)
        tab3 = QWidget()
        tab3.setObjectName("Bulanan")
        tab3.setFont(font)
        tab3.setLayout(layouttab3)
        tab4 = QWidget()
        tab4.setObjectName("Tahunan")
        tab4.setFont(font)
        tab4.setLayout(layouttab4)
        
        tabWidget = QTabWidget()
        tabWidget.addTab(tab1, "Harian")
        tabWidget.addTab(tab2, "Mingguan")
        tabWidget.addTab(tab3, "Bulanan")
        tabWidget.addTab(tab4, "Tahunan")

        # Membuat Layout
        layout1 = QGridLayout()
        layout1.addWidget(button1, 0, 0)
        layout1.addWidget(button2, 0, 1)

        mainLayout = QVBoxLayout()
        mainLayout.addLayout(layout1)
        mainLayout.addWidget(tabWidget)

        widget = QWidget()
        widget.setLayout(mainLayout)
        widget.setFont(font)
        self.setCentralWidget(widget)
        self.adjustSize()

        self.nilai_angka1 = 0
        self.nilai_angka2 = 0
        self.nilai_angka3 = 0
        self.nilai_angka4 = 0
        self.nilai_angka5 = 0
        self.nilai_angka6 = 0
        self.nilai_angka7 = 0
        self.nilai_angka8 = 0

        self.mydb = mc.connect(
                host="localhost",
                user="root",
                password="root",
                database="catatankeuangan"
            )
        
        self.load_catatan1()
        self.load_catatan2()
        self.load_catatan3()
        self.load_catatan4()
        self.load_catatan5()
        self.load_catatan6()
        self.load_catatan7()
        self.load_catatan8()
        self.total1()
        self.total2()
        self.total3()
        self.total4()
        self.total5()
        self.total6()
        self.total7()
        self.total8()
        self.saldo1()
        self.saldo2()
        self.saldo3()
        self.saldo4()

    def load_catatan1(self):
        self.list1.clear()
        try:
            self.mydb._open_connection()
            mycursor = self.mydb.cursor()

            tanggal_sekarang = datetime.now().date().strftime("%Y-%m-%d")

            sql = "SELECT id_pemasukan, nominal, tanggal FROM pemasukan WHERE tanggal = %s"
            val = (tanggal_sekarang,)

            mycursor.execute(sql, val)
            result1 = mycursor.fetchall()

            for id_pemasukan, nominal, tanggal in result1:
                tanggal_baru = tanggal.strftime("%d %B %Y")
                format_nominal = f"{nominal:,}"
                item = QListWidgetItem(f"Rp. {format_nominal}\n{tanggal_baru}\nID: {id_pemasukan}")
                self.list1.addItem(item)

            mycursor.close()
            self.mydb.close()

        except mc.Error as e:
            print("gagal menampilkan data:", e)

    def load_catatan2(self):
        self.list2.clear()
        try:
            self.mydb._open_connection()
            mycursor = self.mydb.cursor()

            tanggal_sekarang = datetime.now().date().strftime("%Y-%m-%d")

            sql = "SELECT id_pengeluaran, nominal, tanggal FROM pengeluaran WHERE tanggal = %s"
            val = (tanggal_sekarang,)

            mycursor.execute(sql, val)
            result = mycursor.fetchall()

            for id_pengeluaran, nominal, tanggal in result:
                tanggal_baru = tanggal.strftime("%d %B %Y")
                format_nominal = f"{nominal:,}"
                item = QListWidgetItem(f"Rp. {format_nominal}\n{tanggal_baru}\nID: {id_pengeluaran}")
                self.list2.addItem(item)

            mycursor.close()
            self.mydb.close()

        except mc.Error as e:
            print("gagal menampilkan data:", e)

    def load_catatan3(self):
        self.list3.clear()
        try:
            self.mydb._open_connection()
            mycursor = self.mydb.cursor()

            tanggal_sekarang = datetime.now().date().strftime("%Y-%m-%d")
            tanggal_7hari = timedelta(days=6)

            tanggal_mingguan = (datetime.now() - tanggal_7hari).date().strftime("%Y-%m-%d")

            sql = "SELECT id_pemasukan, nominal, tanggal FROM pemasukan WHERE tanggal BETWEEN %s AND %s"
            val = (tanggal_mingguan, tanggal_sekarang)

            mycursor.execute(sql, val)
            result = mycursor.fetchall()

            for id_pemasukan, nominal, tanggal in result:
                tanggal_baru = tanggal.strftime("%d %B %Y")
                format_nominal = f"{nominal:,}"
                item = QListWidgetItem(f"Rp. {format_nominal}\n{tanggal_baru}\nID: {id_pemasukan}")
                self.list3.addItem(item)

            mycursor.close()
            self.mydb.close()

        except mc.Error as e:
            print("gagal menampilkan data:", e)

    def load_catatan4(self):
        self.list4.clear()
        try:
            self.mydb._open_connection()
            mycursor = self.mydb.cursor()

            tanggal_sekarang = datetime.now().date().strftime("%Y-%m-%d")
            tanggal_7hari = timedelta(days=6)

            tanggal_mingguan = (datetime.now() - tanggal_7hari).date().strftime("%Y-%m-%d")

            sql = "SELECT id_pengeluaran, nominal, tanggal FROM pengeluaran WHERE tanggal BETWEEN %s AND %s"
            val = (tanggal_mingguan, tanggal_sekarang)

            mycursor.execute(sql, val)
            result = mycursor.fetchall()

            for id_pengeluaran, nominal, tanggal in result:
                tanggal_baru = tanggal.strftime("%d %B %Y")
                format_nominal = f"{nominal:,}"
                item = QListWidgetItem(f"Rp. {format_nominal}\n{tanggal_baru}\nID: {id_pengeluaran}")
                self.list4.addItem(item)

            mycursor.close()
            self.mydb.close()

        except mc.Error as e:
            print("gagal menampilkan data:", e)

    def load_catatan5(self):
        self.list5.clear()
        try:
            self.mydb._open_connection()
            mycursor = self.mydb.cursor()

            tanggal_sekarang = datetime.now().date().strftime("%Y-%m-%d")
            tanggal_30hari = timedelta(days=29)

            tanggal_bulanan = (datetime.now() - tanggal_30hari).date().strftime("%Y-%m-%d")

            sql = "SELECT id_pemasukan, nominal, tanggal FROM pemasukan WHERE tanggal BETWEEN %s AND %s"
            val = (tanggal_bulanan, tanggal_sekarang)

            mycursor.execute(sql, val)
            result = mycursor.fetchall()

            for id_pemasukan, nominal, tanggal in result:
                tanggal_baru = tanggal.strftime("%d %B %Y")
                format_nominal = f"{nominal:,}"
                item = QListWidgetItem(f"Rp. {format_nominal}\n{tanggal_baru}\nID: {id_pemasukan}")
                self.list5.addItem(item)

            mycursor.close()
            self.mydb.close()

        except mc.Error as e:
            print("gagal menampilkan data:", e)

    def load_catatan6(self):
        self.list6.clear()
        try:
            self.mydb._open_connection()
            mycursor = self.mydb.cursor()

            tanggal_sekarang = datetime.now().date().strftime("%Y-%m-%d")
            tanggal_30hari = timedelta(days=29)

            tanggal_bulanan = (datetime.now() - tanggal_30hari).date().strftime("%Y-%m-%d")

            sql = "SELECT id_pengeluaran, nominal, tanggal FROM pengeluaran WHERE tanggal BETWEEN %s AND %s"
            val = (tanggal_bulanan, tanggal_sekarang)

            mycursor.execute(sql, val)
            result = mycursor.fetchall()

            for id_pengeluaran, nominal, tanggal in result:
                tanggal_baru = tanggal.strftime("%d %B %Y")
                format_nominal = f"{nominal:,}"
                item = QListWidgetItem(f"Rp. {format_nominal}\n{tanggal_baru}\nID: {id_pengeluaran}")
                self.list6.addItem(item)

            mycursor.close()
            self.mydb.close()

        except mc.Error as e:
            print("gagal menampilkan data:", e)

    def load_catatan7(self):
        self.list7.clear()
        try:
            self.mydb._open_connection()
            mycursor = self.mydb.cursor()

            tanggal_awal = "0000-00-00"
            tanggal_sekarang = datetime.now().date().strftime("%Y-%m-%d")
            tanggal_365hari = timedelta(days=364)

            sql = "SELECT id_pemasukan, nominal, tanggal FROM pemasukan WHERE tanggal BETWEEN %s AND %s"
            val = (tanggal_awal, tanggal_sekarang)

            mycursor.execute(sql, val)
            result = mycursor.fetchall()

            for id_pemasukan, nominal, tanggal in result:
                tanggal_baru = tanggal.strftime("%d %B %Y")
                format_nominal = f"{nominal:,}"
                item = QListWidgetItem(f"Rp. {format_nominal}\n{tanggal_baru}\nID: {id_pemasukan}")
                self.list7.addItem(item)

            mycursor.close()
            self.mydb.close()

        except mc.Error as e:
            print("gagal menampilkan data:", e)

    def load_catatan8(self):
        self.list8.clear()
        try:
            self.mydb._open_connection()
            mycursor = self.mydb.cursor()

            tanggal_awal = "0000-00-00"
            tanggal_sekarang = datetime.now().date().strftime("%Y-%m-%d")
            tanggal_365hari = timedelta(days=364)

            sql = "SELECT id_pengeluaran, nominal, tanggal FROM pengeluaran WHERE tanggal BETWEEN %s AND %s"
            val = (tanggal_awal, tanggal_sekarang)

            mycursor.execute(sql, val)
            result = mycursor.fetchall()

            for id_pengeluaran, nominal, tanggal in result:
                tanggal_baru = tanggal.strftime("%d %B %Y")
                format_nominal = f"{nominal:,}"
                item = QListWidgetItem(f"Rp. {format_nominal}\n{tanggal_baru}\nID: {id_pengeluaran}")
                self.list8.addItem(item)

            mycursor.close()
            self.mydb.close()

        except mc.Error as e:
            print("gagal menampilkan data:", e)

    def total1(self):
        try:
            self.mydb._open_connection()
            mycursor = self.mydb.cursor()

            tanggal_sekarang = datetime.now().date().strftime("%Y-%m-%d")

            sql = "SELECT SUM(nominal) FROM pemasukan WHERE tanggal = %s"
            val = (tanggal_sekarang, )

            mycursor.execute(sql, val)
            result = mycursor.fetchone()

            if not result == (None,):
                self.nilai_angka1 = float(result[0])
                format_jumlah = f"{self.nilai_angka1:,}"
                hasil = str(format_jumlah).rstrip('0').rstrip('.') if '.' in str(format_jumlah) else str(format_jumlah)
                self.labeltotal1.setText(f"Rp. {hasil}")
            else:
                self.labeltotal1.setText("")

            mycursor.close()
            self.mydb.close()

        except mc.Error as e:
            print("gagal menjumlahkan data:", e)

    def total2(self):
        try:
            self.mydb._open_connection()
            mycursor = self.mydb.cursor()

            tanggal_sekarang = datetime.now().date().strftime("%Y-%m-%d")

            sql = "SELECT SUM(nominal) FROM pengeluaran WHERE tanggal = %s"
            val = (tanggal_sekarang, )

            mycursor.execute(sql, val)
            result = mycursor.fetchone()

            if not result == (None,):
                self.nilai_angka2 = float(result[0])
                format_jumlah = f"{self.nilai_angka2:,}"
                hasil = str(format_jumlah).rstrip('0').rstrip('.') if '.' in str(format_jumlah) else str(format_jumlah)
                self.labeltotal2.setText(f"Rp. {hasil}")
            else:
                self.labeltotal2.setText("")

            mycursor.close()
            self.mydb.close()

        except mc.Error as e:
            print("gagal menjumlahkan data:", e)

    def total3(self):
        try:
            self.mydb._open_connection()
            mycursor = self.mydb.cursor()

            tanggal_sekarang = datetime.now().date().strftime("%Y-%m-%d")
            tanggal_7hari = timedelta(days=6)

            tanggal_mingguan = (datetime.now() - tanggal_7hari).date().strftime("%Y-%m-%d")

            sql = "SELECT SUM(nominal) FROM pemasukan WHERE tanggal BETWEEN %s AND %s"
            val = (tanggal_mingguan, tanggal_sekarang )

            mycursor.execute(sql, val)
            result = mycursor.fetchone()

            if not result == (None,):
                self.nilai_angka3 = float(result[0])
                format_jumlah = f"{self.nilai_angka3:,}"
                hasil = str(format_jumlah).rstrip('0').rstrip('.') if '.' in str(format_jumlah) else str(format_jumlah)
                self.labeltotal3.setText(f"Rp. {hasil}")
            else:
                self.labeltotal3.setText("")

            mycursor.close()
            self.mydb.close()

        except mc.Error as e:
            print("gagal menjumlahkan data:", e)

    def total4(self):
        try:
            self.mydb._open_connection()
            mycursor = self.mydb.cursor()

            tanggal_sekarang = datetime.now().date().strftime("%Y-%m-%d")
            tanggal_7hari = timedelta(days=6)

            tanggal_mingguan = (datetime.now() - tanggal_7hari).date().strftime("%Y-%m-%d")

            sql = "SELECT SUM(nominal) FROM pengeluaran WHERE tanggal BETWEEN %s AND %s"
            val = (tanggal_mingguan, tanggal_sekarang )

            mycursor.execute(sql, val)
            result = mycursor.fetchone()

            if not result == (None,):
                self.nilai_angka4 = float(result[0])
                format_jumlah = f"{self.nilai_angka4:,}"
                hasil = str(format_jumlah).rstrip('0').rstrip('.') if '.' in str(format_jumlah) else str(format_jumlah)
                self.labeltotal4.setText(f"Rp. {hasil}")
            else:
                self.labeltotal4.setText("")

            mycursor.close()
            self.mydb.close()

        except mc.Error as e:
            print("gagal menjumlahkan data:", e)

    def total5(self):
        try:
            self.mydb._open_connection()
            mycursor = self.mydb.cursor()

            tanggal_sekarang = datetime.now().date().strftime("%Y-%m-%d")
            tanggal_30hari = timedelta(days=29)

            tanggal_bulanan = (datetime.now() - tanggal_30hari).date().strftime("%Y-%m-%d")

            sql = "SELECT SUM(nominal) FROM pemasukan WHERE tanggal BETWEEN %s AND %s"
            val = (tanggal_bulanan, tanggal_sekarang )

            mycursor.execute(sql, val)
            result = mycursor.fetchone()

            if not result == (None,):
                self.nilai_angka5 = float(result[0])
                format_jumlah = f"{self.nilai_angka5:,}"
                hasil = str(format_jumlah).rstrip('0').rstrip('.') if '.' in str(format_jumlah) else str(format_jumlah)
                self.labeltotal5.setText(f"Rp. {hasil}")
            else:
                self.labeltotal5.setText("")

            mycursor.close()
            self.mydb.close()

        except mc.Error as e:
            print("gagal menjumlahkan data:", e)

    def total6(self):
        try:
            self.mydb._open_connection()
            mycursor = self.mydb.cursor()

            tanggal_sekarang = datetime.now().date().strftime("%Y-%m-%d")
            tanggal_30hari = timedelta(days=29)

            tanggal_bulanan = (datetime.now() - tanggal_30hari).date().strftime("%Y-%m-%d")

            sql = "SELECT SUM(nominal) FROM pengeluaran WHERE tanggal BETWEEN %s AND %s"
            val = (tanggal_bulanan, tanggal_sekarang )

            mycursor.execute(sql, val)
            result = mycursor.fetchone()

            if not result == (None,):
                self.nilai_angka6 = float(result[0])
                format_jumlah = f"{self.nilai_angka6:,}"
                hasil = str(format_jumlah).rstrip('0').rstrip('.') if '.' in str(format_jumlah) else str(format_jumlah)
                self.labeltotal6.setText(f"Rp. {hasil}")
            else:
                self.labeltotal6.setText("")

            mycursor.close()
            self.mydb.close()

        except mc.Error as e:
            print("gagal menjumlahkan data:", e)

    def total7(self):
        try:
            self.mydb._open_connection()
            mycursor = self.mydb.cursor()

            tanggal_awal = "0000-00-00"
            tanggal_sekarang = datetime.now().date().strftime("%Y-%m-%d")
            tanggal_365hari = timedelta(days=364)

            sql = "SELECT SUM(nominal) FROM pemasukan WHERE tanggal BETWEEN %s AND %s"
            val = (tanggal_awal, tanggal_sekarang )

            mycursor.execute(sql, val)
            result = mycursor.fetchone()

            if not result == (None,):
                self.nilai_angka7 = float(result[0])
                format_jumlah = f"{self.nilai_angka7:,}"
                hasil = str(format_jumlah).rstrip('0').rstrip('.') if '.' in str(format_jumlah) else str(format_jumlah)
                self.labeltotal7.setText(f"Rp. {hasil}")
            else:
                self.labeltotal7.setText("")

            mycursor.close()
            self.mydb.close()

        except mc.Error as e:
            print("gagal menjumlahkan data:", e)

    def total8(self):
        try:
            self.mydb._open_connection()
            mycursor = self.mydb.cursor()

            tanggal_awal = "0000-00-00"
            tanggal_sekarang = datetime.now().date().strftime("%Y-%m-%d")
            tanggal_365hari = timedelta(days=364)

            sql = "SELECT SUM(nominal) FROM pengeluaran WHERE tanggal BETWEEN %s AND %s"
            val = (tanggal_awal, tanggal_sekarang )

            mycursor.execute(sql, val)
            result = mycursor.fetchone()

            if not result == (None,):
                self.nilai_angka8 = float(result[0])
                format_jumlah = f"{self.nilai_angka8:,}"
                hasil = str(format_jumlah).rstrip('0').rstrip('.') if '.' in str(format_jumlah) else str(format_jumlah)
                self.labeltotal8.setText(f"Rp. {hasil}")
            else:
                self.labeltotal8.setText("")

            mycursor.close()
            self.mydb.close()

        except mc.Error as e:
            print("gagal menjumlahkan data:", e)

    def saldo1(self):
        hasil = self.nilai_angka1 - self.nilai_angka2
        format_jumlah = f"{hasil:,}"
        saldo = str(format_jumlah).rstrip('0').rstrip('.') if '.' in str(format_jumlah) else str(format_jumlah)
        self.label17.setText(f"Saldo : Rp. {saldo}")

    def saldo2(self):
        hasil = self.nilai_angka3 - self.nilai_angka4
        format_jumlah = f"{hasil:,}"
        saldo = str(format_jumlah).rstrip('0').rstrip('.') if '.' in str(format_jumlah) else str(format_jumlah)
        self.label18.setText(f"Saldo : Rp. {saldo}")

    def saldo3(self):
        hasil = self.nilai_angka5 - self.nilai_angka6
        format_jumlah = f"{hasil:,}"
        saldo = str(format_jumlah).rstrip('0').rstrip('.') if '.' in str(format_jumlah) else str(format_jumlah)
        self.label19.setText(f"Saldo : Rp. {saldo}")

    def saldo4(self):
        hasil = self.nilai_angka7- self.nilai_angka8
        format_jumlah = f"{hasil:,}"
        saldo = str(format_jumlah).rstrip('0').rstrip('.') if '.' in str(format_jumlah) else str(format_jumlah)
        self.label20.setText(f"Saldo : Rp. {saldo}")

    def tambahCatatanPemasukan(self):
        self.tambah = FormTambahPemasukan()
        self.tambah.show()

    def tambahCatatanPengeluaran(self):
        self.tambah = FormTambahPengeluaran()
        self.tambah.show()

    def show_catatan(self, item):
        itemTerpilih = item.text()
        baris = itemTerpilih.split(": ")
        id_item = baris[1]
        tampilkan = ShowCatatan(id_item)
        tampilkan.exec_()

    def show_diagram1(self):
        sizes = [self.nilai_angka1, self.nilai_angka2]
        labels = ["Pemasukan", "Pengeluaran"]
        judul = "Grafik Pemasukan dan Pengeluaran Harian"
        self.diagram = ShowDiagram(judul, sizes, labels)
        self.diagram.show()

    def show_diagram2(self):
        sizes = [self.nilai_angka3, self.nilai_angka4]
        labels = ["Pemasukan", "Pengeluaran"]
        judul = "Grafik Pemasukan dan Pengeluaran Mingguan"
        self.diagram = ShowDiagram(judul, sizes, labels)
        self.diagram.show()

    def show_diagram3(self):
        sizes = [self.nilai_angka5, self.nilai_angka6]
        labels = ["Pemasukan", "Pengeluaran"]
        judul = "Grafik Pemasukan dan Pengeluaran Bulanan"
        self.diagram = ShowDiagram(judul, sizes, labels)
        self.diagram.show()

    def show_diagram4(self):
        sizes = [self.nilai_angka7, self.nilai_angka8]
        labels = ["Pemasukan", "Pengeluaran"]
        judul = "Grafik Pemasukan dan Pengeluaran Tahunan"
        self.diagram = ShowDiagram(judul, sizes, labels)
        self.diagram.show()

    def ekspor_excel1(self):
        try:
            self.mydb._open_connection()
            mycursor = self.mydb.cursor()

            tanggal_sekarang = datetime.now().date().strftime("%Y-%m-%d")

            sql1 = "SELECT * FROM pemasukan WHERE tanggal = %s"
            val1 = (tanggal_sekarang,)

            mycursor.execute(sql1, val1)
            result1 = mycursor.fetchall()
            
            id_pemasukan = []
            jenis_pemasukan = []
            nominal_pemasukan = []
            tanggal_pemasukan = []
            keterangan_pemasukan = []

            for kolom1, kolom2, kolom3, kolom4, kolom5 in result1:
                tanggal_baru = kolom4.strftime("%d %B %Y")
                id_pemasukan.append(kolom1)
                jenis_pemasukan.append(kolom2)
                nominal_pemasukan.append(kolom3)
                tanggal_pemasukan.append(tanggal_baru)
                keterangan_pemasukan.append(kolom5)
            
            data1 = {"ID pemasukan" : id_pemasukan,
                     "Jenis pemasukan" : jenis_pemasukan,
                     "Nominal" : nominal_pemasukan,
                     "Tanggal" : tanggal_pemasukan,
                     "Keterangan" : keterangan_pemasukan}
            
            df1 = pd.DataFrame(data1)

            sql2 = "SELECT * FROM pengeluaran WHERE tanggal = %s"
            val2 = (tanggal_sekarang,)

            mycursor.execute(sql2, val2)
            result2 = mycursor.fetchall()

            id_pengeluaran = []
            jenis_pengeluaran = []
            nominal_pengeluaran = []
            tanggal_pengeluaran = []
            keterangan_pengeluaran = []

            for kolom1, kolom2, kolom3, kolom4, kolom5 in result2:
                tanggal_baru = kolom4.strftime("%d %B %Y")
                id_pengeluaran.append(kolom1)
                jenis_pengeluaran.append(kolom2)
                nominal_pengeluaran.append(kolom3)
                tanggal_pengeluaran.append(tanggal_baru)
                keterangan_pengeluaran.append(kolom5)
            
            data2 = {"ID pengeluaran" : id_pengeluaran,
                     "Jenis pengeluaran" : jenis_pengeluaran,
                     "Nominal" : nominal_pengeluaran,
                     "Tanggal" : tanggal_pengeluaran,
                     "Keterangan" : keterangan_pengeluaran}
            
            df2 = pd.DataFrame(data2)

            default_file_name = "data_pemasukan_dan_pengeluaran_harian.xlsx"

            file_path = filedialog.asksaveasfilename(
                defaultextension=".xlsx",
                filetypes=[("Excel Files", "*.xlsx")],
                initialfile=default_file_name,
                title="Simpan Sebagai"
            )

            if not file_path:
                return
        
            if os.path.exists(file_path):
                base, extension = os.path.splitext(file_path)
                count = 1
                new_file_path = f"{base} ({count}){extension}"
                while os.path.exists(new_file_path):
                    count += 1
                    new_file_path = f"{base} ({count}){extension}"
                file_path = new_file_path

            with pd.ExcelWriter(file_path, engine='xlsxwriter') as writer:
                df1.to_excel(writer, sheet_name='Pemasukan', index=False)
                df2.to_excel(writer, sheet_name='Pengeluaran', index=False)

            mycursor.close()
            self.mydb.close()

            QMessageBox.information(self, 'Info', f"Berhasil ekspor data ke excel dengan nama '{file_path}'")

        except mc.Error as e:
            print("gagal ekspor data ke excel:", e)
            QMessageBox.warning(self, 'Peringatan', 'Gagal ekspor data ke excel.')

    def ekspor_excel2(self):
        try:
            self.mydb._open_connection()
            mycursor = self.mydb.cursor()

            tanggal_sekarang = datetime.now().date().strftime("%Y-%m-%d")
            tanggal_7hari = timedelta(days=6)

            tanggal_mingguan = (datetime.now() - tanggal_7hari).date().strftime("%Y-%m-%d")

            sql1 = "SELECT * FROM pemasukan WHERE tanggal BETWEEN %s AND %s"
            val1 = (tanggal_mingguan, tanggal_sekarang)

            mycursor.execute(sql1, val1)
            result1 = mycursor.fetchall()
            
            id_pemasukan = []
            jenis_pemasukan = []
            nominal_pemasukan = []
            tanggal_pemasukan = []
            keterangan_pemasukan = []

            for kolom1, kolom2, kolom3, kolom4, kolom5 in result1:
                tanggal_baru = kolom4.strftime("%d %B %Y")
                id_pemasukan.append(kolom1)
                jenis_pemasukan.append(kolom2)
                nominal_pemasukan.append(kolom3)
                tanggal_pemasukan.append(tanggal_baru)
                keterangan_pemasukan.append(kolom5)
            
            data1 = {"ID pemasukan" : id_pemasukan,
                     "Jenis pemasukan" : jenis_pemasukan,
                     "Nominal" : nominal_pemasukan,
                     "Tanggal" : tanggal_pemasukan,
                     "Keterangan" : keterangan_pemasukan}
            
            df1 = pd.DataFrame(data1)

            sql2 = "SELECT * FROM pengeluaran WHERE tanggal BETWEEN %s AND %s"
            val2 = (tanggal_mingguan, tanggal_sekarang)

            mycursor.execute(sql2, val2)
            result2 = mycursor.fetchall()

            id_pengeluaran = []
            jenis_pengeluaran = []
            nominal_pengeluaran = []
            tanggal_pengeluaran = []
            keterangan_pengeluaran = []

            for kolom1, kolom2, kolom3, kolom4, kolom5 in result2:
                tanggal_baru = kolom4.strftime("%d %B %Y")
                id_pengeluaran.append(kolom1)
                jenis_pengeluaran.append(kolom2)
                nominal_pengeluaran.append(kolom3)
                tanggal_pengeluaran.append(tanggal_baru)
                keterangan_pengeluaran.append(kolom5)
            
            data2 = {"ID pengeluaran" : id_pengeluaran,
                     "Jenis pengeluaran" : jenis_pengeluaran,
                     "Nominal" : nominal_pengeluaran,
                     "Tanggal" : tanggal_pengeluaran,
                     "Keterangan" : keterangan_pengeluaran}
            
            df2 = pd.DataFrame(data2)

            default_file_name = "data_pemasukan_dan_pengeluaran_mingguan.xlsx"

            file_path = filedialog.asksaveasfilename(
                defaultextension=".xlsx",
                filetypes=[("Excel Files", "*.xlsx")],
                initialfile=default_file_name,
                title="Simpan Sebagai"
            )

            if not file_path:
                return
        
            if os.path.exists(file_path):
                base, extension = os.path.splitext(file_path)
                count = 1
                new_file_path = f"{base} ({count}){extension}"
                while os.path.exists(new_file_path):
                    count += 1
                    new_file_path = f"{base} ({count}){extension}"
                file_path = new_file_path

            with pd.ExcelWriter(file_path, engine='xlsxwriter') as writer:
                df1.to_excel(writer, sheet_name='Pemasukan', index=False)
                df2.to_excel(writer, sheet_name='Pengeluaran', index=False)

            mycursor.close()
            self.mydb.close()

            QMessageBox.information(self, 'Info', f"Berhasil ekspor data ke excel dengan nama '{file_path}'")

        except mc.Error as e:
            print("gagal ekspor data ke excel:", e)
            QMessageBox.warning(self, 'Peringatan', 'Gagal ekspor data ke excel.')

    def ekspor_excel3(self):
        try:
            self.mydb._open_connection()
            mycursor = self.mydb.cursor()

            tanggal_sekarang = datetime.now().date().strftime("%Y-%m-%d")
            tanggal_30hari = timedelta(days=29)

            tanggal_bulanan = (datetime.now() - tanggal_30hari).date().strftime("%Y-%m-%d")

            sql1 = "SELECT * FROM pemasukan WHERE tanggal BETWEEN %s AND %s"
            val1 = (tanggal_bulanan, tanggal_sekarang)

            mycursor.execute(sql1, val1)
            result1 = mycursor.fetchall()
            
            id_pemasukan = []
            jenis_pemasukan = []
            nominal_pemasukan = []
            tanggal_pemasukan = []
            keterangan_pemasukan = []

            for kolom1, kolom2, kolom3, kolom4, kolom5 in result1:
                tanggal_baru = kolom4.strftime("%d %B %Y")
                id_pemasukan.append(kolom1)
                jenis_pemasukan.append(kolom2)
                nominal_pemasukan.append(kolom3)
                tanggal_pemasukan.append(tanggal_baru)
                keterangan_pemasukan.append(kolom5)
            
            data1 = {"ID pemasukan" : id_pemasukan,
                     "Jenis pemasukan" : jenis_pemasukan,
                     "Nominal" : nominal_pemasukan,
                     "Tanggal" : tanggal_pemasukan,
                     "Keterangan" : keterangan_pemasukan}
            
            df1 = pd.DataFrame(data1)

            sql2 = "SELECT * FROM pengeluaran WHERE tanggal BETWEEN %s AND %s"
            val2 = (tanggal_bulanan, tanggal_sekarang)

            mycursor.execute(sql2, val2)
            result2 = mycursor.fetchall()

            id_pengeluaran = []
            jenis_pengeluaran = []
            nominal_pengeluaran = []
            tanggal_pengeluaran = []
            keterangan_pengeluaran = []

            for kolom1, kolom2, kolom3, kolom4, kolom5 in result2:
                tanggal_baru = kolom4.strftime("%d %B %Y")
                id_pengeluaran.append(kolom1)
                jenis_pengeluaran.append(kolom2)
                nominal_pengeluaran.append(kolom3)
                tanggal_pengeluaran.append(tanggal_baru)
                keterangan_pengeluaran.append(kolom5)
            
            data2 = {"ID pengeluaran" : id_pengeluaran,
                     "Jenis pengeluaran" : jenis_pengeluaran,
                     "Nominal" : nominal_pengeluaran,
                     "Tanggal" : tanggal_pengeluaran,
                     "Keterangan" : keterangan_pengeluaran}
            
            df2 = pd.DataFrame(data2)

            default_file_name = "data_pemasukan_dan_pengeluaran_bulanan.xlsx"

            file_path = filedialog.asksaveasfilename(
                defaultextension=".xlsx",
                filetypes=[("Excel Files", "*.xlsx")],
                initialfile=default_file_name,
                title="Simpan Sebagai"
            )

            if not file_path:
                return
        
            if os.path.exists(file_path):
                base, extension = os.path.splitext(file_path)
                count = 1
                new_file_path = f"{base} ({count}){extension}"
                while os.path.exists(new_file_path):
                    count += 1
                    new_file_path = f"{base} ({count}){extension}"
                file_path = new_file_path

            with pd.ExcelWriter(file_path, engine='xlsxwriter') as writer:
                df1.to_excel(writer, sheet_name='Pemasukan', index=False)
                df2.to_excel(writer, sheet_name='Pengeluaran', index=False)

            mycursor.close()
            self.mydb.close()

            QMessageBox.information(self, 'Info', f"Berhasil ekspor data ke excel dengan nama '{file_path}'")

        except mc.Error as e:
            print("gagal ekspor data ke excel:", e)
            QMessageBox.warning(self, 'Peringatan', 'Gagal ekspor data ke excel.')

    def ekspor_excel4(self):
        try:
            self.mydb._open_connection()
            mycursor = self.mydb.cursor()

            tanggal_awal = "0000-00-00"
            tanggal_sekarang = datetime.now().date().strftime("%Y-%m-%d")

            sql1 = "SELECT * FROM pemasukan WHERE tanggal BETWEEN %s AND %s"
            val1 = (tanggal_awal, tanggal_sekarang)

            mycursor.execute(sql1, val1)
            result1 = mycursor.fetchall()
            
            id_pemasukan = []
            jenis_pemasukan = []
            nominal_pemasukan = []
            tanggal_pemasukan = []
            keterangan_pemasukan = []

            for kolom1, kolom2, kolom3, kolom4, kolom5 in result1:
                tanggal_baru = kolom4.strftime("%d %B %Y")
                id_pemasukan.append(kolom1)
                jenis_pemasukan.append(kolom2)
                nominal_pemasukan.append(kolom3)
                tanggal_pemasukan.append(tanggal_baru)
                keterangan_pemasukan.append(kolom5)
            
            data1 = {"ID pemasukan" : id_pemasukan,
                     "Jenis pemasukan" : jenis_pemasukan,
                     "Nominal" : nominal_pemasukan,
                     "Tanggal" : tanggal_pemasukan,
                     "Keterangan" : keterangan_pemasukan}
            
            df1 = pd.DataFrame(data1)

            sql2 = "SELECT * FROM pengeluaran WHERE tanggal BETWEEN %s AND %s"
            val2 = (tanggal_awal, tanggal_sekarang)

            mycursor.execute(sql2, val2)
            result2 = mycursor.fetchall()

            id_pengeluaran = []
            jenis_pengeluaran = []
            nominal_pengeluaran = []
            tanggal_pengeluaran = []
            keterangan_pengeluaran = []

            for kolom1, kolom2, kolom3, kolom4, kolom5 in result2:
                tanggal_baru = kolom4.strftime("%d %B %Y")
                id_pengeluaran.append(kolom1)
                jenis_pengeluaran.append(kolom2)
                nominal_pengeluaran.append(kolom3)
                tanggal_pengeluaran.append(tanggal_baru)
                keterangan_pengeluaran.append(kolom5)
            
            data2 = {"ID pengeluaran" : id_pengeluaran,
                     "Jenis pengeluaran" : jenis_pengeluaran,
                     "Nominal" : nominal_pengeluaran,
                     "Tanggal" : tanggal_pengeluaran,
                     "Keterangan" : keterangan_pengeluaran}
            
            df2 = pd.DataFrame(data2)

            default_file_name = "data_pemasukan_dan_pengeluaran_tahunan.xlsx"

            file_path = filedialog.asksaveasfilename(
                defaultextension=".xlsx",
                filetypes=[("Excel Files", "*.xlsx")],
                initialfile=default_file_name,
                title="Simpan Sebagai"
            )

            if not file_path:
                return
        
            if os.path.exists(file_path):
                base, extension = os.path.splitext(file_path)
                count = 1
                new_file_path = f"{base} ({count}){extension}"
                while os.path.exists(new_file_path):
                    count += 1
                    new_file_path = f"{base} ({count}){extension}"
                file_path = new_file_path

            with pd.ExcelWriter(file_path, engine='xlsxwriter') as writer:
                df1.to_excel(writer, sheet_name='Pemasukan', index=False)
                df2.to_excel(writer, sheet_name='Pengeluaran', index=False)

            mycursor.close()
            self.mydb.close()

            QMessageBox.information(self, 'Info', f"Berhasil ekspor data ke excel dengan nama '{file_path}'")
            
        except mc.Error as e:
            print("gagal ekspor data ke excel:", e)
            QMessageBox.warning(self, 'Peringatan', 'Gagal ekspor data ke excel.')

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

class EditPemasukan(QDialog):
    def __init__(self, nominal, tanggal, keterangan, parent=None):
        super().__init__(parent)

        self.setWindowTitle("Edit Data")
        self.setGeometry(850, 200, 400, 200)

        self.jenis_edit = QComboBox(self)
        self.jenis_edit.addItems(["Gaji", "Investasi", "Pengembalian Dana",
                                "Penjualan", "Penyewaan", "Tabungan", "Lain - lain"])
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

class ShowCatatan(QDialog):
    def __init__(self, item):
        super().__init__()

        self.setWindowTitle("Form Keterangan Catatan Keuangan")
        self.setGeometry(850, 200, 500, 350)

        self.mydb = mc.connect(
            host="localhost",
            user="root",
            password="root",
            database="catatankeuangan"
        )

        self.pengeluaran_tab = QGridLayout()
        self.pemasukan_tab = QGridLayout()
        self.item = item
        self.setup_ui()

    def setup_ui(self):
        self.tampilkan_pengeluaran(self.item)
        self.tampilkan_pemasukan(self.item)

        mainLayout = QVBoxLayout(self)
        mainLayout.addLayout(self.pengeluaran_tab)
        mainLayout.addLayout(self.pemasukan_tab)
        self.adjustSize()

    def tampilkan_pengeluaran(self, item):
        try:
            mycursor = self.mydb.cursor()

            sql = "SELECT jenis_pengeluaran, nominal, tanggal, keterangan FROM pengeluaran WHERE id_pengeluaran = %s"
            val = (item,)

            mycursor.execute(sql, val)
            result = mycursor.fetchone()

            if result is not None:
                jenis_pengeluaran, nilai_angka, tanggal, keterangan = result
                format_jumlah = f"{nilai_angka:,}"
                nominal = str(format_jumlah).rstrip('0').rstrip('.') if '.' in str(format_jumlah) else str(format_jumlah)

                label1 = QLabel(f"Jenis Pengeluaran")
                label2 = QLabel(f"Nominal")
                label3 = QLabel(f"Tanggal")
                label4 = QLabel(f"Keterangan")
                label5 = QLabel(f": {jenis_pengeluaran}")
                label6 = QLabel(f": {nominal}")
                label7 = QLabel(f": {tanggal.strftime('%d %B %Y')}")
                label8 = QLabel(f": {keterangan}")

                button_edit = QPushButton("Edit")
                button_edit.clicked.connect(lambda: self.edit_pengeluaran(item, nilai_angka, tanggal, keterangan))

                button_hapus = QPushButton("Hapus")
                button_hapus.clicked.connect(lambda: self.hapus_pengeluaran(item))

                button_keluar = QPushButton("Keluar")
                button_keluar.clicked.connect(lambda: self.close())

                layout = QHBoxLayout()
                layout.addWidget(button_edit)
                layout.addWidget(button_hapus)
                layout.addWidget(button_keluar)

                self.pengeluaran_tab.addWidget(label1, 0, 0)
                self.pengeluaran_tab.addWidget(label2, 1, 0)
                self.pengeluaran_tab.addWidget(label3, 2, 0)
                self.pengeluaran_tab.addWidget(label4, 3, 0)
                self.pengeluaran_tab.addWidget(label5, 0, 1)
                self.pengeluaran_tab.addWidget(label6, 1, 1)
                self.pengeluaran_tab.addWidget(label7, 2, 1)
                self.pengeluaran_tab.addWidget(label8, 3, 1)
                self.pengeluaran_tab.addLayout(layout, 4, 0, 1, 2)
            else:
                pass
        except mc.Error as e:
            print("Gagal menampilkan data pengeluaran:", e)

    def tampilkan_pemasukan(self, item):
        try:
            mycursor = self.mydb.cursor()

            sql = "SELECT jenis_pemasukan, nominal, tanggal, keterangan FROM pemasukan WHERE id_pemasukan = %s"
            val = (item,)

            mycursor.execute(sql, val)
            result = mycursor.fetchone()

            if result is not None:
                jenis_pemasukan, nilai_angka, tanggal, keterangan = result
                format_jumlah = f"{nilai_angka:,}"
                nominal = str(format_jumlah).rstrip('0').rstrip('.') if '.' in str(format_jumlah) else str(format_jumlah)

                label1 = QLabel(f"Jenis Pemasukan")
                label2 = QLabel(f"Nominal")
                label3 = QLabel(f"Tanggal")
                label4 = QLabel(f"Keterangan")
                label5 = QLabel(f": {jenis_pemasukan}")
                label6 = QLabel(f": {nominal}")
                label7 = QLabel(f": {tanggal.strftime('%d %B %Y')}")
                label8 = QLabel(f": {keterangan}")

                button_edit = QPushButton("Edit")
                button_edit.clicked.connect(lambda: self.edit_pemasukan(item, nilai_angka , tanggal, keterangan))

                button_hapus = QPushButton("Hapus")
                button_hapus.clicked.connect(lambda: self.hapus_pemasukan(item))

                button_keluar = QPushButton("Keluar")
                button_keluar.clicked.connect(lambda: self.close())

                layout = QHBoxLayout()
                layout.addWidget(button_edit)
                layout.addWidget(button_hapus)
                layout.addWidget(button_keluar)

                self.pemasukan_tab.addWidget(label1, 0, 0)
                self.pemasukan_tab.addWidget(label2, 1, 0)
                self.pemasukan_tab.addWidget(label3, 2, 0)
                self.pemasukan_tab.addWidget(label4, 3, 0)
                self.pemasukan_tab.addWidget(label5, 0, 1)
                self.pemasukan_tab.addWidget(label6, 1, 1)
                self.pemasukan_tab.addWidget(label7, 2, 1)
                self.pemasukan_tab.addWidget(label8, 3, 1)
                self.pemasukan_tab.addLayout(layout, 4, 0, 1, 2)
            else:
                pass
        except mc.Error as e:
            print("Gagal menampilkan data pemasukan:", e)

    def edit_pengeluaran(self, item, nominal, tanggal, keterangan):
        dialog = EditPengeluaran(nominal, tanggal, keterangan, parent=self)
        result = dialog.exec_()

        if result == QDialog.Accepted:
            new_jenis_pengeluaran, new_nominal, new_tanggal, new_keterangan = dialog.get_data()

            try:
                mycursor = self.mydb.cursor()

                sql = "UPDATE pengeluaran SET jenis_pengeluaran = %s, nominal = %s, tanggal = %s, keterangan = %s " \
                      "WHERE id_pengeluaran = %s"
                val = (new_jenis_pengeluaran, new_nominal, new_tanggal, new_keterangan, item)

                mycursor.execute(sql, val)
                self.mydb.commit()

                print("Data pengeluaran berhasil diupdate.")
                QMessageBox.information(self, 'Info', 'Data pengeluaran berhasil diupdate.')

                window.load_catatan1()
                window.load_catatan2()
                window.load_catatan3()
                window.load_catatan4()
                window.load_catatan5()
                window.load_catatan6()
                window.load_catatan7()
                window.load_catatan8()
                window.total1()
                window.total2()
                window.total3()
                window.total4()
                window.total5()
                window.total6()
                window.total7()
                window.total8()       
                window.saldo1()     
                window.saldo2()
                window.saldo3()
                window.saldo4()
                self.close()
                self.tampilkan_pengeluaran(item)

            except mc.Error as e:
                print("Gagal mengupdate data pengeluaran:", e)
                QMessageBox.warning(self, 'Peringatan', 'Gagal mengupdate data pengeluaran.')

    def edit_pemasukan(self, item, nominal, tanggal, keterangan):
        dialog = EditPemasukan(nominal, tanggal, keterangan, parent=self)
        result = dialog.exec_()

        if result == QDialog.Accepted:
            new_jenis_pemasukan, new_nominal, new_tanggal, new_keterangan = dialog.get_data()

            try:
                mycursor = self.mydb.cursor()

                sql = "UPDATE pemasukan SET jenis_pemasukan = %s, nominal = %s, tanggal = %s, keterangan = %s " \
                      "WHERE id_pemasukan = %s"
                val = (new_jenis_pemasukan, new_nominal, new_tanggal, new_keterangan, item)

                mycursor.execute(sql, val)
                self.mydb.commit()

                print("Data pemasukan berhasil diupdate.")
                QMessageBox.information(self, 'Info', 'Data pemasukan berhasil diupdate.')

                # Bersihkan tampilan
                window.load_catatan1()
                window.load_catatan2()
                window.load_catatan3()
                window.load_catatan4()
                window.load_catatan5()
                window.load_catatan6()
                window.load_catatan7()
                window.load_catatan8()
                window.total1()
                window.total2()
                window.total3()
                window.total4()
                window.total5()
                window.total6()
                window.total7()
                window.total8()
                window.saldo1()     
                window.saldo2()
                window.saldo3()
                window.saldo4()        
                self.close()
                self.tampilkan_pemasukan(item)

            except mc.Error as e:
                print("Gagal mengupdate data pemasukan:", e)
                QMessageBox.warning(self, 'Peringatan', 'Gagal mengupdate data pemasukan.')
                
    def hapus_pengeluaran(self, item):
        reply = QMessageBox.question(self, 'Hapus Pengeluaran', 'Anda yakin ingin menghapus pengeluaran ini?',
                                     QMessageBox.Yes | QMessageBox.No, QMessageBox.No)

        if reply == QMessageBox.Yes:
            try:
                mycursor = self.mydb.cursor()

                sql = "DELETE FROM pengeluaran WHERE id_pengeluaran = %s"
                val = (item,)

                mycursor.execute(sql, val)
                self.mydb.commit()

                QMessageBox.information(self, 'Info', 'Data pengeluaran berhasil dihapus.')
                window.load_catatan1()
                window.load_catatan2()
                window.load_catatan3()
                window.load_catatan4()
                window.load_catatan5()
                window.load_catatan6()
                window.load_catatan7()
                window.load_catatan8()
                window.total1()
                window.total2()
                window.total3()
                window.total4()
                window.total5()
                window.total6()
                window.total7()
                window.total8()
                window.saldo1()     
                window.saldo2()
                window.saldo3()
                window.saldo4() 
                self.close()

            except mc.Error as e:
                print("Gagal menghapus data pengeluaran:", e)
                QMessageBox.warning(self, 'Peringatan', 'Gagal menghapus data pengeluaran.')

    def hapus_pemasukan(self, item):
        reply = QMessageBox.question(self, 'Hapus Pemasukan', 'Anda yakin ingin menghapus pemasukan ini?',
                                     QMessageBox.Yes | QMessageBox.No, QMessageBox.No)

        if reply == QMessageBox.Yes:
            try:
                mycursor = self.mydb.cursor()

                sql = "DELETE FROM pemasukan WHERE id_pemasukan = %s"
                val = (item,)

                mycursor.execute(sql, val)
                self.mydb.commit()

                QMessageBox.information(self, 'Info', 'Data pemasukan berhasil dihapus.')

                window.load_catatan1()
                window.load_catatan2()
                window.load_catatan3()
                window.load_catatan4()
                window.load_catatan5()
                window.load_catatan6()
                window.load_catatan7()
                window.load_catatan8()
                window.total1()
                window.total2()
                window.total3()
                window.total4()
                window.total5()
                window.total6()
                window.total7()
                window.total8()
                window.saldo1()     
                window.saldo2()
                window.saldo3()
                window.saldo4()
                self.close()

            except mc.Error as e:
                print("Gagal menghapus data pemasukan:", e)
                QMessageBox.warning(self, 'Peringatan', 'Gagal menghapus data pemasukan.')

class FormTambahPemasukan(QWidget):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("Form Tambah Catatan Keuangan")
        self.setGeometry(850, 200, 500, 350)

        self.mydb = mc.connect(
                host="localhost",
                user="root",
                password="",
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
        window.load_catatan1()
        window.load_catatan2()
        window.load_catatan3()
        window.load_catatan4()
        window.load_catatan5()
        window.load_catatan6()
        window.load_catatan7()
        window.load_catatan8()
        window.total1()
        window.total2()
        window.total3()
        window.total4()
        window.total5()
        window.total6()
        window.total7()
        window.total8()
        window.saldo1()     
        window.saldo2()
        window.saldo3()
        window.saldo4()

class FormTambahPengeluaran(QWidget):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("Form Tambah Catatan Keuangan")
        self.setGeometry(850, 200, 500, 350)

        self.mydb = mc.connect(
                host="localhost",
                user="root",
                password="root",
                database="catatankeuangan"
            )

        # Menambah Widget
        self.comboBox1 = QComboBox(self)
        label1 = QLabel("Jenis Pengeluaran")
        self.comboBox1.addItems(["Pajak", "Makanan", "Pulsa atau Paket Data", "Pendidikan", 
                                "Kebutuhan Rumah Tangga", "Tagihan", "Cicilan Kredit", "Lain - Lain"])    
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

            sql = "INSERT INTO pengeluaran (jenis_pengeluaran, nominal, tanggal, keterangan) VALUES (%s, %s, %s, %s)"
            val = (jenis, nominal, tanggal, text)

            mycursor.execute(sql, val)
            self.mydb.commit()

            mycursor.close()
            self.mydb.close()

            QMessageBox.information(self, 'Info', 'Catatan Pengeluaran berhasil ditambahkan.')

        except Exception as e:
            # print(f"Exception Type: {type(e).__name__}")
            print(f"Gagal menambahkan data pengeluaran: {str(e)}")

            QMessageBox.warning(self, 'Peringatan', 'Gagal menambahkan catatan pengeluaran.')

        self.close()
        window.load_catatan1()
        window.load_catatan2()
        window.load_catatan3()
        window.load_catatan4()
        window.load_catatan5()
        window.load_catatan6()
        window.load_catatan7()
        window.load_catatan8()
        window.total1()
        window.total2()
        window.total3()
        window.total4()
        window.total5()
        window.total6()
        window.total7()
        window.total8()
        window.saldo1()     
        window.saldo2()
        window.saldo3()
        window.saldo4()

if __name__ == "__main__":
    app = QApplication(sys.argv)
    window = CatatanKeuanganApp()
    window.show()
    sys.exit(app.exec_())
