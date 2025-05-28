import pandas as pd
from datetime import datetime

def verify_payment_calculations():
    """Verify payment amount calculations against booking data"""
    
    # Load data
    payments = pd.read_csv('payments.csv')
    past_bookings = pd.read_csv('past_bookings.csv')
    roomtypes = pd.read_csv('roomtype_data.csv')
    
    # Room cost mapping
    costs = {
        "Presidential": 10000,
        "Single": 1500,
        "Double": 2500,
        "Deluxe": 4000,
        "Suite": 6000
    }
    
    def get_room_type(room_id):
        last_two_digits = room_id % 100
        if last_two_digits == 0:
            return "Presidential"
        elif 1 <= last_two_digits <= 10:
            return "Suite"
        elif 11 <= last_two_digits <= 20:
            return "Deluxe"
        elif 21 <= last_two_digits <= 40:
            return "Single"
        else:
            return "Double"
    
    print("=== PAYMENT CALCULATION VERIFICATION ===")
    
    # Check first 5 past bookings
    for i in range(5):
        booking = past_bookings.iloc[i]
        payment = payments[payments['BookingID'] == booking['BookingID']].iloc[0]
        
        # Calculate expected amount
        room_type = get_room_type(booking['RoomID'])
        cost_per_night = costs[room_type]
        
        checkin = datetime.strptime(booking['CheckInDate'], "%Y-%m-%d")
        checkout = datetime.strptime(booking['CheckOutDate'], "%Y-%m-%d")
        days = max(1, (checkout - checkin).days)
        
        expected_amount = cost_per_night * days
        
        print(f"\nBooking {booking['BookingID']}:")
        print(f"  Room {booking['RoomID']} ({room_type}) - ₹{cost_per_night}/night")
        print(f"  {booking['CheckInDate']} to {booking['CheckOutDate']} = {days} days")
        print(f"  Expected: ₹{expected_amount}, Actual: ₹{payment['Amount']}")
        print(f"  Match: {expected_amount == payment['Amount']}")
    
    # Check room type distribution in payments
    print(f"\n=== ROOM TYPE DISTRIBUTION IN PAYMENTS ===")
    room_types = []
    for _, payment in payments.head(100).iterrows():  # Sample first 100
        booking_id = payment['BookingID']
        
        # Find the booking in appropriate file
        if booking_id.startswith('B000'):  # Past booking
            booking = past_bookings[past_bookings['BookingID'] == booking_id].iloc[0]
        else:
            continue
            
        room_type = get_room_type(booking['RoomID'])
        room_types.append(room_type)
    
    from collections import Counter
    type_counts = Counter(room_types)
    for room_type, count in type_counts.items():
        print(f"{room_type}: {count} payments")

if __name__ == "__main__":
    verify_payment_calculations()
