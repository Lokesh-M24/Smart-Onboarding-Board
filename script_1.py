# Create the main dashboard.py file
dashboard_code = """
'''
Smart Onboarding InfoBoard - Interactive Welcome Display for New Joiners
Author: Expert Python Developer
Description: A rotating display application that shows welcome messages and QR codes
             for new employees. Auto-rotates slides every few seconds.
'''

import cv2
import numpy as np
import time
import os
import qrcode
from PIL import Image, ImageDraw, ImageFont
import threading

class OnboardingInfoBoard:
    def __init__(self, content_file="content.txt", qr_image="lms_qr.png"):
        self.content_file = content_file
        self.qr_image = qr_image
        self.messages = []
        self.qr_links = []
        self.slide_duration = 5  # seconds per slide
        self.current_slide = 0
        self.window_name = "Smart Onboarding InfoBoard"
        
        # Display settings
        self.width = 1200
        self.height = 800
        self.font_scale = 1.5
        self.font_thickness = 2
        self.font = cv2.FONT_HERSHEY_SIMPLEX
        
        # Colors (BGR format)
        self.bg_color = (240, 248, 255)  # Alice Blue
        self.text_color = (47, 79, 79)   # Dark Slate Gray
        self.header_color = (25, 25, 112)  # Midnight Blue
        self.accent_color = (0, 191, 255)  # Deep Sky Blue
        
    def load_content(self):
        '''Load messages and QR links from content file'''
        try:
            if not os.path.exists(self.content_file):
                self.create_default_content()
            
            with open(self.content_file, 'r', encoding='utf-8') as f:
                lines = f.readlines()
            
            self.messages = []
            self.qr_links = []
            
            current_section = None
            for line in lines:
                line = line.strip()
                if line.startswith('[MESSAGES]'):
                    current_section = 'messages'
                elif line.startswith('[QR_LINKS]'):
                    current_section = 'qr_links'
                elif line and not line.startswith('#') and current_section:
                    if current_section == 'messages':
                        self.messages.append(line)
                    elif current_section == 'qr_links':
                        parts = line.split('|')
                        if len(parts) == 2:
                            self.qr_links.append({'title': parts[0], 'url': parts[1]})
            
            if not self.messages:
                self.messages = ["Welcome to our company!", "Hope you have a great journey with us!"]
            
            if not self.qr_links:
                self.qr_links = [{'title': 'Company LMS', 'url': 'https://company-lms.example.com'}]
                
        except Exception as e:
            print(f"Error loading content: {e}")
            self.messages = ["Welcome to our company!", "Hope you have a great journey with us!"]
            self.qr_links = [{'title': 'Company LMS', 'url': 'https://company-lms.example.com'}]
    
    def create_default_content(self):
        '''Create a default content.txt file if it doesn't exist'''
        default_content = '''# Smart Onboarding InfoBoard Content File
# Add your welcome messages under [MESSAGES]
# Add QR code links under [QR_LINKS] in format: Title|URL

[MESSAGES]
Welcome to TechCorp! We're excited to have you join our team!
Don't forget to complete your onboarding checklist
Your manager will reach out to you within 24 hours
Building tour starts at 10 AM - meet at reception
Join us for lunch at 12:30 PM in the cafeteria
Visit our Learning Management System for training modules
IT Helpdesk is available 24/7 for technical support
Ask questions, explore, and make yourself at home!

[QR_LINKS]
Company LMS|https://lms.company.com
IT Helpdesk|https://helpdesk.company.com
Employee Portal|https://portal.company.com
'''
        try:
            with open(self.content_file, 'w', encoding='utf-8') as f:
                f.write(default_content)
            print(f"Created default {self.content_file}")
        except Exception as e:
            print(f"Error creating default content file: {e}")
    
    def generate_qr_codes(self):
        '''Generate QR code images for all links'''
        for i, qr_data in enumerate(self.qr_links):
            try:
                # Create QR code
                qr = qrcode.QRCode(
                    version=1,
                    error_correction=qrcode.constants.ERROR_CORRECT_L,
                    box_size=10,
                    border=4,
                )
                qr.add_data(qr_data['url'])
                qr.make(fit=True)
                
                # Create QR code image
                qr_img = qr.make_image(fill_color="black", back_color="white")
                
                # Save the QR code
                if i == 0:  # Save the first QR code as the main one
                    qr_img.save(self.qr_image)
                    
            except Exception as e:
                print(f"Error generating QR code: {e}")
    
    def create_slide(self, message_index):
        '''Create a slide with message and QR code'''
        # Create blank image
        slide = np.full((self.height, self.width, 3), self.bg_color, dtype=np.uint8)
        
        # Add header
        header_text = "Smart Onboarding InfoBoard"
        header_size = cv2.getTextSize(header_text, self.font, self.font_scale, self.font_thickness)[0]
        header_x = (self.width - header_size[0]) // 2
        cv2.putText(slide, header_text, (header_x, 80), self.font, self.font_scale, self.header_color, self.font_thickness)
        
        # Add separator line
        cv2.line(slide, (100, 120), (self.width - 100, 120), self.accent_color, 3)
        
        # Add main message
        if message_index < len(self.messages):
            message = self.messages[message_index]
            self.add_wrapped_text(slide, message, y_start=180)
        
        # Add QR code if exists
        if os.path.exists(self.qr_image):
            self.add_qr_code(slide)
        
        # Add slide counter
        counter_text = f"Slide {message_index + 1} of {len(self.messages)}"
        cv2.putText(slide, counter_text, (50, self.height - 30), cv2.FONT_HERSHEY_SIMPLEX, 0.7, self.text_color, 1)
        
        # Add timestamp
        timestamp = time.strftime("%Y-%m-%d %H:%M:%S")
        time_size = cv2.getTextSize(timestamp, cv2.FONT_HERSHEY_SIMPLEX, 0.7, 1)[0]
        cv2.putText(slide, timestamp, (self.width - time_size[0] - 50, self.height - 30), 
                   cv2.FONT_HERSHEY_SIMPLEX, 0.7, self.text_color, 1)
        
        return slide
    
    def add_wrapped_text(self, image, text, y_start=200, max_width=800):
        '''Add text with automatic word wrapping'''
        words = text.split()
        lines = []
        current_line = ""
        
        for word in words:
            test_line = current_line + " " + word if current_line else word
            text_size = cv2.getTextSize(test_line, self.font, self.font_scale, self.font_thickness)[0]
            
            if text_size[0] <= max_width:
                current_line = test_line
            else:
                if current_line:
                    lines.append(current_line)
                current_line = word
        
        if current_line:
            lines.append(current_line)
        
        # Draw lines
        line_height = 60
        for i, line in enumerate(lines):
            text_size = cv2.getTextSize(line, self.font, self.font_scale, self.font_thickness)[0]
            x = (self.width - text_size[0]) // 2
            y = y_start + (i * line_height)
            cv2.putText(image, line, (x, y), self.font, self.font_scale, self.text_color, self.font_thickness)
    
    def add_qr_code(self, slide):
        '''Add QR code to the slide'''
        try:
            # Load QR code image
            qr_cv_img = cv2.imread(self.qr_image)
            if qr_cv_img is None:
                return
            
            # Resize QR code
            qr_size = 200
            qr_resized = cv2.resize(qr_cv_img, (qr_size, qr_size))
            
            # Position QR code in bottom right
            x_pos = self.width - qr_size - 100
            y_pos = self.height - qr_size - 100
            
            # Add QR code to slide
            slide[y_pos:y_pos + qr_size, x_pos:x_pos + qr_size] = qr_resized
            
            # Add QR code label
            if self.qr_links:
                qr_label = f"Scan: {self.qr_links[0]['title']}"
                label_size = cv2.getTextSize(qr_label, cv2.FONT_HERSHEY_SIMPLEX, 0.8, 2)[0]
                label_x = x_pos + (qr_size - label_size[0]) // 2
                cv2.putText(slide, qr_label, (label_x, y_pos - 20), 
                           cv2.FONT_HERSHEY_SIMPLEX, 0.8, self.header_color, 2)
                
        except Exception as e:
            print(f"Error adding QR code: {e}")
    
    def run_display(self):
        '''Main display loop'''
        print("Starting Smart Onboarding InfoBoard...")
        print("Loading content...")
        self.load_content()
        
        print("Generating QR codes...")
        self.generate_qr_codes()
        
        print("Initializing display...")
        cv2.namedWindow(self.window_name, cv2.WINDOW_AUTOSIZE)
        
        # Make window stay on top (Windows specific)
        try:
            cv2.setWindowProperty(self.window_name, cv2.WND_PROP_TOPMOST, 1)
        except:
            pass
        
        print("InfoBoard is now running!")
        print("Press 'q' to quit, 'n' for next slide, 'p' for previous slide")
        
        last_slide_time = time.time()
        
        while True:
            # Create and display current slide
            slide = self.create_slide(self.current_slide)
            cv2.imshow(self.window_name, slide)
            
            # Handle keyboard input (non-blocking)
            key = cv2.waitKey(100) & 0xFF
            
            if key == ord('q') or key == 27:  # 'q' or ESC to quit
                break
            elif key == ord('n'):  # 'n' for next slide
                self.current_slide = (self.current_slide + 1) % len(self.messages)
                last_slide_time = time.time()
            elif key == ord('p'):  # 'p' for previous slide
                self.current_slide = (self.current_slide - 1) % len(self.messages)
                last_slide_time = time.time()
            elif key == ord('r'):  # 'r' to reload content
                print("Reloading content...")
                self.load_content()
                self.generate_qr_codes()
            
            # Auto-advance slides
            current_time = time.time()
            if current_time - last_slide_time >= self.slide_duration:
                self.current_slide = (self.current_slide + 1) % len(self.messages)
                last_slide_time = current_time
        
        cv2.destroyAllWindows()
        print("InfoBoard stopped. Thank you for using Smart Onboarding InfoBoard!")

def main():
    '''Main function to run the InfoBoard'''
    try:
        infoboard = OnboardingInfoBoard()
        infoboard.run_display()
    except KeyboardInterrupt:
        print("\\nInfoBoard stopped by user.")
    except Exception as e:
        print(f"Error running InfoBoard: {e}")
        input("Press Enter to exit...")

if __name__ == "__main__":
    main()
"""

# Save the dashboard.py file
with open("dashboard.py", "w", encoding="utf-8") as f:
    f.write(dashboard_code)

print("✅ Created dashboard.py")