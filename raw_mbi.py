# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'raw_mbi.ui'
#
# Created by: PyQt5 UI code generator 5.9.2
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtGui, QtWidgets

class Ui_Form(object):
    def setupUi(self, Form):
        Form.setObjectName("Form")
        Form.resize(400, 315)
        Form.setMaximumSize(QtCore.QSize(400, 315))
        self.verticalLayout_2 = QtWidgets.QVBoxLayout(Form)
        self.verticalLayout_2.setObjectName("verticalLayout_2")
        self.horizontalLayout = QtWidgets.QHBoxLayout()
        self.horizontalLayout.setObjectName("horizontalLayout")
        self.formLayout = QtWidgets.QFormLayout()
        self.formLayout.setSizeConstraint(QtWidgets.QLayout.SetMaximumSize)
        self.formLayout.setHorizontalSpacing(20)
        self.formLayout.setVerticalSpacing(7)
        self.formLayout.setObjectName("formLayout")
        self.lbl_id = QtWidgets.QLabel(Form)
        self.lbl_id.setObjectName("lbl_id")
        self.formLayout.setWidget(0, QtWidgets.QFormLayout.LabelRole, self.lbl_id)
        self.txt_id = QtWidgets.QLineEdit(Form)
        self.txt_id.setMaximumSize(QtCore.QSize(120, 16777215))
        self.txt_id.setObjectName("txt_id")
        self.formLayout.setWidget(0, QtWidgets.QFormLayout.FieldRole, self.txt_id)
        self.lbl_code_strate = QtWidgets.QLabel(Form)
        self.lbl_code_strate.setObjectName("lbl_code_strate")
        self.formLayout.setWidget(2, QtWidgets.QFormLayout.LabelRole, self.lbl_code_strate)
        self.txt_code_strate = QtWidgets.QLineEdit(Form)
        self.txt_code_strate.setMaximumSize(QtCore.QSize(120, 16777215))
        self.txt_code_strate.setObjectName("txt_code_strate")
        self.formLayout.setWidget(2, QtWidgets.QFormLayout.FieldRole, self.txt_code_strate)
        self.lbl_value = QtWidgets.QLabel(Form)
        self.lbl_value.setObjectName("lbl_value")
        self.formLayout.setWidget(3, QtWidgets.QFormLayout.LabelRole, self.lbl_value)
        self.txt_value = QtWidgets.QLineEdit(Form)
        self.txt_value.setMaximumSize(QtCore.QSize(120, 16777215))
        self.txt_value.setObjectName("txt_value")
        self.formLayout.setWidget(3, QtWidgets.QFormLayout.FieldRole, self.txt_value)
        self.lbl_ytm = QtWidgets.QLabel(Form)
        self.lbl_ytm.setObjectName("lbl_ytm")
        self.formLayout.setWidget(4, QtWidgets.QFormLayout.LabelRole, self.lbl_ytm)
        self.txt_ytm = QtWidgets.QLineEdit(Form)
        self.txt_ytm.setMaximumSize(QtCore.QSize(120, 16777215))
        self.txt_ytm.setObjectName("txt_ytm")
        self.formLayout.setWidget(4, QtWidgets.QFormLayout.FieldRole, self.txt_ytm)
        self.lbl_coupon = QtWidgets.QLabel(Form)
        self.lbl_coupon.setObjectName("lbl_coupon")
        self.formLayout.setWidget(5, QtWidgets.QFormLayout.LabelRole, self.lbl_coupon)
        self.txt_coupon = QtWidgets.QLineEdit(Form)
        self.txt_coupon.setMaximumSize(QtCore.QSize(120, 16777215))
        self.txt_coupon.setObjectName("txt_coupon")
        self.formLayout.setWidget(5, QtWidgets.QFormLayout.FieldRole, self.txt_coupon)
        self.lbl_sensibilite = QtWidgets.QLabel(Form)
        self.lbl_sensibilite.setObjectName("lbl_sensibilite")
        self.formLayout.setWidget(6, QtWidgets.QFormLayout.LabelRole, self.lbl_sensibilite)
        self.txt_sensibilite = QtWidgets.QLineEdit(Form)
        self.txt_sensibilite.setMaximumSize(QtCore.QSize(120, 16777215))
        self.txt_sensibilite.setObjectName("txt_sensibilite")
        self.formLayout.setWidget(6, QtWidgets.QFormLayout.FieldRole, self.txt_sensibilite)
        self.lbl_duration = QtWidgets.QLabel(Form)
        self.lbl_duration.setObjectName("lbl_duration")
        self.formLayout.setWidget(7, QtWidgets.QFormLayout.LabelRole, self.lbl_duration)
        self.txt_duration = QtWidgets.QLineEdit(Form)
        self.txt_duration.setMaximumSize(QtCore.QSize(120, 16777215))
        self.txt_duration.setObjectName("txt_duration")
        self.formLayout.setWidget(7, QtWidgets.QFormLayout.FieldRole, self.txt_duration)
        self.lbl_date_marche = QtWidgets.QLabel(Form)
        self.lbl_date_marche.setObjectName("lbl_date_marche")
        self.formLayout.setWidget(1, QtWidgets.QFormLayout.LabelRole, self.lbl_date_marche)
        self.dt_date_marche = QtWidgets.QDateEdit(Form)
        self.dt_date_marche.setCalendarPopup(True)
        self.dt_date_marche.setObjectName("dt_date_marche")
        self.formLayout.setWidget(1, QtWidgets.QFormLayout.FieldRole, self.dt_date_marche)
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
        Form.setWindowTitle(_translate("Form", "RAW MBI"))
        self.lbl_id.setText(_translate("Form", "id "))
        self.lbl_code_strate.setText(_translate("Form", "Code strate "))
        self.lbl_value.setText(_translate("Form", "Value"))
        self.lbl_ytm.setText(_translate("Form", "Ytm"))
        self.lbl_coupon.setText(_translate("Form", "Coupon"))
        self.lbl_sensibilite.setText(_translate("Form", "Sensibilite"))
        self.lbl_duration.setText(_translate("Form", "Duration"))
        self.lbl_date_marche.setText(_translate("Form", "Date marche"))
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

