# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file '/home/buildbot/buildbot/worker/probe_basic-dev/sources/debian/python3-probe-basic/usr/share/configs/probe_basic/user_tabs/template_main/template_main.ui'
#
# Created by: PyQt5 UI code generator 5.15.9
#
# WARNING: Any manual changes made to this file will be lost when pyuic5 is
# run again.  Do not edit this file unless you know what you are doing.


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_USER(object):
    def setupUi(self, USER):
        USER.setObjectName("USER")
        USER.resize(1645, 619)
        USER.setMaximumSize(QtCore.QSize(1645, 619))
        USER.setProperty("sidebar", False)

        self.retranslateUi(USER)
        QtCore.QMetaObject.connectSlotsByName(USER)

    def retranslateUi(self, USER):
        _translate = QtCore.QCoreApplication.translate
        USER.setWindowTitle(_translate("USER", "USER MAIN"))

        self.surface_scan_x0_3050.textChanged['QString'].connect(self.update_surface_scan_params.click) # type: ignore
        self.surface_scan_x0_3051.textChanged['QString'].connect(self.update_surface_scan_params.click) # type: ignore
        self.surface_scan_height_3052.textChanged['QString'].connect(self.update_surface_scan_params.click) # type: ignore
        self.surface_scan_width_3053.textChanged['QString'].connect(self.update_surface_scan_params.click) # type: ignore
        
        self.update_surface_scan_params.setText(_translate("Form", "UPDATE SURFACE SCAN PARAMETERS2"))
        self.update_surface_scan_params.setProperty("filename", _translate("Form", "surface_scan_param_update.ngc"))


