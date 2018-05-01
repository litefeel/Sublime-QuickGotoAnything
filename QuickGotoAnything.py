# coding=utf-8
import sublime
import sublime_plugin
import re

class QuickGotoFileCommand(QuickGotoCommand):
    def run(self, edit):
        for sel in self.view.sel():
            if sel.empty():
                self.view.window().run_command("show_overlay", {"overlay": "goto", "show_files": True})
            else:
                word_sel = self.view.substr(sel)
                word_sel = word_sel.strip()
                self.view.window().run_command("show_overlay", {"overlay": "goto", "show_files": True, "text": word_sel})
                self.view.window().run_command("select_all")
        
