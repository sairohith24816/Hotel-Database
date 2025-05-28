#!/usr/bin/env python3
"""
Script to create curr_bookings_sorted.csv
Sorts current_bookings.csv by Room ID
"""

import pandas as pd
import os

def sort_bookings_by_room_id():
    """Sort current bookings by Room ID and create new CSV file"""
    
    # File paths
    input_file = r"c:\Users\sairo\Desktop\Hotel-Database\Data\current_bookings.csv"
    output_file = r"c:\Users\sairo\Desktop\Hotel-Database\Data\curr_bookings_sorted.csv"
    
    try:
        # Read the current bookings CSV
        print("📖 Reading current_bookings.csv...")
        df = pd.read_csv(input_file)
        print(f"✅ Loaded {len(df)} records")
        
        # Sort by RoomID
        print("🔄 Sorting by Room ID...")
        df_sorted = df.sort_values('RoomID')
        
        # Reset index to maintain clean sequential order
        df_sorted = df_sorted.reset_index(drop=True)
        
        # Save to new CSV file
        print(f"💾 Saving sorted data to curr_bookings_sorted.csv...")
        df_sorted.to_csv(output_file, index=False)
        
        print(f"✅ Successfully created curr_bookings_sorted.csv")
        print(f"📊 Total records: {len(df_sorted)}")
        
        # Display first few records to verify sorting
        print(f"\n📋 First 10 records (sorted by Room ID):")
        print("="*80)
        for i in range(min(10, len(df_sorted))):
            row = df_sorted.iloc[i]
            print(f"Room {row['RoomID']:3d} | {row['BookingID']} | Customer {row['CustomerID']} | {row['CheckInDate']} to {row['CheckOutDate']}")
        
        # Display last few records to show range
        print(f"\n📋 Last 10 records (sorted by Room ID):")
        print("="*80)
        for i in range(max(0, len(df_sorted)-10), len(df_sorted)):
            row = df_sorted.iloc[i]
            print(f"Room {row['RoomID']:3d} | {row['BookingID']} | Customer {row['CustomerID']} | {row['CheckInDate']} to {row['CheckOutDate']}")
        
        # Show room ID range
        min_room = df_sorted['RoomID'].min()
        max_room = df_sorted['RoomID'].max()
        print(f"\n🏨 Room ID Range: {min_room} to {max_room}")
        
        return True
        
    except Exception as e:
        print(f"❌ Error: {str(e)}")
        return False

if __name__ == "__main__":
    print("🏨 CREATING SORTED CURRENT BOOKINGS FILE")
    print("="*50)
    
    success = sort_bookings_by_room_id()
    
    if success:
        print(f"\n🎉 File created successfully!")
        print(f"📁 Location: c:\\Users\\sairo\\Desktop\\Hotel-Database\\Data\\curr_bookings_sorted.csv")
    else:
        print(f"\n❌ Failed to create sorted file")
