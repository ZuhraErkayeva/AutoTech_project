
# AutoTech Project

This project is a Django REST Framework-based application for managing vehicles, sensors, service centers, and maintenance schedules. Below is a comprehensive guide to set up and use the project.

---

## Authenticated

- **To use the project, you need to pass authentication**

## Features

- **Vehicles Management**: Add, view, update, and delete vehicles.
- **Sensors Management**: Track various sensors installed in vehicles.
- **Service Centers**: Manage details of service centers, including ratings.
- **Maintenance Scheduling**: Create and validate maintenance schedules for vehicles.

---

## Prerequisites

Ensure you have the following installed:

- Python 3.8+
- Django 5.1.4
- Django REST Framework

---

## Installation

1. **Clone the Repository**:
   ```bash
   git clone <repository-url>
   cd AutoTech_project
   ```

2. **Set up a Virtual Environment**:
   ```bash
   python -m venv .venv
   source .venv/bin/activate  # On Windows: .venv\Scripts\activate
   ```

3. **Install Dependencies**:
   ```bash
   pip install -r requirements.txt
   ```

4. **Apply Migrations**:
   ```bash
   python manage.py makemigrations
   python manage.py migrate
   ```

5. **Run the Development Server**:
   ```bash
   python manage.py runserver
   ```

---

## API Endpoints

The application provides the following API endpoints:

### Vehicles
- **List Vehicles**: `GET /vehicle/`
- **Retrieve a Vehicle**: `GET /vehicle/<id>/`
- **Create a Vehicle**: `POST /vehicle/`
- **Update a Vehicle**: `PUT /vehicle/<id>/`
- **Delete a Vehicle**: `DELETE /vehicle/<id>/`

### Sensors
- **List Sensors**: `GET /sensor/`
- **Retrieve a Sensor**: `GET /sensor/<id>/`
- **Create a Sensor**: `POST /sensor/`
- **Update a Sensor**: `PUT /sensor/<id>/`
- **Delete a Sensor**: `DELETE /sensor/<id>/`

### Service Centers
- **List Service Centers**: `GET /service/`
- **Retrieve a Service Center**: `GET /service/<id>/`
- **Create a Service Center**: `POST /service/`
- **Update a Service Center**: `PUT /service/<id>/`
- **Delete a Service Center**: `DELETE /service/<id>/`

### Maintenance
- **List Maintenance Schedules**: `GET /maintenance/`
- **Retrieve a Maintenance Schedule**: `GET /maintenance/<id>/`
- **Create a Maintenance Schedule**: `POST /maintenance/`
  - Validates that the `scheduled_date` is in the future.
- **Update a Maintenance Schedule**: `PUT /maintenance/<id>/`
- **Delete a Maintenance Schedule**: `DELETE /maintenance/<id>/`

---

## Models Overview

### Vehicles
Represents a vehicle with fields for model, year, and VIN.

### Sensors
Tracks sensors installed in vehicles. Supports three sensor types: Oil Change, Gasoline Refill, and Engine Temperature.

### Service Centers
Manages service center information including name, address, phone, and optional ratings.

### Maintenance
Schedules maintenance tasks for vehicles. Ensures the scheduled date is in the future.

---

## Validation Logic

- **Maintenance Schedule Validation**:
  - Implemented in the `MaintenanceSerializer`.
  - Raises an error if the `scheduled_date` is today or in the past.

---

## Testing

Run the following command to execute tests:
```bash
python manage.py test
```

---



