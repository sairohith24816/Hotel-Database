import pandas as pd
import os

def update_pending_payment_methods(file_path):
    """
    Update payment method to 'Unknown' for all records with status 'Pending'
    
    Args:
        file_path (str): Path to the payments CSV file
    """
    # Read the CSV file
    df = pd.read_csv(file_path)
    
    print(f"Processing file: {os.path.basename(file_path)}")
    print(f"Total records: {len(df)}")
    
    # Check current status distribution
    print("\nCurrent status distribution:")
    print(df['Status'].value_counts())
    
    # Find records with Pending status
    pending_mask = df['Status'] == 'Pending'
    pending_count = pending_mask.sum()
    
    print(f"\nRecords with Pending status: {pending_count}")
    
    if pending_count > 0:
        # Show current payment methods for pending records
        print("\nCurrent payment methods for Pending records:")
        pending_payment_methods = df[pending_mask]['PaymentMethod'].value_counts()
        print(pending_payment_methods)
        
        # Update payment method to 'Unknown' for pending records
        df.loc[pending_mask, 'PaymentMethod'] = 'Unknown'
        
        # Show updated payment methods for pending records
        print("\nAfter update - Payment methods for Pending records:")
        updated_payment_methods = df[pending_mask]['PaymentMethod'].value_counts()
        print(updated_payment_methods)
        
        # Save the updated data back to the file
        df.to_csv(file_path, index=False)
        print(f"\nFile updated successfully: {file_path}")
        
        # Verification
        print("\nVerification - Final status of pending records:")
        verification_df = pd.read_csv(file_path)
        pending_verification = verification_df[verification_df['Status'] == 'Pending']
        print(f"Pending records count: {len(pending_verification)}")
        print("Payment methods for pending records:")
        print(pending_verification['PaymentMethod'].value_counts())
        
    else:
        print("No pending records found to update.")
    
    print("-" * 60)

def main():
    """Main function to update the payments CSV file."""
    file_path = r"c:\Users\sairo\Desktop\Hotel-Database\Data\payments.csv"
    
    print("Updating payment methods for pending records...")
    print("=" * 60)
    
    update_pending_payment_methods(file_path)
    
    print("\nUpdate complete!")

if __name__ == "__main__":
    main()
