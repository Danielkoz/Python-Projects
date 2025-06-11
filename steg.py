import tkinter as tk
from tkinter import filedialog, messagebox
from PIL import Image, ImageTk
import tkinter.simpledialog

class SteganographyApp: # Creating the GUI
    def __init__(self):
        self.root = tk.Tk()
        self.root.title('Image Steganography')
        self.root.geometry('500x600')
        self.create_main_window()
    
    def create_main_window(self): # Clears the widgets
        for widget in self.root.winfo_children():
            widget.destroy()
            
        tk.Label(self.root, text='IMAGE STEGANOGRAPHY', # The home page title
                font=('courier', 20, 'bold')).pack(pady=10)
        
        tk.Button(self.root, text='Encoding an Image', # Button for encoding messages in images
                 command=self.encode_message, 
                 font=('courier', 12), width=20).pack(pady=5)
        
        tk.Button(self.root, text='Decoding an Image', # Button for decoding messages in images
                 command=self.decode_message, 
                 font=('courier', 12), width=20).pack(pady=5)
        
        tk.Label(self.root, text='☜(˚▽˚)☞',  # This is just for the home page design
                font=('courier', 40)).pack(pady=10)
        
    # This is just for the home page design as well
        art = '''⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⡿⠋⠁⠀⠀⠈⠉⠙⠻⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿
⣿⣿⣿⣿⣿⣿⣿⣿⣿⡟⠀⠀⠀⠀⠀⠀⠀⠀⠀⠈⠻⣿⣿⣿⣿⣿⣿⣿⣿⣿
⣿⣿⣿⣿⣿⣿⣿⣿⡟⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠈⢻⣿⣿⣿⣿⣿⣿⣿
⣿⣿⣿⣿⣿⣿⣿⡟⠀⠀⠀⠀⠀⢀⣠⣤⣤⣤⣤⣄⠀⠀⠀⠹⣿⣿⣿⣿⣿⣿
⣿⣿⣿⣿⣿⣿⣿⠁⠀⠀⠀⠀⠾⣿⣿⣿⣿⠿⠛⠉⠀⠀⠀⠀⠘⣿⣿⣿⣿⣿
⣿⣿⣿⣿⣿⣿⡏⠀⠀⠀⣤⣶⣤⣉⣿⣿⡯⣀⣴⣿⡗⠀⠀⠀⠀⣿⣿⣿⣿⣿
⣿⣿⣿⣿⣿⣿⡇⠀⠀⠀⡈⠀⠀⠉⣿⣿⣶⡉⠀⠀⣀⡀⠀⠀⠀⢻⣿⣿⣿⣿
⣿⣿⣿⣿⣿⣿⡇⠀⠀⠸⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⠇⠀⠀⠀⢸⣿⣿⣿⣿
⣿⣿⣿⣿⣿⣿⣿⠀⠀⠀⠉⢉⣽⣿⠿⣿⡿⢻⣯⡍⢁⠄⠀⠀⠀⣸⣿⣿⣿⣿
⣿⣿⣿⣿⣿⣿⣿⡄⠀⠀⠐⡀⢉⠉⠀⠠⠀⢉⣉⠀⡜⠀⠀⠀⠀⣿⣿⣿⣿⣿
⣿⣿⣿⣿⣿⣿⠿⠁⠀⠀⠀⠘⣤⣭⣟⠛⠛⣉⣁⡜⠀⠀⠀⠀⠀⠛⠿⣿⣿⣿
⡿⠟⠛⠉⠉⠀⠀⠀⠀⠀⠀⠀⠈⢻⣿⡀⠀⣿⠏⠀⠀⠀⠀⠀⠀⠀⠀⠀⠈⠉
⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠉⠁⠀⠁⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀'''
        
        tk.Label(self.root, text=art, 
                font=('courier', 20), justify='left').pack(pady=5)
    
    def encode_message(self): # Allowing only image files to be selected when encoding
        image_path = filedialog.askopenfilename(
            title="Select Image",
            filetypes=[('Image files', '*.png *.jpg *.jpeg')])
        
        if not image_path: # Exit the path if no image was selected
            return
            
        message = tk.simpledialog.askstring("Message", "Enter message to hide:") # User's input of their hidden message
        if not message:
            return
            
        try:
            img = Image.open(image_path) # Encoded message in the image
            encoded_img = self.encode_image(img, message)
            
            save_path = filedialog.asksaveasfilename(
                defaultextension=".png",
                filetypes=[('PNG files', '*.png')])
            
            if save_path: # Allows the user to save the encoded file
                encoded_img.save(save_path)
                messagebox.showinfo("Success", "Message hidden successfully!")
        except Exception as e: # Error if encoded incorrectly
            messagebox.showerror("Error", f"Encoding failed: {str(e)}")
    
    def decode_message(self): # Allowing only image files to be selected when decoding
        image_path = filedialog.askopenfilename(
            title="Select Image with Hidden Message",
            filetypes=[('Image files', '*.png *.jpg *.jpeg')])
        
        if not image_path: # Exits if a file wasn't selected
            return
            
        try:
            img = Image.open(image_path)
            message = self.decode_image(img)
            
            msg_window = tk.Toplevel(self.root) # The Decode Page
            msg_window.title("Hidden Message")
            msg_window.geometry("400x200")
            
            tk.Label(msg_window, text="Hidden Message:", # Title of the decode page
                    font=('Arial', 12, 'bold')).pack(pady=10)
            # The text widget
            text_widget = tk.Text(msg_window, height=8, width=50)
            text_widget.insert('1.0', message)
            text_widget.config(state='disabled') # Prevents the user to change the message (read-only)
            text_widget.pack(pady=10)
            
        except Exception as e: # Error message if the decoding fails
            messagebox.showerror("Error", f"Decoding failed: {str(e)}")
    
    def encode_image(self, img, message):
        # Encoding a message into an image using LSB (Least Significant Bit) steganography
        message += chr(0) 
        binary_message = ''.join(format(ord(char), '08b') for char in message) # Converts the characters to a 8 bit binary
        
        pixels = list(img.getdata()) # Collects the pixel data from image
        
        if len(binary_message) > len(pixels) * 3: # Checks if hidden message is too long for the image
            raise ValueError("Message too long for this image")
        
        # Encode message into pixels
        data_index = 0
        new_pixels = [] # Modified pixels
        
        for pixel in pixels: # Grayscale images coverted to RGB tuple
            if isinstance(pixel, int): 
                pixel = (pixel, pixel, pixel)
            
            new_pixel = list(pixel[:3])  # Take only RGB values
            
            # Modify RGB values
            for i in range(3):
                if data_index < len(binary_message):
                    # Set LSB to message bit
                    new_pixel[i] = (new_pixel[i] & 0xFE) | int(binary_message[data_index])
                    data_index += 1
            
            new_pixels.append(tuple(new_pixel)) # Modified pixel to new pixel
        
        # Create new image with the modified pixels
        new_img = Image.new(img.mode, img.size)
        new_img.putdata(new_pixels)
        return new_img
    
    def decode_image(self, img):
        pixels = list(img.getdata()) # Collects the pixel data from the original image
        binary_message = "" # Allows me to store the extracted binary data
        
        # Extract LSBs of each colour channel
        for pixel in pixels:
            if isinstance(pixel, int): 
                pixel = (pixel, pixel, pixel)

            # Only extracting the LSB
            for i in range(3): 
                binary_message += str(pixel[i] & 1) 
        
        # Convert binary to text
        message = ""
        for i in range(0, len(binary_message), 8): # Process 8 bits at a time 
            byte = binary_message[i:i+8]
            if len(byte) == 8: # Confirms if the bytes are accurate
                char = chr(int(byte, 2)) # Converts binary to character
                if char == chr(0):  
                    break
                message += char
        return message
    
    def run(self):
        self.root.mainloop() #starts the loop
# Runs the application
if __name__ == "__main__":
    app = SteganographyApp()
    app.run()