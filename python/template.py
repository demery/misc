#!/usr/bin/env python

# #!/usr/bin/env python - will search for the first python 
#                         interpreter on your path
# unlike
# #!/usr/bin/python2.5  - which will only run if there is a file 
#                         python 2.5 is installed at /usr/bin
"""Module summary

If you import this module and do help (module) you'll see this.
The first line of a docstring is the "summary", and should be
a one line description.

You can go into more detail after the summary if needed.
See http://www.python.org/dev/peps/pep-0257/
for the python docstring style guide.
"""

# optparse is both easy to use and produces clean code
# the main optparse docs can be found here:
# http://docs.python.org/library/optparse.html
# there's a much better tutorial that works you through optparse
# starting with a simple example and slowly adding complexity.
from optparse import OptionParser
import os
import sys


def main(cmdline=None):
    """Example main function.
    
    If cmdline is none, parser.parse_args will look at 
    sys.argv[1:] by default

    However if import this module in python call this main function
    like this:
    
    main(["-n", "3", "asdf", "jkl"])
    
    in addition to running it from the shell.
    """
    parser = make_parser()

    opts, args = parser.parse_args(cmdline)

    if opts.error is not None:
        return opts.error
    elif opts.bad_option:
        # you can call parser.error, which will show an error message
        # displays the help, and then exits the program
        parser.error("you called a bad option")
    elif opts.make_template:
        make_template()
        return 0

    # args is now just a list, of everything that wasn't an
    # "option". AKA everything that started with - or --
    for i in range(len(args)):
        print "arg %d: %s" % (i, args[i])

    print "the number is:", opts.number
    # opts.number is always defined, as I set a default value 
    # up in the make_parser
    
    return 0


def make_parser():
    """Construct an option parser"""

    usage = """%prog: args

Sometimes you might explain the purpose of this program as well.
"""
    
    parser = OptionParser(usage)

    # add_options takes at least one long option
    # you can optionally include a short option.
    # - are one character (short) options (e.g. -h)
    #
    # -- are long options, the name is also used as the 
    #    variable name attached that holds the option

    parser.add_option("-e", "--error", help="set error code")

    # opt_parse can be configured to store different kinds of values
    # like filenames, and boolean options
    parser.add_option("-b", "--bad-option", action="store_true",
                      help="trigger an option error")
    
    # you can also do simple type checking on parameters
    parser.add_option("-n", "--number", help="set a number", type="int")

    # if needed you can tell optparse to use a different variable name.
    # with the dest argument.
    parser.add_option("--index", dest="createRDSIndex", action="store_true")

    parser.add_option("--make-template", action="store_true",
                      help="print a simplified template")
    parser.set_defaults(bad_option=False, 
                        createRDSIndex=False,
                        error=None,
                        make_template=False,
                        number=0)

    return parser

def make_template():
    """Read current source file and print a version with no comments

    run like:
    $ script.py --make-template > my_program.py
    """
    import re
    source = open( __file__,'r' )
    for line in source:
        # include the starting #!, but remove comments
        if not re.match(" *#[^!]", line):
            sys.stdout.write(line)
    
if __name__ == "__main__":
    # this runs when the application is run from the command
    # it grabs sys.argv[1:] which is everything after the program name
    # and passes it to main
    # the return value from main is then used as the argument to
    # sys.exit, which you can test for in the shell.
    # program exit codes are usually 0 for ok, and non-zero for something
    # going wrong.
    sys.exit(main(sys.argv[1:]))

# Try the following examples
# python script_template.py
# python script_template.py --help
# ./script_template.py a b c
# ./script_template.py --bad-option
# python ./script_template.py -n 4
# python ./script_template.py --number foo
#
#
# Guido von Rossum (inventor of python) has this write up on how to
# write a main
# http://www.artima.com/weblogs/viewpost.jsp?thread=4829
# however he used the older getopt module which isn't as easy
# to configure as optparse
