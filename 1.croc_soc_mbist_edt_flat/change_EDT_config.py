import os

def update_croc_chip(filepath, filepath_template, input_channel_count, output_channel_count):
        with open(filepath_template, 'r') as template, open(filepath, 'w') as outfile:
            for line in template:
                if '<ADD EXTRA INPUT PINS>' in line:
                    for i in range(3, 3 + input_channel_count): # the first 3 input signals are used as scan_en, edt_update and test_clock
                        outfile.write(f"  input  wire unused{i}_i,\n")
                    
                elif '<ADD EXTRA OUTPUT PINS>' in line:
                    for i in range(4, 4 + output_channel_count):# the first 4 output signals were present from original croc source code
                        outfile.write(f"  output wire unused{i}_o,\n")

                elif '<ADD IOPADOUT16MA IN>' in line:
                    for i in range(3, 3 + input_channel_count):
                        outfile.write(f"    sg13g2_IOPadIn pad_unused{i}_i (.pad(unused{i}_i), .p2c() );\n")

                elif '<ADD IOPADOUT16MA OUT>' in line :
                    for i in range(4, 4 + output_channel_count):
                        outfile.write(f"    sg13g2_IOPadOut16mA pad_unused{i}_o      (.pad(unused{i}_o),    .c2p());\n")
                
                else:
                    outfile.write(line)


def update_run_insert_bscan_mbist(filepath, input_channel_count, output_channel_count):
    '''Update step 1 MBIST'''
    with open(filepath + 'TEMPLATE', 'r') as template, open(filepath, 'w') as outfile:
        for line in template:
            if '<ADD AUXILIARY INPUT PORTS>' in line:
                newline = '    auxiliary_input_ports  : unused0_i, unused1_i, unused2_i,' # these 3 signals are used as scan_en, edt_update and test_clock
                for i in range(3, 3 + input_channel_count):
                    newline = newline + f" unused{i}_i,"
                
                outfile.write(newline[:-1] + ' ;\n')

            elif '<ADD AUXILIARY OUTPUT PORTS>' in line:
                newline = '    auxiliary_output_ports  :'
                for i in range(4, 4 + output_channel_count): # first 3 "unused*_i" are used in the original design of croc
                    newline = newline + f" unused{i}_o,"

                outfile.write(newline[:-1] + ' ;\n')
            else:
                outfile.write(line)

def update_run_insert_occ_edt(filepath, longest_chain_range, scan_chain_count, input_channel_count, output_channel_count):
    '''Update step 2 EDT params'''
    
    with open(filepath+'TEMPLATE', 'r') as template, open(filepath, 'w') as outfile:
        for line in template:
            if '<ADD EDT INPUT PINS>' in line:
                for i in range(3, 3 + input_channel_count):
                    outfile.write(f"add_dft_control_points [get_auxiliary_pins unused{i}_i -enable -direction input] -dft_signal_source_name ltest_en\n")

            elif '<ADD EDT OUTPUT PINS>' in line:
                for i in range(4, 4 + output_channel_count):
                    outfile.write(f"add_dft_control_points [get_auxiliary_pins unused{i}_o -enable -direction output] -dft_signal_source_name ltest_en\n")
    
            elif '<SET LONGEST CHAIN RANGE>' in line:
                outfile.write(f"         longest_chain_range : {longest_chain_range[0]}, {longest_chain_range[1]};\n")

            elif '<SET SCAN CHAIN COUNT>' in line:
                outfile.write(f"         scan_chain_count : {scan_chain_count};\n")

            elif '<SET INPUT CHANNEL COUNT>' in line:
                outfile.write(f"         input_channel_count : {input_channel_count};\n")

            elif '<SET OUTPUT CHANNEL COUNT>' in line:
                outfile.write(f"         output_channel_count : {output_channel_count};\n")

            elif '<ADD EXTRA EdtChannelsIn>' in line:
                for i in range(1, 1 + input_channel_count):
                    outfile.write(f"            EdtChannelsIn({i}) " + "{\n")
                    outfile.write('            }\n')
            
            elif '<ADD EXTRA EdtChannelsOut>' in line:
                for i in range(1, 1 + output_channel_count):
                    outfile.write(f"            EdtChannelsOut({i}) " + "{\n")
                    outfile.write('            }\n')

            elif '<ADD EXTRA INPUT SPECIFICATION>' in line:
                for i in range(1, 1 + input_channel_count):
                    outfile.write("set_config_value port_pin_name \\" + '\n')
                    outfile.write(f"-in $spec/EDT/Controller(c1)/Connections/EdtChannelsIn({i}) [get_single_name [get_auxiliary_pins unused{i + 2}_i -direction input]]" + '\n')

            elif '<ADD EXTRA OUTPUT SPECIFICATION>' in line:
                for i in range(1, 1 + output_channel_count):
                    outfile.write("set_config_value port_pin_name \\" + '\n')
                    outfile.write(f"-in $spec/EDT/Controller(c1)/Connections/EdtChannelsOut({i}) [get_single_name [get_auxiliary_pins unused{i + 3}_o -direction output] ]" + '\n')

            else:
                outfile.write(line)

def main():
    filepath_step1 = './1.insert_bscan_mbist/run_insert_bscan_mbist'
    filepath_step2 = './2.insert_occ_edt/run_insert_occ_edt'
    filepath_croc_chip = './croc/rtl/croc_chip.sv'
    filepath_croc_chipTemplate = './croc_chip.svTEMPLATE'

    input_channel_count = 3
    output_channel_count = 3
    longest_chain_range = [65, 100]
    scan_chain_count = 100

    update_run_insert_bscan_mbist(filepath_step1, input_channel_count, output_channel_count)
    update_run_insert_occ_edt(filepath_step2, longest_chain_range, scan_chain_count, input_channel_count, output_channel_count)
    update_croc_chip(filepath_croc_chip, filepath_croc_chipTemplate, input_channel_count, output_channel_count)

if __name__ == '__main__':
    main()