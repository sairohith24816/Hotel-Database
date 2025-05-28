import pandas as pd
import random
from datetime import datetime, date, timedelta
import csv

# Set random seed for reproducibility
random.seed(42)

# Read existing data
room_data = pd.read_csv('room_data.csv')
roomtype_data = pd.read_csv('roomtype_data.csv')

# Create a mapping for room capacities
room_capacity_map = dict(zip(roomtype_data['RoomType'], roomtype_data['RoomCapacity']))

def get_room_capacity(room_id):
    """Get room capacity based on room ID pattern"""
    room_str = str(room_id)
    if room_str.endswith('00'):
        return 6  # Presidential
    elif room_str[-2:] in [f'{i:02d}' for i in range(1, 11)]:
        return 4  # Suite
    elif room_str[-2:] in [f'{i:02d}' for i in range(11, 21)]:
        return 3  # Deluxe
    elif room_str[-2:] in [f'{i:02d}' for i in range(21, 41)]:
        return 1  # Single
    else:
        return 2  # Double

def generate_random_date(start_date, end_date):
    """Generate a random date between start_date and end_date"""
    start = datetime.strptime(start_date, '%Y-%m-%d')
    end = datetime.strptime(end_date, '%Y-%m-%d')
    delta = end - start
    random_days = random.randint(0, delta.days)
    return (start + timedelta(days=random_days)).strftime('%Y-%m-%d')

def generate_booking_dates(booking_date_str):
    """Generate check-in and check-out dates ensuring booking < checkin < checkout"""
    booking_date = datetime.strptime(booking_date_str, '%Y-%m-%d')
    
    # Check-in date: 1-30 days after booking date
    checkin_days_after = random.randint(1, 30)
    checkin_date = booking_date + timedelta(days=checkin_days_after)
    
    # Check-out date: 1-14 days after check-in date
    checkout_days_after = random.randint(1, 14)
    checkout_date = checkin_date + timedelta(days=checkout_days_after)
    
    return checkin_date.strftime('%Y-%m-%d'), checkout_date.strftime('%Y-%m-%d')

print("Generating past bookings (2024)...")

# Generate past bookings (2000 rows for 2024)
past_bookings = []
booking_counter = 1

for i in range(2000):
    booking_id = f"B{booking_counter:07d}"
    customer_id = random.randint(1, 1000)
    room_id = random.randint(100, 999)
    
    # Generate booking date in 2024
    booking_date = generate_random_date('2024-01-01', '2024-12-31')
    
    # Generate check-in and check-out dates
    checkin_date, checkout_date = generate_booking_dates(booking_date)
    
    # Ensure checkout date doesn't exceed 2024
    checkout_dt = datetime.strptime(checkout_date, '%Y-%m-%d')
    if checkout_dt.year > 2024:
        checkout_date = '2024-12-31'
    
    # Get number of guests based on room capacity
    room_capacity = get_room_capacity(room_id)
    number_of_guests = random.randint(1, room_capacity)
    
    status = "Checked-Out"
    
    past_bookings.append({
        'BookingID': booking_id,
        'CustomerID': customer_id,
        'RoomID': room_id,
        'CheckInDate': checkin_date,
        'CheckOutDate': checkout_date,
        'BookingDate': booking_date,
        'NumberOfGuests': number_of_guests,
        'Status': status
    })
    
    booking_counter += 1

# Sort by booking date
past_bookings.sort(key=lambda x: x['BookingDate'])

# Re-assign BookingIDs in order after sorting
for i, booking in enumerate(past_bookings, 1):
    booking['BookingID'] = f"B{i:07d}"

# Save past bookings to CSV
past_bookings_df = pd.DataFrame(past_bookings)
past_bookings_df.to_csv('past_bookings.csv', index=False)

print(f"Generated {len(past_bookings)} past bookings")
print("Past bookings saved to past_bookings.csv")

print("\nGenerating current bookings (2025)...")

# Generate current bookings for occupied rooms
occupied_rooms = room_data[room_data['Status'] == 'Occupied']['RoomID'].tolist()
current_bookings = []

# Continue booking counter from where past bookings ended
booking_counter = 2001

for room_id in occupied_rooms:
    booking_id = f"B{booking_counter:07d}"
    customer_id = random.randint(1, 1000)
    
    # Generate booking date in early 2025
    booking_date = generate_random_date('2025-01-01', '2025-05-31')
    
    # Generate check-in and check-out dates
    checkin_date, checkout_date = generate_booking_dates(booking_date)
    
    # Ensure dates are within 2025 range
    checkin_dt = datetime.strptime(checkin_date, '%Y-%m-%d')
    checkout_dt = datetime.strptime(checkout_date, '%Y-%m-%d')
    
    if checkin_dt > datetime(2025, 5, 31):
        checkin_date = '2025-05-31'
        checkout_date = '2025-05-31'
    elif checkout_dt > datetime(2025, 5, 31):
        checkout_date = '2025-05-31'
    
    # Get number of guests based on room capacity
    room_capacity = get_room_capacity(room_id)
    number_of_guests = random.randint(1, room_capacity)
    
    status = "Checked-In"
    
    current_bookings.append({
        'BookingID': booking_id,
        'CustomerID': customer_id,
        'RoomID': room_id,
        'CheckInDate': checkin_date,
        'CheckOutDate': checkout_date,
        'BookingDate': booking_date,
        'NumberOfGuests': number_of_guests,
        'Status': status
    })
    
    booking_counter += 1

# Sort by booking date
current_bookings.sort(key=lambda x: x['BookingDate'])

# Re-assign BookingIDs in order after sorting (starting from B0002001)
for i, booking in enumerate(current_bookings):
    booking['BookingID'] = f"B{2001 + i:07d}"

# Save current bookings to CSV
current_bookings_df = pd.DataFrame(current_bookings)
current_bookings_df.to_csv('current_bookings.csv', index=False)

print(f"Generated {len(current_bookings)} current bookings")
print("Current bookings saved to current_bookings.csv")

print("\nBooking generation completed!")
print(f"Past bookings: {len(past_bookings)} records")
print(f"Current bookings: {len(current_bookings)} records")
print(f"Total bookings: {len(past_bookings) + len(current_bookings)} records")
