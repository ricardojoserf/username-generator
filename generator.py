import os
import sys
import string


def main():
	format_text = "Choose username format:" + "\n"
	format_text += "1) hsimpson" + "\n"
	format_text += "2) h.simpson" + "\n"
	format_text += "3) homersimpson" + "\n"
	format_text += "4) homer.simpson" + "\n"
	format_text += "5) hjsimpson" + "\n"
	format_text += "6) homerjsimpson" + "\n"
	format_text += "7) homerjaysimpson" + "\n"
	format_text += "8) homersimpsonb" + "\n"
	format_text += ""
	format_option = input(format_text)

	mail_domain = input("Mail domain (example: ...@domain.com) [Default: none]: ")
	domain =      input("Domain (example: domain\\...) [Default: none]: ") if mail_domain == '' else None

	names_,surnames_ = None, None
	if format_option == "3" or format_option == "4" or format_option == "6" or format_option == "7" or format_option == "8":
		names = input("Names file path: ")
		if not os.path.isfile(names):
			print("Error: Invalid names file path")
			sys.exit(0)
		names_ = open(names).read().splitlines()

	surnames = input("Surnames file path: ")
	if not os.path.isfile(surnames):
		print("Error: Invalid surnames file path")
		sys.exit(0)
	surnames_ = open(surnames).read().splitlines()

	combinations = get_usernames(format_option, names_, surnames_)
	output_file = input("Output file [Default: results.txt]: ") or "results.txt"
	output_to_file(combinations, output_file, mail_domain, domain)


def get_usernames(format_option, names_, surnames_):
	combinations = []
	letters_ = string.ascii_lowercase

	if format_option == "1":
		for s in surnames_:
			for l in letters_:
				combinations.append(l+s)

	elif format_option == "2":
		for s in surnames_:
			for l in letters_:
				combinations.append(l+"."+s)

	elif format_option == "3":
		for s in surnames_:
			for n in names_:
				combinations.append(n+s)

	elif format_option == "4":
		for s in surnames_:
			for n in names_:
				combinations.append(n+"."+s)

	elif format_option == "5":
		for s in surnames_:
			for l2 in letters_:
				for l in letters_:
					combinations.append(l+l2+s)

	elif format_option == "6":
		for s in surnames_:
			for l in letters_:
				for n in names_:
					combinations.append(n+l+s)

	elif format_option == "7":
		for s in surnames_:
			for n2 in names_:
				for n in names_:
					combinations.append(n+n2+s)

	elif format_option == "8":
		for s in surnames_:
			for n in names_:
				for l in letters_:
					combinations.append(n+s+l)

	else:
		print("Invalid option")

	return combinations


def output_to_file(combinations, output_file, mail_domain, domain):
	with open(output_file , 'w') as f:
		for c in combinations:
			if mail_domain != '':
				f.write("%s\n" % (c+"@"+mail_domain))
			elif domain != '':
				f.write("%s\n" % (domain+"\\"+c))
			else:
				f.write("%s\n" % (c))

	print ("Output saved in %s"%(output_file))


if __name__ == "__main__":
	main()