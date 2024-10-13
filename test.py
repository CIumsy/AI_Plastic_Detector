import streamlit as st
import os
import cv2
from ultralytics import YOLO

def main():
    st.title("Local Object Detection Demo")

    # Display the upload file dialog
    uploaded_file = st.file_uploader("Choose an image", type=["jpg", "jpeg", "png"])

    if uploaded_file is not None:
        # Save the uploaded image
        os.makedirs('static/uploads', exist_ok=True)
        image_path = os.path.join('static/uploads', uploaded_file.name)
        with open(image_path, "wb") as f:
            f.write(uploaded_file.getbuffer())

        # Run YOLO detection
        model = YOLO('best.pt')
        results = model.predict(image_path, save=True)

        # Display the detected image
        result_image_path = results[0].path
        st.image(result_image_path, use_column_width=True)

if __name__ == '__main__':
    main()
