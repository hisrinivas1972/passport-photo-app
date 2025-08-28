# Passport Photo Generator

![Demo](https://passport-photo-app-m3rsasvvvkd3tk3xizf3yq.streamlit.app/)

🛂 A simple web app to generate passport photos with automatic background removal and resizing for various countries.

---

## Project Structure

```bash
📁 passport-photo-app/
├── app.py
├── requirements.txt
└── README.md
...

Features

Upload any photo (JPG, PNG) and automatically remove the background using AI-powered rembg

Resize and crop photos to official passport photo sizes for multiple countries (USA, India, UK, Canada, Australia)

Place the subject on a clean white background (custom background color support coming soon!)

View original and processed photos side by side with pixel dimensions displayed

Download the final image in high resolution (300 DPI) ready for printing or online submission

Live Demo

Try the app live here:
Passport Photo Generator App

Installation & Usage

Clone the repo:

git clone https://github.com/hisrinivas1972/passport-photo-app.git
cd passport-photo-app


Create and activate a virtual environment (optional but recommended):

python -m venv venv
source venv/bin/activate  # Linux/Mac
venv\Scripts\activate     # Windows


Install dependencies:

pip install -r requirements.txt


Run the Streamlit app:

streamlit run app.py


Open your browser at http://localhost:8501

Passport Sizes Supported
Country	Size (inches)	Size (pixels @ 300 DPI)
USA	2 x 2	600 x 600
UK	1.77 x 1.37	531 x 411
Canada	2 x 2.75	600 x 825
Australia	1.97 x 1.57	591 x 471
India	2 x 2	600 x 600
Technologies Used

Python

Streamlit
 — for the web UI

rembg
 — for background removal

Pillow (PIL)
 — for image processing

Contribution

Feel free to open issues or submit pull requests!
Feature requests, bug reports, and improvements are very welcome.
