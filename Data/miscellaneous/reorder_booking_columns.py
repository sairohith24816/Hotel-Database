import pandas as pd
import os

def reorder_booking_columns(file_path):
    """
    Reorder columns in booking CSV files to the specified order:
    BookingID,CustomerID,RoomID,BookingDate,CheckInDate,CheckOutDate,NumberOfGuests,Status
    
    Args:
        file_path (str): Path to the CSV file
    """
    # Read the CSV file
    df = pd.read_csv(file_path)
    
    # Define the desired column order
    desired_order = [
        'BookingID',
        'CustomerID', 
        'RoomID',
        'BookingDate',
        'CheckInDate',
        'CheckOutDate',
        'NumberOfGuests',
        'Status'
    ]
    
    # Check if all required columns exist
    missing_columns = [col for col in desired_order if col not in df.columns]
    if missing_columns:
        print(f"Warning: Missing columns in {os.path.basename(file_path)}: {missing_columns}")
        return False
    
    # Get current column order
    current_order = list(df.columns)
    
    print(f"File: {os.path.basename(file_path)}")
    print(f"Current order: {current_order}")
    print(f"New order:     {desired_order}")
    
    # Reorder the columns
    df_reordered = df[desired_order]
    
    # Save the reordered data back to the file
    df_reordered.to_csv(file_path, index=False)
    print(f"✅ Successfully reordered columns in {os.path.basename(file_path)}")
    print("-" * 60)
    
    return True

def main():
    """Main function to reorder columns in all booking CSV files."""
    base_path = r"c:\Users\sairo\Desktop\Hotel-Database\Data"
    
    # List of booking CSV files to process
    booking_files = [
        "current_bookings.csv",
        "past_bookings.csv", 
        "future_bookings.csv",
        "curr_bookings_sorted.csv"
    ]
    
    print("Reordering columns in booking CSV files...")
    print("Target order: BookingID,CustomerID,RoomID,BookingDate,CheckInDate,CheckOutDate,NumberOfGuests,Status")
    print("=" * 60)
    
    successful_files = 0
    total_files = len(booking_files)
    
    for filename in booking_files:
        file_path = os.path.join(base_path, filename)
        
        # Check if file exists
        if not os.path.exists(file_path):
            print(f"⚠️ File not found: {filename}")
            continue
            
        # Reorder columns
        if reorder_booking_columns(file_path):
            successful_files += 1
    
    print(f"\nSUMMARY:")
    print(f"Successfully processed: {successful_files}/{total_files} files")
    print("Column reordering complete!")

if __name__ == "__main__":
    main()
