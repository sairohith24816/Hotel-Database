# Payment Table Summary

## Overview
Successfully created a comprehensive payment table (`payments.csv`) that corresponds to all booking entries across past, current, and future bookings.

## File Structure

### payments.csv
- **Total Rows**: 3,233 entries
- **PaymentID Range**: P0000001 to P0003233
- **Date Format**: dd-mm-yyyy (as requested)

## Column Structure
- `PaymentID` (PK) - Format: P + 7-digit number
- `BookingID` (FK) - Links to booking entries
- `Amount` - Calculated as: Room Cost × Number of Days Stayed
- `PaymentDate` - Random selection from BookingDate, CheckInDate, or CheckOutDate
- `PaymentMethod` - Random selection from: Cash, Card, UPI, Online
- `Status` - Based on payment timing rules

## Payment Logic Implementation

### 1. Past Bookings (2,000 payments)
- **Payment Date**: Random from booking/checkin/checkout dates
- **Status**: All "Success" ✅
- **Amount Range**: ₹1,500 - ₹270,000

### 2. Current Bookings (733 payments)
- **Payment Date**: Random from booking/checkin/checkout dates
- **Status Logic**:
  - If payment date = booking date → "Success"
  - If payment date = checkin date → "Success"
  - If payment date = checkout date → "Pending"
- **Results**: 498 Success, 235 Pending

### 3. Future Bookings (500 payments)
- **Payment Date**: Random from booking/checkin/checkout dates
- **Status Logic**:
  - If payment date = booking date → "Success"
  - If payment date = checkin/checkout date → "Pending"
- **Results**: 159 Success, 341 Pending

## Room Cost Structure
Based on room type determined by RoomID pattern:
- **Presidential Suite** (X00): ₹10,000/night
- **Suite** (X01-X10): ₹6,000/night
- **Deluxe** (X11-X20): ₹4,000/night
- **Single** (X21-X40): ₹1,500/night
- **Double** (X41-X99): ₹2,500/night

## Payment Statistics
- **Total Payments**: 3,233
- **Success Status**: 2,657 (82.2%)
- **Pending Status**: 576 (17.8%)
- **Average Amount**: ₹20,691.77
- **Min Amount**: ₹1,500 (1 night Single room)
- **Max Amount**: ₹270,000 (27 nights Presidential suite)

## Payment Method Distribution
- **Online**: 828 payments
- **UPI**: 812 payments
- **Cash**: 802 payments
- **Card**: 791 payments

## Data Validation ✅
- ✅ All amounts are positive (minimum 1 day billing)
- ✅ Sequential PaymentID continuity
- ✅ One-to-one mapping with bookings
- ✅ Date format consistency (dd-mm-yyyy)
- ✅ Status logic correctly implemented
- ✅ Payment methods evenly distributed

## Sample Entries
```csv
PaymentID,BookingID,Amount,PaymentDate,PaymentMethod,Status
P0000001,B0000001,12500,16-01-2024,Cash,Success
P0000002,B0000002,9000,01-01-2024,UPI,Success
P0003232,B0003232,6000,31-07-2025,UPI,Pending
P0003233,B0003233,4000,31-07-2025,Card,Pending
```

## Relationships
- **1:1 Relationship** with Booking table (one payment per booking)
- **Foreign Key**: BookingID links to respective booking files
- **Referential Integrity**: All BookingIDs exist in booking tables
