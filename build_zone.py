#!/usr/bin/env python3
'''buid_zone.py builds a simple terraform zone file for the domains provided.
'''

import argparse
import os

ZONE_TEMPLATE_PATH = 'domain_zone.template'

def main():
    '''Processes arguments and then launces the build routine.
    '''
    parser = argparse.ArgumentParser("build_zone.py")
    parser.add_argument("--domain-list", help="A file that has domains listed one per line.")
    args = parser.parse_args()
    if not args.domain_list:
        parser.print_help()

    with open(args.domain_list) as domains_file:
        domains = domains_file.readlines()

    build_zone_files(domains)

def build_zone_files(domains):
    '''Loops through the domains, cleans up the name and then builds the
    terraform zone file using the zone template file.
    '''
    with open(ZONE_TEMPLATE_PATH) as zone_template_path_file:
        zone_template = zone_template_path_file.read()

    for domain in domains:
        domain = domain.lower().strip()
        if not domain:
            continue
        if domain.endswith('.'):
            domain = domain[:-1]
        domain_no_periods = domain.replace('.', '_')
        output_path = domain + ".tf"
        if os.path.isfile(output_path):
            print('{output_path} already exists.'.format(output_path=output_path))
        else:
            output = zone_template.format(domain=domain,
                                        domain_no_periods=domain_no_periods)
            with open(output_path, 'w') as output_file:
                output_file.write(output)
            print('{output_path} created.'.format(output_path=output_path))

if __name__ == '__main__':
    main()
