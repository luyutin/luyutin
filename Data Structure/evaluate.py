import json
import argparse

if __name__ == '__main__':
    parser = argparse.ArgumentParser()
    parser.add_argument('--output', default='output_1.json')
    parser.add_argument('--golden', default='golden_1.json')
    args = parser.parse_args()
    try:
        json_output = json.load(open(args.output, "r"))
        json_golden = json.load(open(args.golden, "r"))
        correct = json_output == json_golden
    except:
        correct = False
    print("correctness of %s : %s" % (args.output, correct))
