import sys
import time
import logging
import subprocess


target = sys.argv[1].split(',')
word = sys.argv[2]

logging.basicConfig(level=logging.INFO,
                   format='%(asctime)s  %(message)s',
                   datefmt='%a, %d %b %Y %H:%M:%S',
                   filename = 'log.txt')



for i in range(100):

    job_table = subprocess.check_output('qstat').decode('utf-8')
    job_list = job_table.split('\n')[2:-1]
    job_id = []

    for j in job_list:
        job_id.append(j.split()[0])

    if set(target).intersection(set(job_id)):

        logging.info('previous job still running!')
        time.sleep(600)

    else:

        logging.info('previous job finished,the next job will be submited in a few seconds!')
        subprocess.call(word,shell=True)
        logginf.info('Job submited,this process will exit!')
        sys.exit()
