# 🏨 Hotel Database Management System

A complete backend system for managing hotel operations, including customer bookings, room management, staff allocation, and payments.

---

## 📑 Entity-Relationship Model

### 🏷️ RoomType
- `RoomType` (PK) (Single, Double, Deluxe, Suite)
- `Cost`
- `RoomCapacity`

### 🛏️ Room
- `RoomID` (PK)
- `RoomType` (FK to RoomType)
- `Status` (Available / Occupied / Maintenance)

### 🧍 Customer
- `CustomerID` (PK)
- `FullName`
- `Phone`
- `Email`
- `Address`
- `IDProof`
- `Gender`
- `CreatedAt`

### 👨‍💼 Staff
- `StaffID` (PK)
- `FullName`
- `Role` (Receptionist, Manager, Housekeeping)
- `Phone`
- `Email`
- `Salary`
- `Gender`
- `JoiningDate`

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

---

## 🔁 Relationships

- **RoomType** ⟶ (1:M) ⟶ **Room**
- **Customer** ⟶ (1:M) ⟶ **Booking**
- **Room** ⟶ (1:M) ⟶ **Booking**
- **Booking** ⟶ (1:1) ⟶ **Payment**

---

## ✅ Features

- Manage customers, rooms, and staff.
- Handle room bookings and payments.
- Track room types with capacity and pricing.
- Maintain staff information and roles.

---

## 👥 TEAM

G.Sai Rohith 142201019  
V.Hemanth 142201020  
M.Rahul 142201022


