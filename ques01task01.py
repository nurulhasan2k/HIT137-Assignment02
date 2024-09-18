import pandas as pd

csv_paths = ['CSV1.csv', 'CSV2.csv', 'CSV3.csv', 'CSV4.csv']

combined_text = ''

# Loop through each CSV file and extract the text
for csv_path in csv_paths:
    try:
        df = pd.read_csv(csv_path)
        # Assuming the text data is stored in a column named 'TEXT' or 'SHORT-TEXT'
        if 'TEXT' in df.columns:
            combined_text += ' '.join(df['TEXT'].dropna()) + '\n'
        elif 'SHORT-TEXT' in df.columns:
            combined_text += ' '.join(df['SHORT-TEXT'].dropna()) + '\n'
    except Exception as e:
        combined_text += f"Error reading {csv_path}: {str(e)}\n"

# Save the combined text into a .txt file
with open('q1Output_combinedText.txt', 'w') as f:
    f.write(combined_text)

print("Text successfully combined and saved to 'q1Output_combinedText.txt'")