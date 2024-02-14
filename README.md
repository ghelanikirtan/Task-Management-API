# Task Management API:

- **RESTful API for a task management system using Django Rest Framework.**
- **This supports CRUD operations for tasks:**
  1. The user can create a new task.
  2. Retrieve a single task by ID.
  3. List all tasks.
  4. Update an existing task.
  5. Delete a task.

- **Key Features:**
  1. Basic Authentication (as of now, Token Base authentication is in progress).
  2. Permissions for performing CRUD operations.
  3. Unit Tests for API views
---

### Step 1: 
- **Clone this repository and navigate into Task-Management-API directory:** 
```
$ git clone https://github.com/ghelanikirtan/Task-Management-API.git
$ cd Task-Management-API
```

### Step 2: 
- **Install Dependencies (i.e.: Django and Django Rest Framework:** 
```
$ pip install -r requirements.txt
```

### Step 3: (optional)
- **Perform migrations upon any changes:**
```
$ python manage.py makemigrations
$ python manage.py migrate
```

### Step 4: 
- **Create a super user for one-time authentication and admin access** 
```
$ python manage.py createsuperuser
```
```
    Username: username-here \n
    Email address: email-id here 
    Password: password-here 
    Password (again): re-type password
```

### Step 5:
- **Run the Django server 😁**
```
$ python manage.py runserver
```

---
## About RESTful API Endpoints [for local server host]:

**Login using the credentials set above first to access over TMS API: http://127.0.0.1:8000/tasks/ 🖇️**

1. Create Task:                `[POST] /tasks/`
2. List all Tasks:             `[GET] /tasks/`
3. Retrieve single task by id: `[GET] /tasks/id-integer/`
4. Update Existing task:       `[PUT/PATCH] /tasks/id-integer/`
5. Delete Task:                `[DELETE] /id-integer/`
