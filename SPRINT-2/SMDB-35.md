# DNS

DNS is a protocol that helps internet users discover websites using human readable addresses.

This protocol translates domain names to IPs, and allows us to write simple addressess instead of hard to remember IPs.

## Records

- **A**: This is the most common used record. They simply point a domain to an IPv4 address.
- **CNAME**: This records are similar to **A** records, but they point to another domain instead of to an IP.
- **TXT**: This record allows you to enter text into a DNS. It was originally intended as a place for human readable notes but it is also used to store some machine-readable data.
  - **SPF**: This is a **TXT** record that helps identify which mail servers are permitted to send emails on behalf of your domain.
  - **DKIM**: This type of records works as an authentication method for emails. It allows a receiver to verify if the message was sent and authorized by the domain owner.
- **Naked**: It is an **A** record of a domain that does not have a *www* prefix.

# Route53

Route53 is a high availability DNS service provided by AWS.

It allows you to register domains and create hosted zones for your domains.

# Cloudflare

Cloudflare is a company that provides different products like global CDNs, DNS management, and DDoS mitigation.

