import sys,os,shutil
    ########################################
    # create tpr files for 50 transitions #
    ########################################
for framenum in range(1,51):      
    cmd = 'gmx grompp -f md.mdp -p topol.top -n md_nolig.ndx -c frame'+str(framenum)+'.gro -o tpr'+str(framenum)+'.tpr -maxwarn 1'
    os.system(cmd)
    #######################
    # run 50 transitions #
    # note that for this step you may need a fast GPU equipped machine #
    # another option is to run this step on a cluster #
    #######################
#for framenum in range(0,51):
#    cmd = 'gmx mdrun -v -deffnm tpr'+str(framenum)+' -pin on -ntomp 20 -nb gpu -pme gpu -bonded gpu'
#    os.system(cmd)
