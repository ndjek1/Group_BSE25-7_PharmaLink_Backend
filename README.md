# Pharmacy Price & Availability Checker API

This is the backend API for the **Pharmacy Price & Availability Checker** project.  
It is built with **Django + Django REST Framework** and provides REST APIs for a React frontend.  

The system allows patients to:  
- Search for medicines  
- Compare prices  
- Check real-time stock availability across pharmacies in **Uganda**  

---

## 🚀 Features
- User management (**Patients, Pharmacists, Admins**)  
- Manage pharmacies and medicines  
- Price & availability checking  
- RESTful API endpoints for frontend consumption  

---

## 🛠️ Tech Stack
- **Backend:** Django, Django REST Framework  
- **Database:** PostgreSQL (production) / SQLite (development)  
- **Frontend:** React (consumes this API)  

---

## 📖 API Documentation

This section provides instructions for frontend developers on how to interact with the Pharmacy API.

### Base URL
All endpoints are relative to the base URL:

Live Server: https://your-app-name.onrender.com

pgsql
Copy code
> Replace `your-app-name` with the actual app name from your Render dashboard.

---

### 🔑 Authentication
The API uses **JWT (JSON Web Tokens)** for authentication.  

1. A user registers for an account.  
2. The user logs in and receives an **access token**.  
3. The access token is included in the `Authorization` header for protected requests.  

**Header format:**
Authorization: Bearer <your_access_token>

yaml
Copy code

---

### 👤 Authentication Workflow

#### A. Register a New User
- **Endpoint:** `POST /api/users/register/`  
- **Authentication:** None  

**Request Body:**
```json
{
  "username": "new_react_user",
  "password": "a-strong-password123"
}
```
Success Response (201 Created):

```json
{
  "id": 5,
  "username": "new_react_user",
  "email": ""
}
```
Error Response (400 Bad Request):

```json
{
  "username": ["A user with that username already exists."]
}
```
B. Log In to Get a Token
Endpoint: POST /api/token/

Authentication: None

Request Body:

```json
{
  "username": "new_react_user",
  "password": "a-strong-password123"
}
```
Success Response (200 OK):

```json
{
  "access": "eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9...",
  "refresh": "eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9..."
}
```
Error Response (401 Unauthorized):

```json
{
  "detail": "No active account found with the given credentials"
}
```
📦 Main Features
A. Get a List of Pharmacies
Endpoint: GET /api/pharmacies/

Authentication: None

Success Response (200 OK):

```json
[
  { "id": 1, "name": "City Health Pharmacy", "address": "123 Main St" },
  { "id": 2, "name": "Render Live Pharmacy", "address": "123 Cloud Way" }
]
```
B. Create a New Medicine
Endpoint: POST /api/medicines/

Authentication: Required (Bearer token)

Headers:

Content-Type: application/json
Authorization: Bearer <your_access_token>
Request Body:

```json
{
  "name": "Ibuprofen 200mg",
  "description": "Relieves pain and reduces inflammation.",
  "price": "9.99",
  "pharmacy": 1
}
```
Success Response (201 Created):

```json
{
  "id": 12,
  "name": "Ibuprofen 200mg",
  "description": "Relieves pain and reduces inflammation.",
  "price": "9.99",
  "pharmacy": 1,
  "owner": "new_react_user"
}
```
Error Responses:

401 Unauthorized: Missing or invalid/expired token.

400 Bad Request: Invalid data (e.g., missing required field, pharmacy ID does not exist).
