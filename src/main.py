#!/usr/bin/python3

from optparse import OptionParser
import sys

from macrogenerator.macrogenerator import MacroGenerator
from error.errorlibrary import get_error_lib
from error.log import Log

error_lib = get_error_lib()

if __name__ == "__main__":
    # CLI Parsing
    usage = "usage: %prog [options] input_file [output_file]"
    opt_parser = OptionParser(usage=usage)
    opt_parser.add_option("-s", "--silent", action="store_true", dest="silent",
                            default=False, help="turns off the error/warning output")
    opt_parser.add_option("-v", "--verbose", action="store_true", dest="verbose",
                            default=False, help="generates descriptive error/warning messages")
    opt_parser.add_option("-n", "--nowarn", action="store_false", dest="warnings",
                            default=True, help="mutes warning output")
    opt_parser.add_option("-o", "--output", action="store", type="string", dest="filename",
                            help="redirects the error/warning output to a file")
    (options, args) = opt_parser.parse_args()

    # CLI Errors/Warnings
    if options.silent and options.verbose:
        opt_parser.error("Options -s and -v are mutually exclusive.")
    if len(args) < 1:
        opt_parser.error("No input file provided!")
    if len(args) > 2:
        print("More than 2 arguments provided, excess arguments will be ignored.")
    
    # Assigning I/O variables
    if options.filename == None:
        log_out = sys.stdout
    else:
        log_out = open(options.filename, 'w')
    input_file = args[0]
    if len(args) == 1:
        output_file = "mg_out"
    else:
        output_file = args[1]
    if input_file == output_file:
        if not options.silent and options.warnings:
            warn = error_lib.get_error("w80")
            if options.verbose:
                warn_str = warn.what_long(None, [input_file])
            else:
                warn_str = warn.what_short(None)
            print(warn_str, file=log_out)

    # Get the input
    try:
        with open(input_file, 'r') as file:
            input_str = file.read()
    except FileNotFoundError as e:
        if not options.silent:
            er = error_lib.get_error("e98")
            if options.verbose:
                er_str = er.what_long(None, [e.strerror])
            else:
                er_str = er.what_short(None)
            print(er_str, file=log_out)
        exit()

    # Call the macro generator
    macro_generator = MacroGenerator()

    try:
        (output_str, logs) = macro_generator.transform(input_str)
    except Log as e:
        if not options.silent:
            print("Execution unsuccesful.", file=log_out)
            if options.verbose:
                er_str = error_lib.what_long(e)
            else:
                er_str = error_lib.what_short(e)
            print(er_str, file=log_out)
        exit()
    # Print warnings
    if len(logs) == 1:
        print("Execution completed with %d warning:" % len(logs), file=log_out)
    elif len(logs) > 1:
        print("Execution completed with %d warnings:" % len(logs), file=log_out)
    else:
        print("Execution completed with no warnings.", file=log_out)
    for log in logs:
        if not options.silent and options.warnings:
            if options.verbose:
                warn_str = error_lib.what_long(log)
            else:
                warn_str = error_lib.what_short(log)
            print(warn_str, file=log_out)

    # Output
    try:
        with open(output_file, 'w') as file:
            file.write(output_str)
    except FileNotFoundError as e:
        if not options.silent:
            er = error_lib.get_error("e98")
            if options.verbose:
                er_str = er.what_long(None, [e.strerror])
            else:
                er_str = er.what_short(None)
            print(er_str, file=log_out)
        exit()
