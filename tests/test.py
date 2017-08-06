import sublime
import sys
from unittest import TestCase

version = sublime.version()


class stderrobj:
    def __init__(self):
        self.buff=''
        self.__console__=sys.stderr
        sys.stderr = self
        
    def write(self, output_stream):
        self.buff+=output_stream

    def empty(self):
        return self.buff == ''

    def reset(self):
        if self.__console__ is not None:
            sys.stderr = self.__console__
            self.__console__ = None


# for testing sublime command
class TestQuickGotoAnything(TestCase):

    def setUp(self):
        self.view = sublime.active_window().new_file()
        # make sure we have a window to work with
        s = sublime.load_settings("Preferences.sublime-settings")
        s.set("close_windows_when_empty", False)

        self.obj = stderrobj()

    def tearDown(self):
        self.obj.reset()
        if self.view:
            self.view.set_scratch(True)
            self.view.window().focus_view(self.view)
            self.view.window().run_command("close_file")

        self.assertTrue(self.obj.empty(), self.obj.buff)

    # since ST3 uses python 2 and python 2 doesn't support @unittest.skip,
    # we have to do primitive skipping
    # if version >= '3000':
    #     def test_hello_world_st3(self):
    #         self.view.run_command("quick_goto_function")
    #         first_row = self.getRow(0)
    #         self.assertEqual(first_row, "hello world")

    def test_goto_function(self):
        self.view.run_command("quick_goto_function")

    def test_goto_variable(self):
        self.view.run_command("quick_goto_variable")

    def test_goto_file(self):
        self.view.run_command("quick_goto_file")
        


# for testing internal function
# if version < '3000':
#     # st2
#     QuickGotoAnything = sys.modules["QuickGotoAnything"]
# else:
#     # st3
#     QuickGotoAnything = sys.modules["QuickGotoAnything.QuickGotoAnything"]


# class TestFunctions(TestCase):

#     def setUp(self):
#         self.view = sublime.active_window().new_file()
#         # make sure we have a window to work with
#         s = sublime.load_settings("Preferences.sublime-settings")
#         s.set("close_windows_when_empty", False)

#     def tearDown(self):
#         if self.view:
#             self.view.set_scratch(True)
#             self.view.window().focus_view(self.view)
#             self.view.window().run_command("close_file")

#     def test_foo(self):
#         command = QuickGotoAnything.QuickGotoFunctionCommand()
#         command.run(None)