import pandas as pd
from datetime import datetime

def validate_payments():
    """Validate payment data against booking data"""
    
    # Load all data files
    payments = pd.read_csv('payments.csv')
    past_bookings = pd.read_csv('past_bookings.csv')
    current_bookings = pd.read_csv('current_bookings.csv') 
    future_bookings = pd.read_csv('future_bookings.csv')
    
    print("=== PAYMENT VALIDATION ===")
    
    # 1. Check past bookings (all should be Success)
    past_payments = payments[payments['BookingID'].isin(past_bookings['BookingID'])]
    past_success_count = (past_payments['Status'] == 'Success').sum()
    print(f"Past bookings: {len(past_payments)} payments, {past_success_count} Success status")
    print(f"Past bookings - All Success: {past_success_count == len(past_payments)}")
    
    # 2. Check current bookings payment status logic
    current_payments = payments[payments['BookingID'].isin(current_bookings['BookingID'])]
    current_success = (current_payments['Status'] == 'Success').sum()
    current_pending = (current_payments['Status'] == 'Pending').sum()
    print(f"\nCurrent bookings: {len(current_payments)} payments")
    print(f"  Success: {current_success}, Pending: {current_pending}")
    
    # 3. Check future bookings payment status logic
    future_payments = payments[payments['BookingID'].isin(future_bookings['BookingID'])]
    future_success = (future_payments['Status'] == 'Success').sum()
    future_pending = (future_payments['Status'] == 'Pending').sum()
    print(f"\nFuture bookings: {len(future_payments)} payments")
    print(f"  Success: {future_success}, Pending: {future_pending}")
    
    # 4. Check for any negative amounts
    negative_amounts = payments[payments['Amount'] < 0]
    print(f"\nNegative amounts: {len(negative_amounts)}")
    
    # 5. Verify payment ID continuity
    expected_ids = [f"P{i:07d}" for i in range(1, len(payments) + 1)]
    actual_ids = payments['PaymentID'].tolist()
    print(f"\nPaymentID continuity: {expected_ids == actual_ids}")
    
    # 6. Sample validation - check specific booking
    print(f"\n=== SAMPLE VALIDATION ===")
    sample_booking = past_bookings.iloc[0]
    sample_payment = payments[payments['BookingID'] == sample_booking['BookingID']].iloc[0]
    
    print(f"Sample Booking: {sample_booking['BookingID']}")
    print(f"  Room ID: {sample_booking['RoomID']}")
    print(f"  Check-in: {sample_booking['CheckInDate']}")
    print(f"  Check-out: {sample_booking['CheckOutDate']}")
    print(f"  Nights: {(datetime.strptime(sample_booking['CheckOutDate'], '%Y-%m-%d') - datetime.strptime(sample_booking['CheckInDate'], '%Y-%m-%d')).days}")
    
    print(f"Sample Payment: {sample_payment['PaymentID']}")
    print(f"  Amount: ₹{sample_payment['Amount']}")
    print(f"  Payment Date: {sample_payment['PaymentDate']}")
    print(f"  Method: {sample_payment['PaymentMethod']}")
    print(f"  Status: {sample_payment['Status']}")
    
    # 7. Payment distribution by booking type
    print(f"\n=== PAYMENT DISTRIBUTION ===")
    print(f"Total payments: {len(payments)}")
    print(f"Past booking payments: {len(past_payments)}")
    print(f"Current booking payments: {len(current_payments)}")
    print(f"Future booking payments: {len(future_payments)}")
    print(f"Total check: {len(past_payments) + len(current_payments) + len(future_payments) == len(payments)}")
    
    return payments

if __name__ == "__main__":
    validate_payments()
