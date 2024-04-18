import sys

import argparse
import logging

from utils import create_dict_from_lists, sort_by_ascending
from report_generation import generate_report_data_list
from report_exporter import CSVExporter

logger = logging.getLogger(__name__)

def ExportToCSV(calls_file, operators_file, output_file) -> None:
    """
    Function that generates, processes and exports report from calls and operators files
    """
    # Generation
    (report_data_list) = generate_report_data_list(calls_file, operators_file)
    logger.info('Report successfully generated.')
    # Processing
    report_dict = create_dict_from_lists(*report_data_list)
    sorted_report = sort_by_ascending(report_dict)
    logger.info('Report successfully processed.')
    # Export
    report_exporter = CSVExporter()
    report_exporter.export(output_file, sorted_report)
    logger.info('Report successfully exported.')
    
    logging.info('Terminating ExportToCSV...')
    sys.exit(0)
    

def main() -> None:
    """
    Main entry point for application
    """

    parser = argparse.ArgumentParser(
        description='ExtractToCSV: a tool to process calls and operators generate a report',
        add_help=False
    )

    parser.add_argument(
        '--calls',
        '--input-calls',
        type=str,
        required=True,
        help="Input file containing calls data"
    )

    parser.add_argument(
        '--operators',
        '--input-operators',
        type=str,
        required=True,
        help="Input file containing operators data"
    )

    parser.add_argument(
        '--output',
        '--output-file',
        type=str,
        required=False,
        default='output.csv',
        help="Output file for generate report e.g. report.csv"
    )

    parser.add_argument(
        '--log-level',
        type=str,
        required=False,
        default='INFO',
        help='Sets the logging level [DEBUG, INFO]',
    )

    args = parser.parse_args()

    logging.basicConfig(filename='ExtractCSV.log',
                    encoding='utf-8',
                    level=args.log_level.upper(),
                    format='[%(levelname)s] %(filename)s: \t\t%(message)s',
                    filemode = "w+")
    logging.getLogger().addHandler(logging.StreamHandler(sys.stdout))
    print()

    logger.debug('ExtractToCSV ran with args: %s', args)
    
    ExportToCSV(args.calls, args.operators, args.output) # run report generation

if __name__ == '__main__':
    main()