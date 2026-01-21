# Dynamic University Application Backend

This is backend application built in Django and Django REST Framework.This system allows to define dynamic application form for different universities.The universities can have their own custom application fields (like text,file,date etc.) and applicant can submit applications accordingly.

---

## Tech stack 
* Python
* Django
* Django REST Framework(DRF)
* SQLite

---

## Features
* Admin can manage Universities and application forms
* Add dynamic application fields per universities
* Field type validation 
* File upload handling
* API for fetching university details,application forms and to submit applications

---

## API Endpoints

### 1. List Universities

```
GET /api/universities/
```
Returns a list of all universities.

### 2. View Single University Details

```
GET /api/universities/<university_id>/
```
Returns details like name, location, and description of a university.

### 3. Get Fields of a University

```
GET /api/universities/<university_id>/fields/
```
Returns dynamic application fields configured for the selected university.

### 4. Submit Application

```
POST /api/application/submit/
```

**Request type:** `multipart/form-data`

**Example fields:**

```
university_id=1
field_2=John Doe
field_3=2001-05-10
field_4=Engineering
field_5=<file>
```

---

## How to Test

* Use **Django Admin** to:

  * Create universities
  * Add application fields
* Use **Postman or DRF Browsable API** to:

  * Fetch universities
  * Fetch dynamic fields
  * Submit applications

---

## Postman Collection For Testing

A Postman collection is included in the repository.  

**File:**
`postman/University Form.postman_collection.json`  

You can import this file into Postman to test API's locally

---

## Working Demo
Screenshots of demonstrating the working of API in Postman and Frontend is added in `screenshots/` in the repository. 

---

## Design Decisions

* Dynamic fields are stored separately to allow flexibility
* University metadata is separated from application data
* File uploads are handled using multipart requests
* Admin panel is used instead of APIs for managing universities

---
## 👤 Author

**Devaswin K.S**  
Diploma in Computer Engineering  
Python Backend Developer

---

## 📄 License

This project is created for evaluation and learning purposes.


