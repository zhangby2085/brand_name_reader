# Brand Name Extractor

A Streamlit-based web application that extracts brand names from images using Optical Character Recognition (OCR) technology. The application processes uploaded images, identifies potential brand names, and overlays the detected brand name on the image.

## Features

- Image upload support for JPG, JPEG, and PNG formats
- Automated brand name detection using OCR
- Visual display of both original and processed images
- Brand name overlay on the processed image
- User-friendly web interface

## Prerequisites

Before running this application, ensure you have the following installed:

- Python 3.6 or higher
- Tesseract OCR engine
- Required Python packages:
  ```
  streamlit
  opencv-python
  pytesseract
  Pillow
  numpy
  ```

## Installation

1. Clone this repository:
   ```bash
   git clone https://github.com/yourusername/brand-name-extractor.git
   cd brand-name-extractor
   ```

2. Install the required Python packages:
   ```bash
   pip install -r requirements.txt
   ```

3. Install Tesseract OCR:
   - **Windows**: Download and install from [Tesseract GitHub](https://github.com/UB-Mannheim/tesseract/wiki)
   - **Mac**: `brew install tesseract`
   - **Linux**: `sudo apt-get install tesseract-ocr`

4. Configure Tesseract path in the script:
   ```python
   pytesseract.pytesseract.tesseract_cmd = r'C:\Program Files\Tesseract-OCR\tesseract.exe'
   ```
   Adjust the path according to your installation location.

## Usage

1. Start the Streamlit application:
   ```bash
   streamlit run brand_extraction_streamlit.py
   ```

2. Open your web browser and navigate to the provided local URL (typically `http://localhost:8501`)

3. Upload an image using the file uploader

4. Click the "Extract Brand Name" button to process the image

5. View the results, including:
   - The original uploaded image
   - The detected brand name
   - The processed image with the brand name overlay

## How It Works

1. **Image Processing**:
   - Converts the uploaded image to grayscale
   - Applies thresholding for better text recognition
   - Uses OCR to extract text from the image

2. **Brand Detection**:
   - Analyzes extracted text to identify potential brand names
   - Currently identifies brands based on uppercase words
   - Returns the first detected brand name or "No brand detected"

3. **Visualization**:
   - Overlays the detected brand name on the original image
   - Centers the text for optimal visibility
   - Displays both original and processed images

## Limitations

- The current brand detection algorithm is based on simple uppercase word detection
- OCR accuracy depends on image quality and text clarity
- May not detect stylized or logo-based brand names
- Requires proper Tesseract OCR installation and configuration

## Future Improvements

- Enhanced brand detection algorithms
- Support for additional image formats
- Improved text recognition accuracy
- Custom brand name placement options
- Batch processing capabilities
- Export functionality for processed images

## Contributing

Contributions are welcome! Please feel free to submit a Pull Request.

## License

This project is licensed under the MIT License - see the LICENSE file for details.

## Acknowledgments

- [Tesseract OCR](https://github.com/tesseract-ocr/tesseract)
- [Streamlit](https://streamlit.io/)
- [OpenCV](https://opencv.org/)
