# DfT examples on croc SoC

This repository provides a series of examples of for DfT insertion using Tessent tools. In order to illustrate the usage of the DfT flow, this repository used the [croc SoC](https://github.com/pulp-platform/croc). The examples are implmented using the IHP130nm PDK to make the flow more realistic. 

Currently, the repository provides three initial examples, however the repository is going to be continously updated with additional examples and study cases. The following is the list of the examples. 

- [1.croc_soc_mbist_edt_flat](./1.croc_soc_mbist_edt_flat/): This example demostrates the DfT insertion of MBIST and EDT on the flatten version of the croc SoC. 

    The following is a general file tree representation of this example. Under every directory, several scripts are in charge of executing one step across the whole DfT insertion process. The complete flow can be executed by running the `run_dft_flow.sh` script. 

    ```bash
    1.croc_soc_mbist_edt_flat
    ├── 1.insert_bscan_mbist # mbist and bscan insertion
    │   ├── croc.flist
    │   ├── run_insert_bscan_mbist
    ├── 2.insert_occ_edt # logic test instrument insertion
    │   ├── run_insert_occ_edt
    ├── 3.synthesize_rtl # synthesis step
    │   ├── run_dc_synthesis
    │   ├── to_dc_synthesis.tcl
    ├── 4.insert_scan # Scan chain insertion
    │   ├── run_scan_insertion
    │   └── scan_cells.list
    ├── 5.generate_atpg_patterns # ATPG generation
    │   ├── 1.run_stuck_tessent_scan
    │   ├── 2.run_transition_tessent_scan
    │   ├── 3.run_sims
    │   ├── stuck.do
    │   ├── transition.do
    ├── 6.validate_mbist_gate_level # intruments signoff
    │   ├── run_mbist_gate_sim
    ├── croc # Design files croc SoC
    ├── run_dft_flow.sh # Full fow execution
    ```

[!NOTE]
Helper diagrams to be added here 

- [2.croc_soc_mbist_tk_lbist_flat](./2.croc_soc_mbist_tk_lbist_flat/): This example demostrates the insertion of both MBIST and LBIST on the flatten version of the Croc SoC. 

    The complete flow can be executed by running the `run_dft_flow.sh` script. 

    ```bash
    2.croc_soc_mbist_tk_lbist_flat
    ├── 01.mbist_insertion
    │   ├── croc.flist
    │   ├── run_insert_bscan_mbist
    ├── 02.dft_insertion
    │   ├── logic_instruments.dfpspec
    │   ├── run_dft_insertion
    ├── 03.synthesis
    │   ├── run_synth
    │   ├── run_tessent_synth.tcl
    ├── 04.tpi_insertion
    │   ├── run_tpi_insertion
    ├── 05.scan_insertion
    │   ├── run_scan_insertion
    ├── 06.atpg_generation
    │   ├── run_sim
    │   ├── run_stuck
    ├── 07.lbist_fsim
    │   ├── run_fsim
    │   ├── run_lbist_parallel_pattern
    ├── 08.bist_retargeting
    │   ├── lbist_mbist_pattern.patspec
    │   ├── run_retargeting
    ├── croc
    ├── run_dft_flow.sh
    ```
[!NOTE]
Helper diagrams to be added here 

- [3.croc_soc-mbist-tk_lbist_hier](./3.croc_soc-mbist-tk_lbist_hier/): This example shows a hierarchical DfT insertion of MBIST and Hybrid TK/LBIST on the Croc SoC. This also includes de usage of single chain mode for testing the DfT instruments as well. 

    The complete flow at each design block can be executed by running the `run_dft_flow.sh` script. 

    ```bash
    3.croc_soc-mbist-tk_lbist_hier
    ├── croc # source files 
    ├── croc_soc # physical design 
    │   ├── 1.insert_mbist
    │   │   ├── croc.flist
    │   │   ├── run_mbist_insertion
    │   ├── 2.insert_htklb_occ
    │   │   ├── for_dc_synthesis.tcl
    │   │   ├── run_htklb_occ_insertion
    │   ├── 3.synthesize_rtl
    │   │   ├── run_dc_synthesis
    │   │   ├── to_dc_synthesis.tcl
    │   ├── 4.insert_testpoint_xbound_scan
    │   │   ├── run_testpoint_xbound_scan_insertion
    │   ├── 5.lbist_fault_simulation
    │   │   └── run_lbist_fault_simulations
    │   ├── 6.lbist_patterns_generation
    │   │   ├── run_lbist_patterns_generation
    │   ├── 7.generate_atpg_patterns
    │   │   ├── 1.run_graybox_generation
    │   │   ├── 2.run_ext_multi_stuck
    │   │   ├── 3.run_internal_stuck
    │   │   ├── 4.run_ext_multi_transition
    │   │   ├── 5.run_internal_transition
    │   │   ├── 6.run_sims
    │   │   ├── run_all
    │   ├── 8.generate_ccm_patterns
    │   │   └── run_ccm_pattern
    │   ├── 9.generate_atpg_patterns_post_layout
    │   │   ├── 0.write_design_in_tsdb
    │   │   ├── 1.run_graybox_generation
    │   │   ├── 2.run_internal_stuck
    │   │   ├── 3.run_internal_transition
    │   │   ├── 4.run_sims
    │   │   ├── 5.export_pre_layout_modes
    │   │   ├── 6.run_lbist_layout_fsims
    │   │   ├── 7.run_lbist_mbist_layout_sims
    │   ├── netlist
    │   │   ├── run_dc_postlayout
    │   │   └── to_dc_for_flattening.tcl
    │   ├── run_all
    └── top #top designs
        ├── 1.insert_bscan
        │   ├── croc.flist
        │   ├── run_bscan_insertion
        ├── 2.insert_edt_occ
        │   ├── run_edt_occ_insertion
        ├── 3.insert_scan
        │   ├── run_scan_insertion
        │   └── scan_cells.list
        ├── 4.generate_atpg_patterns
        │   ├── 1.run_tk_chip_stuck
        │   ├── 2.run_tk_chip_ccm
        │   ├── 3.run_tk_chip_transition
        │   ├── run_sims
        ├── 5.retarget_atpg_patterns
        │   ├── run_dft_instr_signoff
        │   ├── run_retarget_mode1
        │   ├── run_retarget_mode1_transition
        │   ├── run_sims
        ├── 6.generate_atpg_patterns_post_layout
        │   ├── 0.write_design_in_tsdb
        │   ├── 1.run_tk_chip_stuck
        │   ├── 2.run_tk_chip_ccm
        │   ├── 2.run_tk_chip_transition
        │   ├── 4.run_retarget_mode1
        │   ├── 5.run_retarget_mode1_transition
        ├── netlist
        │   ├── run_dc_postlayout
        │   └── to_dc_for_flattening.tcl
        ├── run_all
    ```

[!NOTE]
Helper diagrams to be added here 

# Examples work in progress
- [4. Gate-level Dft insertion](./)
- [5. sub-block Dft insertion](./)

# DfT on NVDLA Accelerator

- [6.nvdla_edt_gate](6.nvdla_edt_gate/)

This example shows how to insert DfT (EDT, OCC) in the NVDLA accelerator across all it partitions. The examples uses the nv_small 
project. The synthesis and all DfT process has been implemented using the open source PDK from IHP. It is worth noting that the 
NVDLA memories are treated as blackboxes as they are not available in the IHP PDK. 

As the memoeries are not available the DfT does not incorporate MBIST.

It is worth noting that some Scan Cells use some sort of clock gating or clock selection requiring the innsertion of custom DfT control points. In addition some cell instances connected to TIE0 or TIE1 are required to be defined as non-scan. 


- [7.nvdla_edt_gate](7.nvdla_lbist_gate/)

This example shows how to insert DfT (EDT, OCC, LBIST) in the NVDLA accelerator across all it partitions. The examples uses the nv_small  project. The synthesis and all DfT process has been implemented using the open source PDK from IHP. It is worth noting that the  NVDLA memories are treated as blackboxes as they are not available in the IHP PDK. 

As the memoeries are not available the DfT does not incorporate MBIST.
