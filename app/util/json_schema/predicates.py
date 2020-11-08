import uuid

def bool_from_str(val):
  if type(val) is str:
    val = val.strip().lower()
    return len(val) == 0 or val == 'true' or val == 't' or val == '1'
  return False

def coerce(pytype, default_value=None):
  return lambda val: val if val is None else pytype(val)

def is_uuid(val):
  if val:
    return uuid.UUID(val)
  return None
