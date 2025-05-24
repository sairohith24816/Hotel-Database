# 🏨 Hotel Database Management System

A complete backend system for managing hotel operations, including customer bookings, room management, staff allocation, service usage, and payments.

---

## 📑 Entity-Relationship Model

### 🧍 Customer
- `CustomerID` (PK)
- `FullName`
- `Phone`
- `Email`
- `Address`
- `IDProof`

### 🛏️ Room
- `RoomID` (PK)
- `RoomNumber`
- `RoomType` (FK to RoomType)
- `Status` (Available / Occupied / Maintenance)
- `PricePerNight`
- `Floor`

### 🏷️ RoomType
- `RoomTypeID` (PK)
- `TypeName` (Single, Double, Deluxe, Suite)
- `Description`
- `MaxOccupancy`

### 📆 Booking
- `BookingID` (PK)
- `CustomerID` (FK to Customer)
- `RoomID` (FK to Room)
- `CheckInDate`
- `CheckOutDate`
- `BookingDate`
- `NumberOfGuests`
- `Status`

### 💳 Payment
- `PaymentID` (PK)
- `BookingID` (FK to Booking)
- `Amount`
- `PaymentDate`
- `PaymentMethod` (Cash, Card, UPI, Online)
- `Status`

### 👨‍💼 Staff
- `StaffID` (PK)
- `FullName`
- `Role` (Receptionist, Manager, Housekeeping)
- `Phone`
- `Email`
- `Salary`
- `Shift`

### 🛎️ Service
- `ServiceID` (PK)
- `ServiceName` (Laundry, Spa, Food)
- `Description`
- `Charge`

### 🧾 ServiceUsage
- `UsageID` (PK)
- `BookingID` (FK to Booking)
- `ServiceID` (FK to Service)
- `DateUsed`
- `Quantity`
- `TotalCharge`

### 🧹 RoomMaintenance
- `MaintenanceID` (PK)
- `RoomID` (FK to Room)
- `StaffID` (FK to Staff)
- `StartDate`
- `EndDate`
- `Remarks`

---

## 🔁 Relationships

- **Customer** ⟶ (1:M) ⟶ **Booking**
- **Booking** ⟶ (M:1) ⟶ **Room**
- **Room** ⟶ (M:1) ⟶ **RoomType**
- **Booking** ⟶ (1:1) ⟶ **Payment**
- **Booking** ⟶ (1:M) ⟶ **ServiceUsage**
- **ServiceUsage** ⟶ (M:1) ⟶ **Service**
- **Room** ⟶ (1:M) ⟶ **RoomMaintenance**
- **RoomMaintenance** ⟶ (M:1) ⟶ **Staff**

---

## 🚀 Tech Stack

- **Backend**: FastAPI
- **Database**: PostgreSQL / MySQL
- **ORM**: SQLAlchemy
- **Schema Validation**: Pydantic

---

## ✅ Features

- Manage customers, rooms, and staff.
- Handle room bookings and payments.
- Track service usage (spa, laundry, etc.).
- Maintain room service and maintenance history.

---

## 👥 TEAM

G.Sai Rohith   142201019  
V.Hemanth      142201020  
M.Rahul        142201022


