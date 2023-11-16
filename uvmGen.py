import sys

def createfiles(filename):
    name=str(filename)
    top=name+"_top.sv"
    test=name+"_test.sv"
    env=name+"_env.sv"
    seq=name+"_seq.sv"
    agent=name+"_agent.sv"
    scb=name+"_scb.sv"
    sub=name+"_sub.sv"
    seqr=name+"_seqr.sv"
    dri=name+"_dri.sv"
    mon=name+"_mon.sv"
    seq_item=name+"_seq_item.sv"
    
    
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
    with open(seq,'w') as seqfile:
        seqfile.write('import uvm_pkg::*;\n')
        seqfile.write(f'class {name}_sequence extends uvm_sequence#({name}_seq_item);\n')
        seqfile.write(f'  `uvm_component_utils({name}_sequence)\n')
        seqfile.write('endclass')


if len(sys.argv)==2:
    filename=sys.argv[1]
    createfiles(filename)
else:
    print("Enter filename")
