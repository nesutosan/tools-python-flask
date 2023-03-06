from flask import Flask, request, send_file, render_template
from PyPDF2 import PdfMerger, PdfReader, PdfWriter
from io import BytesIO
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

# Error handling function for Internal Server Error (500)


@app.errorhandler(500)
def internal_server_error(error):
    return render_template('error.html'), 500

# Route that raises an Internal Server Error (500)


@app.route('/raise_error')
def raise_error():
    raise Exception('Internal Server Error')

# Error handling function for 404 Page Not Found


@app.errorhandler(404)
def page_not_found(error):
    return render_template('404.html'), 404

# Route that does not exist to test the 404 error page


@app.route('/not_found')
def not_found():
    return 'This page does not exist', 404


if __name__ == '__main__':
    app.run(debug=True)
