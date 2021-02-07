import argparse
import psycopg2

parser = argparse.ArgumentParser()
parser.add_argument("-u", "--username", dest="username", type=str, action='store')
parser.add_argument("-p", "--password", dest="password", type=str, action='store')
parser.add_argument("-n", "--new-pass", dest="new_pass", type=str, action='store')
parser.add_argument("-l", "--list", dest="list", action='store_true')
parser.add_argument("-d", "--delete", dest="delete", action='store_true')
parser.add_argument("-e", "--edit", dest="edit", action='store_true')
args = parser.parse_args()
 

