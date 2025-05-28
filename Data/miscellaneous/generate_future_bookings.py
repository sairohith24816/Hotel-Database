import pandas as pd
import random
from datetime import datetime, timedelta

def generate_future_bookings():
    # Starting BookingID (continuing from current bookings)
    start_booking_num = 2734
    
    # Room capacity mapping based on room number pattern
    def get_room_capacity(room_id):
        last_two_digits = room_id % 100
        if last_two_digits == 0:  # Presidential Suite (X00)
            return random.randint(1, 4)  # Can accommodate up to 4 guests
        elif 1 <= last_two_digits <= 10:  # Suite (X01-X10)
            return random.randint(1, 3)  # Can accommodate up to 3 guests
        elif 11 <= last_two_digits <= 20:  # Deluxe (X11-X20)
            return random.randint(1, 3)  # Can accommodate up to 3 guests
        elif 21 <= last_two_digits <= 40:  # Single (X21-X40)
            return 1  # Only 1 guest
        else:  # Double (X41-X99)
            return random.randint(1, 2)  # Can accommodate up to 2 guests
    
    # Generate random date within range
    def random_date(start_date, end_date):
        time_between = end_date - start_date
        days_between = time_between.days
        random_days = random.randrange(days_between + 1)
        return start_date + timedelta(days=random_days)
    
    # Date ranges
    start_date = datetime(2025, 6, 1)
    end_date = datetime(2025, 7, 31)
    
    bookings = []
    
    # Generate 1500 future bookings
    for i in range(1500):
        booking_id = f"B{start_booking_num + i:07d}"
        customer_id = random.randint(1, 1000)
        room_id = random.randint(100, 999)        # Generate check-in date first (but not on the very first day to allow booking date before it)
        checkin_start = start_date + timedelta(days=1)  # Start from June 2nd to allow June 1st for booking
        checkin_date = random_date(checkin_start, end_date)
        
        # Booking date must be before check-in date
        booking_end = checkin_date - timedelta(days=1)
        booking_date = random_date(start_date, booking_end)
        
        # Check-out date must be after check-in date
        checkout_start = checkin_date + timedelta(days=1)
        if checkout_start > end_date:
            checkout_start = checkin_date + timedelta(days=1)
            # Extend end date for checkout if needed
            checkout_end = max(end_date, checkout_start + timedelta(days=7))
        else:
            checkout_end = end_date + timedelta(days=7)  # Allow checkout beyond July
        
        checkout_date = random_date(checkout_start, checkout_end)
        
        # Number of guests based on room capacity
        num_guests = get_room_capacity(room_id)
        
        # Status is always "Confirmed" for future bookings
        status = "Confirmed"
        
        bookings.append({
            'BookingID': booking_id,
            'CustomerID': customer_id,
            'RoomID': room_id,
            'CheckInDate': checkin_date.strftime('%Y-%m-%d'),
            'CheckOutDate': checkout_date.strftime('%Y-%m-%d'),
            'BookingDate': booking_date.strftime('%Y-%m-%d'),
            'NumberOfGuests': num_guests,
            'Status': status
        })
    
    # Create DataFrame and sort by BookingDate
    df = pd.DataFrame(bookings)
    df = df.sort_values('BookingDate')
    
    # Reassign BookingIDs to maintain order after sorting
    for i, idx in enumerate(df.index):
        df.at[idx, 'BookingID'] = f"B{start_booking_num + i:07d}"
    
    # Save to CSV
    df.to_csv('future_bookings.csv', index=False)
    print(f"Generated {len(df)} future bookings")
    print(f"BookingID range: {df['BookingID'].iloc[0]} to {df['BookingID'].iloc[-1]}")
    print(f"Date range: {df['BookingDate'].min()} to {df['BookingDate'].max()}")
    print("Future bookings saved to future_bookings.csv")
    
    # Display first few rows
    print("\nFirst 5 rows:")
    print(df.head().to_string())
    
    # Display last few rows
    print("\nLast 5 rows:")
    print(df.tail().to_string())

if __name__ == "__main__":
    generate_future_bookings()
