# 🏨 Hotel Database Management System

A PostgreSQL-based database management system for hotel operations.

## 🗃️ Database Schema

The database consists of 5 main tables:

### Tables and Columns

| Table | Columns |
|-------|---------|
| **RoomType** | ***RoomType*** (PK), Cost, RoomCapacity |
| **Room** | ***RoomID*** (PK), RoomType (FK), Status |
| **Customer** | ***CustomerID*** (PK), FullName, Phone, Email, Address, IDProof, Gender, CreatedAt |
| **Staff** | ***StaffID*** (PK), FullName, Role, Phone, Email, Salary, Gender, JoiningDate |
| **Booking** | ***BookingID*** (PK), CustomerID (FK), RoomID (FK), CheckInDate, CheckOutDate, BookingDate, NumberOfGuests, Status |
| **Payment** | ***PaymentID*** (PK), BookingID (FK), Amount, PaymentDate, PaymentMethod, Status |

### Relationships
```
RoomType (1) ──→ (M) Room (1) ──→ (M) Booking
Customer (1) ──→ (M) Booking (1) ──→ (1) Payment
Staff (independent table)
```

## 👥 Team

- **G.Sai Rohith** - 142201019
- **V.Hemanth** - 142201020  
- **M.Rahul** - 142201022
