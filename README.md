# 🤖 NeuralBot — Khud Ka AI Model

Ek **100% custom AI chatbot** jo:
- **Koi API nahi** (OpenAI, Anthropic — kuch nahi)
- **Koi PyTorch/TensorFlow nahi**
- **Sirf NumPy + Math** se banaya Neural Network!

---

## 🧠 AI Model kaise kaam karta hai?

```
User Input
    ↓
Tokenize (words mein todna)
    ↓
Bag of Words (binary vector)
    ↓
Neural Network Forward Pass:
  Input Layer  →  128 neurons (ReLU)
              →   64 neurons  (ReLU)
              →  N intents    (Softmax)
    ↓
Highest Probability Intent
    ↓
Random Response from that Intent
```

**Training:**  Backpropagation + Gradient Descent (pure NumPy!)

---

## 📁 Files

```
my-ai/
├── backend/
│   ├── model.py       ← Neural Network class (from scratch!)
│   ├── train.py       ← Training script
│   ├── app.py         ← Flask API server
│   ├── intents.json   ← Training data
│   └── requirements.txt
└── frontend/
    └── index.html     ← React UI
```

---

## 🚀 Setup

```bash
cd backend
pip install -r requirements.txt

# Step 1: Model train karo
python train.py

# Step 2: Server start karo
python app.py

# Step 3: frontend/index.html browser mein kholo
```

---

## 🎓 Naya Intent Add Karna

`intents.json` mein add karo:

```json
{
  "tag": "cricket",
  "patterns": [
    "cricket", "ipl", "virat kohli", "match kab hai"
  ],
  "responses": [
    "Cricket India ka passion hai! 🏏",
    "IPL best tournament hai!"
  ]
}
```

Phir dobara train karo: `python train.py`

---

## 🔗 API Endpoints

| Endpoint | Kya karta hai |
|----------|---------------|
| `GET /` | Server health check |
| `POST /api/chat` | AI se baat karo |
| `GET /api/model-info` | Neural network info |
| `GET /api/intents` | Saare intents |

---

Made with ❤️ using Pure Python + NumPy — **No AI API!**
