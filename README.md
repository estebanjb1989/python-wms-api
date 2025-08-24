# Inventory Management System

> A robust Flask-based backend system for managing inventory, warehouses, and user authentication.

---

## Table of Contents

- [Project Overview](#project-overview)  
- [Features](#features)  
- [Tech Stack](#tech-stack)  
- [Repository Structure](#repository-structure)  
- [Getting Started](#getting-started)  
  - [Prerequisites](#prerequisites)  
  - [Setup Backend](#setup-backend)  
  - [Running the Application](#running-the-application)  
- [Database Migrations](#database-migrations)  
- [Troubleshooting](#troubleshooting)  
- [Contributing](#contributing)  
- [License](#license)  

---

## Project Overview

This backend system provides RESTful APIs for user authentication, inventory management, and warehouse operations. It is built with Flask, uses SQLAlchemy for ORM, and Flask-Migrate for database migrations.

---

## Features

- User Authentication & Authorization  
- Inventory CRUD operations  
- Warehouse management  
- Database migrations with Alembic/Flask-Migrate  
- Environment-based configuration (development, staging, production)  

---

## Tech Stack

| Layer         | Technology                         |
| ------------- | --------------------------------- |
| Backend       | Python, Flask, SQLAlchemy, Flask-Migrate |
| Database      | SQLite (default), configurable for others |
| Dev Tools     | Flask CLI, Alembic                |

---

## Repository Structure

