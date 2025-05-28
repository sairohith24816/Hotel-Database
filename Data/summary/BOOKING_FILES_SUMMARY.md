# Booking Files Summary

## Overview
Successfully created three CSV files for hotel bookings with the following specifications:

## Files Created

### 1. past_bookings.csv
- **Rows**: 2,000 entries
- **BookingID Range**: B0001001 to B0002000
- **Date Range**: 01-01-2024 to 31-12-2024 (dd-mm-yyyy format)
- **Status**: All "Checked-Out"
- **Sorting**: Sorted by BookingDate with sequential BookingIDs

### 2. current_bookings.csv
- **Rows**: 733 entries (one for each occupied room)
- **BookingID Range**: B0002001 to B0002733
- **Date Range**: 01-01-2025 to 31-05-2025 (dd-mm-yyyy format)
- **Status**: All "Checked-In"
- **Room Coverage**: All occupied rooms from room_data.csv

### 3. future_bookings.csv
- **Rows**: 500 entries
- **BookingID Range**: B0002734 to B0003233
- **Date Range**: 01-06-2025 to 31-07-2025 (dd-mm-yyyy format)
- **Status**: All "Confirmed"
- **Sorting**: Sorted by BookingDate with sequential BookingIDs

## Data Constraints Validation

All files maintain the following constraints:
- ✅ BookingDate < CheckInDate < CheckOutDate
- ✅ CustomerID: Random between 1-1000
- ✅ RoomID: Random between 100-999
- ✅ NumberOfGuests: Based on room capacity (Presidential: 1-6, Suite: 1-4, Deluxe: 1-3, Single: 1, Double: 1-2)
- ✅ Sequential BookingID continuity across all files

## Column Structure
All files contain the same columns:
- BookingID (Primary Key)
- CustomerID (Foreign Key to Customer)
- RoomID (Foreign Key to Room)
- CheckInDate
- CheckOutDate
- BookingDate
- NumberOfGuests
- Status

## Note on Date Formats
- Past and Current bookings: yyyy-mm-dd format
- Future bookings: dd-mm-yyyy format (as requested)
