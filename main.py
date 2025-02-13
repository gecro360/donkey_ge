#! /usr/bin/env python


"""
Main module for the donkey_ge project.

This module parses YML configuration files and calls the `donkey_ge` function.
It is the entry point for running the genetic programming-based heuristics.

Author: Erik Hemberg
"""

__author__ = "Erik Hemberg"

import sys
import argparse
from typing import Any, Dict, List


import yaml


from heuristics import donkey_ge, donkey_ge_coev


def parse_arguments(param: List[str]) -> Dict[str, Any]:
    """
    Parse command line arguments (`sys.argv`).

    :return: settings from configuration file and CLI arguments
    :rtype dict:
    """
    parser = argparse.ArgumentParser(description="Run donkey_ge")
    parser.add_argument(
        "-f",
        "--configuration_file",
        type=str,
        required=True,
        help="YAML configuration file. E.g. " "configurations/demo_ge.yml",
    )
    parser.add_argument(
        "-o",
        "--output_dir",
        type=str,
        default=".",
        help="Path to directory for output files. E.g. " "donkey_ge_output",
    )
    parser.add_argument("--coev", action="store_true", help="Coevolution")
    parser.add_argument(
        "-r", 
        "--repetitions",
        type=int, 
        default=0,
        ) # TODO: Added by German

    _args = parser.parse_args(param)

    # Read configuration file
    with open(_args.configuration_file, "r") as configuration_file:
        settings: Dict[str, Any] = yaml.load(configuration_file, Loader=yaml.FullLoader)

    # Set CLI arguments in settings
    settings["output_dir"] = _args.output_dir
    settings["coev"] = _args.coev
    settings["repetitions"] = _args.repetitions # TODO: Added by German

    return settings


def main(args: List[str]) -> Dict[str, Any]:
    """
    Run donkey_ge.
    """
    # Parse CLI arguments
    args = parse_arguments(args)
    # Run heuristic search
    if args["coev"]:
        donkey_ge_coev.run(args)
    else:
        donkey_ge.run(args)

    return args


if __name__ == "__main__":
    main(sys.argv[1:])
