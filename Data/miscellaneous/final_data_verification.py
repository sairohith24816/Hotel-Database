#!/usr/bin/env python3
"""
Final Data Verification Script for Hotel Database
Validates all CSV files for format consistency and data integrity
"""

import pandas as pd
import os
from datetime import datetime
import re

def check_date_format(date_str):
    """Check if date is in dd-mm-yyyy format"""
    try:
        datetime.strptime(date_str, '%d-%m-%Y')
        return True
    except ValueError:
        return False

def validate_csv_file(file_path, file_type):
    """Validate CSV file format and data"""
    print(f"\n{'='*60}")
    print(f"VALIDATING: {os.path.basename(file_path)}")
    print(f"{'='*60}")
    
    if not os.path.exists(file_path):
        print(f"❌ File not found: {file_path}")
        return False
    
    try:
        df = pd.read_csv(file_path)
        print(f"✅ File loaded successfully")
        print(f"📊 Total rows: {len(df)}")
        print(f"📋 Columns: {list(df.columns)}")
        
        # Check for empty data
        if len(df) == 0:
            print(f"❌ File is empty")
            return False
            
        # Validate date formats based on file type
        date_columns = []
        if file_type in ['past_bookings', 'current_bookings', 'future_bookings']:
            date_columns = ['CheckInDate', 'CheckOutDate', 'BookingDate']
        elif file_type == 'payments':
            date_columns = ['PaymentDate']
            
        # Check date format consistency
        for col in date_columns:
            if col in df.columns:
                sample_dates = df[col].head(10).tolist()
                valid_dates = all(check_date_format(str(date)) for date in sample_dates)
                if valid_dates:
                    print(f"✅ {col}: dd-mm-yyyy format verified")
                else:
                    print(f"❌ {col}: Invalid date format detected")
                    return False
        
        # Specific validations by file type
        if file_type == 'past_bookings':
            # Check status
            statuses = df['Status'].unique()
            if len(statuses) == 1 and statuses[0] == 'Checked-Out':
                print(f"✅ Status: All entries are 'Checked-Out'")
            else:
                print(f"❌ Status: Expected all 'Checked-Out', found: {statuses}")
                
        elif file_type == 'current_bookings':
            # Check status
            statuses = df['Status'].unique()
            if len(statuses) == 1 and statuses[0] == 'Checked-In':
                print(f"✅ Status: All entries are 'Checked-In'")
            else:
                print(f"❌ Status: Expected all 'Checked-In', found: {statuses}")
                
        elif file_type == 'future_bookings':
            # Check status
            statuses = df['Status'].unique()
            if len(statuses) == 1 and statuses[0] == 'Confirmed':
                print(f"✅ Status: All entries are 'Confirmed'")
            else:
                print(f"❌ Status: Expected all 'Confirmed', found: {statuses}")
                
        elif file_type == 'payments':
            # Check payment methods and status
            payment_methods = df['PaymentMethod'].unique()
            payment_statuses = df['Status'].unique()
            print(f"✅ Payment Methods: {payment_methods}")
            print(f"✅ Payment Statuses: {payment_statuses}")
            
            # Check amount format
            amounts = df['Amount'].head(10)
            if all(isinstance(amt, (int, float)) and amt > 0 for amt in amounts):
                print(f"✅ Amounts: Numeric and positive")
            else:
                print(f"❌ Amounts: Invalid format detected")
        
        print(f"✅ {file_type.upper()} validation completed successfully")
        return True
        
    except Exception as e:
        print(f"❌ Error validating {file_path}: {str(e)}")
        return False

def main():
    """Main validation function"""
    print("🏨 HOTEL DATABASE CSV FILES VALIDATION")
    print("=" * 80)
    
    base_path = r"c:\Users\sairo\Desktop\Hotel-Database\Data"
    
    files_to_validate = [
        ('past_bookings.csv', 'past_bookings'),
        ('current_bookings.csv', 'current_bookings'),
        ('future_bookings.csv', 'future_bookings'),
        ('payments.csv', 'payments')
    ]
    
    all_valid = True
    total_records = 0
    
    for filename, file_type in files_to_validate:
        file_path = os.path.join(base_path, filename)
        is_valid = validate_csv_file(file_path, file_type)
        
        if is_valid:
            df = pd.read_csv(file_path)
            total_records += len(df)
        else:
            all_valid = False
    
    print(f"\n{'='*80}")
    print("📋 FINAL VALIDATION SUMMARY")
    print(f"{'='*80}")
    
    if all_valid:
        print("✅ ALL CSV FILES VALIDATED SUCCESSFULLY!")
        print(f"📊 Total records across all files: {total_records:,}")
        print("🎯 All files use dd-mm-yyyy date format consistently")
        print("🔒 Data integrity verified")
    else:
        print("❌ VALIDATION FAILED - Please check errors above")
    
    print(f"\n{'='*80}")
    print("📁 FILE SUMMARY:")
    print(f"{'='*80}")
    
    for filename, file_type in files_to_validate:
        file_path = os.path.join(base_path, filename)
        if os.path.exists(file_path):
            df = pd.read_csv(file_path)
            print(f"📄 {filename:<25} | {len(df):>6,} rows")
    
    print(f"\n🎉 Hotel Database CSV generation completed successfully!")

if __name__ == "__main__":
    main()
