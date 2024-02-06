import sys
import os

def createfiles(filename):
    name=str(filename)
    top=name+"_top.sv" ##
    test=name+"_test.sv" ##
    env=name+"_env.sv"  ##
    seq=name+"_seq.sv"  ##
    agent=name+"_agent.sv"  ##
    scb=name+"_scb.sv"  ##
    sub=name+"_sub.sv"  ##
    seqr=name+"_seqr.sv"  ##
    dri=name+"_dri.sv"  ##
    mon=name+"_mon.sv"  ##
    seq_item=name+"_seq_item.sv"  ##
    
    
#topfile
    with open(top,'w') as topfile:
        topfile.write('import uvm_pkg::*;\n')
        topfile.write(f'module {name}_top;\n')
        topfile.write('endmodule')
#testfile
    with open(test,'w') as testfile:
        testfile.write('import uvm_pkg::*;\n')
        testfile.write(f'class {name}_test extends uvm_test;\n')
        testfile.write(f'  {name}_seq ;\n')
        testfile.write(f'  {name}_env ;\n')
        testfile.write(f'  `uvm_component_utils({name}_test)\n')
        testfile.write('endclass')
#envfile
    with open(env,'w') as envfile:
        envfile.write('import uvm_pkg::*;\n')
        envfile.write(f'class {name}_env extends uvm_env;\n')
        envfile.write(f'  {name}_agent ;\n')
        envfile.write(f'  {name}_scb ;\n')
        envfile.write(f'  {name}_sub ;\n')
        envfile.write(f'  `uvm_component_utils({name}_env)\n')
        envfile.write('endclass')
#agentfile
    with open(agent,'w') as agentfile:
        agentfile.write('import uvm_pkg::*;\n')
        agentfile.write(f'class {name}_agent extends uvm_agent;\n')
        agentfile.write(f'  {name}_sqcr ;\n')
        agentfile.write(f'  {name}_dri ;\n')
        agentfile.write(f'  {name}_mon ;\n')
        agentfile.write(f'  `uvm_component_utils({name}_agent)\n')
        agentfile.write('endclass')
#sequencefile
#object utils
    with open(seq,'w') as seqfile:
        seqfile.write('import uvm_pkg::*;\n')
        seqfile.write(f'class {name}_sequence extends uvm_sequence#({name}_seq_item);\n')
        seqfile.write(f'  `uvm_object_utils({name}_sequence)\n')
        seqfile.write('endclass')
        
#scoreboard
    with open(scb,'w') as scbfile:
        scbfile.write('import uvm_pkg::*;\n')
        scbfile.write(f'class {name}_scoreboard extends uvm_scoreboard;\n')
        scbfile.write(f'  `uvm_component_utils({name}_scoreboard)\n')
        scbfile.write('endclass')

#subscriber
    with open(sub,'w') as subfile:
        subfile.write('import uvm_pkg::*;\n')
        subfile.write(f'class {name}_subscriber extends uvm_subscriber;\n')
        subfile.write(f'  `uvm_component_utils({name}_subscriber)\n')
        subfile.write('endclass')

#sequencer
    with open(seqr,'w') as seqrfile:
        seqrfile.write('import uvm_pkg::*;\n')
        seqrfile.write(f'class {name}_sequencer extends uvm_sequencer#({name}_seq_item);\n')
        seqrfile.write(f'  `uvm_component_utils({name}_sequencer)\n')
        seqrfile.write('endclass')

#driver
    with open(dri,'w') as drifile:
        drifile.write('import uvm_pkg::*;\n')
        drifile.write(f'class {name}_driver extends uvm_driver#({name}_seq_item);\n')
        drifile.write(f'  `uvm_component_utils({name}_driver)\n')
        drifile.write('endclass')

#monitor
    with open(mon,'w') as monfile:
        monfile.write('import uvm_pkg::*;\n')
        monfile.write(f'class {name}_monitor extends uvm_monitor;\n')
        monfile.write(f'  `uvm_component_utils({name}_monitor)\n')
        monfile.write('endclass')

#seq_item
    with open(seq_item,'w') as seq_item_file:
        seq_item_file.write('import uvm_pkg::*;\n')
        seq_item_file.write(f'class {name}_seq_item extends uvm_sequence_item;\n')
        seq_item_file.write(f'  `uvm_object_utils({name}_seq_item)\n')
        seq_item_file.write('endclass')



if len(sys.argv)==2:
    filename=sys.argv[1]
    createfiles(filename)
else:
    print("Enter filename")
