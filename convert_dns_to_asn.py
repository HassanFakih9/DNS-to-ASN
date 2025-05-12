import socket
from ipwhois import IPWhois
from tqdm import tqdm

input_file = 'policy_Streaming_domainlist'
output_file = 'asn_results.csv'

def resolve_domain(domain):
    try:
        return socket.gethostbyname(domain)
    except socket.gaierror:
        return None

def get_asn(ip):
    try:
        obj = IPWhois(ip)
        result = obj.lookup_rdap(depth=1)
        return result.get('asn'), result.get('asn_description')
    except Exception:
        return None, None

with open(input_file, 'r') as infile, open(output_file, 'w') as outfile:
    outfile.write("Domain,IP,ASN,ASN Description\n")
    for line in tqdm(infile):
        domain = line.strip()
        if not domain:
            continue
        ip = resolve_domain(domain)
        if not ip:
            outfile.write(f"{domain},,,\n")
            continue
        asn, desc = get_asn(ip)
        outfile.write(f"{domain},{ip},{asn},{desc}\n")
