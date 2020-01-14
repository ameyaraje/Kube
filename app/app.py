from flask import Flask, render_template
# from healthcheck import HealthCheck, EnvironmentDump


app = Flask(__name__)

@app.route('/', methods = ['GET'])
def index():
    return "Sample app in flask"

@app.route('/test', methods = ['GET'])
def test():
    return render_template('test.html')

@app.route('/healthz', methods = ['GET'])
def healthcheck():
    return "Healthy"

if __name__ == "__main__":
    app.run(host='0.0.0.0', port=9000)