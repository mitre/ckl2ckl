import argparse
import pathlib
import xml.etree.ElementTree as ET
from operator import itemgetter

def parse_args():
    parser = argparse.ArgumentParser(description='Translate findings from older to newer versions of a Checklist.')
    parser.add_argument('old_path', type=pathlib.Path, help='path to the old CKL file')
    parser.add_argument('new_path', type=pathlib.Path, help='path to the new CKL file')
    parser.add_argument('result_path', type=pathlib.Path, help='path to where the result CKL file should be saved')
    args = parser.parse_args()
    return args

def main():
    args = parse_args()
    old, new = [ET.parse(path) for path in itemgetter('old_path', 'new_path')(vars(args))]

    # make a map of id -> vuln
    old_root = old.getroot()
    old_vulns = {}
    for vuln in old_root.findall('./STIGS/iSTIG/VULN'):
        for s_d in vuln.findall('./STIG_DATA'):
            vuln_attribute, attribute_data = list(s_d)
            if vuln_attribute.text == 'Rule_ID':
                old_vulns[attribute_data.text.partition('r')[0]] = vuln

    # find the legacy id of the correct form so as to match the new vuln with an old one
    new_root = new.getroot()
    for vuln in new_root.findall('./STIGS/iSTIG/VULN'):
        for s_d in vuln.findall('./STIG_DATA'):
            vuln_attribute, attribute_data = list(s_d)
            if vuln_attribute.text == 'LEGACY_ID':
                if not attribute_data.text or len(attribute_data.text) < 2 or not attribute_data.text[0:2] == 'SV':
                    print('Vuln_Num', vuln.findall('./STIG_DATA')[0][1].text, 'has no legacy ids starting with "SV" listed')
                    continue

                if not attribute_data.text in old_vulns.keys():
                    print('Legacy ID', attribute_data.text, 'not found in the old CKL')
                    continue

                # then put the old data in the new file
                vuln.find('./STATUS').text = old_vulns[attribute_data.text].find('./STATUS').text
                vuln.find('./FINDING_DETAILS').text = old_vulns[attribute_data.text].find('./FINDING_DETAILS').text

    new.write(args.result_path, encoding='utf8')

if __name__ == "__main__":
    main()
