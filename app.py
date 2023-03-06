from flask import Flask, request, send_file, render_template, redirect, url_for
from PyPDF2 import PdfMerger, PdfReader, PdfWriter
from io import BytesIO
import base64
import qrcode
app = Flask(__name__)

# Define a route for the index page


@app.route('/')
def index():
    return render_template('index.html')


@app.route('/pdf', methods=['GET'])
def pdf():
    return render_template('pdf.html')


@app.route('/pdf/merge', methods=['GET'])
def pdf_merge():
    return render_template('merge.html')


@app.route('/pdf/split', methods=['GET'])
def pdf_split():
    return render_template('split.html')


@app.route('/qrcode', methods=['GET'])
def gen_qrcode():
    return render_template('qrcode.html')

# Define a route for the PDF merging function


@app.route('/merge_pdf', methods=['POST'])
def merge_pdf():
    # Get a list of uploaded PDF files from the POST request
    uploaded_files = request.files.getlist('pdf_files')
    # Create a PdfMerger object
    merger = PdfMerger()
    # Loop through the uploaded PDF files and append them to the PdfMerger object
    for file in uploaded_files:
        pdf_reader = PdfReader(file)
        merger.append(pdf_reader)
    # Write the merged PDF to a BytesIO object
    merged_file = BytesIO()
    merger.write(merged_file)
    merged_file.seek(0)
    # Return the merged PDF as a downloadable file
    return send_file(merged_file, download_name='merged.pdf', as_attachment=True)

# Define a route for the PDF splitting function


@app.route('/split_pdf', methods=['POST'])
def split_pdf():
    # Get the uploaded PDF file from the POST request
    uploaded_file = request.files['pdf_file']
    # Create a PdfReader object from the uploaded file
    pdf_reader = PdfReader(uploaded_file)
    page_start = int(request.form.get('page_start'))
    page_end = int(request.form.get('page_end'))
    # Create a list of PdfWriter objects, one for each page range
    writers = []
    # Create a new PdfWriter object for this page range
    writer = PdfWriter()
    # Loop through the pages in the page range and add them to the PdfWriter object
    for page in range(page_start, page_end + 1):
        writer.add_page(pdf_reader.pages[page - 1])
    # Add the PdfWriter object to the list of writers
    writers.append(writer)
    # Loop through the PdfWriter objects and write each one to a BytesIO object
    for i, writer in enumerate(writers):
        output_file = BytesIO()
        writer.write(output_file)
        output_file.seek(0)
        # Set the filename for the downloaded file
        filename = f'split_{i+1}.pdf'
        # Return the split PDF as a downloadable file
        return send_file(output_file, download_name=filename, as_attachment=True)

# Define a route for generate QRCODE


@app.route('/generate_qrcode', methods=['POST'])
def generate_qrcode():
    # Get the text to encode from the form
    text = request.form.get('text-input')
    # Generate the QR code as a PNG image
    qr = qrcode.QRCode(version=1, box_size=10, border=5)
    qr.add_data(text)
    qr.make(fit=True)
    img = qr.make_image(fill_color='black', back_color='white')
    # Store the image in a BytesIO buffer so that it can be sent as a response
    img_io = BytesIO()
    img.save(img_io, 'PNG')
    img_io.seek(0)
    # Encode image bytes as base64 string
    encoded_img = base64.b64encode(img_io.read()).decode()
    # Render the image in the HTML template
    return render_template('qrcode.html', qr_image=encoded_img)


# Error handling function for 404 Page Not Found


@app.errorhandler(404)
def page_not_found(error):
    return render_template('404.html'), 404

# Route that does not exist to test the 404 error page


@app.route('/not_found')
def not_found():
    return 'This page does not exist', 404

# Custom error handling function for all error codes


@app.errorhandler(Exception)
def handle_error(error):
    return redirect(url_for('custom_error_page')), 302

# Custom error page to redirect to


@app.route('/custom_error_page')
def custom_error_page():
    return render_template('error.html')


if __name__ == '__main__':
    app.run(debug=True)
