canque
======

Helps you (or at least, me) write CANFAR queue submission files.

::

  >>> from canque import Submission
  >>> sub = Submission(user_name, script_path)
  >>> sub.add_job('my args', "job.log")
  >>> sub.write("jobs.sub")

