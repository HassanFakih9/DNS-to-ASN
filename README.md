# Domain-to-ASN Filter & VPN Policy Cleaner

This utility resolves a list of domains, identifies their ASN (Autonomous System
Number), and filters out domains already handled by a VPN policy. It generates
clean CSVs and a bash script to remove handled domains from Asus-Merlin's
`domain_vpn_routing.sh`.

---

## 🔧 Features

- Resolves all A records for each domain
- Looks up ASN via RDAP
- Compares against a list of handled ASNs
- **Strict include** logic: only skips domains if _all_ IPs map to known ASNs
- Deduplicates output by `(domain, ASN)`
- Generates:
  - `*_asn_results.csv`: domains requiring VPN routing
  - `*_skipped.csv`: already-handled domains
  - `remove_*.sh`: auto-generated bash script for removing skipped domains
  - `*_errors.log`: resolution and ASN lookup failures

---

## 🚀 Usage

```bash
python script.py policy_{POLICY_NAME}_domainlist handled_asns.txt
```

### Example

```bash
python script.py policy_Streaming_domainlist handled_asns.txt
```

---

## 📁 handled_asns.txt Format

The `handled_asns.txt` file should contain **one ASN per line**, without the
`AS` prefix. These are the ASNs you've already configured for VPN routing.

### handled_asns.txt Example

```text
13335
16509
14618
```

You can find these ASNs in your router’s policy config, or by looking up existing routes.

---

## 📦 Outputs

| File                        | Description                                |
| --------------------------- | ------------------------------------------ |
| `Streaming_asn_results.csv` | Domains not yet routed via known ASNs      |
| `Streaming_skipped.csv`     | Domains that match handled ASNs            |
| `Streaming_errors.log`      | DNS or ASN lookup errors                   |
| `remove_Streaming.sh`       | Bash script to run deletedomain per domain |

---

## 🧩 Environment Setup

This project uses Python 3.12.6 with `pyenv` and a virtual environment:

### 1. Install Python via pyenv

```bash
pyenv install 3.12.6
pyenv local 3.12.6
```

### 2. Create and activate a virtual environment

```bash
python -m venv venv
source venv/bin/activate
```

### 3. Install dependencies

```bash
pip install -r requirements.txt
```

---

## 🛡️ Intended Use

Helps manage and optimize domain-level VPN routing on Asus-Merlin firmware using
[domain_vpn_routing.sh](https://github.com/Ranger802004/asusmerlin/tree/main/domain_vpn_routing).

---

## 📄 License

MIT — use freely, contribute improvements, and give credit if you fork.
