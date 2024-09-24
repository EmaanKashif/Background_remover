from rembg import remove
import easygui

# Define input and output paths correctly
input_path = r'C:\Users\LENOVO\python_directory\cat.png'  # Use a raw string
output_path = r'C:\Users\LENOVO\python_directory\output_img.png'  # Define where to save the output

try:
    # Open the input image as binary
    with open(input_path, 'rb') as input_file:
        input_image = input_file.read()

    # Remove the background
    output_image = remove(input_image)

    # Save the output image
    with open(output_path, 'wb') as output_file:
        output_file.write(output_image)

    # Notify the user of success
    easygui.msgbox(f"Background removed and saved to: {output_path}")

except Exception as e:
    # Display any error messages
    easygui.msgbox(f"An error occurred: {str(e)}")
