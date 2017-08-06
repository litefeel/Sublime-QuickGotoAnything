# coding=utf-8
import sublime
import sublime_plugin
import re

class QuickGotoCommand(sublime_plugin.TextCommand):
    def doCommand(self, edit, prifix, reg, show_files = True):
        for sel in self.view.sel():
            if sel.empty():
                sel = self.view.word(sel)
            word_sel = self.view.substr(sel)
            word_sel = word_sel.strip()

            # delete prefix and suffix
            settings = sublime.load_settings('QuickGotoAnything.sublime-settings')
            del_prefix = settings.get('del_prefix')
            del_suffix = settings.get('del_suffix')
            if del_prefix and word_sel[0:len(del_prefix)] == del_prefix:
                word_sel = word_sel[len(del_prefix):len(word_sel)]
            if del_suffix and word_sel[-len(del_suffix):len(word_sel)] == del_suffix:
                word_sel = word_sel[0:-len(del_suffix)]

            if not re.match(reg, word_sel):
                word_sel = ''
            self.view.window().run_command("show_overlay", {"overlay": "goto", "show_files": show_files, "text": prifix+word_sel})

class QuickGotoFunctionCommand(QuickGotoCommand):
    def run(self, edit):
        self.doCommand(edit, '@', '^[a-zA-Z_]+[a-zA-Z0-9_]*$')
        
class QuickGotoVariableCommand(QuickGotoCommand):
    def run(self, edit):
        self.doCommand(edit, '#', '^[a-zA-Z_]+[a-zA-Z0-9_]*$')
        
class QuickGotoFileCommand(QuickGotoCommand):
    def run(self, edit, show_files = True):
        # space to '~' and not ':*?"<>|'
        self.doCommand(edit, '', '^[ !#-)+-9;=@-{}~]+$', show_files)
        
