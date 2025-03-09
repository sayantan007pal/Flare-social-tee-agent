# Using n2d-standard-2 machine type with AMD SEV
gcloud compute instances create flare-social-agent \
  --machine-type=n2d-standard-2 \
  --confidential-compute \
  --maintenance-policy=TERMINATE