# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file '.\agregarCanal.ui'
#
# Created by: PyQt5 UI code generator 5.15.4
#
# WARNING: Any manual changes made to this file will be lost when pyuic5 is
# run again.  Do not edit this file unless you know what you are doing.


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_AgregarCanal(object):
    def setupUi(self, AgregarCanal):
        AgregarCanal.setObjectName("AgregarCanal")
        AgregarCanal.resize(381, 341)
        self.cancelar = QtWidgets.QPushButton(AgregarCanal)
        self.cancelar.setGeometry(QtCore.QRect(240, 280, 83, 29))
        font = QtGui.QFont()
        font.setPointSize(10)
        self.cancelar.setFont(font)
        self.cancelar.setObjectName("cancelar")
        self.agregar = QtWidgets.QPushButton(AgregarCanal)
        self.agregar.setGeometry(QtCore.QRect(60, 280, 83, 29))
        font = QtGui.QFont()
        font.setPointSize(10)
        self.agregar.setFont(font)
        self.agregar.setObjectName("agregar")
        self.label = QtWidgets.QLabel(AgregarCanal)
        self.label.setGeometry(QtCore.QRect(60, 150, 151, 20))
        self.label.setObjectName("label")
        self.osciloscopio = QtWidgets.QComboBox(AgregarCanal)
        self.osciloscopio.setGeometry(QtCore.QRect(210, 150, 121, 21))
        self.osciloscopio.setObjectName("osciloscopio")
        self.label_2 = QtWidgets.QLabel(AgregarCanal)
        self.label_2.setGeometry(QtCore.QRect(60, 90, 151, 20))
        self.label_2.setObjectName("label_2")
        self.label_3 = QtWidgets.QLabel(AgregarCanal)
        self.label_3.setGeometry(QtCore.QRect(60, 210, 151, 20))
        self.label_3.setObjectName("label_3")
        self.canal = QtWidgets.QComboBox(AgregarCanal)
        self.canal.setGeometry(QtCore.QRect(210, 210, 121, 21))
        self.canal.setObjectName("canal")
        self.label_91 = QtWidgets.QLabel(AgregarCanal)
        self.label_91.setGeometry(QtCore.QRect(30, 20, 311, 31))
        font = QtGui.QFont()
        font.setPointSize(12)
        font.setBold(True)
        self.label_91.setFont(font)
        self.label_91.setAlignment(QtCore.Qt.AlignCenter)
        self.label_91.setObjectName("label_91")
        self.nombre_variable = QtWidgets.QLineEdit(AgregarCanal)
        self.nombre_variable.setGeometry(QtCore.QRect(210, 90, 121, 21))
        self.nombre_variable.setText("")
        self.nombre_variable.setObjectName("nombre_variable")

        self.retranslateUi(AgregarCanal)
        QtCore.QMetaObject.connectSlotsByName(AgregarCanal)

    def retranslateUi(self, AgregarCanal):
        _translate = QtCore.QCoreApplication.translate
        AgregarCanal.setWindowTitle(_translate("AgregarCanal", "Dialog"))
        self.cancelar.setText(_translate("AgregarCanal", "Cancelar"))
        self.agregar.setText(_translate("AgregarCanal", "Agregar"))
        self.label.setText(_translate("AgregarCanal", "Osciloscopio"))
        self.label_2.setText(_translate("AgregarCanal", "Nombre Curva"))
        self.label_3.setText(_translate("AgregarCanal", "Canal"))
        self.label_91.setText(_translate("AgregarCanal", "Agregar Nuevo Canal"))


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    AgregarCanal = QtWidgets.QDialog()
    ui = Ui_AgregarCanal()
    ui.setupUi(AgregarCanal)
    AgregarCanal.show()
    sys.exit(app.exec_())
