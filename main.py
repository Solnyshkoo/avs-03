from Container import Container

import sys
import logging
import time

USAGE_HINT = """
Input format:
-n <amount> <output_file before sort> <output file after sort> <logs file (.log)>
-f <input file> <output_file before sort> <output file after sort> <logs file (.log)>
"""


def main():
    start_time = time.time()
    if len(sys.argv) == 6:
        # -n 1000 output.txt output2.txt
        codec = sys.argv[1]

        logger_file = sys.argv[5]

        logger = logging.getLogger("Vehicles")
        logger.setLevel(logging.ERROR)

        # create the logging file handler
        fh = logging.FileHandler(logger_file)

        formatter = logging.Formatter('%(asctime)s - %(name)s - %(levelname)s - %(message)s')
        fh.setFormatter(formatter)

        # add handler to logger object
        logger.addHandler(fh)

        if codec == '-n':
            amount = int(sys.argv[2])
            output_file = sys.argv[3]

            t = Container(randomly=True, amount=amount, logger=logger)
            t.to_file(output_file)

            output_file_2 = sys.argv[4]

            t.shaker_sort()

            t.to_file(output_file_2)

        elif codec == '-f':
            input_file = sys.argv[2]
            output_file = sys.argv[3]

            t = Container(filename=input_file, logger=logger)

            t.to_file(output_file)

            output_file_2 = sys.argv[4]

            t.shaker_sort()

            t.to_file(output_file_2)

        else:
            sys.stdout.write(str(sys.argv))
            sys.stdout.write('Wrong input format! Use this hint:\n' + USAGE_HINT)
            return 1

    else:
        sys.stdout.write('Wrong input format! Use this hint:\n' + USAGE_HINT)
        return 1

    end_time = time.time()
    eval_time = end_time - start_time
    print(eval_time)


if __name__ == '__main__':
    main()
