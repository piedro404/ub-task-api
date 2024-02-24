from src.main.server.server import app

vercel_app = app

if __name__ == '__main__':
    vercel_app.run(host='0.0.0.0', port=3000, debug=True)
