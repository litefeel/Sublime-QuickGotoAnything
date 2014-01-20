import sublime
import sublime_plugin
import re

class QuickGotoCommand(sublime_plugin.TextCommand):
    def doCommand(self, edit, prifix):
        for sel in self.view.sel():
            if sel.empty():
                sel = self.view.word(sel)
            word_sel = self.view.substr(sel)
            if not re.search('[a-zA-Z]', word_sel):
                word_sel = ''
            self.view.window().run_command("show_overlay", {"overlay": "goto", "text": prifix+word_sel})

class QuickGotoFunctionCommand(QuickGotoCommand):
    def run(self, edit):
        self.doCommand(edit, '@')
        
class QuickGotoVariableCommand(QuickGotoCommand):
    def run(self, edit):
        self.doCommand(edit, '#')
        
class QuickGotoFileCommand(QuickGotoCommand):
    def run(self, edit):
        self.doCommand(edit, '')
        
