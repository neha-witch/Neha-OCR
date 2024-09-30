import easyocr
import gradio as gr
import re

reader = easyocr.Reader(['en', 'hi'])

def ocr_text(image):
  """
  Performs OCR on the given image and returns the extracted text.

  Args:
    image: The image to perform OCR on.

  Returns:
    The extracted text and the original image.
  """
  result = reader.readtext(image)
  full_text = ' '.join([text for bbox, text, conf in result])
  return full_text, image


def highlight_text(full_text, search_term):
  """
  Highlights the search term in the given text.

  Args:
    full_text: The text to search in.
    search_term: The term to search for.

  Returns:
    The text with the search term highlighted.
  """
  if search_term:
    highlighted_text =  highlighted_text = re.sub(f"({search_term})", r"<mark>\1</mark>", full_text, flags=re.IGNORECASE)
    return highlighted_text
  return


with gr.Blocks() as demo:
    image_input = gr.Image(type="filepath")
    extracted_text = gr.Textbox(lines=5, placeholder="Extracted text will appear here...")
    ocr_button = gr.Button("Extract Text")
    ocr_button.click(fn=ocr_text, inputs=image_input, outputs=[extracted_text, image_input])
    search_term = gr.Textbox(lines=1, placeholder="Enter search term")
    highlighted_text = gr.HTML()

    search_button = gr.Button("Search")
    search_button.click(fn=highlight_text, inputs=[extracted_text, search_term], outputs=highlighted_text)

demo.launch(share=True)
