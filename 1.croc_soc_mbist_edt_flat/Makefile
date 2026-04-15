INPUT_CHANNEL_COUNT=3
OUTPUT_CHANNEL_COUNT=3
LONGEST_CHAIN_RANGE="65_100"
SCAN_CHAIN_COUNT=100

SAVEOUTPUT_DIR=logs_inChannelCnt${INPUT_CHANNEL_COUNT}_outChannelCnt${OUTPUT_CHANNEL_COUNT}_range${LONGEST_CHAIN_RANGE}_chainsCount${SCAN_CHAIN_COUNT}

.PHONY: change_EDT_config
change_EDT_config:
	python3 change_EDT_config.py --input_channel_count="${INPUT_CHANNEL_COUNT}" --output_channel_count="${OUTPUT_CHANNEL_COUNT}" \
	    --longest_chain_range="${LONGEST_CHAIN_RANGE}" --scan_chain_count="${SCAN_CHAIN_COUNT}"

.PHONY: rename_logsdir
save_steps_outputs:
	mkdir -p 1.insert_bscan_mbist/${SAVEOUTPUT_DIR}
	cd 1.insert_bscan_mbist && mv logfiles simulation_outdir ${SAVEOUTPUT_DIR}

	mkdir -p 2.insert_occ_edt/${SAVEOUTPUT_DIR}
	cd 2.insert_occ_edt && mv logfiles simulation_outdir ${SAVEOUTPUT_DIR}

	mkdir -p 3.synthesize_rtl/${SAVEOUTPUT_DIR}
	cd 3.synthesize_rtl && mv command.log mbist_edt_area.rpt mbist_edt_power.rpt mbist_edt_timing.rpt croc_chip_synthesized.vg default.svf work logfiles ${SAVEOUTPUT_DIR}

	mkdir -p 4.insert_scan/${SAVEOUTPUT_DIR}
	cd 4.insert_scan && mv logfiles scan_cells.list ${SAVEOUTPUT_DIR}

	mkdir -p 5.generate_atpg_patterns/${SAVEOUTPUT_DIR}
	cd 5.generate_atpg_patterns && mv logfiles patterns work ${SAVEOUTPUT_DIR}

	mkdir -p 6.validate_mbist_gate_level/${SAVEOUTPUT_DIR}
	cd 6.validate_mbist_gate_level && mv logfiles patterns simulation_outdir ${SAVEOUTPUT_DIR}