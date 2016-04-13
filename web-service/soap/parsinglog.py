from ladon.ladonizer import ladonize
from ladon.compat import PORTABLE_STRING

class ParsingLog(object):
  """
  This service does the math, and serves as example for new potential Ladon users.
  """
  @ladonize(rtype=PORTABLE_STRING)
  def add(self):
    """
    Add two integers together and return the result

    @param a: 1st integer
    @param b: 2nd integer
    @rtype: The result of the addition
    """
    a = []
    a = ["cek1","cek2"]
    return a

