import ollama
from PIL import Image
import base64
import io

def analyze_image(image_path, question):
    try:
        # Open the image and convert it to base64
        image = Image.open(image_path)
        buffer = io.BytesIO()
        image.save(buffer, format="JPEG")  # Adjust if your image format is different
        image_base64 = base64.b64encode(buffer.getvalue()).decode('utf-8')

        # Create the message for Ollama
        message = {
            "role": "user",
            "content": question,
            "images": [image_base64]
        }

        # Send request to Ollama
        response = ollama.chat(model='granite3.2-vision', messages=[message])

        # Return the model's reply
        return response

    except Exception as e:
        return f"Error: {e}"
