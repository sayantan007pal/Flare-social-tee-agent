# Flare-social-tee-agent
# Flare Social AI Agent with TEE Verification

A verifiably autonomous social AI agent for the Flare Network that operates within Trusted Execution Environments (TEEs) to provide secure, transparent, and attestable interactions on social media platforms.

## Overview

This project implements a secure X (Twitter) account management system with comprehensive social media monitoring capabilities. The agent uses vector embedding models for intelligent tweet classification and responds to Flare-related queries using AI models while maintaining verifiable autonomy through TEE attestations.

![Architecture Overview](https://your-repo-url/assets/architecture-diagram.svg)

## Features

- **TEE-Based Security**: Runs in AMD SEV secure environments with vTPM attestations
- **Autonomous X Account Management**: Securely interacts with the X platform API
- **Intelligent Tweet Classification**: Uses vector embeddings to understand tweet content and context
- **LLM Response Generation**: Gemini models provide accurate, helpful responses
- **Safety Filters**: Comprehensive safety checks before publishing responses
- **On-Chain Verification**: Flare smart contract integration for transparent attestation
- **Self-Regulation**: Ability to shut down based on predefined conditions

## Requirements

- Google Cloud Platform with Confidential Computing support
- Docker and Docker Compose
- Python 3.9+
- Node.js 16+
- Flare Network account with FLR for contract deployment
- X Developer Account with Elevated API access

## Quick Start

### 1. Environment Setup

Clone the repository and set up the environment:

```bash
# Clone the repository
git clone https://github.com/yourusername/flare-social-tee-agent.git
cd flare-social-tee-agent

# Create environment file from template
cp .env.example .env

# Edit .env with your credentials
nano .env
```

### 2. Configure X API Access

You'll need to set up a Twitter Developer account and create an app with Elevated access to use the v2 API:

1. Go to [Twitter Developer Portal](https://developer.twitter.com/en/portal/dashboard)
2. Create a Project and App
3. Apply for Elevated access
4. Generate API keys and tokens
5. Add these to your .env file

### 3. TEE Environment Setup

Set up a Confidential Computing VM in Google Cloud:

```bash
# Set up GCP CLI
gcloud auth login

# Create Confidential Computing VM
./scripts/setup_tee.sh
```

### 4. Smart Contract Deployment

Deploy the verification contract to Flare Network:

```bash
# Navigate to smart contracts directory
cd smart-contracts

# Install dependencies
npm install

# Deploy to Coston2 testnet
npx truffle migrate --network coston2
```

### 5. Building and Running

Build and run the application in Docker:

```bash
# Build Docker image
docker build -f docker/Dockerfile -t flare-social-agent .

# Run the container
docker run -d --name flare-agent \
  --env-file .env \
  flare-social-agent
```

For production deployment, use the GitHub Actions workflow:

1. Push code to your repository
2. GitHub Actions will build and deploy to your Confidential Computing VM

### 6. Testing in Controlled Environment

Test the agent with mock interactions:

```bash
# Run test environment
python scripts/run_test_environment.py
```

## Project Structure

```
flare-social-tee-agent/
│
├── .github/workflows/     # CI/CD pipeline
├── docker/                # Containerization
├── smart-contracts/       # Flare network integration
├── src/                   # Source code
│   ├── attestation/       # TEE attestation logic
│   ├── blockchain/        # Contract interaction
│   ├── social/            # Social media integration
│   ├── ai/                # AI processing
│   ├── safety/            # Safety filters
│   ├── data/              # Knowledge management
│   └── utils/             # Utilities
├── test/                  # Test suite
├── data/                  # Data for embeddings
├── scripts/               # Utility scripts
└── config/                # Configuration files
```

## Technical Details

### TEE Implementation

The system runs in a Trusted Execution Environment (TEE) using AMD SEV on n2d-standard-2 GCP VMs. Key security features:

- vTPM for attestation generation
- Confidential Space for secure memory encryption
- Remote attestation verification

### Vector Embedding Pipeline

Social media content is classified using:
- Gemini text-embedding-004 model
- Chroma vector database
- Flare knowledge base for relevance scoring

### Smart Contract Integration

The system integrates with Flare Network through:
- TeeV1Verifier contract for attestation verification
- Custom FlareSocialAgentVerifier contract for operational status
- Auto-shutdown capabilities based on predefined conditions

## Development

### Setting Up Development Environment

```bash
# Create virtual environment
python -m venv venv
source venv/bin/activate

# Install dependencies
pip install -r requirements.txt
npm install

# Run tests
pytest
```

### Adding New Features

1. Fork the repository
2. Create a feature branch
3. Add tests for your feature
4. Implement your feature
5. Run the test suite
6. Submit a pull request

## Security Considerations

- All sensitive credentials are stored only within the TEE
- Regular attestation verification prevents tampering
- Multiple safety filters prevent harmful outputs
- Smart contract integration provides transparent audit trail

## License

This project is licensed under the MIT License - see the LICENSE file for details.

## Acknowledgments

- Flare Network team for TEE verification contracts
- Google Cloud for Confidential Computing infrastructure

## Contact

For questions or support, please open an issue on the GitHub repository.
