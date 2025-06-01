#!/bin/bash

# Install uv package manager
curl -LsSf https://astral.sh/uv/install.sh | sh
echo 'eval "$(uv generate-shell-completion bash)"' >> ~/.bashrc

sudo tailscale up --accept-routes --auth-key=$TS_AUTH_KEY