from flask import Flask, request, jsonify
app = Flask(__name__)

@app.route("/run", methods=["POST"])
def run_script():
    return jsonify({"message": "Script exécuté avec succès !"})

if __name__ == "__main__":
    app.run(port=5000, debug=True)
