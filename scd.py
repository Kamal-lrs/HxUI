# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'scd.ui'
#
# Created by: PyQt5 UI code generator 5.9.2
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtGui, QtWidgets

class Ui_Form(object):
    def setupUi(self, Form):
        Form.setObjectName("Form")
        Form.resize(330, 257)
        Form.setMaximumSize(QtCore.QSize(330, 260))
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
        self.lbl_fonds = QtWidgets.QLabel(Form)
        self.lbl_fonds.setObjectName("lbl_fonds")
        self.formLayout.setWidget(1, QtWidgets.QFormLayout.LabelRole, self.lbl_fonds)
        self.cb_code_fonds = QtWidgets.QComboBox(Form)
        self.cb_code_fonds.setMaximumSize(QtCore.QSize(120, 16777215))
        self.cb_code_fonds.setObjectName("cb_code_fonds")
        self.formLayout.setWidget(1, QtWidgets.QFormLayout.FieldRole, self.cb_code_fonds)
        self.lbl_attribut = QtWidgets.QLabel(Form)
        self.lbl_attribut.setObjectName("lbl_attribut")
        self.formLayout.setWidget(2, QtWidgets.QFormLayout.LabelRole, self.lbl_attribut)
        self.txt_attribut = QtWidgets.QLineEdit(Form)
        self.txt_attribut.setMaximumSize(QtCore.QSize(120, 16777215))
        self.txt_attribut.setObjectName("txt_attribut")
        self.formLayout.setWidget(2, QtWidgets.QFormLayout.FieldRole, self.txt_attribut)
        self.lbl_old_value = QtWidgets.QLabel(Form)
        self.lbl_old_value.setObjectName("lbl_old_value")
        self.formLayout.setWidget(3, QtWidgets.QFormLayout.LabelRole, self.lbl_old_value)
        self.txt_old_value = QtWidgets.QLineEdit(Form)
        self.txt_old_value.setMaximumSize(QtCore.QSize(120, 16777215))
        self.txt_old_value.setObjectName("txt_old_value")
        self.formLayout.setWidget(3, QtWidgets.QFormLayout.FieldRole, self.txt_old_value)
        self.lbl_new_value = QtWidgets.QLabel(Form)
        self.lbl_new_value.setObjectName("lbl_new_value")
        self.formLayout.setWidget(4, QtWidgets.QFormLayout.LabelRole, self.lbl_new_value)
        self.txt_new_value = QtWidgets.QLineEdit(Form)
        self.txt_new_value.setMaximumSize(QtCore.QSize(120, 16777215))
        self.txt_new_value.setObjectName("txt_new_value")
        self.formLayout.setWidget(4, QtWidgets.QFormLayout.FieldRole, self.txt_new_value)
        self.lbl_date_effet = QtWidgets.QLabel(Form)
        self.lbl_date_effet.setObjectName("lbl_date_effet")
        self.formLayout.setWidget(5, QtWidgets.QFormLayout.LabelRole, self.lbl_date_effet)
        self.dt_date_effet = QtWidgets.QDateEdit(Form)
        self.dt_date_effet.setMaximumSize(QtCore.QSize(120, 16777215))
        self.dt_date_effet.setCalendarPopup(True)
        self.dt_date_effet.setObjectName("dt_date_effet")
        self.formLayout.setWidget(5, QtWidgets.QFormLayout.FieldRole, self.dt_date_effet)
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
        self.txt_description_2 = QtWidgets.QTextEdit(Form)
        self.txt_description_2.setMaximumSize(QtCore.QSize(16777215, 50))
        self.txt_description_2.setFocusPolicy(QtCore.Qt.NoFocus)
        self.txt_description_2.setFrameShape(QtWidgets.QFrame.NoFrame)
        self.txt_description_2.setTabChangesFocus(True)
        self.txt_description_2.setDocumentTitle("")
        self.txt_description_2.setUndoRedoEnabled(False)
        self.txt_description_2.setReadOnly(True)
        self.txt_description_2.setAcceptRichText(True)
        self.txt_description_2.setObjectName("txt_description_2")
        self.verticalLayout_2.addWidget(self.txt_description_2)
        spacerItem2 = QtWidgets.QSpacerItem(20, 40, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Expanding)
        self.verticalLayout_2.addItem(spacerItem2)

        self.retranslateUi(Form)
        QtCore.QMetaObject.connectSlotsByName(Form)

    def retranslateUi(self, Form):
        _translate = QtCore.QCoreApplication.translate
        Form.setWindowTitle(_translate("Form", "SCD FONDS MARKET"))
        self.lbl_id.setText(_translate("Form", "id"))
        self.lbl_fonds.setText(_translate("Form", "Code fonds"))
        self.lbl_attribut.setText(_translate("Form", "Attribut"))
        self.lbl_old_value.setText(_translate("Form", "Old value"))
        self.lbl_new_value.setText(_translate("Form", "New value"))
        self.lbl_date_effet.setText(_translate("Form", "Date effet"))
        self.bu_add.setText(_translate("Form", "Enregistrer"))
        self.bu_delete.setText(_translate("Form", "Supprimer"))
        self.bu_close.setText(_translate("Form", "Fermer"))
        self.txt_description_2.setToolTip(_translate("Form", "Block d\'affichage des messages système."))
        self.txt_description_2.setHtml(_translate("Form", "<!DOCTYPE HTML PUBLIC \"-//W3C//DTD HTML 4.0//EN\" \"http://www.w3.org/TR/REC-html40/strict.dtd\">\n"
"<html><head><meta name=\"qrichtext\" content=\"1\" /><style type=\"text/css\">\n"
"p, li { white-space: pre-wrap; }\n"
"</style></head><body style=\" font-family:\'MS Shell Dlg 2\'; font-size:7.8pt; font-weight:400; font-style:normal;\">\n"
"<p style=\"-qt-paragraph-type:empty; margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px; font-size:14pt;\"><br /></p></body></html>"))
        self.txt_description_2.setPlaceholderText(_translate("Form", "Messages Système"))


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    Form = QtWidgets.QWidget()
    ui = Ui_Form()
    ui.setupUi(Form)
    Form.show()
    sys.exit(app.exec_())

