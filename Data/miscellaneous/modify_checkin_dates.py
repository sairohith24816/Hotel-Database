import pandas as pd
import random
import os

def modify_checkin_dates(file_path, percentage=0.1):
    """
    Modify the check-in date to match the booking date for a random percentage of records.
    
    Args:
        file_path (str): Path to the CSV file
        percentage (float): Percentage of records to modify (default 0.1 for 10%)
    """
    # Read the CSV file
    df = pd.read_csv(file_path)
    
    # Calculate number of records to modify
    total_records = len(df)
    records_to_modify = int(total_records * percentage)
    
    print(f"File: {os.path.basename(file_path)}")
    print(f"Total records: {total_records}")
    print(f"Records to modify (10%): {records_to_modify}")
    
    # Randomly select indices to modify
    random.seed(42)  # For reproducible results
    indices_to_modify = random.sample(range(total_records), records_to_modify)
    
    # Create a backup of original data for verification
    original_checkin_dates = df.loc[indices_to_modify, 'CheckInDate'].copy()
    booking_dates = df.loc[indices_to_modify, 'BookingDate'].copy()
    
    # Modify the check-in dates to match booking dates
    df.loc[indices_to_modify, 'CheckInDate'] = df.loc[indices_to_modify, 'BookingDate']
    
    # Print some examples of changes
    print("\nExamples of modifications:")
    print("BookingID | Original CheckIn | New CheckIn (=BookingDate)")
    print("-" * 55)
    for i, idx in enumerate(indices_to_modify[:5]):  # Show first 5 examples
        booking_id = df.loc[idx, 'BookingID']
        original_checkin = original_checkin_dates.iloc[i]
        new_checkin = df.loc[idx, 'CheckInDate']
        print(f"{booking_id} | {original_checkin} | {new_checkin}")
    
    if records_to_modify > 5:
        print(f"... and {records_to_modify - 5} more records")
    
    # Save the modified data back to the file
    df.to_csv(file_path, index=False)
    print(f"\nFile saved successfully: {file_path}")
    print("-" * 60)
    
    return records_to_modify

def main():
    """Main function to modify both CSV files."""
    base_path = r"c:\Users\sairo\Desktop\Hotel-Database\Data"
    
    current_bookings_path = os.path.join(base_path, "current_bookings.csv")
    past_bookings_path = os.path.join(base_path, "past_bookings.csv")
    
    print("Modifying check-in dates to match booking dates for 10% of records...")
    print("=" * 60)
    
    # Modify current bookings
    current_modified = modify_checkin_dates(current_bookings_path)
    
    # Modify past bookings
    past_modified = modify_checkin_dates(past_bookings_path)
    
    print(f"\nSUMMARY:")
    print(f"Current bookings modified: {current_modified} records")
    print(f"Past bookings modified: {past_modified} records")
    print(f"Total records modified: {current_modified + past_modified}")
    print("\nModification complete!")

if __name__ == "__main__":
    main()
