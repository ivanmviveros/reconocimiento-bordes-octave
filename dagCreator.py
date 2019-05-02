#!/usr/bin/env python3
#generates a list of dagman jobs, this is a combinatory problem.
import numpy as np
JOB = 'JOB {} test_condor.condor\n'
VARIABLES = 'VARS {0} threshold="{1}"'

currentjob = 1
jobs = ""
variables = ""

for threshold in np.arange(0.1, 1, 0.1):    
    jobs += JOB.format('TEST'+str(currentjob))
    variables += VARIABLES.format('TEST'+str(currentjob), threshold)
    variables += '\n'
    currentjob+=1


dagmanFile = open('test_condor.dag', 'w')
dagmanFile.write(jobs)
dagmanFile.write('\n')
dagmanFile.write(variables)
