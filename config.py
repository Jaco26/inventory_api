from os import environ

class BaseConfig:
  SQLALCHEMY_DATABASE_URI = environ.get('DATABASE_URL')
  SQLALCHEMY_TRACK_MODIFICATIONS = False


class ConfigDev(BaseConfig):
  pass


class ConfigStage(BaseConfig):
  pass


class ConfigProd(BaseConfig):
  pass