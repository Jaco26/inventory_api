from flask import request
from voluptuous import Schema, Required, REMOVE_EXTRA

def create_schema(template_dict):
  accum = {}
  for key in template_dict:
    predicate = template_dict[key]
    if type(key) is tuple:
      try:
        field_name, default_value = key
        accum.update({ Required(field_name, default_value): predicate })
      except:
        raise 'template_dict keys of type tuple must contain two items: (<field_name>, <default_value>)'
    elif type(key) is str:
      accum.update({ Required(key, default=None): predicate })
  return Schema(accum, extra=REMOVE_EXTRA)


def should_look_like(schema, source=None):
  '''
  :schema: a [voluptuous](https://github.com/alecthomas/voluptuous) dictionary `Schema`

  :source: A `dict` (or dict-like value) that will be validated against the `schema_func`. If no value is passed, 
  the value returned from `request.get_json()` will be used.
  '''
  if not source:
    source = request.get_json()
  if not source:
    source = {}
  return schema(dict(source))