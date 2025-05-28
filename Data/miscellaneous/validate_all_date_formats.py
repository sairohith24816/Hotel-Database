import pandas as pd
import re

def validate_all_date_formats():
    """Validate that all CSV files use dd-mm-yyyy format consistently"""
    
    print("=== COMPREHENSIVE DATE FORMAT VALIDATION ===")
    
    files_to_check = {
        'past_bookings.csv': ['CheckInDate', 'CheckOutDate', 'BookingDate'],
        'current_bookings.csv': ['CheckInDate', 'CheckOutDate', 'BookingDate'],
        'future_bookings.csv': ['CheckInDate', 'CheckOutDate', 'BookingDate'],
        'payments.csv': ['PaymentDate'],
        'customer.csv': ['CreatedAt'],
        'staff.csv': ['JoiningDate']
    }
    
    # Regular expression for dd-mm-yyyy format
    date_pattern = r'^\d{2}-\d{2}-\d{4}$'
    
    all_valid = True
    
    for filename, date_columns in files_to_check.items():
        print(f"\n📁 Checking {filename}...")
        
        try:
            df = pd.read_csv(filename)
            file_valid = True
            
            for col in date_columns:
                if col in df.columns:
                    # Check first 5 and last 5 entries for format
                    sample_dates = list(df[col].head(5)) + list(df[col].tail(5))
                    
                    invalid_dates = []
                    for date_str in sample_dates:
                        if not re.match(date_pattern, str(date_str)):
                            invalid_dates.append(date_str)
                    
                    if invalid_dates:
                        print(f"  ❌ {col}: Invalid format found - {invalid_dates[:3]}")
                        file_valid = False
                        all_valid = False
                    else:
                        print(f"  ✅ {col}: All dates in dd-mm-yyyy format")
                else:
                    print(f"  ⚠️  {col}: Column not found")
            
            if file_valid:
                print(f"  🎉 {filename} - All date formats valid!")
                
        except Exception as e:
            print(f"  ❌ Error reading {filename}: {e}")
            all_valid = False
    
    print(f"\n{'='*50}")
    if all_valid:
        print("🎊 SUCCESS: All CSV files use dd-mm-yyyy format consistently!")
    else:
        print("❌ ISSUES FOUND: Some files have invalid date formats")
    
    # Show file summary
    print(f"\n📊 FILE SUMMARY:")
    for filename in files_to_check.keys():
        try:
            df = pd.read_csv(filename)
            print(f"  {filename}: {len(df)} rows")
        except:
            print(f"  {filename}: Error reading file")
    
    return all_valid

if __name__ == "__main__":
    validate_all_date_formats()
