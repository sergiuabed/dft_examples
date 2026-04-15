#!/bin/bash
INPUT_CHANNEL_COUNT=3
OUTPUT_CHANNEL_COUNT=3
LONGEST_CHAIN_RANGE="[65, 100]"
SCAN_CHAIN_COUNT=100

python3 change_EDT_config.py --input_channel_count="${INPUT_CHANNEL_COUNT}" --output_channel_count="${OUTPUT_CHANNEL_COUNT}" \
    --longest_chain_range="${LONGEST_CHAIN_RANGE}" --scan_chain_count="${SCAN_CHAIN_COUNT}"