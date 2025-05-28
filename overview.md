# 🏨 Hotel Database Management System

A complete backend system for managing hotel operations, including customer bookings, room management, staff allocation, and payments.

---

## 📑 Entity-Relationship Model

### 🏷️ RoomType
- `RoomType` (PK) (Presidential, Single, Double, Deluxe, Suite)
- `Cost`
- `RoomCapacity`

### 🛏️ Room
- `RoomID` (PK)
- `RoomType` (FK to RoomType)
- `Status` (Available / Occupied / Maintenance)

Room Distribution per Floor (9 floors, 100 rooms each):
- Room X00: Presidential Suite (1 room)
- Rooms X01-X10: Suite (10 rooms)
- Rooms X11-X20: Deluxe (10 rooms)
- Rooms X21-X40: Single (20 rooms)
- Rooms X41-X99: Double (59 rooms)

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
- `Status` (Confirmed, Checked-In, Checked-Out, Cancelled, No-Show)

### 💳 Payment
- `PaymentID` (PK)
- `BookingID` (FK to Booking)
- `Amount`
- `PaymentDate`
- `PaymentMethod` (Cash, Card, UPI, Online)
- `Status` (Success, Failed, Pending)

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
- Track room types with capacity and pricing including Presidential suites.
- Maintain staff information and roles.
- Support for 900 rooms across 9 floors with varied room types.

---

## 👥 TEAM

G.Sai Rohith 142201019  
V.Hemanth 142201020  
M.Rahul 142201022


