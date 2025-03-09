# Use a base image compatible with Confidential Computing
FROM us-docker.pkg.dev/cloud-marketplace/google/confidential-space:latest

# Install dependencies
RUN apt-get update && apt-get install -y \
    python3 \
    python3-pip \
    nodejs \
    npm \
    solc \
    curl

# Install Python dependencies
COPY requirements.txt /app/
RUN pip3 install --no-cache-dir -r /app/requirements.txt

# Install web3.js
WORKDIR /app
RUN npm init -y && npm install web3

# Copy application code
COPY . /app/

# Set up attestation verification
RUN mkdir -p /attestation

# Set environment variables
ENV PYTHONUNBUFFERED=1
ENV ATTESTATION_PATH=/attestation
ENV NODE_ENV=production

# Generate entrypoint script that verifies attestation on startup
RUN echo '#!/bin/bash\n\
# Verify attestation and store result\n\
python3 /app/verify_attestation.py\n\
\n\
# Start the application only if attestation is valid\n\
if [ -f "/attestation/valid" ]; then\n\
    echo "Attestation valid, starting application"\n\
    python3 /app/main.py\n\
else\n\
    echo "Attestation invalid, shutting down"\n\
    exit 1\n\
fi' > /app/entrypoint.sh && chmod +x /app/entrypoint.sh

# Set entrypoint
ENTRYPOINT ["/app/entrypoint.sh"]