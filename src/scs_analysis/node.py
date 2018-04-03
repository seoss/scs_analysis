#!/usr/bin/env python3

"""
Created on 11 Apr 2017

@author: Bruno Beloff (bruno.beloff@southcoastscience.com)

SYNOPSIS
node.py [-i] [-v] [PATH]

DESCRIPTION
The node utility is used to extract a node from within a JSON document. Data is presented as a sequence of documents on
stdin, and the extracted node is passed to stdout. The extracted node may be a leaf node or an internal node. If no
node path is specified, the whole input document is passed to stdout.

The node utility may be set to either ignore documents that do not contain the specified node, or to terminate when the
node is not present.

EXAMPLES
./socket_receiver.py | ./node.py -i val.afe.sns.CO
"""

import sys

from scs_analysis.cmd.cmd_node import CmdNode

from scs_core.data.json import JSONify
from scs_core.data.path_dict import PathDict


# --------------------------------------------------------------------------------------------------------------------

if __name__ == '__main__':

    # ----------------------------------------------------------------------------------------------------------------
    # cmd...

    cmd = CmdNode()

    if cmd.verbose:
        print(cmd, file=sys.stderr)
        sys.stderr.flush()


    try:
        # ------------------------------------------------------------------------------------------------------------
        # run...

        for line in sys.stdin:
            datum = PathDict.construct_from_jstr(line)

            if datum is None:
                continue

            if cmd.ignore and not datum.has_path(cmd.path):
                continue

            node = datum.node(cmd.path)

            print(JSONify.dumps(node))
            sys.stdout.flush()


    # ----------------------------------------------------------------------------------------------------------------
    # end...

    except KeyboardInterrupt:
        if cmd.verbose:
            print("node: KeyboardInterrupt", file=sys.stderr)
