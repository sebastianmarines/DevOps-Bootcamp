# 1. SSL Certificates

SSL (Secure Sockets Layer) is a protocol for establishing authenticated and encrypted links between networked computers.

SSL was deprecated in 1999 with the release of TLS, but it is common to refer to TLS as SSL/TLS or just as SSL.

## 1.1. Types of SSL certificates

- **Single domain**: Certificate that applies to one domain only and can't be used with subdomains.
- **Wildcard**: Certificates that are valid in a domain and all of its subdomains.
- **Multi-Domain**: This certificates list multiple domains on one certificate.

## 1.2. Self signed certificate

A self signed certificate is a certificate that is not signed by a publicly trusted certificate authority.

The reason they are considered different from a traditional authority certificate-authority signed certificates is that they are created, issued, and signed by the company or developer who is responsible for the website or software being signed.

Usually self signed certificates are not considered secure.

## 1.3. Csr and key files

### 1.3.1. CSR

A Certificate Signing Request file (.csr) is the signed SSL certificate.

A CSR is created in PEM format and contains:

- **CN (Common Name)**: The fully qualified domain name of your server.
- **O (Organization)**: Legal name of the organization.
- **OU (Organizational Unit)**: The department of your organization that manages the certificate.
- **L (Location)**: The city in which the organization is located at.
- **S (State)**: The state in which the organization is located at.
- **C (Country)**: The country in which the organization is located at.
- **Public Key**
- **Information about the type and length of the key**: The most common is RSA 2048

### 1.3.2. Key

The .key file is the private key that is used to sign requests.

## 1.4. Intermediate certificates and bundle certificates

### 1.4.1. Intermediate Certificates

An intermediate certificate sits between the root certificate and the server certificates.

They are usually issued by a known certificate authority and helps validate the integrity of the server certificates.

### 1.4.2. Bundle certificates

Bundle certificates group together the whole certificate chain: the root certificate, the intermediate certificates, and the server certificate.

## 1.5. Let's Encrypt

Let's Encrypt is a nonprofit Certificate Authority created by the Internet Security Research Group.

It lets you create SSL certificates in an automated way without human intervention.

## 1.6. Cloudflare and AWS ACM

AWS Certificate Manager and Cloudflare lets you get a free SSL certificate to protect your website, you have the option of encrypting traffic from the client to Cloudflare, but also from Cloudflare to your server.
