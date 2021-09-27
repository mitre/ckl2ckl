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
    used_old_vulns = set()
    new_root = new.getroot()
    for vuln in new_root.findall('./STIGS/iSTIG/VULN'):
        found_sv_flag = False
        for s_d in vuln.findall('./STIG_DATA'):
            vuln_attribute, attribute_data = list(s_d)
            if vuln_attribute.text == 'LEGACY_ID':
                if not attribute_data.text or len(attribute_data.text) < 2 or not attribute_data.text[0:2] == 'SV':
                    continue
                found_sv_flag = True

                if not attribute_data.text in old_vulns.keys():
                    print(vuln.findall('./STIG_DATA')[3][1].text, 'had a legacy ID', attribute_data.text, 'that was not found in the old CKL')
                    continue

                # then put the old data in the new file
                vuln.find('./STATUS').text = old_vulns[attribute_data.text].find('./STATUS').text
                vuln.find('./FINDING_DETAILS').text = old_vulns[attribute_data.text].find('./FINDING_DETAILS').text

                if vuln.findall('./STIG_DATA')[8][1].text != old_vulns[attribute_data.text].findall('./STIG_DATA')[8][1].text:
                    print('Check text does not match between', vuln.findall('./STIG_DATA')[3][1].text, 'and', attribute_data.text, 'but data still transferred')
                if vuln.findall('./STIG_DATA')[9][1].text != old_vulns[attribute_data.text].findall('./STIG_DATA')[9][1].text:
                    print('Fix text does not match between', vuln.findall('./STIG_DATA')[3][1].text, 'and', attribute_data.text, 'but data still transferred')

                used_old_vulns.add(attribute_data.text)
        if not found_sv_flag:
            print(vuln.findall('./STIG_DATA')[3][1].text, 'has no legacy ids starting with "SV" listed')
    if (diff := set(old_vulns.keys()).difference(used_old_vulns)):
        print('The following rules did not have any data transferred to the new CKL:', sorted(diff))

    new.write(args.result_path, encoding='utf8')

if __name__ == "__main__":
    main()
