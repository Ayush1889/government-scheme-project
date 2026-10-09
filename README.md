# Government Scheme Assistant

## About the Project

The Government Scheme Assistant is a Python-based application that helps users discover relevant government schemes based on their needs and personal information. It uses TF-IDF retrieval, Gemini-powered profile extraction, and rule-based eligibility checking to provide scheme recommendations and application guidance.

## Features

- **Scheme Discovery:** Retrieves relevant schemes using TF-IDF and cosine similarity.
- **AI-Powered Profile Extraction:** Uses Google Gemini to extract structured information from natural-language queries.
- **Eligibility Checking:** Evaluates user profiles against implemented eligibility rules.
- **Application Guidance:** Provides available documents, application steps, and official website links.
- **Multi-Agent Architecture:** Separates discovery, eligibility, application guidance, and orchestration into individual modules.

## Tech Stack

- Python
- Google Gemini API (`google-genai`)
- scikit-learn
- TF-IDF and cosine similarity
- CSV dataset
- python-dotenv

## Project Structure

| File | Purpose |
|---|---|
| `rag.py` | Retrieves relevant schemes using TF-IDF and cosine similarity |
| `discovery_agent.py` | Finds candidate schemes |
| `llm.py` | Extracts user profiles using Gemini |
| `eligibility.py` | Checks profiles against implemented rules |
| `application_agent.py` | Provides application information |
| `orchestrator.py` | Coordinates the agents |
| `government_schemes.csv` | Stores scheme information |
| `test_llm.py` | Tests Gemini profile extraction |
| `test_discovery.py` | Tests scheme retrieval |
| `test_eligibility.py` | Tests eligibility checking |
| `test_application.py` | Tests application guidance |
| `test_orchestrator.py` | Tests the complete workflow |

## Setup

### 1. Create a virtual environment

```bash
python -m venv .venv
```

Activate it in Windows PowerShell:

```powershell
.\.venv\Scripts\Activate.ps1
```

### 2. Install dependencies

```powershell
python -m pip install -U google-genai python-dotenv scikit-learn
```

### 3. Configure the API key

Create a `.env` file in the project root:

```env
GEMINI_API_KEY=your_api_key_here
```

Get a key from [Google AI Studio](https://aistudio.google.com/apikey).

Never commit your `.env` file or expose your API key publicly.

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

Test the complete workflow:

```bash
python test_orchestrator.py
```

## How It Works

1. The user submits a natural-language query.
2. Gemini extracts available profile information.
3. The Discovery Agent retrieves relevant schemes.
4. The Eligibility Agent evaluates the profile against implemented rules.
5. The Application Agent provides available application information.
6. The Orchestrator coordinates the workflow.

## Limitations

- Results depend on the quality and completeness of the scheme dataset and implemented rules.
- TF-IDF relevance scores indicate textual similarity, not the probability of eligibility.
- Users should verify eligibility requirements and application details through official government sources.

## Future Improvements

- Streamlit user interface
- FastAPI backend
- More comprehensive eligibility rules
- OCR-based document information extraction
- Authentication and deployment
