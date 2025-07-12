# 💰 Expense Tracker App

A web-based Expense Tracker application that helps users manage and monitor their income and expenses in an organized way.

## 🚀 Features

- Add, edit, and delete income or expense entries
- View total balance, income, and expense summary
- Filter transactions by type (income/expense)
- Persistent storage using MongoDB
- Simple and clean UI with Streamlit
- Export data as CSV (optional)



Expense Tracker 
<img width="1253" height="864" alt="Screenshot 2025-07-12 165608" src="https://github.com/user-attachments/assets/92c78bbc-dc26-4778-a869-8f466f714a80" />
<img width="1076" height="881" alt="Screenshot 2025-07-12 165628" src="https://github.com/user-attachments/assets/b1e3d7c9-d3f8-4d97-81b7-3cb3b7b51b70" />

## 🛠️ Tech Stack

- **Frontend**: Streamlit (Python-based web UI)
- **Backend**: FastAPI (or plain Python if no API used)
- **Database**: MongoDB (via `pymongo` or `motor`)
- **Language**: Python 3

## 📦 Installation

1. **Clone the repository**

```bash

git clone https://github.com/anas-fareedi/Expense_tracker.git
cd Expense_tracker
Create a virtual environment

bash
Copy
Edit
python -m venv my-env
source my-env/Scripts/activate   # For Windows
# or
source my-env/bin/activate       # For Linux/macOS
Install dependencies

bash
Copy
Edit
pip install -r requirements.txt
Run the app

bash
Copy
Edit
streamlit run app.py
Make sure MongoDB is running and your connection string is correctly set in your code.

🧾 Folder Structure
pgsql
Copy
Edit
Expense_tracker/
├── app.py
├── database.py
├── models.py
├── utils.py
├── requirements.txt
└── README.md
🔒 Environment Variables
If you're using a .env file for MongoDB credentials:

env
Copy
Edit
MONGO_URI=mongodb+srv://username:password@cluster.mongodb.net/expense_db
Load it using python-dotenv or in code directly.

📤 Export Feature (Optional)
You can allow users to download their transaction data using:

python
Copy
Edit
st.download_button("Download CSV", data=csv, file_name="transactions.csv")
🧑‍💻 Author
Anas Fareedi

📄 License
This project is licensed under the MIT License.

