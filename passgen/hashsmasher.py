from datetime import datetime
import hashlib
from random import randint

class HashSmasher(object):
  def __init__(self, options):
    self.sourcestr = "%s" % datetime.now()
    self.alphamode = options.alphanumeric
    saltstr = "%s" % datetime.now()
    hashstr = "%s%s" % (hashlib.sha256(saltstr).hexdigest(),hashlib.sha256(saltstr).hexdigest())
    self.inputstr = hashstr[:int(options.length)]

    if options.alphanumeric:
      self.replacechars = "ABCDEFGHIJKLMNOPQRSTUVWXYZabcdefghijklmnopqrstuvwxyz0123456789"
    else:
      if options.limited:
        self.replacechars = r"-_+.ABCDEFGHIJKLMNOPQRSTUVWXYZabcdefghijklmnopqrstuvwxyz0123456789"
      else:
        self.replacechars = r" `~!@#$%^&*()_+-=[]{}|\:;,./<>?ABCDEFGHIJKLMNOPQRSTUVWXYZabcdsfghijklmnopqrstuvwxyz"

  @property
  def SmashedHash(self):
    return smashhash(self.inputstr, self.replacechars)


def smashhash(thestr, replacechars):
  smashedhash = ""
  casedeformed = ""
  for eachletter in thestr:
    dosmash = randint(0,1) == 0
    if dosmash:
      eachletter = replacechars[randint(0,len(replacechars)-1)]
    smashedhash = "%s%s" % (eachletter, smashedhash)
  for eachletter in smashedhash:
    dosmash = randint(0,1) == 0
    if dosmash:
      eachletter = eachletter.upper()
    else:
      eachletter = eachletter.lower()
    casedeformed = "%s%s" % (casedeformed, eachletter)

  return casedeformed
