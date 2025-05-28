import pandas as pd

# Load and validate future bookings
df = pd.read_csv('future_bookings.csv')

print("=== FUTURE BOOKINGS VALIDATION ===")
print(f"Total rows: {len(df)}")
print(f"BookingID range: {df['BookingID'].iloc[0]} to {df['BookingID'].iloc[-1]}")
print(f"Date range: {df['BookingDate'].min()} to {df['CheckOutDate'].max()}")

# Parse dates
df['BookingDateParsed'] = pd.to_datetime(df['BookingDate'], format='%d-%m-%Y')
df['CheckInDateParsed'] = pd.to_datetime(df['CheckInDate'], format='%d-%m-%Y')
df['CheckOutDateParsed'] = pd.to_datetime(df['CheckOutDate'], format='%d-%m-%Y')

# Validate date constraints
valid_dates = (df['BookingDateParsed'] < df['CheckInDateParsed']) & (df['CheckInDateParsed'] < df['CheckOutDateParsed'])
print(f"\nDate constraints validation:")
print(f"All constraints valid: {valid_dates.all()}")
print(f"Valid entries: {valid_dates.sum()}/{len(df)}")

# Check date ranges
print(f"\nDate ranges check:")
print(f"All booking dates in Jun-Jul 2025: {df['BookingDateParsed'].dt.year.eq(2025).all() and df['BookingDateParsed'].dt.month.isin([6,7]).all()}")
print(f"All checkin dates in Jun-Jul 2025: {df['CheckInDateParsed'].dt.year.eq(2025).all() and df['CheckInDateParsed'].dt.month.isin([6,7]).all()}")
print(f"All checkout dates in Jun-Jul 2025: {df['CheckOutDateParsed'].dt.year.eq(2025).all() and df['CheckOutDateParsed'].dt.month.isin([6,7]).all()}")

print(f"\nSample entries:")
print(df[['BookingID', 'CustomerID', 'RoomID', 'CheckInDate', 'CheckOutDate', 'BookingDate', 'NumberOfGuests', 'Status']].head())

print(f"\nLast 5 entries:")
print(df[['BookingID', 'CustomerID', 'RoomID', 'CheckInDate', 'CheckOutDate', 'BookingDate', 'NumberOfGuests', 'Status']].tail())
