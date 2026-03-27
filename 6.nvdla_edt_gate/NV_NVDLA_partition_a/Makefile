FLOW_EDT_OCC=2.insert_edt_occ
FLOW_SCAN=4.insert_scan
FLOW_ATPG=7.generate_atpg_patterns

all: atpg

edt_occ:
	cd $(FLOW_EDT_OCC) ; ./run_edt_occ_insertion

scan: edt_occ
	cd $(FLOW_SCAN); ./run_scan_insertion
atpg: scan
	cd $(FLOW_ATPG); ./1.run_graybox_generation.sh; ./2.run_ext_multi_stuck; ./3.run_internal_stuck; ./4.run_ext_multi_transition; ./5.run_internal_transition; ./7.merge_faults_report; ./6.run_sims


clean:
	rm -rf tsdb_outdir
	rm -rf $(FLOW_EDT_OCC)/logfiles $(FLOW_EDT_OCC)/simulation_outdir $(FLOW_EDT_OCC)/synthesis_outdir
	rm -rf $(FLOW_SCAN)/logfiles $(FLOW_SCAN)/*.rpt $(FLOW_SCAN)/*.list  
	rm -rf $(FLOW_ATPG)/logfiles $(FLOW_ATPG)/patterns $(FLOW_ATPG)/work $(FLOW_ATPG)/*.tcd


