import getopt
import subprocess
import sys

from bs4 import BeautifulSoup

jacoco_html_report_path = "/app/build/reports/jacoco/jacocoTestReport/html/index.html"
repo_path = "./"


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

        check_out_if_need(arg_branch, arg_verbose)
        generate_jacoco_report(arg_verbose)
        find_coverage(arg_verbose)

    except getopt.error as err:
        # output error, and return with an error code
        print(str(err))
    except Exception as e:
        print(e)


def check_out_if_need(branch, verbose):
    # current branch
    command = "git -C {} branch --show".format(repo_path)
    if verbose:
        print("Executing:: {}".format(command))
    output = subprocess.getoutput("git -C {} branch --show".format(repo_path))
    if verbose:
        print(output)
    if output != branch:
        check_out = subprocess.getoutput("git -C {} checkout branch".format(repo_path))
        if check_out.startswith('error: '):
            raise Exception(check_out)
        if verbose:
            print(check_out)


def generate_jacoco_report(verbose):
    # jacoco report
    command = "{}/gradlew -p {} jacocoTestReport".format(repo_path, repo_path)
    if verbose:
        print("Executing:: {}".format(command))
    output = subprocess.getoutput(command)
    if "FAILURE: " in output:
        raise Exception(output)
    if verbose:
        print(output)


def find_coverage(verbose):
    jacoco_path = jacoco_html_report_path
    current_folder = repo_path
    full_path = current_folder + jacoco_path
    try:
        if verbose:
            print("Opening:: {}".format(full_path))
        with open(full_path) as fp:
            soup = BeautifulSoup(fp, 'html.parser')
            td = soup.find("tfoot").find_all("td", )
            print(td[2].text)
    except IOError as e:
        raise Exception(e)


if __name__ == "__main__":
    main(sys.argv)
