# -*- coding: utf-8 -*-

"""
    pugdebug - a standalone PHP debugger
    =========================
    copyright: (c) 2015 Robert Basic
    license: GNU GPL v3, see LICENSE for more details
"""

__author__ = "robertbasic"

from PyQt5.QtWidgets import QMainWindow, QGridLayout, QWidget, QDockWidget, QToolBar
from PyQt5.QtGui import QFont
from PyQt5.QtCore import Qt

from pugdebug.gui.breakpoints import PugdebugBreakpointViewer
from pugdebug.gui.documents import PugdebugDocumentViewer
from pugdebug.gui.file_browser import PugdebugFileBrowser
from pugdebug.gui.settings import PugdebugSettingsWindow
from pugdebug.gui.stacktraces import PugdebugStacktraceViewer
from pugdebug.gui.variables import PugdebugVariableViewer


class PugdebugMainWindow(QMainWindow):

    def __init__(self):
        super(PugdebugMainWindow, self).__init__()
        self.setObjectName("pugdebug")
        self.setWindowTitle("pugdebug")
        self.setup_gui_elements()

    def setup_gui_elements(self):
        self.setup_toolbar()
        self.setup_fonts()
        self.setup_components()
        self.setup_main_window()

        self.set_statusbar_text("Idle...")

    def setup_components(self):
        self.document_viewer = PugdebugDocumentViewer()
        self.file_browser = PugdebugFileBrowser()
        self.stacktrace_viewer = PugdebugStacktraceViewer()
        self.breakpoint_viewer = PugdebugBreakpointViewer()
        self.variable_viewer = PugdebugVariableViewer()
        self.settings_window = PugdebugSettingsWindow(self)

    def setup_main_window(self):
        """ Sets up the central and dockable widgets on the main window.
        """

        self.setCentralWidget(self.document_viewer)

        dw = QDockWidget("File Browser", self)
        dw.setWidget(self.file_browser)
        self.addDockWidget(Qt.LeftDockWidgetArea, dw)

        dw = QDockWidget("Stack Traces", self)
        dw.setWidget(self.stacktrace_viewer)
        self.addDockWidget(Qt.RightDockWidgetArea, dw)

        dw = QDockWidget("Breakpoints", self)
        dw.setWidget(self.breakpoint_viewer)
        self.addDockWidget(Qt.RightDockWidgetArea, dw)

        dw = QDockWidget("Variables", self)
        dw.setWidget(self.variable_viewer)
        self.addDockWidget(Qt.RightDockWidgetArea, dw)

        dw = QDockWidget("Settings", self)
        dw.setWidget(self.settings_window)
        self.addDockWidget(Qt.LeftDockWidgetArea, dw)

    def setup_fonts(self):
        font = QFont('mono')
        font.setStyleHint(QFont.Monospace)
        font.setPixelSize(12)
        self.setFont(font)

    def setup_toolbar(self):
        toolbar = QToolBar()

        self.start_debug_action = toolbar.addAction("Start")
        self.stop_debug_action = toolbar.addAction("Stop")
        self.run_debug_action = toolbar.addAction("Run")
        self.step_over_action = toolbar.addAction("Over")
        self.step_into_action = toolbar.addAction("In")
        self.step_out_action = toolbar.addAction("Out")

        self.toggle_actions(False)

        self.addToolBar(toolbar)

    def toggle_actions(self, enabled):
        self.run_debug_action.setEnabled(enabled)
        self.step_over_action.setEnabled(enabled)
        self.step_into_action.setEnabled(enabled)
        self.step_out_action.setEnabled(enabled)

        self.start_debug_action.setEnabled(not enabled)

    def get_file_browser(self):
        return self.file_browser

    def get_settings(self):
        return self.settings_window

    def get_document_viewer(self):
        return self.document_viewer

    def get_variable_viewer(self):
        return self.variable_viewer

    def get_breakpoint_viewer(self):
        return self.breakpoint_viewer

    def set_statusbar_text(self, text):
        self.statusBar().showMessage(text)
