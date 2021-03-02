import os
import sys
import string


def main():
	mail_domain = input("Mail domain (example: ...@domain.com) [Default: none]: ")
	domain =      input("Domain (example: domain\\...) [Default: none]: ") if mail_domain == '' else None

	format_text = "Choose username format:" + "\n"
	format_text += "1) gwashington" + "\n"
	format_text += "2) g.washington" + "\n"
	format_text += "3) georgewashington" + "\n"
	format_text += "4) george.washington" + "\n"
	format_text += ""
	format_text += ""
	format_option = input(format_text)

	names_,surnames_ = None, None
	
	if format_option == "3" or format_option == "4":
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