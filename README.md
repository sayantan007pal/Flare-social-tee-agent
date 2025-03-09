# Flare-social-tee-agent
# Flare Social AI Agent with TEE Verification

A verifiably autonomous social AI agent for the Flare Network that operates within Trusted Execution Environments (TEEs) to provide secure, transparent, and attestable interactions on social media platforms.

## Overview

This project implements a secure X (Twitter) account management system with comprehensive social media monitoring capabilities. The agent uses vector embedding models for intelligent tweet classification and responds to Flare-related queries using AI models while maintaining verifiable autonomy through TEE attestations.

![Architecture Overview]<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 800 600">
  <!-- Background -->
  <rect width="800" height="600" fill="#f8f9fa" />
  
  <!-- TEE Container -->
  <rect x="50" y="50" width="700" height="500" rx="10" fill="#e6f7ff" stroke="#1890ff" stroke-width="2" stroke-dasharray="5,5" />
  <text x="400" y="80" font-family="Arial" font-size="16" text-anchor="middle" fill="#1890ff">Trusted Execution Environment (TEE)</text>
  
  <!-- X Account Manager -->
  <rect x="100" y="120" width="180" height="100" rx="5" fill="#fff" stroke="#1890ff" stroke-width="2" />
  <text x="190" y="150" font-family="Arial" font-size="14" text-anchor="middle" fill="#000">X Account Manager</text>
  <text x="190" y="175" font-family="Arial" font-size="12" text-anchor="middle" fill="#555">Authentication</text>
  <text x="190" y="195" font-family="Arial" font-size="12" text-anchor="middle" fill="#555">API Interaction</text>
  
  <!-- Social Media Monitor -->
  <rect x="320" y="120" width="180" height="100" rx="5" fill="#fff" stroke="#1890ff" stroke-width="2" />
  <text x="410" y="150" font-family="Arial" font-size="14" text-anchor="middle" fill="#000">Social Media Monitor</text>
  <text x="410" y="175" font-family="Arial" font-size="12" text-anchor="middle" fill="#555">Stream Processing</text>
  <text x="410" y="195" font-family="Arial" font-size="12" text-anchor="middle" fill="#555">Vector Embeddings</text>
  
  <!-- AI Processing -->
  <rect x="540" y="120" width="180" height="100" rx="5" fill="#fff" stroke="#1890ff" stroke-width="2" />
  <text x="630" y="150" font-family="Arial" font-size="14" text-anchor="middle" fill="#000">AI Processing</text>
  <text x="630" y="175" font-family="Arial" font-size="12" text-anchor="middle" fill="#555">Gemini Models</text>
  <text x="630" y="195" font-family="Arial" font-size="12" text-anchor="middle" fill="#555">Classification Logic</text>
  
  <!-- Safety Filters -->
  <rect x="100" y="260" width="180" height="100" rx="5" fill="#fff" stroke="#1890ff" stroke-width="2" />
  <text x="190" y="290" font-family="Arial" font-size="14" text-anchor="middle" fill="#000">Safety Filters</text>
  <text x="190" y="315" font-family="Arial" font-size="12" text-anchor="middle" fill="#555">Content Moderation</text>
  <text x="190" y="335" font-family="Arial" font-size="12" text-anchor="middle" fill="#555">Response Verification</text>
  
  <!-- Response Generator -->
  <rect x="320" y="260" width="180" height="100" rx="5" fill="#fff" stroke="#1890ff" stroke-width="2" />
  <text x="410" y="290" font-family="Arial" font-size="14" text-anchor="middle" fill="#000">Response Generator</text>
  <text x="410" y="315" font-family="Arial" font-size="12" text-anchor="middle" fill="#555">Tweet Composition</text>
  <text x="410" y="335" font-family="Arial" font-size="12" text-anchor="middle" fill="#555">Context Management</text>
  
  <!-- Smart Contract Integration -->
  <rect x="540" y="260" width="180" height="100" rx="5" fill="#fff" stroke="#1890ff" stroke-width="2" />
  <text x="630" y="290" font-family="Arial" font-size="14" text-anchor="middle" fill="#000">Smart Contract</text>
  <text x="630" y="315" font-family="Arial" font-size="12" text-anchor="middle" fill="#555">TeeV1Verifier</text>
  <text x="630" y="335" font-family="Arial" font-size="12" text-anchor="middle" fill="#555">Attestation Logic</text>
  
  <!-- Attestation Manager -->
  <rect x="210" y="400" width="380" height="100" rx="5" fill="#fff" stroke="#1890ff" stroke-width="2" />
  <text x="400" y="430" font-family="Arial" font-size="14" text-anchor="middle" fill="#000">Attestation Manager</text>
  <text x="400" y="455" font-family="Arial" font-size="12" text-anchor="middle" fill="#555">vTPM Attestations</text>
  <text x="400" y="475" font-family="Arial" font-size="12" text-anchor="middle" fill="#555">Remote Verification</text>
  
  <!-- Connection Lines -->
  <!-- X Account Manager to Social Media Monitor -->
  <line x1="280" y1="170" x2="320" y2="170" stroke="#1890ff" stroke-width="2" />
  <!-- Social Media Monitor to AI Processing -->
  <line x1="500" y1="170" x2="540" y2="170" stroke="#1890ff" stroke-width="2" />
  <!-- AI Processing to Safety Filters -->
  <line x1="630" y1="220" x2="630" y2="240" stroke="#1890ff" stroke-width="2" />
  <line x1="630" y1="240" x2="190" y2="240" stroke="#1890ff" stroke-width="2" />
  <line x1="190" y1="240" x2="190" y2="260" stroke="#1890ff" stroke-width="2" />
  <!-- Safety Filters to Response Generator -->
  <line x1="280" y1="310" x2="320" y2="310" stroke="#1890ff" stroke-width="2" />
  <!-- Response Generator to Smart Contract Integration -->
  <line x1="500" y1="310" x2="540" y2="310" stroke="#1890ff" stroke-width="2" />
  <!-- All to Attestation Manager -->
  <line x1="190" y1="360" x2="190" y2="380" stroke="#1890ff" stroke-width="2" />
  <line x1="190" y1="380" x2="400" y2="380" stroke="#1890ff" stroke-width="2" />
  <line x1="400" y1="380" x2="400" y2="400" stroke="#1890ff" stroke-width="2" />
  <line x1="410" y1="360" x2="410" y2="380" stroke="#1890ff" stroke-width="2" />
  <line x1="630" y1="360" x2="630" y2="380" stroke="#1890ff" stroke-width="2" />
  <line x1="630" y1="380" x2="400" y2="380" stroke="#1890ff" stroke-width="2" />
  
  <!-- Flare Network Connection -->
  <line x1="630" y1="360" x2="700" y2="380" stroke="#1890ff" stroke-width="2" />
  <text x="715" y="385" font-family="Arial" font-size="12" text-anchor="middle" fill="#1890ff">Flare Network</text>
  
  <!-- External Twitter Icon -->
  <line x1="190" y1="120" x2="190" y2="100" stroke="#1890ff" stroke-width="2" />
  <text x="190" y="95" font-family="Arial" font-size="12" text-anchor="middle" fill="#1890ff">X Platform</text>
</svg>


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
