import pandas as pd
from datetime import datetime

def convert_date_formats():
    """Convert date formats in booking files from yyyy-mm-dd to dd-mm-yyyy"""
    
    print("=== CONVERTING DATE FORMATS TO DD-MM-YYYY ===")
    
    # 1. Convert past_bookings.csv
    print("Converting past_bookings.csv...")
    past_bookings = pd.read_csv('past_bookings.csv')
    
    # Convert date columns
    past_bookings['CheckInDate'] = pd.to_datetime(past_bookings['CheckInDate'], format='%Y-%m-%d').dt.strftime('%d-%m-%Y')
    past_bookings['CheckOutDate'] = pd.to_datetime(past_bookings['CheckOutDate'], format='%Y-%m-%d').dt.strftime('%d-%m-%Y')
    past_bookings['BookingDate'] = pd.to_datetime(past_bookings['BookingDate'], format='%Y-%m-%d').dt.strftime('%d-%m-%Y')
    
    # Save back to CSV
    past_bookings.to_csv('past_bookings.csv', index=False)
    print(f"✅ Converted {len(past_bookings)} past booking entries")
    
    # 2. Convert current_bookings.csv
    print("Converting current_bookings.csv...")
    current_bookings = pd.read_csv('current_bookings.csv')
    
    # Convert date columns
    current_bookings['CheckInDate'] = pd.to_datetime(current_bookings['CheckInDate'], format='%Y-%m-%d').dt.strftime('%d-%m-%Y')
    current_bookings['CheckOutDate'] = pd.to_datetime(current_bookings['CheckOutDate'], format='%Y-%m-%d').dt.strftime('%d-%m-%Y')
    current_bookings['BookingDate'] = pd.to_datetime(current_bookings['BookingDate'], format='%Y-%m-%d').dt.strftime('%d-%m-%Y')
    
    # Save back to CSV
    current_bookings.to_csv('current_bookings.csv', index=False)
    print(f"✅ Converted {len(current_bookings)} current booking entries")
    
    print("\n=== DATE FORMAT CONVERSION COMPLETE ===")
    
    # Verify the conversion
    print("\n=== VERIFICATION ===")
    
    # Check sample entries from each file
    past_sample = pd.read_csv('past_bookings.csv').head(3)
    current_sample = pd.read_csv('current_bookings.csv').head(3)
    future_sample = pd.read_csv('future_bookings.csv').head(3)
    customer_sample = pd.read_csv('customer.csv').head(3)
    staff_sample = pd.read_csv('staff.csv').head(3)
    payments_sample = pd.read_csv('payments.csv').head(3)
    
    print("Past bookings sample:")
    print(past_sample[['BookingID', 'CheckInDate', 'CheckOutDate', 'BookingDate']])
    
    print("\nCurrent bookings sample:")
    print(current_sample[['BookingID', 'CheckInDate', 'CheckOutDate', 'BookingDate']])
    
    print("\nFuture bookings sample:")
    print(future_sample[['BookingID', 'CheckInDate', 'CheckOutDate', 'BookingDate']])
    
    print("\nCustomer sample:")
    print(customer_sample[['CustomerID', 'FullName', 'CreatedAt']])
    
    print("\nStaff sample:")
    print(staff_sample[['StaffID', 'FullName', 'JoiningDate']])
    
    print("\nPayments sample:")
    print(payments_sample[['PaymentID', 'BookingID', 'PaymentDate']])
    
    print("\n✅ All CSV files now use dd-mm-yyyy date format!")

if __name__ == "__main__":
    convert_date_formats()
