from replica_failover import write_test
import sys
def main():
    write_test(sys.argv[0] == 'true')

main()