"""
Created on 16 Mar 2017

@author: Bruno Beloff (bruno.beloff@southcoastscience.com)
"""

import optparse


# --------------------------------------------------------------------------------------------------------------------

class CmdLowPassFilter(object):
    """
    unix command line handler
    """

    def __init__(self):
        """
        Constructor
        """
        self.__parser = optparse.OptionParser(usage="%prog -d DELTA_T -c CUT_OFF_FREQ [-v] PATH", version="%prog 1.0")

        # compulsory...
        self.__parser.add_option("--delta", "-d", type="float", nargs=1, action="store", dest="delta",
                                 help="sampling time interval")

        self.__parser.add_option("--cut-off", "-c", type="float", nargs=1, action="store", dest="cut_off",
                                 help="cut-off frequency")

        # optional...
        self.__parser.add_option("--verbose", "-v", action="store_true", dest="verbose", default=False,
                                 help="report narrative to stderr")

        self.__opts, self.__args = self.__parser.parse_args()


    # ----------------------------------------------------------------------------------------------------------------

    def is_valid(self):
        if self.delta is None or self.cut_off is None:
            return False

        return True


    # ----------------------------------------------------------------------------------------------------------------

    @property
    def path(self):
        return self.__args[0] if len(self.__args) > 0 else None


    @property
    def delta(self):
        return self.__opts.delta


    @property
    def cut_off(self):
        return self.__opts.cut_off


    @property
    def verbose(self):
        return self.__opts.verbose


    @property
    def args(self):
        return self.__args


    # ----------------------------------------------------------------------------------------------------------------

    def print_help(self, file):
        self.__parser.print_help(file)


    def __str__(self, *args, **kwargs):
        return "CmdLowPassFilter:{path:%s, delta:%s, cut_off:%s, verbose:%s, args:%s}" % \
               (self.path, self.delta, self.cut_off, self.verbose, self.args)
