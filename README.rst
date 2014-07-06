canque
======

Helps you (or at least, me) write CANFAR queue submission files.

::

  >>> from canque import Submission
  >>> sub = Submission(vm_name, script_path, user='jonathansick', memory=2048, cpus=1)
  >>> sub.add_job('my args', "job.log")
  >>> sub.write("jobs.sub")

