# ✅ Todo Django App

A simple yet functional task‑management application built using **Django**. Users can add tasks, mark them complete, or delete them — ideal for learning Django or as a foundation for a larger project.

---

## 🔧 Features

- 📝 Create tasks with a title and description  
- 📋 View a list of all tasks  
- ✔️ Mark tasks as complete  
- 🗑️ Delete tasks  
- ✅ Lightweight, clean UI using Django templates  
- 🧮 Built with Django’s MVC (MTV) architecture

---

## 📦 Tech Stack

- **Backend**: Django (Python)  
- **Database**: SQLite (default for development)  
- **Frontend**: Django Templates, HTML & CSS  

---

## 🛠️ Setup Instructions

### 1. Prerequisites

This is an example of how to list things you need to use the software and how to install them.
* Create a folder
* Open the folder with the terminal then create the environment using venv
  ```sh
  python -m venv .venv  
  ```
* Take right-click on the folder and open it with git bash then clone the project using the command
  ```sh
  https://github.com/balajishiva2001/todo-django.git
  ```
* Download the IDE like VS Code
* Open the project using the VS Code
* Open the terminal and do the following operations:
  * Change the directory
    ```sh
    cd .\.venv\Scripts\
    ```
  * Invoke the below command to activate the .venv in Windows power shell/ vs code
    ```sh
    .\Activate.ps1
    ```
  * Install the Django
    ```sh
    pip install django
    ``` 
  * Make migrations to create the models
    ```sh
    python Manage.py makemigrations
    python Manage.py migrate
    ```
  * Run the Django app
    ```sh
    pythom Manage.py runserver 
    ```

<p align="right">(<a href="#readme-top">back to top</a>)</p>



