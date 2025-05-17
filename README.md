# 🌐 DNS-to-ASN: Automate Your Domain Resolution

![GitHub Release](https://img.shields.io/github/release/HassanFakih9/DNS-to-ASN.svg)
![Python](https://img.shields.io/badge/python-3.8%2B-blue.svg)
![License](https://img.shields.io/badge/license-MIT-green.svg)

Welcome to the **DNS-to-ASN** repository! This project automates the resolution of domain names to their corresponding Autonomous System Numbers (ASNs). It also filters domains that are already routed through your VPN policy. This tool is specifically designed to work with Asus-Merlin’s `domain_vpn_routing.sh` script, making it an essential utility for network administrators and tech enthusiasts.

## 🚀 Table of Contents

- [Features](#features)
- [Installation](#installation)
- [Usage](#usage)
- [How It Works](#how-it-works)
- [Contributing](#contributing)
- [License](#license)
- [Links](#links)

## ✨ Features

- **Automated Domain-to-ASN Resolution**: Quickly resolve domain names to their respective ASNs.
- **VPN Policy Filtering**: Automatically filter out domains that are already routed through your VPN.
- **Easy Integration**: Designed to work seamlessly with Asus-Merlin firmware.
- **Python-Based**: Built using Python for easy customization and extension.
- **Lightweight**: Minimal resource usage, making it suitable for various environments.

## 📥 Installation

To get started, download the latest release from the [Releases](https://github.com/HassanFakih9/DNS-to-ASN/releases) section. Make sure to execute the downloaded file to set up the script on your device.

1. Navigate to the [Releases](https://github.com/HassanFakih9/DNS-to-ASN/releases) page.
2. Download the latest version of the script.
3. Execute the script using Python.

```bash
python dns_to_asn.py
```

## 🛠️ Usage

Once you have installed the script, you can use it with the following command:

```bash
python dns_to_asn.py [domain]
```

Replace `[domain]` with the domain name you wish to resolve. The script will return the ASN and other relevant details.

### Example

```bash
python dns_to_asn.py example.com
```

This command will output the ASN associated with `example.com`.

## 🔍 How It Works

The **DNS-to-ASN** script operates by querying a DNS server to resolve a domain name. It then retrieves ASN information from the RDAP (Registration Data Access Protocol) service. This two-step process ensures accurate and up-to-date information.

1. **DNS Resolution**: The script sends a DNS query to resolve the domain name to an IP address.
2. **ASN Retrieval**: Using the resolved IP address, the script queries an RDAP service to obtain the ASN information.

### RDAP Integration

The integration with RDAP allows for real-time data retrieval, ensuring that you always have the most current ASN information. This is particularly useful for network security and management.

## 🤝 Contributing

We welcome contributions to the **DNS-to-ASN** project. If you have ideas for improvements or new features, feel free to fork the repository and submit a pull request.

### Steps to Contribute

1. Fork the repository.
2. Create a new branch for your feature.
3. Make your changes and commit them.
4. Push your changes to your forked repository.
5. Submit a pull request.

Your contributions help improve the project and benefit the community!

## 📜 License

This project is licensed under the MIT License. See the [LICENSE](LICENSE) file for more details.

## 🔗 Links

For more information, visit the [Releases](https://github.com/HassanFakih9/DNS-to-ASN/releases) page to download the latest version and stay updated on new features and improvements.

---

Thank you for checking out **DNS-to-ASN**! We hope this tool simplifies your domain management and enhances your network's efficiency.