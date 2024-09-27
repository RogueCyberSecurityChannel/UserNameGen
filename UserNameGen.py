import argparse
import sys
from os import path

def welcome():
  print(r'''
 _____             _____               _____         
|  |  |___ ___ ___|   | |___ _____ ___|   __|___ ___ 
|  |  |_ -| -_|  _| | | | .'|     | -_|  |  | -_|   |
|_____|___|___|_| |_|___|__,|_|_|_|___|_____|___|_|_|
''')

def parse_args():

  parser = argparse.ArgumentParser(prog='UserNameGen.py', description='A Simple CMD Line Username Generator {GitHub:https://github.com/RogueCyberSecurityChannel}')

  parser.add_argument('-u', '--user-file', dest='users_file',  metavar='users.txt', type=str,
                    help='A list of First and Last names to generate usernames from. Example: "users.txt"')
  parser.add_argument('-o', '--output-file', dest='output_file', metavar='output.txt', type=str,
                    help='Output file for generated usernames. Example: "output.txt"')
  parser.add_argument('-d', '--domain-name', dest='domain', metavar='@domain.com', type=str,
                    help='Domain name you would like to append to generated usernames. Example: "@domain.com"')

  parser.set_defaults(users_file=False, output_file=False, domain=False)

  args = parser.parse_args(sys.argv[1:])
  arg_errors = arg_error_check(args)

  if len(arg_errors) > 0:
        for error in arg_errors:
            print("[-] {0}".format(error))
            print()
        parser.print_help()
        sys.exit(1)

  return args

def arg_error_check(args):

  arg_errors = []

  if args.users_file and args.output_file and args.domain and len(vars(args)) == 3:
      if(path.exists(args.output_file)):
        arg_errors.append('The file \"' + args.output_file + '\" already exists')
  else:
    arg_errors.append('Argument error. Example: "UserNameGen.py UserNameGene.py -u <user file> -o <output file> -d <domain> "')
  return arg_errors

def generator(user_file,output_file,domain):
  output = open(output_file,'w')
  nb_user=0
  with open(user_file) as fp:
    line = fp.readline().lower()
    while line:

       list_name=line.strip().split()

       if(len(list_name)!=2):
            print("Warning: The line \"" + line.rstrip() + "\" inside " + user_file  + " is not correct. The data must be formatted with this format: [first name] [surname]")
            line = fp.readline().lower()
       else:
         #### Just the Name
         output.write(list_name[1]+ domain + '\n')
         #### Just the firstname
         output.write(list_name[0] +  domain + '\n')
         #### firstname.name
         output.write(list_name[0] + "." + list_name[1] + domain + '\n')
         #### name.firstname
         output.write(list_name[1] + "." + list_name[0] + domain + '\n')
         #### firstname-name
         output.write(list_name[0] + "-" + list_name[1] + domain + '\n')
         #### name-firstname
         output.write(list_name[1] + "-" + list_name[0] + domain + '\n')
         #### firstnamename
         output.write(list_name[0] + list_name[1] +  domain + '\n')
         #### namefirstname
         output.write(list_name[1] + list_name[0] + domain + '\n')
         #### firstname_name
         output.write(list_name[0] + "_" + list_name[1] + domain + '\n')
         #### name_firstname
         output.write(list_name[1] + "_" + list_name[0] + domain + '\n')
         #### F.name
         output.write(list_name[0][0] + "." + list_name[1] + domain + '\n')
         #### N.firstname
         output.write(list_name[1][0] + "." + list_name[0] + domain +  '\n')
         #### name.F
         output.write(list_name[1] + "." + list_name[0][0] + domain + '\n')
         #### firstname.N
         output.write(list_name[0] + "." + list_name[1][0] + domain + '\n')
         #### F-name
         output.write(list_name[0][0] + "-" + list_name[1] + domain + '\n')
         #### N-firstname
         output.write(list_name[1][0] + "-" + list_name[0] +  domain + '\n')
         #### name-F
         output.write(list_name[1] + "-" + list_name[0][0] +  domain + '\n')
         #### firstname-N
         output.write(list_name[0] + "-" + list_name[1][0] +  domain + '\n')
         #### Fname
         output.write(list_name[0][0] + list_name[1] + domain + '\n')
         #### Nfirstname
         output.write(list_name[1][0] + list_name[0] + domain + '\n')
         #### nameF
         output.write(list_name[1] + list_name[0][0] + domain + '\n')
         #### firstnameN
         output.write(list_name[0] + list_name[1][0] + domain + '\n')
         #### F_name
         output.write(list_name[0][0] + "_" + list_name[1] + domain + '\n')
         #### N_firstname
         output.write(list_name[1][0] + "_" + list_name[0] + domain + '\n')
         #### name_F
         output.write(list_name[1] + "_" + list_name[0][0] + domain + '\n')
         #### firstname_N
         output.write(list_name[0] + "_" + list_name[1][0] + domain + '\n')

         #put maj
         list_name[0]=list_name[0].capitalize()
         list_name[1]=list_name[1].capitalize()

         #### Just the Name with uppercase
         output.write(list_name[1]+'\n')
         #### Just the firstname with uppercase
         output.write(list_name[0] + '\n')
         #### firstname.name with uppercase
         output.write(list_name[0] + "." + list_name[1] + domain + '\n')
         #### name.firstname with uppercase
         output.write(list_name[1] + "." + list_name[0] + domain + '\n')
         #### firstname-name with uppercase
         output.write(list_name[0] + "-" + list_name[1] + domain +  '\n')
         #### name-firstname with uppercase
         output.write(list_name[1] + "-" + list_name[0] + domain +  '\n')
         #### firstnamename with uppercase
         output.write(list_name[0] + list_name[1] + domain +  '\n')
         #### namefirstname with uppercase
         output.write(list_name[1] + list_name[0] + domain +  '\n')
         #### firstname_name with uppercase
         output.write(list_name[0] + "_" + list_name[1] + domain +  '\n')
         #### name_firstname with uppercase
         output.write(list_name[1] + "_" + list_name[0] + domain +  '\n')
         #### F.name with uppercase
         output.write(list_name[0][0] + "." + list_name[1] + domain +  '\n')
         #### N.firstname with uppercase
         output.write(list_name[1][0] + "." + list_name[0] + domain +  '\n')
         #### name.F with uppercase
         output.write(list_name[1] + "." + list_name[0][0] + domain +  '\n')
         #### firstname.N with uppercase
         output.write(list_name[0] + "." + list_name[1][0] + domain +  '\n')
         #### F-name with uppercase
         output.write(list_name[0][0] + "-" + list_name[1] + domain +  '\n')
         #### N-firstname with uppercase
         output.write(list_name[1][0] + "-" + list_name[0] + domain +  '\n')
         #### name-F with uppercase
         output.write(list_name[1] + "-" + list_name[0][0] + domain +  '\n')
         #### firstname-N with uppercase
         output.write(list_name[0] + "-" + list_name[1][0] + domain +  '\n')
         #### Fname with uppercase
         output.write(list_name[0][0] + list_name[1] + domain +  '\n')
         #### Nfirstname with uppercase
         output.write(list_name[1][0] + list_name[0] + domain +  '\n')
         #### nameF with uppercase
         output.write(list_name[1] + list_name[0][0] + domain +  '\n')
         #### firstnameN with uppercase
         output.write(list_name[0] + list_name[1][0] + domain +  '\n')
         #### F_name with uppercase
         output.write(list_name[0][0] + "_" + list_name[1] + domain +  '\n')
         #### N_firstname with uppercase
         output.write(list_name[1][0] + "_" + list_name[0] + domain +  '\n')
         #### name_F with uppercase
         output.write(list_name[1] + "_" + list_name[0][0] + domain +  '\n')
         #### firstname_N with uppercase
         output.write(list_name[0] + "_" + list_name[1][0] + domain +  '\n')

         line = fp.readline().lower()
         nb_user+=52

    print('[*] Number of users created: ' + str(nb_user) )
    print("[+] Usernames written to output file " + output_file)

def main():

  welcome()
  args = parse_args()
  generator(args.users_file, args.output_file, args.domain)

if __name__ == '__main__':
    main()
