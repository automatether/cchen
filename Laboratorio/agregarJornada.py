# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file '.\agregarJornada.ui'
#
# Created by: PyQt5 UI code generator 5.15.4
#
# WARNING: Any manual changes made to this file will be lost when pyuic5 is
# run again.  Do not edit this file unless you know what you are doing.


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_AgregarJornada(object):
    def setupUi(self, AgregarJornada):
        AgregarJornada.setObjectName("AgregarJornada")
        AgregarJornada.resize(381, 344)
        self.cancelar = QtWidgets.QPushButton(AgregarJornada)
        self.cancelar.setGeometry(QtCore.QRect(220, 290, 111, 29))
        font = QtGui.QFont()
        font.setPointSize(10)
        self.cancelar.setFont(font)
        self.cancelar.setObjectName("cancelar")
        self.agregar = QtWidgets.QPushButton(AgregarJornada)
        self.agregar.setGeometry(QtCore.QRect(58, 290, 101, 29))
        font = QtGui.QFont()
        font.setPointSize(10)
        self.agregar.setFont(font)
        self.agregar.setObjectName("agregar")
        self.label = QtWidgets.QLabel(AgregarJornada)
        self.label.setGeometry(QtCore.QRect(60, 150, 151, 20))
        self.label.setObjectName("label")
        self.experimento = QtWidgets.QComboBox(AgregarJornada)
        self.experimento.setGeometry(QtCore.QRect(210, 150, 121, 21))
        self.experimento.setObjectName("experimento")
        self.label_2 = QtWidgets.QLabel(AgregarJornada)
        self.label_2.setGeometry(QtCore.QRect(60, 90, 151, 20))
        self.label_2.setObjectName("label_2")
        self.label_91 = QtWidgets.QLabel(AgregarJornada)
        self.label_91.setGeometry(QtCore.QRect(30, 20, 311, 31))
        font = QtGui.QFont()
        font.setPointSize(12)
        font.setBold(True)
        self.label_91.setFont(font)
        self.label_91.setAlignment(QtCore.Qt.AlignCenter)
        self.label_91.setObjectName("label_91")
        self.nombre = QtWidgets.QLineEdit(AgregarJornada)
        self.nombre.setGeometry(QtCore.QRect(210, 90, 121, 21))
        self.nombre.setText("")
        self.nombre.setObjectName("nombre")
        self.label_3 = QtWidgets.QLabel(AgregarJornada)
        self.label_3.setGeometry(QtCore.QRect(60, 200, 261, 51))
        self.label_3.setAlignment(QtCore.Qt.AlignCenter)
        self.label_3.setWordWrap(True)
        self.label_3.setObjectName("label_3")

        self.retranslateUi(AgregarJornada)
        QtCore.QMetaObject.connectSlotsByName(AgregarJornada)

    def retranslateUi(self, AgregarJornada):
        _translate = QtCore.QCoreApplication.translate
        AgregarJornada.setWindowTitle(_translate("AgregarJornada", "Dialog"))
        self.cancelar.setText(_translate("AgregarJornada", "Cancelar"))
        self.agregar.setText(_translate("AgregarJornada", "Agregar"))
        self.label.setText(_translate("AgregarJornada", "Experimento"))
        self.label_2.setText(_translate("AgregarJornada", "Nombre"))
        self.label_91.setText(_translate("AgregarJornada", "Agregar Jornada"))
        self.label_3.setText(_translate("AgregarJornada", "Nota: Esto agregara la nueva jornada al servidor"))


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    AgregarJornada = QtWidgets.QDialog()
    ui = Ui_AgregarJornada()
    ui.setupUi(AgregarJornada)
    AgregarJornada.show()
    sys.exit(app.exec_())
