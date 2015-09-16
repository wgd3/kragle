#!/usr/bin/python


from jinja2 import Environment, FileSystemLoader 
from subprocess import call 
import argparse

parser = argparse.ArgumentParser()
parser.add_argument('--username', dest='username', help='Username used for subscription-manage', required=True)
parser.add_argument('--password', dest='password', help='Password used for subscription-maange', required=True)
parser.add_argument('--packer', dest='packer', help='Options required for packer', required=True)
args = parser.parse_args()


env = Environment(loader=FileSystemLoader('/opt/kragle/templates'))
#env = Environment(loader=FileSystemLoader('./templates'))
template = env.get_template('ks-isolinux-packer.cfg.j2')

output = template.render(submgr_username=args.username, submgr_password=args.password)

with open('/opt/kragle/kickstart-files/ks-isolinux-packer.cfg', 'w') as f:
#with open('./kickstart-files/ks-isolinux-packer.cfg', 'w') as f:
	f.write(output)

packer_args = args.packer.split()
packer_args.insert(0, '/opt/packer/packer')
call(packer_args)

