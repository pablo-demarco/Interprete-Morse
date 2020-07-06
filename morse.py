from PyQt5 import QtCore, QtGui, QtWidgets

class Ui_Form(object):
    def setupUi(self, Form):
        Form.setObjectName("Form")
        Form.resize(400, 234)
        self.widget = QtWidgets.QWidget(Form)
        self.widget.setGeometry(QtCore.QRect(14, 10, 371, 211))
        self.widget.setObjectName("widget")
        self.gridLayout = QtWidgets.QGridLayout(self.widget)
        self.gridLayout.setContentsMargins(0, 0, 0, 0)
        self.gridLayout.setObjectName("gridLayout")
        self.label = QtWidgets.QLabel(self.widget)
        font = QtGui.QFont()
        font.setFamily("Manjari")
        font.setPointSize(14)
        font.setBold(False)
        font.setItalic(False)
        font.setWeight(50)
        self.label.setFont(font)
        self.label.setStyleSheet("font: 14pt \"Manjari\";\n"
"\n"
"")
        self.label.setAlignment(QtCore.Qt.AlignCenter)
        self.label.setObjectName("label")
        self.gridLayout.addWidget(self.label, 0, 0, 1, 2)
        self.label_2 = QtWidgets.QLabel(self.widget)
        self.label_2.setAlignment(QtCore.Qt.AlignBottom|QtCore.Qt.AlignLeading|QtCore.Qt.AlignLeft)
        self.label_2.setObjectName("label_2")
        self.gridLayout.addWidget(self.label_2, 1, 0, 1, 1)
        self.label_3 = QtWidgets.QLabel(self.widget)
        self.label_3.setAlignment(QtCore.Qt.AlignBottom|QtCore.Qt.AlignLeading|QtCore.Qt.AlignLeft)
        self.label_3.setObjectName("label_3")
        self.gridLayout.addWidget(self.label_3, 3, 0, 1, 1)
        self.label_4 = QtWidgets.QLabel(self.widget)
        self.label_4.setAlignment(QtCore.Qt.AlignBottom|QtCore.Qt.AlignLeading|QtCore.Qt.AlignLeft)
        self.label_4.setObjectName("label_4")
        self.gridLayout.addWidget(self.label_4, 3, 1, 1, 1)
        self.txt_cantidad = QtWidgets.QLineEdit(self.widget)
        self.txt_cantidad.setObjectName("txt_cantidad")
        self.gridLayout.addWidget(self.txt_cantidad, 4, 0, 1, 1)
        self.txt_intervalo = QtWidgets.QLineEdit(self.widget)
        self.txt_intervalo.setObjectName("txt_intervalo")
        self.gridLayout.addWidget(self.txt_intervalo, 4, 1, 1, 1)
        self.btn_enviar = QtWidgets.QPushButton(self.widget)
        self.btn_enviar.setObjectName("btn_enviar")
        self.gridLayout.addWidget(self.btn_enviar, 5, 0, 1, 1)
        self.btn_borrar = QtWidgets.QPushButton(self.widget)
        self.btn_borrar.setObjectName("btn_borrar")
        self.gridLayout.addWidget(self.btn_borrar, 5, 1, 1, 1)
        self.txt_mensaje = QtWidgets.QLineEdit(self.widget)
        self.txt_mensaje.setObjectName("txt_mensaje")
        self.gridLayout.addWidget(self.txt_mensaje, 2, 0, 1, 2)

        self.retranslateUi(Form)
        QtCore.QMetaObject.connectSlotsByName(Form)
        
        for puerto in range(0, 9):
            try:
                if 'nt' in os.name:
                    self.arduino = serial.Serial(f'COM{puerto}', 9600)
                else:
                    self.arduino = serial.Serial(f'/dev/ttyACM{puerto}', 9600)
            except Exception as e:
                pass
        
        self.btn_enviar.clicked.connect(self.enviar)
        self.btn_borrar.clicked.connect(self.borrar)
        
        
    def enviar(self):
        if len(self.txt_intervalo.text().strip()) == 0:
            inter = ''
        else:
            inter = ' ' * round(int(self.txt_intervalo.text()) / 1.75)
        m = (self.txt_mensaje.text() + inter) * int(self.txt_cantidad.text())
        self.arduino.write(m.encode())
        
        
    def borrar(self):
        self.txt_intervalo.setText('')
        self.txt_cantidad.setText('')
        self.txt_mensaje.setText('')
        
        
    def retranslateUi(self, Form):
        _translate = QtCore.QCoreApplication.translate
        Form.setWindowTitle(_translate("Form", "Interprete Morse"))
        self.label.setText(_translate("Form", "Interprete de Código Morse"))
        self.label_2.setText(_translate("Form", "Mensaje"))
        self.label_3.setText(_translate("Form", "Cantidad de repeticiones"))
        self.label_4.setText(_translate("Form", "Intervalo entre repeticiones (segundos)"))
        self.btn_enviar.setText(_translate("Form", "Enviar"))
        self.btn_borrar.setText(_translate("Form", "Borrar"))


if __name__ == "__main__":
    import sys
    import serial
    import os
    app = QtWidgets.QApplication(sys.argv)
    Form = QtWidgets.QWidget()
    ui = Ui_Form()
    ui.setupUi(Form)
    Form.show()
    sys.exit(app.exec_())
