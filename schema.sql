-- Staff table
CREATE TABLE staff (
    staffid INT PRIMARY KEY,
    fullname VARCHAR(25) NOT NULL,
    gender VARCHAR(10),
    role VARCHAR(15) NOT NULL,
    phone BIGINT NOT NULL UNIQUE,
    email VARCHAR(40) UNIQUE,
    salary INT CHECK (salary > 0),
    joiningdate TIMESTAMP NOT NULL DEFAULT CURRENT_TIMESTAMP,
    CONSTRAINT chk_staff_gender CHECK (gender IN ('Male', 'Female','Other')),
    CONSTRAINT chk_staff_role CHECK (role IN ('Housekeeping', 'Receptionist', 'Manager', 'Security', 'Maintenance'))
);

-- Customer table
CREATE TABLE customer (
    customerid INT PRIMARY KEY,
    fullname VARCHAR(25) NOT NULL,
    phone BIGINT NOT NULL UNIQUE,
    email VARCHAR(40) UNIQUE,
    address VARCHAR(30),
    idproof VARCHAR(20),
    gender VARCHAR(10),
    createdat TIMESTAMP NOT NULL,
    age INT CHECK (age >= 18 AND age <= 100),
    CONSTRAINT chk_customer_gender CHECK (gender IN ('Male', 'Female', 'Other')),
    CONSTRAINT chk_customer_idproof CHECK (idproof IN ('Driving License', 'ID Card', 'PAN Card', 'Voter Card', 'Passport', 'Aadhar'))
);

-- Room type table
CREATE TABLE roomtype_data (
    roomtype VARCHAR(15) PRIMARY KEY,
    cost INT NOT NULL CHECK (cost > 0),
    roomcapacity INT NOT NULL CHECK (roomcapacity > 0 AND roomcapacity <= 10),
    CONSTRAINT chk_roomtype CHECK (roomtype IN ('Single', 'Double', 'Deluxe', 'Suite', 'Presidential'))
);

-- Room table
CREATE TABLE room_data (
    roomid INT PRIMARY KEY,
    roomtype VARCHAR(15) NOT NULL,
    status VARCHAR(10) NOT NULL DEFAULT 'Available',
    CONSTRAINT fk_room_roomtype FOREIGN KEY (roomtype) REFERENCES roomtype_data(roomtype),
    CONSTRAINT chk_room_status CHECK (status IN ('Available', 'Occupied', 'Maintenance'))
);

-- Bookings table (consolidated from all booking tables)
CREATE TABLE bookings (
    bookingid VARCHAR(10) PRIMARY KEY,
    customerid INT NOT NULL,
    roomid INT NOT NULL,    bookingdate TIMESTAMP NOT NULL,
    checkindate TIMESTAMP NOT NULL,
    checkoutdate TIMESTAMP NOT NULL,
    numberofguests INT NOT NULL CHECK (numberofguests > 0),
    status VARCHAR(15) NOT NULL,
    CONSTRAINT fk_booking_customer FOREIGN KEY (customerid) REFERENCES customer(customerid),
    CONSTRAINT fk_booking_room FOREIGN KEY (roomid) REFERENCES room_data(roomid),
    CONSTRAINT chk_booking_dates CHECK (checkindate < checkoutdate),
    CONSTRAINT chk_booking_status CHECK (status IN ('Confirmed', 'Checked-In', 'Checked-Out', 'Cancelled', 'Pending'))
);

-- Payments table
CREATE TABLE payments (
    paymentid VARCHAR(10) PRIMARY KEY,
    bookingid VARCHAR(10) NOT NULL,
    amount INT NOT NULL CHECK (amount > 0),
    paymentdate TIMESTAMP NOT NULL DEFAULT CURRENT_TIMESTAMP,
    paymentmethod VARCHAR(10) NOT NULL,
    status VARCHAR(10) NOT NULL,
    CONSTRAINT fk_payment_booking FOREIGN KEY (bookingid) REFERENCES bookings(bookingid),
    CONSTRAINT chk_payment_method CHECK (paymentmethod IN ('Cash', 'Card', 'UPI', 'Online')),
    CONSTRAINT chk_payment_status CHECK (status IN ('Pending', 'Completed', 'Failed', 'Refunded'))
);
