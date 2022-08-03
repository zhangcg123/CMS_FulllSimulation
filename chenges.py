import os
import sys
import glob

new_ = str(sys.argv[1])

fs = glob.glob('*_cfg.py')
for f in fs:
	print '\n','\n'
	print f
	with open(f,'r') as fin:
		for i_,l in enumerate(fin):
			i = i_	
			new = new_
			if 'input = cms.untracked.int32' in l:
				new = new_
				print l.strip()
				old = l.split('int32')[-1].strip('\n').strip("()")
				old = 'int32('+old+')'
				new = 'int32('+new+')'
				l = l.strip()
				print 'sed -i "'+str(i+1)+'s/'+old+'/'+new+'/g" ' + f
				os.system( 'sed -i "'+str(i+1)+'s/'+old+'/'+new+'/g" ' + f )
			if ' nevts:' in l:
				new = new_
				print '\n'
				print l.strip()
				old = l.split(':')[-1].strip('\n').strip(",").strip(")").strip("'")
				old = 'nevts:'+old
				new = 'nevts:'+new
				l = l.strip()
				print 'sed -i "'+str(i+1)+'s/'+old+'/'+new+'/g" ' + f 
				os.system( 'sed -i "'+str(i+1)+'s/'+old+'/'+new+'/g" ' + f )
			if 'nEvents = cms.untracked.uint32' in l:
				new = new_
				print '\n'
				print l.strip()
				old = l.split('uint32')[-1].strip('\n').strip(",").strip("()")
				old = 'uint32('+old+')'
				new = 'uint32('+new+')'
				l = l.strip()
				print 'sed -i "'+str(i+1)+'s/'+old+'/'+new+'/g" ' + f
				os.system( 'sed -i "'+str(i+1)+'s/'+old+'/'+new+'/g" ' + f )
