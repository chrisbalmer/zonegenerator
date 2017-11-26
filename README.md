# Zone Generator

This project creates basic terraform files for DNS zones. It uses another project of mine that is a terraform module for Route53 DNS records.

## Usage

```
./build_zone.py --domain-list domains.txt
```

This will take the domains from `domains.txt` and build terraform configs using the template. Only the `domain` and `domain_without_periods` variables are used to populate the template.

It is a simple script to manage generating some basic records in Route53.
