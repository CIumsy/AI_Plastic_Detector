import streamlit as st
import os
import zipfile
import cv2
import numpy as np  # Import numpy to handle image arrays
from ultralytics import YOLO

def main():
    st.title("Plastic Detection and Annotation Tool")  # Updated title

    # Display the upload file dialog for multiple images
    uploaded_files = st.file_uploader("Choose images", type=["jpg", "jpeg", "png"], accept_multiple_files=True)

    if uploaded_files:
        result_images = []  # To store processed images for zip

        # Load the YOLO model
        model = YOLO('best.pt')

        # Process each uploaded image
        for uploaded_file in uploaded_files:
            # Read the uploaded image into memory
            image = cv2.imdecode(np.frombuffer(uploaded_file.read(), np.uint8), cv2.IMREAD_COLOR)

            # Run YOLO detection on the image (do not save automatically)
            results = model.predict(image, save=False)

            # Extract the annotated image from results and convert it to RGB format for Streamlit
            annotated_image = results[0].plot()  # Get the annotated image
            annotated_image_rgb = cv2.cvtColor(annotated_image, cv2.COLOR_BGR2RGB)

            # Save the annotated image temporarily to display
            result_images.append(annotated_image_rgb)

            # Display the annotated image
            st.image(annotated_image_rgb, caption=uploaded_file.name, use_column_width=True)

        # Create a zip file of annotated images
        zip_filename = "annotated_images.zip"
        with zipfile.ZipFile(zip_filename, 'w') as zipf:
            for i, uploaded_file in enumerate(uploaded_files):
                # Save the annotated image to a temporary file to zip
                temp_image_path = f"static/annotated_{uploaded_file.name}"
                cv2.imwrite(temp_image_path, result_images[i])
                zipf.write(temp_image_path, os.path.basename(temp_image_path))

        # Provide a download link for the zip file
        with open(zip_filename, 'rb') as f:
            st.download_button("Download Annotated Images", data=f, file_name=zip_filename)

if __name__ == '__main__':
    main()
