from flask import Flask, request, jsonify
from flask_cors import CORS
from groq import Groq
import os
from datetime import datetime

app = Flask(__name__)
CORS(app)

client = Groq(api_key=os.environ.get("GROQ_API_KEY"))

SYSTEM_PROMPT = """
Tu Invertis University ke canteen ka helpful chatbot hai.
Tera naam CanteenBot hai.
Hindi aur English dono mein baat kar.
Friendly aur helpful raho, emojis use karo.
Sirf canteen food aur university se related sawaalon ka jawab do.

=== INVERTIS UNIVERSITY CANTEEN MENU ===

--- MAIN COURSE (Rs. 160-180) ---
- Kadhai Paneer - Rs. 180
- Shahi Paneer - Rs. 180
- Paneer Butter Masala - Rs. 180
- Dal Makhani - Rs. 160
- Matar Paneer - Rs. 180
- Paneer Tikka Masala - Rs. 180
- Chaap Masala - Rs. 160
- Paneer Lababdaar - Rs. 180
- Paneer Do Pyaz - Rs. 180
- Matar Mushroom - Rs. 180

--- TANDOORI ---
- Plain Roti - Rs. 15
- Butter Roti - Rs. 20
- Plain Naan - Rs. 25
- Butter Naan - Rs. 30
- Aloo Parantha - Rs. 60
- Paneer Parantha - Rs. 80
- Aloo Kulcha - Rs. 70
- Paneer Tikka - Rs. 170
- Tandoori Chaap - Rs. 100
- Malai Chaap - Rs. 120

--- INDIAN SNACKS ---
- Chole Bhature - Rs. 70
- Chole Chawal - Rs. 65
- Pav Bhaji - Rs. 75

--- CHINESE ---
- Veg Hakka Noodle - Rs. 70
- Veg Fried Rice - Rs. 70
- Manchurian Dry & Gravy - Rs. 75
- Chilli Paneer Dry & Gravy - Rs. 150
- Chilli Potato - Rs. 75
- Honey Chilli Potato - Rs. 75
- Spring Roll - Rs. 75
- Momos Steam/Fries - Rs. 60/65
- Macaroni - Rs. 60

--- SOUTH INDIAN ---
- Masala Dosa - Rs. 80
- Paneer Dosa - Rs. 100

--- CONTINENTAL ---
- French Fries - Rs. 70
- Pasta - Rs. 85
- Veg Cheese Burger - Rs. 60
- Hot Dog - Rs. 50
- Veg Sandwich (2 Layer) - Rs. 35
- Cream Roll/Chocolate - Rs. 25
- Aloo Patty - Rs. 30
- Eggless Pastries (Small) - Rs. 35
- Eggless Cakes (Pineapple/Strawberry/Choco Vanilla/Black Forest) - Rs. 340

--- BEVERAGES ---
- Tea - Rs. 15 | Coffee - Rs. 25
- Cold Coffee - Rs. 40
- Cold Drink 250ml - Rs. 35 | 750ml - Rs. 60
- Cold Drink Can - Rs. 45
- Frooti/Appy/Sting - Rs. 35
- Amul Lassi - Rs. 35
- Amulcool/Amulchach - Rs. 35/25
- Juice - Rs. 30
- Ice Cream - Rs. 40/50/60
- Chocolate - Rs. 25/45/110/195
- Lays - Rs. 30 | Kurkure - Rs. 20
- Water Bottle - Rs. 20

=== IMPORTANT RULES ===
- Outside food allowed nahi hai cafe mein
- Agar koi budget pooche toh saste options pehle batao
- Agar koi spicy pooche toh Chinese ya Chaap suggest karo
- Agar healthy pooche toh Dosa ya Dal Makhani suggest karo
- Hamesha prices sahi batao jo upar diye hain
"""

@app.route("/", methods=["GET"])
def home():
    return jsonify({"status": "Invertis University CanteenBot chal raha hai!"})

@app.route("/api/chat", methods=["POST"])
def chat():
    data = request.get_json()
    if not data or "message" not in data:
        return jsonify({"error": "Message do!"}), 400
    user_message = data["message"].strip()
    if not user_message:
        return jsonify({"error": "Empty!"}), 400
    history = data.get("history", [])
    messages = []
    for msg in history[-10:]:
        messages.append({
            "role": msg["role"],
            "content": msg["content"]
        })
    messages.append({
        "role": "user",
        "content": user_message
    })
    response = client.chat.completions.create(
        model="llama-3.3-70b-versatile",
        messages=[
            {"role": "system", "content": SYSTEM_PROMPT}
        ] + messages,
        max_tokens=500,
        temperature=0.7
    )
    ai_reply = response.choices[0].message.content
    return jsonify({
        "reply": ai_reply,
        "timestamp": datetime.now().isoformat()
    })

if __name__ == "__main__":
    print("====================================")
    print("  Invertis University CanteenBot!")
    print("  URL: http://localhost:5000")
    print("====================================")
    app.run(debug=True, host="0.0.0.0" ,port=5000)