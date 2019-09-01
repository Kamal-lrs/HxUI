# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'devise.ui'
#
# Created by: PyQt5 UI code generator 5.9.2
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtGui, QtWidgets

class Ui_Form(object):
    def setupUi(self, Form):
        Form.setObjectName("Form")
        Form.resize(350, 195)
        Form.setMaximumSize(QtCore.QSize(350, 250))
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
        self.txt_id.setObjectName("txt_id")
        self.formLayout.setWidget(0, QtWidgets.QFormLayout.FieldRole, self.txt_id)
        self.lbl_code = QtWidgets.QLabel(Form)
        self.lbl_code.setObjectName("lbl_code")
        self.formLayout.setWidget(1, QtWidgets.QFormLayout.LabelRole, self.lbl_code)
        self.txt_code = QtWidgets.QLineEdit(Form)
        self.txt_code.setObjectName("txt_code")
        self.formLayout.setWidget(1, QtWidgets.QFormLayout.FieldRole, self.txt_code)
        self.lbl_description = QtWidgets.QLabel(Form)
        self.lbl_description.setObjectName("lbl_description")
        self.formLayout.setWidget(2, QtWidgets.QFormLayout.LabelRole, self.lbl_description)
        self.txt_description = QtWidgets.QLineEdit(Form)
        self.txt_description.setObjectName("txt_description")
        self.formLayout.setWidget(2, QtWidgets.QFormLayout.FieldRole, self.txt_description)
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
        Form.setWindowTitle(_translate("Form", "DEVISE"))
        self.lbl_id.setText(_translate("Form", "id"))
        self.lbl_code.setText(_translate("Form", "Code"))
        self.lbl_description.setText(_translate("Form", "Description"))
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

