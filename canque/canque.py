#!/usr/bin/env python
# encoding: utf-8
"""
Generator for CANFAR submission templates.
"""

import os

from jinja2 import Environment, PackageLoader


class Submission(object):
    """Represents a submission file."""
    def __init__(self, user, script_path):
        super(Submission, self).__init__()
        self._env = Environment(loader=PackageLoader('canque', 'templates'))
        self._args = {'script_path': script_path,
                      'user': user,
                      'jobs': []}

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
