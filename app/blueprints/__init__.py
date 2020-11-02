
def init_app(app):
  from .stock_bp import stock_bp

  app.register_blueprint(stock_bp, url_prefix='/api/v1/stock')
