-- Hotel Database Management System

-- CREATE DATABASE hotel_management;

-- Use the database
-- \c hotel_management;
-- Create RoomType table first (referenced by Room)
CREATE TABLE RoomType (
    RoomTypeID SERIAL PRIMARY KEY,
    TypeName VARCHAR(50) NOT NULL CHECK (TypeName IN ('Single', 'Double', 'Deluxe', 'Suite')),
    Description TEXT,
    MaxOccupancy INTEGER NOT NULL CHECK (MaxOccupancy > 0),
    UNIQUE(TypeName)
);

-- Create Room table
CREATE TABLE Room (
    RoomID SERIAL PRIMARY KEY,
    RoomNumber VARCHAR(10) NOT NULL UNIQUE,
    RoomTypeID INTEGER NOT NULL REFERENCES RoomType(RoomTypeID),
    Status VARCHAR(20) NOT NULL DEFAULT 'Available' CHECK (Status IN ('Available', 'Occupied', 'Maintenance')),
    PricePerNight DECIMAL(10,2) NOT NULL CHECK (PricePerNight > 0),
    Floor INTEGER NOT NULL CHECK (Floor > 0)
);

-- Create Customer table
CREATE TABLE Customer (
    CustomerID SERIAL PRIMARY KEY,
    FullName VARCHAR(100) NOT NULL,
    Phone VARCHAR(15) NOT NULL UNIQUE,
    Email VARCHAR(100) UNIQUE,
    Address TEXT,
    IDProof VARCHAR(50) NOT NULL,
    CreatedAt TIMESTAMP DEFAULT CURRENT_TIMESTAMP
);

-- Create Staff table
CREATE TABLE Staff (
    StaffID SERIAL PRIMARY KEY,
    FullName VARCHAR(100) NOT NULL,
    Role VARCHAR(50) NOT NULL CHECK (Role IN ('Receptionist', 'Manager', 'Housekeeping')),
    Phone VARCHAR(15) NOT NULL UNIQUE,
    Email VARCHAR(100) UNIQUE,
    Salary DECIMAL(10,2) CHECK (Salary > 0),
    Shift VARCHAR(20) CHECK (Shift IN ('Morning', 'Evening', 'Night')),
    HiredDate TIMESTAMP DEFAULT CURRENT_TIMESTAMP
);

-- Create Booking table
CREATE TABLE Booking (
    BookingID SERIAL PRIMARY KEY,
    CustomerID INTEGER NOT NULL REFERENCES Customer(CustomerID),
    RoomID INTEGER NOT NULL REFERENCES Room(RoomID),
    CheckInDate DATE NOT NULL,
    CheckOutDate DATE NOT NULL,
    BookingDate TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
    NumberOfGuests INTEGER NOT NULL CHECK (NumberOfGuests > 0),
    Status VARCHAR(20) NOT NULL DEFAULT 'Confirmed' CHECK (Status IN ('Confirmed', 'CheckedIn', 'CheckedOut', 'Cancelled')),
    CONSTRAINT check_dates CHECK (CheckOutDate > CheckInDate)
);

-- Create Payment table
CREATE TABLE Payment (
    PaymentID SERIAL PRIMARY KEY,
    BookingID INTEGER NOT NULL REFERENCES Booking(BookingID),
    Amount DECIMAL(10,2) NOT NULL CHECK (Amount > 0),
    PaymentDate TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
    PaymentMethod VARCHAR(20) NOT NULL CHECK (PaymentMethod IN ('Cash', 'Card', 'UPI', 'Online')),
    Status VARCHAR(20) NOT NULL DEFAULT 'Pending' CHECK (Status IN ('Pending', 'Completed', 'Failed', 'Refunded'))
);

-- Create Service table
CREATE TABLE Service (
    ServiceID SERIAL PRIMARY KEY,
    ServiceName VARCHAR(100) NOT NULL CHECK (ServiceName IN ('Laundry', 'Spa', 'Food', 'Room Service', 'Gym', 'Pool')),
    Description TEXT,
    Charge DECIMAL(10,2) NOT NULL CHECK (Charge >= 0),
    UNIQUE(ServiceName)
);

-- Create ServiceUsage table
CREATE TABLE ServiceUsage (
    UsageID SERIAL PRIMARY KEY,
    BookingID INTEGER NOT NULL REFERENCES Booking(BookingID),
    ServiceID INTEGER NOT NULL REFERENCES Service(ServiceID),
    DateUsed TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
    Quantity INTEGER NOT NULL DEFAULT 1 CHECK (Quantity > 0),
    TotalCharge DECIMAL(10,2) NOT NULL CHECK (TotalCharge >= 0)
);

-- Create RoomMaintenance table
CREATE TABLE RoomMaintenance (
    MaintenanceID SERIAL PRIMARY KEY,
    RoomID INTEGER NOT NULL REFERENCES Room(RoomID),
    StaffID INTEGER NOT NULL REFERENCES Staff(StaffID),
    StartDate TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
    EndDate TIMESTAMP,
    Remarks TEXT,
    Status VARCHAR(20) DEFAULT 'In Progress' CHECK (Status IN ('Scheduled', 'In Progress', 'Completed')),
    CONSTRAINT check_maintenance_dates CHECK (EndDate IS NULL OR EndDate >= StartDate)
);

-- Show all tables in the database
SELECT table_name 
FROM information_schema.tables 
WHERE table_schema = 'public' 
ORDER BY table_name;

-- Show detailed information about all tables
SELECT 
    table_name,
    column_name,
    data_type,
    is_nullable,
    column_default
FROM information_schema.columns 
WHERE table_schema = 'public' 
ORDER BY table_name, ordinal_position;

-- Show table constraints
SELECT 
    tc.table_name,
    tc.constraint_name,
    tc.constraint_type
FROM information_schema.table_constraints tc
WHERE tc.table_schema = 'public'
ORDER BY tc.table_name;
