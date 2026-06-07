@app.route('/submittodoitem', methods=['POST'])
def submit_todo():
    data = request.json

    todo = {
        "itemName": data["itemName"],
        "itemDescription": data["itemDescription"]
    }

    collection.insert_one(todo)

    return {"message": "Saved"}, 201