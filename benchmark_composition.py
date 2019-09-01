# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'benchmark_composition.ui'
#
# Created by: PyQt5 UI code generator 5.9.2
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtGui, QtWidgets

class Ui_Form(object):
    def setupUi(self, Form):
        Form.setObjectName("Form")
        Form.resize(410, 228)
        Form.setMaximumSize(QtCore.QSize(410, 260))
        self.verticalLayout_2 = QtWidgets.QVBoxLayout(Form)
        self.verticalLayout_2.setObjectName("verticalLayout_2")
        self.horizontalLayout = QtWidgets.QHBoxLayout()
        self.horizontalLayout.setObjectName("horizontalLayout")
        self.formLayout = QtWidgets.QFormLayout()
        self.formLayout.setHorizontalSpacing(20)
        self.formLayout.setObjectName("formLayout")
        self.lbl_id = QtWidgets.QLabel(Form)
        self.lbl_id.setObjectName("lbl_id")
        self.formLayout.setWidget(0, QtWidgets.QFormLayout.LabelRole, self.lbl_id)
        self.txt_id = QtWidgets.QLineEdit(Form)
        self.txt_id.setMaximumSize(QtCore.QSize(120, 16777215))
        self.txt_id.setObjectName("txt_id")
        self.formLayout.setWidget(0, QtWidgets.QFormLayout.FieldRole, self.txt_id)
        self.lbl_code_benchmark = QtWidgets.QLabel(Form)
        self.lbl_code_benchmark.setObjectName("lbl_code_benchmark")
        self.formLayout.setWidget(1, QtWidgets.QFormLayout.LabelRole, self.lbl_code_benchmark)
        self.cb_code_benchmark = QtWidgets.QComboBox(Form)
        self.cb_code_benchmark.setMaximumSize(QtCore.QSize(120, 16777215))
        self.cb_code_benchmark.setObjectName("cb_code_benchmark")
        self.formLayout.setWidget(1, QtWidgets.QFormLayout.FieldRole, self.cb_code_benchmark)
        self.lbl_code_indice = QtWidgets.QLabel(Form)
        self.lbl_code_indice.setObjectName("lbl_code_indice")
        self.formLayout.setWidget(2, QtWidgets.QFormLayout.LabelRole, self.lbl_code_indice)
        self.cb_code_indice = QtWidgets.QComboBox(Form)
        self.cb_code_indice.setMaximumSize(QtCore.QSize(120, 16777215))
        self.cb_code_indice.setObjectName("cb_code_indice")
        self.formLayout.setWidget(2, QtWidgets.QFormLayout.FieldRole, self.cb_code_indice)
        self.lbl_poinds = QtWidgets.QLabel(Form)
        self.lbl_poinds.setObjectName("lbl_poinds")
        self.formLayout.setWidget(3, QtWidgets.QFormLayout.LabelRole, self.lbl_poinds)
        self.txt_poids = QtWidgets.QLineEdit(Form)
        self.txt_poids.setMaximumSize(QtCore.QSize(120, 16777215))
        self.txt_poids.setObjectName("txt_poids")
        self.formLayout.setWidget(3, QtWidgets.QFormLayout.FieldRole, self.txt_poids)
        self.lbl_spread_indice = QtWidgets.QLabel(Form)
        self.lbl_spread_indice.setObjectName("lbl_spread_indice")
        self.formLayout.setWidget(4, QtWidgets.QFormLayout.LabelRole, self.lbl_spread_indice)
        self.txt_spread_indice = QtWidgets.QLineEdit(Form)
        self.txt_spread_indice.setMaximumSize(QtCore.QSize(120, 16777215))
        self.txt_spread_indice.setObjectName("txt_spread_indice")
        self.formLayout.setWidget(4, QtWidgets.QFormLayout.FieldRole, self.txt_spread_indice)
        self.horizontalLayout.addLayout(self.formLayout)
        spacerItem = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout.addItem(spacerItem)
        self.verticalLayout = QtWidgets.QVBoxLayout()
        self.verticalLayout.setSpacing(7)
        self.verticalLayout.setObjectName("verticalLayout")
        self.bu_add = QtWidgets.QPushButton(Form)
        self.bu_add.setObjectName("bu_add")
        self.verticalLayout.addWidget(self.bu_add)
        self.bu_delete = QtWidgets.QPushButton(Form)
        self.bu_delete.setObjectName("bu_delete")
        self.verticalLayout.addWidget(self.bu_delete)
        self.bu_close = QtWidgets.QPushButton(Form)
        self.bu_close.setObjectName("bu_close")
        self.verticalLayout.addWidget(self.bu_close)
        spacerItem1 = QtWidgets.QSpacerItem(20, 40, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Expanding)
        self.verticalLayout.addItem(spacerItem1)
        self.horizontalLayout.addLayout(self.verticalLayout)
        self.verticalLayout_2.addLayout(self.horizontalLayout)
        self.txt_description = QtWidgets.QTextEdit(Form)
        self.txt_description.setMaximumSize(QtCore.QSize(16777215, 50))
        self.txt_description.setFocusPolicy(QtCore.Qt.NoFocus)
        self.txt_description.setFrameShape(QtWidgets.QFrame.NoFrame)
        self.txt_description.setTabChangesFocus(True)
        self.txt_description.setDocumentTitle("")
        self.txt_description.setUndoRedoEnabled(False)
        self.txt_description.setReadOnly(True)
        self.txt_description.setAcceptRichText(True)
        self.txt_description.setObjectName("txt_description")
        self.verticalLayout_2.addWidget(self.txt_description)
        spacerItem2 = QtWidgets.QSpacerItem(20, 40, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Expanding)
        self.verticalLayout_2.addItem(spacerItem2)

        self.retranslateUi(Form)
        QtCore.QMetaObject.connectSlotsByName(Form)

    def retranslateUi(self, Form):
        _translate = QtCore.QCoreApplication.translate
        Form.setWindowTitle(_translate("Form", "BENCHMARK COMPOSITION"))
        self.lbl_id.setText(_translate("Form", "id"))
        self.lbl_code_benchmark.setText(_translate("Form", "Code benchmark"))
        self.lbl_code_indice.setText(_translate("Form", "Code indice"))
        self.lbl_poinds.setText(_translate("Form", "Poids"))
        self.lbl_spread_indice.setText(_translate("Form", "Spread indice"))
        self.bu_add.setText(_translate("Form", "Enregistrer"))
        self.bu_delete.setText(_translate("Form", "Supprimer"))
        self.bu_close.setText(_translate("Form", "Fermer"))
        self.txt_description.setToolTip(_translate("Form", "Block d\'affichage des messages système."))
        self.txt_description.setHtml(_translate("Form", "<!DOCTYPE HTML PUBLIC \"-//W3C//DTD HTML 4.0//EN\" \"http://www.w3.org/TR/REC-html40/strict.dtd\">\n"
"<html><head><meta name=\"qrichtext\" content=\"1\" /><style type=\"text/css\">\n"
"p, li { white-space: pre-wrap; }\n"
"</style></head><body style=\" font-family:\'MS Shell Dlg 2\'; font-size:7.8pt; font-weight:400; font-style:normal;\">\n"
"<p style=\"-qt-paragraph-type:empty; margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px; font-size:14pt;\"><br /></p></body></html>"))
        self.txt_description.setPlaceholderText(_translate("Form", "Messages Système"))


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    Form = QtWidgets.QWidget()
    ui = Ui_Form()
    ui.setupUi(Form)
    Form.show()
    sys.exit(app.exec_())

