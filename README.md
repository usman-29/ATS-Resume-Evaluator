# ATS Resume Evaluator

ATS Resume Evaluator is a project that analyzes resumes against job descriptions using advanced NLP techniques. It provides a match percentage, missing keywords, and a profile summary, helping users optimize their resumes for technical roles.

## Features

- Match percentage between resume and job description.
- Identification of missing keywords.
- Profile summary generation.
- Support for roles in the tech industry.

## Dependencies

- **Streamlit**: For the interactive user interface.
- **PyPDF2**: To handle PDF resume parsing.
- **google.generativeai**: For advanced natural language processing.
- **python-dotenv**: To manage environment variables.

## Installation

1. Clone the repository:

   ```bash
   git clone https://github.com/yourusername/ats-resume-evaluator.git

2. Navigate to project directory:

   ```bash
   cd ats-resume-evaluator

3. Install the required packages:

   ```bash
   pip install -r requirements.txt

4. Create a .env file in the root directory and add your API keys and configuration:

   ```bash
   GOOGLE_GENERATIVEAI_API_KEY=your_api_key_here

## Usage

   ```bash
   streamlit run app.py

