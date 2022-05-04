#-----------------------------------------------
import datetime
import pytz
import dateutil.parser
#-----------------------------------------------

utc = pytz.utc
BERLIN = pytz.timezone('Asia/Bangkok')
#-----------------------------------------------

def to_iso8601(when=None, tz=BERLIN):
  if not when:
    when = datetime.datetime.now(tz)
  if not when.tzinfo:
    when = tz.localize(when)
  _when = when.strftime("%Y-%m-%dT%H:%M:%S.%f%z")
  return _when[:-8] + _when[-5:] # Remove microseconds
#-----------------------------------------------

def from_iso8601(when=None, tz=BERLIN):
  _when = dateutil.parser.parse(when)
  if not _when.tzinfo:
    _when = tz.localize(_when)
  return _when
#-----------------------------------------------

test = from_iso8601("2022-02-04T17:13:02.748Z",BERLIN)
print(test)