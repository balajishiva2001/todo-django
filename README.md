📝 Todo Django API

A simple and clean RESTful API for a Todo application built using Django and Django REST Framework.  
It allows you to create, read, update, and delete todo items — ideal for learning Django or as a backend for your todo app.

---

🔧 Features

- ✅ Create todo items with title and description  
- 📖 Retrieve all todo items or a single item by ID  
- ✏️ Update existing todo items  
- 🗑️ Delete todo items  
- 🔐 JWT-based authentication and security  
- 🚀 Built using Django with Django REST Framework  

---

📦 Tech Stack

- Backend: Python 3.9 & Django  
- API Framework: Django REST Framework  
- Database: SQLite (default for development)  
- Security: Simple JWT for authentication  
- Build Tool: pip & virtualenv  

---

🛠️ Setup Instructions

1️⃣ Prerequisites

Before getting started, ensure you have:

- 🐍 Python 3.9 or higher installed  
- 📦 pip installed  
- 🧪 A code editor like VS Code or PyCharm  
- 🔧 Git installed and configured  

---

2️⃣ Clone the Repository

Open your terminal or Git Bash and run:

git clone https://github.com/balajishiva2001/todo-django.git  
cd todo-django

---

3️⃣ Create a Virtual Environment

python -m venv venv  
source venv/bin/activate  # On Windows use `venv\Scripts\activate`

---

4️⃣ Install Dependencies

pip install -r requirements.txt

---

5️⃣ Apply Migrations

python manage.py migrate

---

6️⃣ Run the Application

Start the Django development server:

python manage.py runserver

The app will be running at http://localhost:8000

---

7️⃣ Test the APIs

You can test the API endpoints using tools like Postman or curl.

Basic available endpoints:

Method   Endpoint           Description  
------   ------------------ --------------------------  
POST     /api/auth/login    Authenticate user & get JWT token  
GET      /api/todos         Get all todo items  
GET      /api/todos/{id}    Get todo item by ID  
POST     /api/todos         Create a new todo item  
PUT      /api/todos/{id}    Update existing todo item  
DELETE   /api/todos/{id}    Delete a todo item  

⚠️ Note: All `/api/todos` endpoints require an Authorization header with the JWT token except `/api/auth/login`.

---

📂 Project Structure

todo-django/  
├── todo/  
│   ├── migrations/          # Database migrations  
│   ├── models.py            # Database models  
│   ├── serializers.py       # API serializers  
│   ├── views.py             # API views  
│   ├── urls.py              # API routing  
├── manage.py                # Django project management  
├── requirements.txt         # Python dependencies  
└── README.md                # This documentation  

---

📌 Future Improvements

- ➕ Add user registration and profile management  
- 📄 Add pagination and filtering to todos  
- 🛢️ Switch to a persistent DB like PostgreSQL  
- 📚 Add Swagger UI for API docs  
- 🔒 Enhance security with OAuth2  

---

🤝 Contributing

Contributions welcome! Feel free to fork the repo, create a branch, and submit pull requests.

---

📜 License

This project is licensed under the MIT License. See the LICENSE file for details.

---

🙋 Author

Balaji Shiva  
GitHub: https://github.com/balajishiva2001
