# AI Plastic Detector

An AI-powered system for detecting plastic waste using drone images. By leveraging machine learning and the YOLO algorithm, the system identifies various types of plastic waste in real-time, enhancing waste management efficiency in hard-to-reach areas.

## Table of Contents

- [Introduction](#introduction)
- [Features](#features)
- [Installation](#installation)
- [Usage](#usage)
- [Contributing](#contributing)
- [License](#license)

## Introduction

Plastic waste is a major environmental issue that affects ecosystems worldwide. The AI Plastic Detector aims to address this problem by using advanced AI models to detect and classify plastic waste in real-time. This system leverages the YOLO (You Only Look Once) algorithm to provide accurate and efficient waste detection.

## Features

- **Real-time Detection**: Utilizes the YOLO algorithm for fast and accurate identification of plastic waste.
- **Image Upload**: Works by uploading drone images, which are then processed to mark detected plastic waste.
- **Machine Learning**: Trained on a diverse dataset of plastic waste images to improve detection accuracy.
- **Scalability**: Can be deployed in various environments, from urban areas to remote locations.

## Installation

To install and set up the AI Plastic Detector, follow these steps:

1. **Clone the repository**:
    ```bash
    git clone https://github.com/CIumsy/AI_Plastic_Detector.git
    cd AI_Plastic_Detector
    ```

2. **Create and activate a virtual environment (optional but recommended)**:
    ```bash
    python -m venv venv
    source venv/bin/activate  # On Windows, use `venv\Scripts\activate`
    ```

3. **Install the required dependencies**:
    ```bash
    pip install -r requirements.txt
    ```

## Usage

To use the AI Plastic Detector, navigate to the link: https://aiplasticdetector.streamlit.app/

Alternatively, to run the application locally, follow these steps:

1. **Run the detection script**:
    ```bash
    python detect_plastic.py --input <input_image_folder> --output <output_folder>
    ```

    Replace `<input_image_folder>` with the path to your folder containing drone images and `<output_folder>` with the desired path for the output images.

2. **View the results**:
    The output images will show the detected plastic waste with bounding boxes and labels.

## Contributing

We welcome contributions to the AI Plastic Detector project. If you have any ideas, suggestions, or improvements, feel free to submit a pull request or open an issue.

1. **Fork the repository**.
2. **Create a new branch**:
    ```bash
    git checkout -b feature-branch
    ```

3. **Make your changes and commit them**:
    ```bash
    git commit -m "Description of your changes"
    ```

4. **Push to the branch**:
    ```bash
    git push origin feature-branch
    ```

5. **Open a pull request**.

## License

This project is licensed under the MIT License. See the [LICENSE](LICENSE) file for more details.