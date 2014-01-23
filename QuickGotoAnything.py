import sublime
import sublime_plugin
import re

class QuickGotoCommand(sublime_plugin.TextCommand):
    def doCommand(self, edit, prifix, reg):
        for sel in self.view.sel():
            if sel.empty():
                sel = self.view.word(sel)
            word_sel = self.view.substr(sel)
            word_sel = word_sel.strip()
            if not re.match(reg, word_sel):
                word_sel = ''
            self.view.window().run_command("show_overlay", {"overlay": "goto", "text": prifix+word_sel})

class QuickGotoFunctionCommand(QuickGotoCommand):
    def run(self, edit):
        self.doCommand(edit, '@', '^[a-zA-Z_]+[a-zA-Z0-9_]*$')
        
class QuickGotoVariableCommand(QuickGotoCommand):
    def run(self, edit):
        self.doCommand(edit, '#', '^[a-zA-Z_]+[a-zA-Z0-9_]*$')
        
class QuickGotoFileCommand(QuickGotoCommand):
    def run(self, edit):
        # space to '~' and not ':*?"<>|'
        self.doCommand(edit, '', '^[ !#-)+-9;=@-{}~]+$')
        
