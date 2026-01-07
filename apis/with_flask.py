from flask import Flask, request, jsonify

app = Flask(__name__)

# get
@app.route("/get-user/<user_id>")
def get_user(user_id):
    user_data = {
        "user_id": user_id,
        "name" : "Arsham Hajeb",
        "email" : "arshsm.hajeb@gmail.com"
    }

    extra = request.args.get("extra")
    if extra:
        user_data["extra"] = extra


    return jsonify(user_data), 200

# http://127.0.0.1:5000/get-user/123?extra=%22Hello%22 --> url

#post
@app.route("/create-user", methods=["POST"])
def create_user():
    # if request.method == "POST":
    data = request.get_json()

    return jsonify(data), 201

if __name__ == '__main__':
    app.run(debug=True)