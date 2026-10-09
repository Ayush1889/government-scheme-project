# Government Scheme Assistant

## About the Project

The Government Scheme Assistant is a Python-based project that helps users discover relevant government schemes based on their personal information and needs. It uses text retrieval, profile extraction, and rule-based eligibility checking to provide scheme recommendations and application guidance.

## Features

- **Scheme Discovery:** Finds relevant government schemes using TF-IDF and cosine similarity.
- **AI-Powered Profile Extraction:** Uses the Gemini API to extract user information from natural-language queries.
- **Eligibility Checking:** Evaluates user profiles against the eligibility conditions available in the dataset.
- **Application Guidance:** Provides information about required documents, application steps, and official application websites.
- **Multi-Agent Architecture:** Separates scheme discovery, eligibility checking, application guidance, and orchestration into different modules.

## Tech Stack

- Python
- Google Gemini API
- scikit-learn
- TF-IDF and cosine similarity
- CSV dataset
- python-dotenv

## Project Structure

| File | Purpose |
|---|---|
| `rag.py` | Retrieves relevant schemes using TF-IDF and cosine similarity |
| `discovery_agent.py` | Finds candidate schemes relevant to the user's query |
| `llm.py` | Extracts a structured user profile using Gemini |
| `eligibility.py` | Checks the profile against available eligibility rules |
| `application_agent.py` | Provides scheme application information |
| `orchestrator.py` | Coordinates the agents |
| `government_schemes.csv` | Stores government scheme information |
| `test_llm.py` | Tests Gemini profile extraction |
| `test_discovery.py` | Tests scheme discovery |
| `test_eligibility.py` | Tests eligibility checking |
| `test_application.py` | Tests application guidance |
| `test_orchestrator.py` | Tests the complete workflow |

## Setup and Installation

### 1. Clone the repository

```bash
git clone <your-repository-url>
cd government-scheme-project
```

### 2. Create a virtual environment

```bash
python -m venv .venv
```

Activate it on Windows PowerShell:

```powershell
.\.venv\Scripts\Activate.ps1
```

### 3. Install dependencies

```bash
python -m pip install -U google-genai python-dotenv scikit-learn
```

Install any additional dependencies required by the project.

### 4. Configure the Gemini API key

Create a `.env` file in the project root:

```env
GEMINI_API_KEY=your_api_key_here
```

Obtain an API key from [Google AI Studio](https://aistudio.google.com/apikey).

**Security:** Never commit your `.env` file or expose your API key publicly.

## Running the Project

Test Gemini profile extraction:

```bash
python test_llm.py
```

Test scheme discovery:

```bash
python test_discovery.py
```

Test eligibility checking:

```bash
python test_eligibility.py
```

Test the complete assistant workflow:

```bash
python test_orchestrator.py
```

## How It Works

1. The user submits a natural-language query.
2. Gemini extracts the available user-profile information.
3. The Discovery Agent retrieves relevant schemes using TF-IDF and cosine similarity.
4. The Eligibility Agent checks the profile against the implemented rules.
5. The Application Agent provides available documents, application steps, and website information.
6. The Orchestrator coordinates the workflow and presents the results.

## Limitations

- Eligibility results depend on the accuracy and completeness of the dataset and implemented rules.
- A relevance score measures textual similarity; it is not a probability of eligibility.
- Users should verify eligibility requirements and application details through official government sources.

## Future Improvements

- Streamlit user interface
- FastAPI backend
- More comprehensive eligibility rules
- OCR-based document information extraction
- Authentication and deployment
