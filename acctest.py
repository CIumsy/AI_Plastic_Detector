import streamlit as st
import os
import cv2
from ultralytics import YOLO
import matplotlib.pyplot as plt
import numpy as np

def evaluate_model_on_test_images(model, test_images_path):
    accuracy_scores = []
    image_files = [f for f in os.listdir(test_images_path) if f.endswith(('.jpg', '.jpeg', '.png'))]

    for image_file in image_files:
        image_path = os.path.join(test_images_path, image_file)
        results = model.predict(image_path)

        # YOLO output handling - access confidence scores from results[0].boxes.conf
        if len(results) > 0:
            confidences = results[0].boxes.conf.cpu().numpy()  # Convert to numpy for easier handling
            accuracy = np.mean(confidences) if len(confidences) > 0 else 0
        else:
            accuracy = 0  # No predictions were made
        
        accuracy_scores.append(accuracy)

    return accuracy_scores, image_files

def plot_accuracy_graph(accuracy_scores, image_files):
    fig, ax = plt.subplots()
    ax.plot(image_files, accuracy_scores, marker='o', linestyle='-', color='b')
    ax.set_xlabel('Image')
    ax.set_ylabel('Accuracy (Confidence Score)')
    ax.set_title('Model Accuracy Across Test Images')
    ax.grid(True)
    plt.xticks(rotation=45, ha='right')
    st.pyplot(fig)

def main():
    st.title("YOLO Model Accuracy Graph for Plastic Detection")

    # Select folder containing test images
    test_images_path = st.text_input("Test\Test Runs\Run 7")

    # Check if the path exists
    if os.path.exists(test_images_path):
        st.write(f"Found {len(os.listdir(test_images_path))} test images.")

        # Load pre-trained YOLO model
        model = YOLO('best.pt')

        # Evaluate the model on the test images
        accuracy_scores, image_files = evaluate_model_on_test_images(model, test_images_path)

        # Display the graph of accuracy scores
        plot_accuracy_graph(accuracy_scores, image_files)
    else:
        st.error(f"Directory '{test_images_path}' not found. Please enter a valid path.")

if __name__ == '__main__':
    main()
