# AI Compliance Assistant

An intelligent tool to help individuals and organizations achieve AI compliance with EU and Saudi Arabian AI regulations.

## Overview

This tool provides four specialized pathways to support different stakeholders in their AI compliance journey:

1. **Building AI** - For developers and teams creating AI systems
2. **Procuring AI** - For organizations evaluating and purchasing AI solutions
3. **Operating AI** - For teams deploying and managing AI systems in production
4. **Training on AI** - For individuals seeking to understand AI compliance requirements

## Features

- **Pathway Selection**: Choose the pathway that matches your role and objectives
- **Goal-Driven Guidance**: Set specific compliance goals and receive structured guidance
- **Document Upload**: Upload project documents for contextualized recommendations
- **Adaptive Feedback**: Provide feedback at each stage to customize your pathway
- **Regulatory Knowledge**: Access EU AI Act and Saudi Arabian AI regulations
- **AI-Powered Assistance**: Leverage OpenAI to generate tailored compliance advice

## Project Structure

```
AI_Compliance_Assistant/
├── src/
│   ├── pathways/          # Four pathway implementations
│   │   ├── building.py
│   │   ├── procuring.py
│   │   ├── operating.py
│   │   └── training.py
│   ├── knowledge/         # Compliance knowledge bases
│   │   ├── eu_regulations.py
│   │   └── saudi_regulations.py
│   ├── llm/              # OpenAI integration
│   │   └── openai_client.py
│   ├── document_processor/  # Document handling
│   │   └── processor.py
│   ├── feedback/         # Adaptive feedback system
│   │   └── adapter.py
│   └── models.py         # Data models
├── data/
│   ├── regulations/      # Regulatory documents
│   │   ├── eu_ai_act/
│   │   └── saudi_ai_regs/
│   └── templates/        # Compliance templates
├── web_app.py           # Main Streamlit application
├── requirements.txt     # Python dependencies
├── .env.example        # Environment variable template
└── README.md
```

## Quick Start

### 1. Installation

```bash
# Clone the repository
git clone https://github.com/MattStroud1/AI_Compliance_Assistant.git
cd AI_Compliance_Assistant

# Create virtual environment
python -m venv venv
source venv/bin/activate  # On Windows: venv\Scripts\activate

# Install dependencies
pip install -r requirements.txt
```

### 2. Configuration

```bash
# Copy environment template
cp .env.example .env

# Edit .env and add your OpenAI API key
# OPENAI_API_KEY=your-api-key-here
```

### 3. Run the Application

```bash
# Launch web interface
streamlit run web_app.py
```

## Usage

1. **Select Your Pathway**: Choose from Building, Procuring, Operating, or Training
2. **Define Your Goal**: Enter what you want to achieve (e.g., "Ensure my AI project complies with EU AI Act high-risk requirements")
3. **Upload Documents** (optional): Provide project documentation for contextualized guidance
4. **Follow the Steps**: Work through structured compliance steps
5. **Provide Feedback**: At each stage, give feedback to adapt the pathway to your needs

## Regulatory Coverage

### EU AI Act
- Risk classification (Minimal, Limited, High, Unacceptable)
- High-risk system requirements
- Transparency obligations
- Conformity assessments
- Documentation requirements

### Saudi Arabian AI Regulations
- National AI principles
- Data governance requirements
- Ethical AI guidelines
- Sector-specific regulations

## Technology Stack

- **Python 3.11+**: Core language
- **Streamlit**: Web interface
- **OpenAI API**: AI-powered guidance (GPT-4)
- **LangChain**: Document processing and retrieval
- **Pydantic**: Data validation
- **SQLite**: Session and progress storage

## License

MIT License

## Support

For issues or questions, please open an issue on GitHub.
