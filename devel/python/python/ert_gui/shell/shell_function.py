from math import floor
import shlex
import textwrap
from ert_gui.shell import createParameterizedHelpFunction, autoCompleteList


class ShellFunction(object):
    command_help_message = "The command: '%s' supports the following keywords:"

    def __init__(self, name, cmd):
        super(ShellFunction, self).__init__()
        self.cmd = cmd
        """ :type: Cmd """
        self.name = name
        """ :type: ErtShell """

        setattr(cmd.__class__, "do_%s" % name, self.doKeywords)
        setattr(cmd.__class__, "complete_%s" % name, self.completeKeywords)
        setattr(cmd.__class__, "help_%s" % name, self.helpKeywords)


    def ert(self):
        """ @rtype: ert.enkf.enkf_main.EnKFMain """
        return self.cmd.ert()

    def isConfigLoaded(self, verbose=True):
        """ @rtype: bool """
        if self.ert() is None:
            if verbose:
                print("Error: A config file has not been loaded!")
            return False
        return True

    def addHelpFunction(self, function_name, parameter, help_message):
        setattr(self.__class__, "help_%s" % function_name, createParameterizedHelpFunction(parameter, help_message))

    def findKeywords(self):
        return [name[3:] for name in dir(self.__class__) if name.startswith("do_")]

    def helpKeywords(self):
        print(self.command_help_message % self.name)
        keywords = self.findKeywords()
        keyword_column_width = self.widthAsPercentageOfConsoleWidth(20)
        parameter_column_width = self.widthAsPercentageOfConsoleWidth(30)
        help_column_width = self.widthAsPercentageOfConsoleWidth(48)
        help_format = " %-" + str(keyword_column_width) + "s %-" + str(parameter_column_width) + "s %-" + str(help_column_width) + "s"
        print(help_format % ("Keyword", "Parameter(s)", "Help"))

        for keyword in keywords:
            message = "No help available!"
            parameters = None
            if hasattr(self, "help_%s" % keyword):
                func = getattr(self, "help_%s" % keyword)
                parameters, message = func()

            message = textwrap.wrap(message, help_column_width)
            print(help_format % (keyword, parameters, message[0]))

            if len(message) > 1:
                for line in message[1:]:
                    print(help_format % ("", "", line))


    def completeKeywords(self, text, line, begidx, endidx):
        arguments = shlex.split(line)
        assert arguments[0] == self.name

        line = line[len(self.name) + 1:]
        begidx = begidx - len(self.name) + 1
        endidx = endidx - len(self.name) + 1
        keyword, sep, arguments = line.partition(' ')

        if begidx >= len(keyword) and keyword in self.findKeywords():
            if hasattr(self, "complete_%s" % keyword):
                func = getattr(self, "complete_%s" % keyword)
                return func(text, line, begidx, endidx)
            else:
                return []
        else:
            return autoCompleteList(text, self.findKeywords())

    def doKeywords(self, line):
        keyword, sep, arguments = line.partition(' ')

        if hasattr(self, "do_%s" % keyword):
            func = getattr(self, "do_%s" % keyword)
            return func(arguments)
        else:
            print("Error: Unknown keyword: '%s'" % keyword)

    def splitArguments(self, line):
        """ @rtype: list of str """
        return shlex.split(line)

    def columnize(self, items):
        self.cmd.columnize(items, self.getTerminalSize()[0])


    def widthAsPercentageOfConsoleWidth(self, percentage):
        width, height = self.getTerminalSize()
        return int(floor(percentage * width / 100.0))


    def getTerminalSize(self):
        """
         @rtype: tuple of (int,int)
         @return: Console dimensions as: width, height
        """
        import os
        env = os.environ

        def ioctl_GWINSZ(fd):
            try:
                import fcntl, termios, struct, os
                cr = struct.unpack('hh', fcntl.ioctl(fd, termios.TIOCGWINSZ, '1234'))
            except:
                return
            return cr

        cr = ioctl_GWINSZ(0) or ioctl_GWINSZ(1) or ioctl_GWINSZ(2)

        if not cr:
            try:
                fd = os.open(os.ctermid(), os.O_RDONLY)
                cr = ioctl_GWINSZ(fd)
                os.close(fd)
            except:
                pass

        if not cr:
            cr = (env.get('LINES', 25), env.get('COLUMNS', 80))
        return int(cr[1]), int(cr[0])