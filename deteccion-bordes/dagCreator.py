#!/usr/bin/env python3
#generates a list of dagman jobs, this is a combinatory problem.
import numpy as np
JOB = 'JOB {} test_condor.condor\n'
VARIABLES = 'VARS {0} filename="{1}" threshold="{2}"'

currentjob = 1
jobs = ""
variables = ""
files = ['rubik.png', 'rubik8.png']

for threshold in np.arange(0.1, 10.0, 0.1):        
    for filename in files:
        jobs += JOB.format('TEST'+str(currentjob))
        variables += VARIABLES.format('TEST'+str(currentjob), filename,  float(threshold))
        variables += '\n'
        currentjob+=1


dagmanFile = open('test_condor.dag', 'w')
dagmanFile.write(jobs)
dagmanFile.write('\n')
dagmanFile.write(variables)
