# 🛒 Amazon Backend — E-Commerce REST API

A production-oriented **Amazon-style e-commerce backend** built with **Python and FastAPI**, designed around modular REST APIs for authentication, product management, shopping carts, orders, and payment processing.

The project demonstrates backend engineering principles including **RESTful API design, authentication and authorization, database persistence, request validation, modular architecture, API documentation, containerization, and deployment readiness**.

---

## 📌 Table of Contents

* [Overview](#-overview)
* [Objectives](#-objectives)
* [Key Features](#-key-features)
* [Technology Stack](#-technology-stack)
* [System Architecture](#-system-architecture)
* [Request Flow](#-request-flow)
* [Project Structure](#-project-structure)
* [Core Modules](#-core-modules)
* [Authentication & Authorization](#-authentication--authorization)
* [Database Architecture](#-database-architecture)
* [API Architecture](#-api-architecture)
* [API Documentation](#-api-documentation)
* [Installation](#-installation)
* [Configuration](#-configuration)
* [Running Locally](#-running-locally)
* [Running with Docker](#-running-with-docker)
* [Testing](#-testing)
* [Security Considerations](#-security-considerations)
* [Error Handling](#-error-handling)
* [Deployment Architecture](#-deployment-architecture)
* [DevOps Workflow](#-devops-workflow)
* [Future Enhancements](#-future-enhancements)
* [Learning Outcomes](#-learning-outcomes)
* [Author](#-author)

---

# 📖 Overview

This project implements the backend architecture of an **Amazon-style online shopping platform**.

Instead of building a traditional monolithic webpage, the application exposes a set of RESTful APIs that can be consumed by a web frontend, mobile application, or other services.

The backend handles the complete shopping workflow:

```text
User
  │
  ▼
Authentication
  │
  ▼
Browse Products
  │
  ▼
Add Products to Cart
  │
  ▼
Create Order
  │
  ▼
Payment Processing
  │
  ▼
Order Confirmation
```

The application is designed with separation of concerns between API routing, business logic, authentication, data validation, and database persistence.

---

# 🎯 Objectives

The primary objectives of the project are:

* Build a scalable REST API using FastAPI.
* Implement secure user authentication.
* Implement JWT-based authorization.
* Provide product management APIs.
* Implement shopping cart functionality.
* Implement order management.
* Implement payment workflow.
* Persist application data using a relational database.
* Provide automatic API documentation.
* Containerize the application using Docker.
* Follow modular backend architecture.
* Create a foundation suitable for cloud deployment.

---

# ✨ Key Features

## 👤 User Management

* User registration
* User authentication
* Password-based login
* JWT token generation
* Protected API endpoints
* Role-based access concepts

## 📦 Product Management

* Product creation
* Product retrieval
* Product updates
* Product deletion
* Product information management

## 🛒 Shopping Cart

* Add products to cart
* View cart
* Update cart items
* Remove products
* Calculate cart totals

## 📋 Order Management

* Create orders
* Retrieve orders
* Track order information
* Associate orders with authenticated users
* Maintain order data in the database

## 💳 Payment Flow

The application contains a payment workflow integrated into the order lifecycle.

```text
Cart
 │
 ▼
Order Creation
 │
 ▼
Payment
 │
 ▼
Payment Status
 │
 ▼
Order Confirmation
```

> Payment processing in this project represents a backend payment workflow. Production systems should integrate a certified payment provider rather than handling raw card information directly.

## 📚 API Documentation

FastAPI automatically generates interactive API documentation.

Available documentation typically includes:

```text
/swagger
/redoc
```

The exact paths depend on the application's FastAPI configuration.

---

# 🧰 Technology Stack

| Layer                | Technology |
| -------------------- | ---------- |
| Programming Language | Python     |
| API Framework        | FastAPI    |
| API Server           | Uvicorn    |
| ORM                  | SQLAlchemy |
| Database             | SQLite     |
| Authentication       | JWT        |
| Validation           | Pydantic   |
| API Style            | REST       |
| Containerization     | Docker     |
| Version Control      | Git        |
| Repository           | GitHub     |

---

# 🏗️ System Architecture

The application follows a modular layered backend architecture.

```text
                    ┌──────────────────────┐
                    │       CLIENT         │
                    │ Web / Mobile / API   │
                    └──────────┬───────────┘
                               │
                               │ HTTP / HTTPS
                               ▼
                    ┌──────────────────────┐
                    │      FASTAPI         │
                    │    API Layer         │
                    └──────────┬───────────┘
                               │
                 ┌─────────────┼─────────────┐
                 │             │             │
                 ▼             ▼             ▼
          ┌────────────┐ ┌────────────┐ ┌────────────┐
          │   Auth     │ │  Products  │ │    Cart    │
          │   Module   │ │   Module   │ │   Module   │
          └──────┬─────┘ └──────┬─────┘ └──────┬─────┘
                 │              │              │
                 └──────────────┼──────────────┘
                                ▼
                     ┌────────────────────┐
                     │  Business Logic    │
                     │ / Service Layer    │
                     └──────────┬─────────┘
                                │
                                ▼
                     ┌────────────────────┐
                     │    SQLAlchemy      │
                     │       ORM          │
                     └──────────┬─────────┘
                                │
                                ▼
                     ┌────────────────────┐
                     │      SQLite        │
                     │     Database       │
                     └────────────────────┘
```

---

# 🔄 Request Flow

A typical authenticated request follows this lifecycle:

```text
Client
  │
  │ HTTP Request
  ▼
FastAPI Router
  │
  ▼
Request Validation
  │
  ▼
Authentication / JWT
  │
  ▼
Business Logic
  │
  ▼
SQLAlchemy ORM
  │
  ▼
Database
  │
  ▼
Response Model
  │
  ▼
JSON Response
```

This approach separates request handling from persistence and makes the application easier to maintain and extend.

---

# 📁 Project Structure

A recommended structure for the backend is:

```text
Amazon_backend/
│
├── app/
│   ├── __init__.py
│   ├── main.py
│   │
│   ├── models/
│   │   ├── __init__.py
│   │   ├── user.py
│   │   ├── product.py
│   │   ├── cart.py
│   │   ├── order.py
│   │   └── payment.py
│   │
│   ├── schemas/
│   │   ├── user.py
│   │   ├── product.py
│   │   ├── cart.py
│   │   ├── order.py
│   │   └── payment.py
│   │
│   ├── routers/
│   │   ├── auth.py
│   │   ├── products.py
│   │   ├── cart.py
│   │   ├── orders.py
│   │   └── payments.py
│   │
│   ├── services/
│   │   ├── auth_service.py
│   │   ├── product_service.py
│   │   ├── cart_service.py
│   │   ├── order_service.py
│   │   └── payment_service.py
│   │
│   ├── database/
│   │   ├── database.py
│   │   └── dependencies.py
│   │
│   └── core/
│       ├── security.py
│       └── config.py
│
├── tests/
│
├── requirements.txt
├── Dockerfile
├── docker-compose.yml
├── seed_admin.py
├── .env
├── .gitignore
└── README.md
```

> The exact structure should be adjusted to match the actual source code in the repository.

---

# 🧩 Core Modules

## 1. Authentication Module

Responsible for:

```text
Registration
    ↓
Password Validation
    ↓
Login
    ↓
JWT Generation
    ↓
Authenticated Requests
```

The JWT token is sent with subsequent protected requests.

Example:

```http
Authorization: Bearer <access_token>
```

---

## 2. Product Module

Responsible for product-related operations.

Typical operations:

```text
CREATE  → Add Product
GET     → Retrieve Products
GET /id → Retrieve Product
PUT     → Update Product
DELETE  → Delete Product
```

---

## 3. Cart Module

The cart associates users with products.

```text
User
 │
 └── Cart
      │
      ├── Product A
      ├── Product B
      └── Product C
```

The backend calculates quantities and cart totals before order creation.

---

## 4. Order Module

The order module converts a user's shopping cart into an order.

```text
Shopping Cart
     │
     ▼
Order Creation
     │
     ├── User
     ├── Products
     ├── Quantity
     ├── Total
     └── Status
```

---

## 5. Payment Module

The payment module manages payment-related state associated with an order.

Example lifecycle:

```text
PENDING
   │
   ▼
PROCESSING
   │
   ├──────────────┐
   ▼              ▼
SUCCESS        FAILED
   │
   ▼
ORDER CONFIRMED
```

---

# 🔐 Authentication & Authorization

Authentication is implemented using token-based authentication.

```text
                 ┌───────────────┐
                 │     Login     │
                 └───────┬───────┘
                         │
                         ▼
                 ┌───────────────┐
                 │ Verify User   │
                 └───────┬───────┘
                         │
                         ▼
                 ┌───────────────┐
                 │ Generate JWT  │
                 └───────┬───────┘
                         │
                         ▼
                 ┌───────────────┐
                 │ Client Stores │
                 │     Token     │
                 └───────┬───────┘
                         │
                         ▼
                 Protected API
```

Protected resources validate the JWT before processing the request.

---

# 🗄️ Database Architecture

The application uses a relational database accessed through SQLAlchemy.

A conceptual database model is:

```text
┌──────────────┐
│    USERS     │
├──────────────┤
│ id           │
│ name         │
│ email        │
│ password     │
└──────┬───────┘
       │
       │ 1:N
       ▼
┌──────────────┐
│    ORDERS    │
├──────────────┤
│ id           │
│ user_id      │
│ total        │
│ status       │
└──────┬───────┘
       │
       │ 1:N
       ▼
┌────────────────┐
│ ORDER_ITEMS    │
├────────────────┤
│ id             │
│ order_id       │
│ product_id     │
│ quantity       │
└───────┬────────┘
        │
        │ N:1
        ▼
┌──────────────┐
│   PRODUCTS   │
├──────────────┤
│ id           │
│ name         │
│ description  │
│ price        │
│ stock        │
└──────────────┘
```

The exact entity relationships should be synchronized with the implementation.

---

# 🌐 API Architecture

The backend follows REST principles.

Typical endpoint groups include:

| Module         | Method | Purpose           |
| -------------- | ------ | ----------------- |
| Authentication | POST   | Register/Login    |
| Products       | GET    | Retrieve products |
| Products       | POST   | Create product    |
| Products       | PUT    | Update product    |
| Products       | DELETE | Delete product    |
| Cart           | GET    | View cart         |
| Cart           | POST   | Add item          |
| Cart           | PUT    | Update item       |
| Cart           | DELETE | Remove item       |
| Orders         | POST   | Create order      |
| Orders         | GET    | Retrieve orders   |
| Payments       | POST   | Process payment   |

The exact endpoint paths should be taken from the actual application routes.

---

# 📚 API Documentation

After starting the application, FastAPI provides interactive documentation.

### Swagger UI

```text
http://127.0.0.1:8000/docs
```

### ReDoc

```text
http://127.0.0.1:8000/redoc
```

Swagger UI can be used to:

* Explore endpoints
* Send HTTP requests
* Test authentication
* Inspect request schemas
* Inspect response models
* Debug API behavior

---

# ⚙️ Installation

## 1. Clone Repository

```bash
git clone https://github.com/POORNIMA205/Amazon_backend.git
```

```bash
cd Amazon_backend
```

## 2. Create Virtual Environment

### Windows

```bash
python -m venv venv
```

Activate:

```bash
venv\Scripts\activate
```

### Linux / macOS

```bash
python3 -m venv venv
```

```bash
source venv/bin/activate
```

---

# 📦 Install Dependencies

```bash
pip install -r requirements.txt
```

---

# 🔑 Configuration

Create a `.env` file for environment-specific configuration.

Example:

```env
DATABASE_URL=sqlite:///./amazon.db
SECRET_KEY=your-secret-key
ALGORITHM=HS256
ACCESS_TOKEN_EXPIRE_MINUTES=30
```

### Security Note

Never commit real credentials, secret keys, API keys, or production database credentials to GitHub.

Use:

```text
.env
```

inside `.gitignore`.

---

# ▶️ Running Locally

Start the FastAPI server using Uvicorn:

```bash
uvicorn app.main:app --reload
```

The API will be available at:

```text
http://127.0.0.1:8000
```

Swagger documentation:

```text
http://127.0.0.1:8000/docs
```

---

# 🐳 Running with Docker

The application can be containerized to provide a consistent runtime environment.

Build the image:

```bash
docker build -t amazon-backend .
```

Run the container:

```bash
docker run -d \
  --name amazon-backend \
  -p 8000:8000 \
  amazon-backend
```

Check running containers:

```bash
docker ps
```

View logs:

```bash
docker logs amazon-backend
```

Stop the container:

```bash
docker stop amazon-backend
```

Remove the container:

```bash
docker rm amazon-backend
```

---

# 🧪 Testing

API testing can be performed using:

* Swagger UI
* Postman
* cURL
* Automated Python tests

Example:

```bash
pytest
```

A recommended test structure:

```text
tests/
│
├── test_auth.py
├── test_products.py
├── test_cart.py
├── test_orders.py
└── test_payments.py
```

---

# 🛡️ Security Considerations

The project demonstrates several backend security concepts:

### Authentication

JWT-based authentication protects private resources.

### Password Protection

Passwords should never be stored as plaintext.

Use a secure password hashing algorithm.

### Environment Variables

Sensitive configuration should be stored outside the source code.

### Input Validation

Pydantic models validate incoming API data before business logic executes.

### Authorization

Protected endpoints should verify that the authenticated user has permission to perform the requested operation.

### Production Security

For production deployment:

* Use HTTPS.
* Rotate secrets.
* Use a production-grade database.
* Enable rate limiting.
* Add structured logging.
* Implement security headers.
* Enable dependency vulnerability scanning.
* Never expose sensitive credentials.

GitHub also recommends security features such as Dependabot alerts, secret scanning, push protection, and code scanning for repositories.

---

# ❌ Error Handling

The API should return meaningful HTTP status codes.

Example:

```text
200 OK
201 Created
400 Bad Request
401 Unauthorized
403 Forbidden
404 Not Found
409 Conflict
422 Validation Error
500 Internal Server Error
```

Example JSON response:

```json
{
    "detail": "Product not found"
}
```

---

# ☁️ Deployment Architecture

A cloud-ready version of the application can be deployed using the following architecture:

```text
                    INTERNET
                       │
                       ▼
                ┌──────────────┐
                │ Load Balancer│
                └──────┬───────┘
                       │
                       ▼
                ┌──────────────┐
                │    Docker    │
                │   Container  │
                └──────┬───────┘
                       │
                       ▼
                ┌──────────────┐
                │   FastAPI    │
                │ Application  │
                └──────┬───────┘
                       │
              ┌────────┴─────────┐
              │                  │
              ▼                  ▼
       ┌──────────────┐   ┌──────────────┐
       │   Database   │   │   Logging    │
       │    Server    │   │ / Monitoring │
       └──────────────┘   └──────────────┘
```

For a production environment, SQLite can be replaced with a managed relational database such as PostgreSQL.

---

# 🔄 DevOps Workflow

The project can be integrated into a CI/CD pipeline:

```text
Developer
    │
    ▼
Git Push
    │
    ▼
GitHub
    │
    ▼
CI Pipeline
    │
    ├── Install Dependencies
    │
    ├── Lint
    │
    ├── Run Tests
    │
    ├── Security Scan
    │
    ▼
Build Docker Image
    │
    ▼
Container Registry
    │
    ▼
Deployment
    │
    ▼
Cloud Environment
```

Possible future tooling:

```text
GitHub Actions
Docker
Docker Hub
AWS
Terraform
Prometheus
Grafana
```

---

# 📊 Backend Design Principles

The project follows several important software engineering concepts:

### Separation of Concerns

Different responsibilities are separated into modules.

### Modularity

Authentication, products, carts, orders, and payments can evolve independently.

### API-First Design

The backend exposes REST APIs that can be consumed by multiple clients.

### Stateless Authentication

JWT authentication allows authenticated requests to carry their own authorization context.

### ORM-Based Persistence

SQLAlchemy abstracts database interactions and reduces direct SQL coupling.

### Schema Validation

Pydantic provides structured request and response validation.

### Containerization

Docker packages the application and dependencies into a reproducible runtime environment.

---

# 🚀 Future Enhancements

The following improvements can take the project closer to production scale:

* PostgreSQL integration
* Redis caching
* Redis-based session/rate limiting
* Real payment gateway integration
* Product search
* Product filtering
* Pagination
* Wishlist functionality
* Product reviews and ratings
* Inventory management
* Email notifications
* Order tracking
* Admin dashboard
* Docker Compose
* CI/CD using GitHub Actions
* AWS deployment
* Infrastructure as Code using Terraform
* Prometheus monitoring
* Grafana dashboards
* Centralized logging
* Automated security scanning
* API rate limiting

---

# 🎓 Learning Outcomes

This project demonstrates practical understanding of:

* Python backend development
* FastAPI
* REST API development
* HTTP methods and status codes
* JWT authentication
* Authorization
* Pydantic validation
* SQLAlchemy ORM
* Relational databases
* CRUD operations
* E-commerce workflows
* API documentation
* Docker
* Git and GitHub
* Backend architecture
* DevOps deployment concepts

---

# 📌 Project Highlights

```text
Backend Framework     → FastAPI
Language              → Python
Database              → SQLite
ORM                   → SQLAlchemy
Authentication        → JWT
API Style             → REST
Documentation         → Swagger / ReDoc
Containerization      → Docker
Version Control       → Git / GitHub
```

---

# 🔗 Repository

**GitHub:**
https://github.com/POORNIMA205/Amazon_backend

---

# 👩‍💻 Author

**Poornima H B**

Information Science & Engineering Student
Aspiring DevOps / Cloud Engineer

GitHub:

https://github.com/POORNIMA205

---


