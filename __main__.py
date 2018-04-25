from replica_failover import write_test
import sys
def main():
    write_test(len(sys.argv) == 2 and sys.argv[1] == 'true')

main()