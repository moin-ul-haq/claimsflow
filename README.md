# ClaimsFlow

A comprehensive Django REST Framework-based medical claims management system designed to streamline healthcare billing operations across organizations, practices, patients, claims, and payments.

## 📋 Overview

ClaimsFlow is a multi-tenant healthcare claims management system that enables healthcare organizations to manage their practices, procedures, patients, medical claims, and payment processing. The system implements role-based access control with three distinct user levels: SuperAdmin, Organization Admin, and Practice Admin.

## ✨ Features

- **Multi-tenant Architecture**: Support for multiple organizations and their associated practices
- **Role-Based Access Control**: Three permission levels (SuperAdmin, OrgAdmin, PracAdmin)
- **Patient Management**: Comprehensive patient record management
- **Claims Processing**: Create and track medical claims with multiple procedures
- **Payment Processing**: Automated payment generation and tracking linked to claims
- **Automatic Calculations**: Auto-calculation of claim totals based on procedures
- **Automatic Status Updates**: Payment status automatically updates claim status
- **RESTful API**: Full CRUD operations on all resources
- **Filtering & Search**: Advanced filtering, searching, and ordering capabilities
- **Authentication**: Session-based and Token-based authentication
- **First Login Security**: Mandatory password change on first login

## 🛠️ Technology Stack

- **Framework**: Django 4.0.10
- **REST API**: Django REST Framework 3.14.0
- **Database**: SQLite (default, easily swappable)
- **Filtering**: django-filter 23.2
- **Authentication**: Django Session Authentication & Token Authentication
- **Python**: 3.x

## 📁 Project Structure

```
claimsflow/
├── claim/              # Claim management app
├── claimsflow/         # Main project settings
├── organization/       # Organization, Practice, and Procedure management
├── patient/            # Patient management
├── payment/            # Payment processing
├── user/               # Custom user model and authentication
├── db.sqlite3          # SQLite database
├── manage.py           # Django management script
└── requirements.txt    # Python dependencies
```

## 🚀 Installation

### Prerequisites

- Python 3.x installed
- pip package manager
- Virtual environment (recommended)

### Setup Instructions

1. **Clone the repository**
   ```bash
   cd claimsflow
   ```

2. **Create and activate a virtual environment**
   
   **Windows:**
   ```powershell
   python -m venv venv
   .\venv\Scripts\Activate.ps1
   ```
   
   **Linux/Mac:**
   ```bash
   python -m venv venv
   source venv/bin/activate
   ```

3. **Install dependencies**
   ```bash
   pip install -r requirements.txt
   ```

4. **Apply database migrations**
   ```bash
   python manage.py migrate
   ```

5. **Create a superuser**
   ```bash
   python manage.py createsuperuser
   ```
   - Enter username, email, and password
   - Set role as 'superadmin' in Django admin after creation

6. **Run the development server**
   ```bash
   python manage.py runserver
   ```

7. **Access the application**
   - API Root: `http://127.0.0.1:8000/api/`
   - Django Admin: `http://127.0.0.1:8000/admin/`
   - API Browser: `http://127.0.0.1:8000/auth/login/`

## 🗄️ Database Schema

### Core Models

**Organization**
- Company or healthcare organization entity
- Has multiple practices

**Practice**
- Physical location or department within an organization
- Associated with procedures and patients

**Procedure**
- Medical procedure with cost
- Belongs to a specific practice

**Patient**
- Patient records with contact information
- Assigned to an organization and practice

**User**
- Custom user model with roles
- Roles: `superadmin`, `orgadmin`, `pracadmin`
- Default password: 'moin' (must be changed on first login)

**Claim**
- Medical claim for a patient
- Contains multiple procedures
- Total amount automatically calculated
- Status: `pending` or `successfull`

**Payment**
- Payment record linked to a claim
- Automatically created/updated when claim procedures change
- Status: `pending` or `completed`

## 🔐 Authentication

### Available Authentication Methods

1. **Session Authentication**: Browser-based login
2. **Token Authentication**: API token-based authentication

### Getting an Authentication Token

**Endpoint:** `POST /api/gettoken/`

**Request:**
```json
{
  "username": "your_username",
  "password": "your_password"
}
```

**Response:**
```json
{
  "token": "your_auth_token_here"
}
```

**Using the Token:**
Add the token to your request headers:
```
Authorization: Token your_auth_token_here
```

### Browser Authentication

Navigate to `http://127.0.0.1:8000/auth/login/` to log in via browser.

## 👥 User Roles & Permissions

### SuperAdmin
- Full access to all resources
- Can manage all organizations, practices, procedures, patients, claims, and payments
- Can create users

### OrgAdmin (Organization Admin)
- Can view and manage their own organization
- Can create practices within their organization
- Can create procedures for their organization's practices
- Can manage patients within their organization

### PracAdmin (Practice Admin)
- Can view and manage their own practice
- Can create procedures for their practice
- Can manage patients in their practice
- Can manage claims for their practice

## 📡 API Endpoints

All endpoints are prefixed with `/api/`

### Organizations
- `GET /api/organization/` - List organizations
- `POST /api/organization/` - Create organization (SuperAdmin only)
- `GET /api/organization/{id}/` - Retrieve organization
- `PUT /api/organization/{id}/` - Update organization
- `DELETE /api/organization/{id}/` - Delete organization

### Practices
- `GET /api/practice/` - List practices
- `POST /api/practice/` - Create practice
- `GET /api/practice/{id}/` - Retrieve practice
- `PUT /api/practice/{id}/` - Update practice
- `DELETE /api/practice/{id}/` - Delete practice

**Filters:** `organization`, `location`  
**Search:** `name`, `location`, `organization__name`  
**Ordering:** `created_at`, `name`, `location`

### Procedures
- `GET /api/procedure/` - List procedures
- `POST /api/procedure/` - Create procedure
- `GET /api/procedure/{id}/` - Retrieve procedure
- `PUT /api/procedure/{id}/` - Update procedure
- `DELETE /api/procedure/{id}/` - Delete procedure

**Filters:** `cost`, `practice`  
**Search:** `name`, `practice__name`  
**Ordering:** `created_at`, `name`, `cost`

### Patients
- `GET /api/patient/` - List patients
- `POST /api/patient/` - Create patient
- `GET /api/patient/{id}/` - Retrieve patient
- `PUT /api/patient/{id}/` - Update patient
- `DELETE /api/patient/{id}/` - Delete patient

**Filters:** `organization`, `practice`  
**Search:** `name`, `organization__name`, `practice__name`, `email`  
**Ordering:** `name`, `created_at`, `age`

### Claims
- `GET /api/claim/` - List claims
- `POST /api/claim/` - Create claim
- `GET /api/claim/{id}/` - Retrieve claim
- `PUT /api/claim/{id}/` - Update claim
- `DELETE /api/claim/{id}/` - Delete claim

**Filters:** `practice`, `status`, `patient`  
**Search:** `practice`, `status`  
**Ordering:** `status`, `created_at`, `total_amount`

### Payments
- `GET /api/payment/` - List payments
- `POST /api/payment/` - Create payment
- `GET /api/payment/{id}/` - Retrieve payment
- `PUT /api/payment/{id}/` - Update payment
- `DELETE /api/payment/{id}/` - Delete payment

**Filters:** `status`

### Users
- `GET /api/user/` - List users (SuperAdmin only)
- `POST /api/user/` - Create user (SuperAdmin only)
- `GET /api/user/{id}/` - Retrieve user
- `PUT /api/user/{id}/` - Update user
- `DELETE /api/user/{id}/` - Delete user

### Authentication
- `POST /api/gettoken/` - Obtain authentication token
- `POST /api/changepassword/` - Change password
- `GET /auth/login/` - Browser login
- `GET /auth/logout/` - Browser logout

## 📖 Usage Examples

### Using Browser (Session Authentication)

1. **Login**
   - Navigate to `http://127.0.0.1:8000/auth/login/`
   - Enter credentials (default password for new users: 'moin')
   - First-time users will be redirected to change password

2. **Access API**
   - Navigate to `http://127.0.0.1:8000/api/`
   - Browse and interact with all available endpoints

### Using cURL (Token Authentication)

1. **Get Token**
```bash
curl -X POST http://127.0.0.1:8000/api/gettoken/ \
  -H "Content-Type: application/json" \
  -d '{"username": "admin", "password": "yourpassword"}'
```

2. **Create an Organization** (SuperAdmin only)
```bash
curl -X POST http://127.0.0.1:8000/api/organization/ \
  -H "Authorization: Token your_token_here" \
  -H "Content-Type: application/json" \
  -d '{"name": "City Medical Center"}'
```

3. **Create a Practice**
```bash
curl -X POST http://127.0.0.1:8000/api/practice/ \
  -H "Authorization: Token your_token_here" \
  -H "Content-Type: application/json" \
  -d '{
    "name": "Downtown Clinic",
    "location": "123 Main St",
    "organization": 1
  }'
```

4. **Create a Procedure**
```bash
curl -X POST http://127.0.0.1:8000/api/procedure/ \
  -H "Authorization: Token your_token_here" \
  -H "Content-Type: application/json" \
  -d '{
    "name": "X-Ray Chest",
    "cost": 150,
    "practice": 1
  }'
```

5. **Create a Patient**
```bash
curl -X POST http://127.0.0.1:8000/api/patient/ \
  -H "Authorization: Token your_token_here" \
  -H "Content-Type: application/json" \
  -d '{
    "name": "John Doe",
    "email": "john.doe@example.com",
    "age": 45,
    "phone": "555-0123",
    "address": "456 Oak Ave",
    "organization": 1,
    "practice": 1
  }'
```

6. **Create a Claim**
```bash
curl -X POST http://127.0.0.1:8000/api/claim/ \
  -H "Authorization: Token your_token_here" \
  -H "Content-Type: application/json" \
  -d '{
    "practice": 1,
    "patient": 1,
    "procedures": [1, 2],
    "status": "pending"
  }'
```

7. **List Claims with Filters**
```bash
curl -X GET "http://127.0.0.1:8000/api/claim/?status=pending&ordering=-created_at" \
  -H "Authorization: Token your_token_here"
```

8. **Update Payment Status** (automatically updates claim status)
```bash
curl -X PATCH http://127.0.0.1:8000/api/payment/1/ \
  -H "Authorization: Token your_token_here" \
  -H "Content-Type: application/json" \
  -d '{"status": "completed"}'
```

9. **Search Patients**
```bash
curl -X GET "http://127.0.0.1:8000/api/patient/?search=John" \
  -H "Authorization: Token your_token_here"
```

### Using Python Requests

```python
import requests

# Base URL
BASE_URL = "http://127.0.0.1:8000/api"

# Get token
response = requests.post(f"{BASE_URL}/gettoken/", json={
    "username": "admin",
    "password": "yourpassword"
})
token = response.json()["token"]

# Set headers
headers = {
    "Authorization": f"Token {token}",
    "Content-Type": "application/json"
}

# Create a patient
patient_data = {
    "name": "Jane Smith",
    "email": "jane.smith@example.com",
    "age": 32,
    "phone": "555-0199",
    "organization": 1,
    "practice": 1
}
response = requests.post(f"{BASE_URL}/patient/", json=patient_data, headers=headers)
print(response.json())

# List all claims
response = requests.get(f"{BASE_URL}/claim/", headers=headers)
claims = response.json()
print(claims)

# Search for procedures
response = requests.get(f"{BASE_URL}/procedure/?search=X-Ray", headers=headers)
print(response.json())
```

## 🔄 How It Works

### Claim & Payment Workflow

1. **Create a Claim**
   - A claim is created with a patient and associated procedures
   - The system automatically calculates `total_amount` by summing procedure costs

2. **Automatic Payment Generation**
   - When procedures are added/removed from a claim, a signal triggers
   - A payment record is automatically created or updated with the claim's total amount
   - Payment status is set to 'pending'

3. **Payment Processing**
   - Update the payment status to 'completed'
   - A signal automatically updates the claim status to 'successfull'

4. **Status Synchronization**
   - Claim and payment statuses are kept in sync via Django signals
   - When payment status changes, the related claim status updates accordingly

### Security Features

1. **First Login Middleware**
   - New users are created with default password 'moin'
   - Users are forced to change password on first login
   - Cannot access other endpoints until password is changed

2. **Permission Classes**
   - Custom permission classes enforce role-based access
   - Users can only access resources within their organization/practice scope
   - SuperAdmins have unrestricted access

## 🧪 Testing

Run tests for each app:

```bash
# Test all apps
python manage.py test

# Test specific app
python manage.py test organization
python manage.py test patient
python manage.py test claim
python manage.py test payment
python manage.py test user
```

## 🔧 Configuration

### Key Settings (claimsflow/settings.py)

- **SECRET_KEY**: Change in production
- **DEBUG**: Set to False in production
- **ALLOWED_HOSTS**: Configure for production
- **DATABASES**: Currently using SQLite, can be changed to PostgreSQL/MySQL
- **AUTH_USER_MODEL**: Custom user model 'user.User'

### REST Framework Settings

```python
REST_FRAMEWORK = {
    'DEFAULT_AUTHENTICATION_CLASSES': [
        'rest_framework.authentication.SessionAuthentication'
    ],
    'DEFAULT_PERMISSION_CLASSES': [
        'rest_framework.permissions.IsAuthenticated'
    ],
    'DEFAULT_FILTER_BACKENDS': [
        'django_filters.rest_framework.DjangoFilterBackend',
        'rest_framework.filters.SearchFilter',
        'rest_framework.filters.OrderingFilter'
    ],
}
```

## 📝 Development

### Creating a New SuperAdmin User

```bash
python manage.py createsuperuser
```

Then, access Django admin at `http://127.0.0.1:8000/admin/` and set the user's role to 'superadmin'.

### Database Migrations

After model changes:

```bash
python manage.py makemigrations
python manage.py migrate
```

### Resetting Database

```bash
# Delete db.sqlite3
rm db.sqlite3

# Delete migration files (keep __init__.py)
# Then run
python manage.py makemigrations
python manage.py migrate
python manage.py createsuperuser
```

## 🐛 Common Issues

### Issue: Cannot login
**Solution**: Ensure user has the correct role set in Django admin.

### Issue: Permission denied
**Solution**: Check user role and permissions. Verify the user is associated with the correct organization/practice.

### Issue: Signal not triggering
**Solution**: Ensure the app's `ready()` method in `apps.py` imports signals:
```python
def ready(self):
    import claim.signals
```

### Issue: First login redirect loop
**Solution**: Change password at `/api/changepassword/` endpoint.

## 📄 License

This project is for educational/demonstration purposes.

## 🤝 Contributing

This is a sample project. Feel free to fork and modify as needed.

## 📧 Support

For questions or issues, please check the code documentation or create an issue in the repository.

---

**Happy Coding! 🎉**
