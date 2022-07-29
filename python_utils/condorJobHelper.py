import os
import sys

class condorJobHelper(object):
    """docstring for condorJobHelper"""
    def __init__(self, fileName="test",
                 listOfFilesToTransfer="",
                 request_memory=0,
                 request_cpus=0,
                 Destination = 'TEST',
                 Arguments="",
                 Queue=1,
		 jobflavour = 'espresso'):
        self.fileName = fileName
        self.listOfFilesToTransfer = listOfFilesToTransfer
        self.request_memory = request_memory
        self.request_cpus = request_cpus
        self.Destination = Destination
        self.Arguments = Arguments
        self.Queue = Queue
	self.jobflavour = jobflavour

    def jdlFileHeaderCreater(self):
        outJdl = open(self.fileName+'.jdl','w')
        outJdl.write('Proxy_path = /afs/cern.ch/user/c/chenguan/private/voms_proxy.txt')
	outJdl.write('\n')
	outJdl.write('Executable = '+self.fileName+'.sh')
	outJdl.write('\n')
        outJdl.write('\n'+'Universe = vanilla')
	outJdl.write('\n')
        outJdl.write('\n'+'Notification = ERROR')
	outJdl.write('\n')
        outJdl.write('\n'+'Should_Transfer_Files = YES')
	outJdl.write('\n')
        outJdl.write('\n'+'WhenToTransferOutput = ON_EXIT')
	outJdl.write('\n')
        outJdl.write('\n'+'Transfer_Input_Files = '+self.fileName+'.sh, ' + self.listOfFilesToTransfer)
	outJdl.write('\n')
        #outJdl.write('\n'+'x509userproxy = $ENV(X509_USER_PROXY)')
	outJdl.write('\n')
	outJdl.write('\n'+'+JobFlavour = '+self.jobflavour)
	outJdl.write('\n')
	outJdl.write('\n'+'output_destination = ' + self.Destination)
	outJdl.write('\n')
	outJdl.write('\n'+'transfer_output_files = out_$(Cluster)_$(Process).root')
	outJdl.write('\n')
        if self.request_memory != 0: outJdl.write('\n'+'request_memory = '+str(self.request_memory))
        if self.request_cpus != 0: outJdl.write('\n'+'request_cpus = '+ str(self.request_cpus))
        return self.fileName+'.jdl'

    def jdlFileAppendLogInfo(self):
        outJdl = open(self.fileName+'.jdl','a')
        outJdl.write('\n')
	outJdl.write('\n'+'Output = outs/$(Cluster)_$(Process).out')
        outJdl.write('\n'+'Error  = errors/$(Cluster)_$(Process).err')
        outJdl.write('\n'+'Log  = logs/$(Cluster)_$(Process).log')
        outJdl.write('\n'+'Arguments = $(Proxy_path) $(Cluster) $(Process) '+self.Arguments)
        outJdl.write('\n'+'Queue '+str(self.Queue))
        outJdl.close()

    def shFileHeaderCreater(self):
        outScript = open(self.fileName+".sh","w");
        outScript.write('#!/bin/bash')
        outScript.write('\n'+'echo "Starting job on " `date`')
        outScript.write('\n'+'echo "Running on: `uname -a`"')
        outScript.write('\n'+'echo "System software: `cat /etc/redhat-release`"')
        outScript.write('\n'+'source /cvmfs/cms.cern.ch/cmsset_default.sh')
        outScript.write('\n'+'echo "'+'#'*51+'"')
        outScript.write('\n'+'echo "#    List of Input Arguments: "')
        outScript.write('\n'+'echo "'+'#'*51+'"')
        outScript.write('\n'+'echo "Input Arguments (CluserID): $1" ')
        outScript.write('\n'+'echo "Input Arguments (ProcessID): $2" ')
        for x in xrange(3,len(self.Arguments)+3):
            outScript.write('\n'+'echo "Input Arguments: $'+x+'" ')
        outScript.write('\n'+'echo "'+'#'*51+'"')
        outScript.write('\n'+'')
        outScript.close()
        return self.fileName+'.sh'

    def jdlAndShFileCreater(self):
        jdlFile = self.jdlFileHeaderCreater()
        jdlFile = self.jdlFileAppendLogInfo()
        shFile = self.shFileCreater()
        return jdlFile, shFile
