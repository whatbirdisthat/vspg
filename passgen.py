#!/usr/bin/env python
from optparse import OptionParser
from passgen.hashsmasher import HashSmasher
__version__ = "0"

def run():

  usagestr = "usage: %prog [options]"
  parser = OptionParser(usage=usagestr, version="%prog "+__version__,description="""
%prog builds passwords.
"""
)
  parser.add_option("-a", "--alphanumeric", dest="alphanumeric", action="store_true", default=False,
      help="Generator mode. Limits char output to alphanumeric only (0-9A-Za-z). Default = off")
  parser.add_option("-i", "--limited", dest="limited", action="store_true", default=False,
      help="Generator mode. Limits the char output to letters, digits and \"+_-.\". Default = off")
  parser.add_option("-l", "--length", dest="length", type="int", default=16,
      help="Generated pw will be LENGTH characters long. Default is 16.")
  (options, args) = parser.parse_args();

  maxlength = 128
  if options.length > maxlength:
    parser.error("LENGTH maximum %0d chars." % maxlength)

  h = HashSmasher(options)
  print h.SmashedHash
if __name__ == "__main__":
  run()
