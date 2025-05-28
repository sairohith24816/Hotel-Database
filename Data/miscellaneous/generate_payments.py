import pandas as pd
import random
from datetime import datetime, timedelta

# Set random seed for reproducibility
random.seed(42)

def get_room_type(room_id):
    """Determine room type based on room ID pattern"""
    last_two_digits = room_id % 100
    if last_two_digits == 0:  # Presidential Suite (X00)
        return "Presidential"
    elif 1 <= last_two_digits <= 10:  # Suite (X01-X10)
        return "Suite"
    elif 11 <= last_two_digits <= 20:  # Deluxe (X11-X20)
        return "Deluxe"
    elif 21 <= last_two_digits <= 40:  # Single (X21-X40)
        return "Single"
    else:  # Double (X41-X99)
        return "Double"

def get_room_cost(room_type):
    """Get cost per night for room type"""
    costs = {
        "Presidential": 10000,
        "Single": 1500,
        "Double": 2500,
        "Deluxe": 4000,
        "Suite": 6000
    }
    return costs[room_type]

def calculate_days_stayed(checkin_date, checkout_date, date_format):
    """Calculate number of days between checkin and checkout"""
    if date_format == "yyyy-mm-dd":
        checkin = datetime.strptime(checkin_date, "%Y-%m-%d")
        checkout = datetime.strptime(checkout_date, "%Y-%m-%d")
    else:  # dd-mm-yyyy
        checkin = datetime.strptime(checkin_date, "%d-%m-%Y")
        checkout = datetime.strptime(checkout_date, "%d-%m-%Y")
    
    days = (checkout - checkin).days
    # Ensure at least 1 day stay (minimum billing)
    return max(1, days)

def generate_payment_date(booking_date, checkin_date, checkout_date, date_format):
    """Generate random payment date from booking, checkin, or checkout date"""
    if date_format == "yyyy-mm-dd":
        dates = [
            datetime.strptime(booking_date, "%Y-%m-%d"),
            datetime.strptime(checkin_date, "%Y-%m-%d"),
            datetime.strptime(checkout_date, "%Y-%m-%d")
        ]
    else:  # dd-mm-yyyy
        dates = [
            datetime.strptime(booking_date, "%d-%m-%Y"),
            datetime.strptime(checkin_date, "%d-%m-%Y"),
            datetime.strptime(checkout_date, "%d-%m-%Y")
        ]
    
    selected_date = random.choice(dates)
    return selected_date, dates.index(selected_date)  # Return date and index (0=booking, 1=checkin, 2=checkout)

def generate_payments():
    """Generate payment data for all booking files"""
    
    # Load room type data
    roomtypes = pd.read_csv('roomtype_data.csv')
    
    # Payment methods
    payment_methods = ["Cash", "Card", "UPI", "Online"]
    
    all_payments = []
    payment_id_counter = 1
    
    print("=== GENERATING PAYMENTS ===")
    
    # 1. Process Past Bookings (Success status)
    print("Processing past bookings...")
    past_bookings = pd.read_csv('past_bookings.csv')
    
    for _, booking in past_bookings.iterrows():
        room_type = get_room_type(booking['RoomID'])
        cost_per_night = get_room_cost(room_type)
        days_stayed = calculate_days_stayed(booking['CheckInDate'], booking['CheckOutDate'], "yyyy-mm-dd")
        total_amount = cost_per_night * days_stayed
        
        payment_date_obj, date_index = generate_payment_date(
            booking['BookingDate'], booking['CheckInDate'], booking['CheckOutDate'], "yyyy-mm-dd"
        )
        
        payment_id = f"P{payment_id_counter:07d}"
        
        all_payments.append({
            'PaymentID': payment_id,
            'BookingID': booking['BookingID'],
            'Amount': total_amount,
            'PaymentDate': payment_date_obj.strftime('%d-%m-%Y'),
            'PaymentMethod': random.choice(payment_methods),
            'Status': 'Success'  # All past payments are successful
        })
        
        payment_id_counter += 1
    
    # 2. Process Current Bookings
    print("Processing current bookings...")
    current_bookings = pd.read_csv('current_bookings.csv')
    
    for _, booking in current_bookings.iterrows():
        room_type = get_room_type(booking['RoomID'])
        cost_per_night = get_room_cost(room_type)
        days_stayed = calculate_days_stayed(booking['CheckInDate'], booking['CheckOutDate'], "yyyy-mm-dd")
        total_amount = cost_per_night * days_stayed
        
        payment_date_obj, date_index = generate_payment_date(
            booking['BookingDate'], booking['CheckInDate'], booking['CheckOutDate'], "yyyy-mm-dd"
        )
        
        # Determine status based on payment date
        if date_index == 0:  # booking date
            status = 'Success'
        elif date_index == 1:  # checkin date
            status = 'Success'
        else:  # checkout date
            status = 'Pending'
        
        payment_id = f"P{payment_id_counter:07d}"
        
        all_payments.append({
            'PaymentID': payment_id,
            'BookingID': booking['BookingID'],
            'Amount': total_amount,
            'PaymentDate': payment_date_obj.strftime('%d-%m-%Y'),
            'PaymentMethod': random.choice(payment_methods),
            'Status': status
        })
        
        payment_id_counter += 1
    
    # 3. Process Future Bookings
    print("Processing future bookings...")
    future_bookings = pd.read_csv('future_bookings.csv')
    
    for _, booking in future_bookings.iterrows():
        room_type = get_room_type(booking['RoomID'])
        cost_per_night = get_room_cost(room_type)
        days_stayed = calculate_days_stayed(booking['CheckInDate'], booking['CheckOutDate'], "dd-mm-yyyy")
        total_amount = cost_per_night * days_stayed
        
        payment_date_obj, date_index = generate_payment_date(
            booking['BookingDate'], booking['CheckInDate'], booking['CheckOutDate'], "dd-mm-yyyy"
        )
        
        # Determine status based on payment date
        if date_index == 0:  # booking date
            status = 'Success'
        else:  # checkin or checkout date
            status = 'Pending'
        
        payment_id = f"P{payment_id_counter:07d}"
        
        all_payments.append({
            'PaymentID': payment_id,
            'BookingID': booking['BookingID'],
            'Amount': total_amount,
            'PaymentDate': payment_date_obj.strftime('%d-%m-%Y'),
            'PaymentMethod': random.choice(payment_methods),
            'Status': status
        })
        
        payment_id_counter += 1
    
    # Create DataFrame
    payments_df = pd.DataFrame(all_payments)
    
    # Sort by PaymentID to maintain order
    payments_df = payments_df.sort_values('PaymentID').reset_index(drop=True)
    
    # Save to CSV
    payments_df.to_csv('payments.csv', index=False)
    
    print(f"\n=== PAYMENT GENERATION COMPLETE ===")
    print(f"Total payments generated: {len(payments_df)}")
    print(f"PaymentID range: {payments_df['PaymentID'].iloc[0]} to {payments_df['PaymentID'].iloc[-1]}")
    
    # Show statistics
    print(f"\nPayment Status Distribution:")
    print(payments_df['Status'].value_counts())
    
    print(f"\nPayment Method Distribution:")
    print(payments_df['PaymentMethod'].value_counts())
    
    print(f"\nAmount Statistics:")
    print(f"Min Amount: ₹{payments_df['Amount'].min()}")
    print(f"Max Amount: ₹{payments_df['Amount'].max()}")
    print(f"Average Amount: ₹{payments_df['Amount'].mean():.2f}")
    
    print(f"\nSample entries:")
    print(payments_df.head(10))
    
    print(f"\nLast 5 entries:")
    print(payments_df.tail(5))
    
    return payments_df

if __name__ == "__main__":
    generate_payments()
