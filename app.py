from flask import Flask, request, jsonify, render_template_string

app = Flask(__name__)

stored_message = "Hello ❤️"

# Page to update the stored message
@app.route("/", methods=["GET", "POST"])
def index():
    global stored_message

    if request.method == "POST":
        stored_message = request.form["message"]
    
    return render_template_string(PAGE, message=stored_message)

# Endpoint for ESP32 to get the latest message
@app.route("/getMessage", methods=["GET"])
def get_message():
    return jsonify({"message": stored_message})

# HTML page (simple)
PAGE = """
<html>
<body style="font-family:Arial; text-align:center; padding-top:30px;">
  <h2>Send Message to ESP32 Display</h2>

  <form method="POST">
    <input name="message" style="width:300px; font-size:20px;" />
    <br><br>
    <button style="font-size:20px;" type="submit">Send</button>
  </form>

  <p style="margin-top:20px;">Current Message: <b>{{ message }}</b></p>
</body>
</html>
"""

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=10000)
