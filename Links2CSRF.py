import csv

def process_csv(input_csv, output_txt):
    # processed_data = set()  # Use a set to store unique values
    output_data = []  # List to maintain the order of processed entries
    
    with open(input_csv, mode='r', newline='') as csvfile:
        reader = csv.reader(csvfile)
        
        for row in reader:
            if row and row[0]:  # Check if row is not empty and first column is not empty
                column_data = row[0]
                processed_string = ''
                
                for char in column_data:
                    if char in ['?', '(', ' ', '{']:
                        break
                    processed_string += char
                
                processed_string = processed_string.lower()  # Lowercase the string
                
                if not processed_string.startswith('/'):
                    processed_string = '/' + processed_string
                
                processed_string = processed_string.replace('//', '/')
                
                if processed_string.endswith('/'):
                    processed_string = processed_string[:-1]
                
                # if processed_string not in processed_data:
                #     processed_data.add(processed_string)
                #     # output_data.append(processed_string)

                if processed_string not in output_data:
                    output_data.append(processed_string)
    
    with open(output_txt, mode='w') as txtfile:
        for item in output_data:
            txtfile.write(f'"{item}",\n')


# Usage
input_csv = 'input.csv'  # Replace with your input CSV file path
output_txt = 'output.txt'  # Replace with your desired output TXT file path
process_csv(input_csv, output_txt)
