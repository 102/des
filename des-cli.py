import des
import argparse

parser = argparse.ArgumentParser()
group = parser.add_mutually_exclusive_group(required=True)
group.add_argument('-e', '--encode', dest='encode', action='store_true')
group.add_argument('-d', '--decode', dest='encode', action='store_false')
parser.add_argument('-w', '--word', required=True)
parser.add_argument('-i', '--initial-value', default='01234567')
parser.add_argument('-k', '--key', default='76543210')

args = parser.parse_args()

if args.encode:
    print(des.cfb_encrypt(word=args.word, key=args.key, iv=args.initial_value))
else:
    print(des.cfb_decrypt(cword=args.word, key=args.key, iv=args.initial_value))
