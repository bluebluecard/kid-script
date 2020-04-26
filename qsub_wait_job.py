import sys,time
import logging
import subprocess
import argparse

logging.basicConfig(level=logging.INFO,
                   format='%(asctime)s  %(message)s',
                   datefmt='%a, %d %b %Y %H:%M:%S',
                   filename = 'log.txt')

def run_args():

    parser = argparse.ArgumentParser()

    parser.add_argument("qsub_command",type=str,help=
            'commands submiting work shell through qsub')
    parser.add_argument("--job_id",type=str,default='',help=
            'job_ids in qstat need finishing,seperate with \',\',like 324,326,370')
    parser.add_argument("--id_file",type=str,default='',help=
            'job_ids in qstat need finishing,one line one job')
    parser.add_argument("--wait_day",type = float,default = 1.0,help='days need to be wait,default = 1 day')
    parser.add_argument("--check_interval",type = int,default = 600,help = 'time interval to check job status each circle,default=600s')

    return parser.parse_args()

def get_job_id(file_status,id_stream):
    id_list = []
    if file_status:
        with open(id_stream,'r') as f:
            for line in f:
                id_list.append(line.strip())
    else:
        id_list =id_stream.split(',')
    return id_list

def wait_log(wait_time,job_list):
    logging.info(','.join([str(j) for j in job_list])+' previous job still running!')
    time.sleep(wait_time)

def submit_log(qsub_shell):
    logging.info('previous job finished,the next job will be submited in a few seconds!')
    subprocess.call(word,shell=True)
    logginf.info('Job submited,this process will exit!')
    sys.exit()

def run():

    args = run_args()

    if args.job_id:
        target = get_job_id(0,args.job_id)
    elif args.id_file:
        target = get_job_id(1,args.id_file)
    else:
        logging.info("You can not run this process without job_id which need waiting!This process will bed terminated!")
        sys.exit()

    total_circle = int(args.wait_day*24*60*60/args.check_interval)
    for i in range(total_circle):

        job_table = subprocess.check_output('qstat').decode('utf-8')
        job_id = [j.split()[0] for j in job_table.split('\n')[2:-1] ]

        if set(target).intersection(set(job_id)):
            wait_log(args.check_interval,list(set(target).intersection(set(job_id))))
        else:
            submit_log(args.qsub_command)

run()

    else:

        logging.info('previous job finished,the next job will be submited in a few seconds!')
        subprocess.call(word,shell=True)
        logginf.info('Job submited,this process will exit!')
        sys.exit()
