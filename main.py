import getopt
import subprocess
import sys
import os
from bs4 import BeautifulSoup


def main(argv):
    argv_list = argv[1:]
    arg_branch = None
    arg_verbose = False
    opts = []
    arg_help = "{0} -b <branch>".format(argv[0])

    # Options
    options = "hb:"

    # Long options
    long_options = ["Help", "branch=", "verbose"]

    try:
        # Parsing argument
        opts, args = getopt.getopt(argv_list, options, long_options)

        # checking each argument
        for opt, arg in opts:
            if opt in ("-h", "--help"):
                print(arg_help)
                sys.exit()

            elif opt in ("-b", "--branch"):
                arg_branch = arg

            elif opt in ("-v", "--verbose"):
                arg_verbose = True

    except getopt.error as err:
        # output error, and return with an error code
        print(str(err))

    if arg_branch is None:
        print(arg_help)

    check_out_if_need(arg_branch, arg_verbose)
    generate_jacoco_report(arg_verbose)
    find_coverage(arg_verbose)


def check_out_if_need(branch, verbose):
    # current branch
    output = subprocess.getoutput("git branch --show")
    if output != branch:
        check_out = subprocess.getoutput("git checkout branch")
        if verbose:
            print(check_out)


def generate_jacoco_report(verbose):
    # jacoco report
    output = subprocess.getoutput("./gradlew jacocoTestReport")
    if verbose:
        print(output)


def find_coverage(verbose):
    jacoco_path = "/app/build/reports/jacoco/jacocoTestReport/html/index.html"
    current_folder = os.getcwd()
    full_path = current_folder + jacoco_path
    with open(full_path) as fp:
        soup = BeautifulSoup(fp, 'html.parser')
        td = soup.find("tfoot").find_all("td", )
        print(td[2].text)


if __name__ == "__main__":
    main(sys.argv)
