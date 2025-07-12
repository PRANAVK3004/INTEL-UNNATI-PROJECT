import pandas as pd
import qrcode
import os

# Load dataset
df = pd.read_csv('pcb_data.csv')

# Output folder
output_dir = 'qr_labels'
os.makedirs(output_dir, exist_ok=True)

# Generate QR code for each row
for idx, row in df.iterrows():
    # Customize the data string in QR code
    qr_data = f"PCB ID: {row['PCB_ID']}\nComponent: {row['Component_Name']}\nSerial: {row['Serial_Number']}"

    # Generate QR code
    qr_img = qrcode.make(qr_data)

    # Save as image
    filename = f"{output_dir}/{row['PCB_ID']}_label.png"
    qr_img.save(filename)

    print(f"Saved: {filename}")
