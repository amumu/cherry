import cherry
import argparse

parser = argparse.ArgumentParser(description='Native bayes testing.')
parser.add_argument(
    '-l', '--language', type=str, default='Chinese',
    help='Which language\'s dataset we will use')
parser.add_argument(
    '-t', '--test_time', type=int, default=10,
    help='How many times we split data for testing')
parser.add_argument(
    '-n', '--num', type=int, default=60,
    help='How many test data we need every time')
parser.add_argument(
    '-p', dest='positive', const=True, action='store_const',
    help='Draw ROC curve or not')
parser.add_argument(
    '-d', dest='debug', const=True, action='store_const',
    help='Show wrong classified data when testing')
args = parser.parse_args()


def main():
    print('This may take 5 minutes, Go get a coffee :D.')
    a = cherry.analysis(
        lan=args.language, test_time=args.test_time,
        test_num=args.num, debug=args.debug, positive=args.positive)
    print(a.ctable)


if __name__ == '__main__':
    main()
