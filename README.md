**💸 Finance Tracker**

Welcome to Finance Tracker, the ultimate budgeting sidekick. Built on Django, this app helps you stay on top of your money game. Track your income, expenses, and savings while getting dope insights into your financial health.


**⚡ Features**
* 🔑 Secure user authentication (custom user model)
* 💰 Track income & expenses like a boss
* 📂 Categorize transactions for clarity
* 📊 Dashboard with spicy charts & insights
* 📜 Export reports (CSV/Excel) for receipts
* 🔄 Offline mode that auto-syncs when online


**🛠 Tech Stack**
* Backend: Django, Django REST Framework
* Database: PostgreSQL (hosted on ElephantSQL)
* Hosting: Render (for backend deployment)


**🚀 Getting Started**
Prerequisites
Make sure you have these installed:
* Python 3.10+
* PostgreSQL
* Git


Setup Instructions
1. Clone the repo:
git clone <your-repo-url>
cd FinanceTracker

2. Create & activate a virtual environment:
python -m venv venv
source venv/bin/activate  # On Windows use: venv\Scripts\activate

3. Install dependencies:
pip install -r requirements.txt

4. Set up environment variables:
Create a .env file and add:

  SECRET_KEY=your_secret_key
  DEBUG=True
  DATABASE_URL=your_postgresql_connection_string

5. Apply migrations & start the server:
  python manage.py migrate
  python manage.py runserver

6. Open in your browser:
  http://127.0.0.1:8000/


**🌎 Deployment**
To deploy on Render:
* Push your code to GitHub.
* Connect your repo to Render.
* Set environment variables in Render settings.
* Deploy & enjoy.


**🙌 Contributing**
1. Fork the repo.

2. Create a new branch:
  git checkout -b feature-branch

3. Make changes & commit:
  git commit -m "🔥 Added a cool feature"

4. Push the changes:
  git push origin feature-branch

5. Open a Pull Request.


**📜 License
**
Open-source & MIT Licensed. Feel free to build on it. 🚀


**💬 Questions?**

Open an issue or hit me up. Let's build something awesome! 🤙
