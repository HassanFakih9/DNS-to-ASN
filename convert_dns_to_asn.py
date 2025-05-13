import socket
from ipwhois import IPWhois
from tqdm import tqdm
import sys
import os
import re
import time

def resolve_domain_all_ips(domain, retries=3):
    for _ in range(retries):
        try:
            return list({res[4][0] for res in socket.getaddrinfo(domain, None)}), None
        except socket.gaierror as e:
            last_err = str(e)
    return None, last_err

def get_asn(ip):
    try:
        obj = IPWhois(ip)
        result = obj.lookup_rdap(depth=1)
        return result.get('asn'), result.get('asn_description'), None
    except Exception as e:
        return None, None, str(e)

if len(sys.argv) != 3:
    print("Usage: python script.py policy_{POLICY}_domainlist handled_asns.txt")
    sys.exit(1)

input_file = sys.argv[1]
asn_file = sys.argv[2]
basename = os.path.basename(input_file)

match = re.match(r'policy_(.+?)_domainlist', basename)
if not match:
    print("Input filename must match pattern: policy_{POLICY}_domainlist")
    sys.exit(1)

policy_name = match.group(1)
output_file = f"{policy_name}_asn_results.csv"
skipped_file = f"{policy_name}_skipped.csv"
error_log = f"{policy_name}_errors.log"
bash_file = f"remove_{policy_name}.sh"

# Load handled ASNs from asn.conf format: AS#####|interface
with open(asn_file, 'r') as f:
    handled_asns = {
        line.split('|')[0].replace('AS', '').strip()
        for line in f
        if line.strip() and line.startswith('AS')
    }

start_time = time.time()
errors = []
results_set = set()
skipped_set = set()
delete_domains = set()

with open(input_file, 'r') as infile, \
     open(output_file, 'w') as out_new, \
     open(skipped_file, 'w') as out_skipped, \
     open(error_log, 'w') as errfile, \
     open(bash_file, 'w') as bashout:

    out_new.write("Domain,IP,ASN,ASN Description\n")
    out_skipped.write("Domain,IP,ASN,ASN Description\n")
    bashout.write("#!/bin/bash\n\n")

    for line in tqdm(infile):
        domain = line.strip()
        if not domain:
            continue

        ip_list, err = resolve_domain_all_ips(domain)
        if not ip_list:
            out_new.write(f"{domain},,,\n")
            errors.append(f"{domain}: DNS resolution failed - {err}")
            continue

        if len(ip_list) > 1:
            errors.append(f"{domain}: Multiple IPs found - {', '.join(ip_list)}")

        ip_asn_data = []
        any_unhandled = False

        for ip in ip_list:
            asn, desc, asn_err = get_asn(ip)
            if not asn:
                errors.append(f"{domain} ({ip}): ASN lookup failed - {asn_err}")
                ip_asn_data.append((ip, '', ''))
                any_unhandled = True
            else:
                ip_asn_data.append((ip, asn, desc))
                if asn not in handled_asns:
                    any_unhandled = True

        # Dedup by (domain, asn)
        seen_asns = set()
        for ip, asn, desc in ip_asn_data:
            key = (domain, asn)
            if asn in seen_asns:
                continue
            seen_asns.add(asn)
            row = f"{domain},{ip},{asn},{desc}\n"
            if any_unhandled:
                if key not in results_set:
                    out_new.write(row)
                    results_set.add(key)
            else:
                if key not in skipped_set:
                    out_skipped.write(row)
                    skipped_set.add(key)
                    delete_domains.add(domain)

    if errors:
        errfile.write('\n'.join(errors))

    for domain in sorted(delete_domains):
        bashout.write(f"/jffs/scripts/domain_vpn_routing.sh deletedomain {domain}\n")

elapsed = round(time.time() - start_time, 2)
print(f"\n✅ Done.")
print(f"    Output         → {output_file}")
print(f"    Skipped        → {skipped_file}")
print(f"    Bash Script    → {bash_file}")
print(f"    Errors         → {error_log}")
print(f"    Elapsed Time   → {elapsed} seconds")
