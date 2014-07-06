#!/usr/bin/env python
# encoding: utf-8
"""
Generator for CANFAR submission templates.
"""

import os

from jinja2 import Environment, PackageLoader


class Submission(object):
    """Represents a submission file."""
    def __init__(self, vmname, script_path, user="jonathansick",
                 memory=2048, cpus=1, getenv=False,
                 vmmem=None, vmstorage=25):
        super(Submission, self).__init__()
        self._env = Environment(loader=PackageLoader('canque', 'templates'))
        self._args = {'vmname': vmname,
                      'script_path': script_path,
                      'user': user,
                      'memory': str(memory),
                      'cpus': str(cpus),
                      'getenv': str(getenv),
                      'jobs': []}
        if vmmem is None:
            # Boost requested memory to get around CANFAR issue
            self._args['vmmem'] = str(int(1.76 * int(memory)))
        else:
            self._args['vmmem'] = str(memory)
        self._args['vmstorage'] = str(vmstorage)

    def add_job(self, argstr, logpath, outpath=None, errpath=None):
        """Add a job to the submission queue."""
        if outpath is None:
            outpath = ".".join((os.path.splitext(logpath)[0], "out"))
        if errpath is None:
            errpath = outpath
        self._args['jobs'].append({"args": argstr,
                                   "logpath": logpath,
                                   "outpath": outpath,
                                   "errpath": errpath})

    def write(self, path):
        template = self._env.get_template('sub_template.txt')
        txt = template.render(**self._args)
        print(txt)
        with open(path, 'w') as f:
            f.write(txt)
        print("Wrote {0}".format(path))
