from app.routes.main import main


@main.route("/")
def home():
    return "<h1>Welcome to StockFlow IMS 🚀</h1>"
