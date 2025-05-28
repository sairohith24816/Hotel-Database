import pandas as pd
import random
from datetime import datetime, timedelta

# Set random seed for reproducibility
random.seed(42)

def generate_future_bookings():
    # Read current bookings to get the last BookingID
    current_bookings = pd.read_csv('current_bookings.csv')
    last_booking_id = current_bookings['BookingID'].iloc[-1]
    last_number = int(last_booking_id[1:])  # Remove 'B' prefix and convert to int
    
    # Room capacity mapping based on room number pattern
    def get_room_capacity(room_id):
        last_two_digits = room_id % 100
        if last_two_digits == 0:  # Presidential Suite (X00)
            return random.randint(1, 6)  # Can accommodate up to 6 guests
        elif 1 <= last_two_digits <= 10:  # Suite (X01-X10)
            return random.randint(1, 4)  # Can accommodate up to 4 guests
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
        if days_between < 0:
            return start_date
        random_days = random.randrange(days_between + 1)
        return start_date + timedelta(days=random_days)
    
    # Date ranges: June 1, 2025 to July 31, 2025
    start_date = datetime(2025, 6, 1)
    end_date = datetime(2025, 7, 31)
    
    future_bookings = []
    num_bookings = 500  # Generate 500 future bookings
    
    for i in range(num_bookings):
        customer_id = random.randint(1, 1000)
        room_id = random.randint(100, 999)
        
        # Generate booking date first (June 1 to July 29 to ensure valid constraints)
        booking_start = start_date
        booking_end = end_date - timedelta(days=2)  # Leave room for checkin and checkout
        booking_date = random_date(booking_start, booking_end)
        
        # Generate check-in date (must be after booking date, but within our range)
        checkin_start = booking_date + timedelta(days=1)
        checkin_end = end_date - timedelta(days=1)  # Leave room for checkout
        
        if checkin_start <= checkin_end:
            checkin_date = random_date(checkin_start, checkin_end)
        else:
            # If no valid checkin date, use next day after booking
            checkin_date = booking_date + timedelta(days=1)
        
        # Generate check-out date (must be after check-in date)
        checkout_start = checkin_date + timedelta(days=1)
        checkout_end = end_date
        
        if checkout_start <= checkout_end:
            checkout_date = random_date(checkout_start, checkout_end)
        else:
            # If no valid checkout date, use checkin + 1 day
            checkout_date = checkin_date + timedelta(days=1)
        
        # Get number of guests based on room capacity
        num_guests = get_room_capacity(room_id)
        
        status = "Confirmed"
        
        future_bookings.append([
            i + 1,  # Temporary placeholder for BookingID
            customer_id,
            room_id,
            checkin_date.strftime('%d-%m-%Y'),  # dd-mm-yyyy format
            checkout_date.strftime('%d-%m-%Y'),  # dd-mm-yyyy format
            booking_date.strftime('%d-%m-%Y'),   # dd-mm-yyyy format
            num_guests,
            status
        ])
    
    # Create DataFrame and sort by booking date
    df = pd.DataFrame(future_bookings, columns=[
        'BookingID', 'CustomerID', 'RoomID', 'CheckInDate', 
        'CheckOutDate', 'BookingDate', 'NumberOfGuests', 'Status'
    ])
    
    # Sort by booking date first
    df['BookingDateSort'] = pd.to_datetime(df['BookingDate'], format='%d-%m-%Y')
    df = df.sort_values('BookingDateSort').reset_index(drop=True)
    df = df.drop('BookingDateSort', axis=1)
    
    # Assign sequential BookingIDs after sorting
    for i in range(len(df)):
        df.iloc[i, 0] = f"B{last_number + i + 1:07d}"
    
    # Save to CSV
    df.to_csv('future_bookings.csv', index=False)
    
    print(f"Generated {len(df)} future bookings")
    print(f"BookingID range: {df['BookingID'].iloc[0]} to {df['BookingID'].iloc[-1]}")
    print(f"Date range: {df['BookingDate'].min()} to {df['CheckOutDate'].max()}")
    print("Sample entries:")
    print(df.head(10))
    
    return df

if __name__ == "__main__":
    generate_future_bookings()
