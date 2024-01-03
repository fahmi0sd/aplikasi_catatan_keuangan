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
from editPemasukan import EditPemasukan
from editPengeluaran import EditPengeluaran

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

                self.close()

            except mc.Error as e:
                print("Gagal menghapus data pemasukan:", e)
                QMessageBox.warning(self, 'Peringatan', 'Gagal menghapus data pemasukan.')