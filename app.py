from flask import Flask, request, jsonify, json



app = Flask(__name__)

@app.route("/")
def index():
    return "Incident Tracker API"


# read
@app.route("/incidents")
def get_incidents():
    with open("incidents.json", "r", encoding="utf-8") as f:
        existing = json.load(f)
    return existing

# create
@app.route("/incidents", methods=["POST"])
def add_incident():
    data = request.json
    
    with open("incidents.json", "r", encoding="utf-8") as f:
        existing = json.load(f)
    
    data["id"] = len(existing) + 1
    data["status"] = "open"
    existing.append(data)
    
    with open("incidents.json", "w", encoding="utf-8") as f:
        json.dump(existing, f, ensure_ascii=False, indent=2)
    
    return jsonify(data)

# delete 
@app.route("/incidents/<int:id>", methods=["DELETE"])
def delete_incident(id):
    with open("incidents.json", "r", encoding="utf-8") as f:
        existing = json.load(f)
    
    existing = [h for h in existing if h["id"] != id]
    
    with open("incidents.json", "w", encoding="utf-8") as f:
        json.dump(existing, f, ensure_ascii=False, indent=2)
    
    return jsonify({"message": "deleted"})

#   update
@app.route("/incidents/<int:id>", methods=["PUT"])
def update_incident(id):
    data = request.json
    
    with open("incidents.json", "r", encoding="utf-8") as f:
        existing = json.load(f)
    
    for hata in existing:
        if hata["id"] == id:
            hata.update(data)
    
    with open("incidents.json", "w", encoding="utf-8") as f:
        json.dump(existing, f, ensure_ascii=False, indent=2)
    
    return jsonify({"message": "updated"})


if __name__ == "__main__":
    app.run(debug=True)