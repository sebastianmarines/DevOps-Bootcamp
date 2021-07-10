# Final activity

## Security headers

- **HTTP Strict Transport Security**: HSTST is a web security policy mechanism which helps to protect websites against protocol downgrade attacks.
  - **max-age=SECONDS**: The time, in seconds, that the website should remember that te site is only accessed using HTTPS.
  - **includeSubDomains**: If this optional parameter is specified, this rule applies to all of the subdomains as well.
- **X-Frame-Options**: This response header improves protection of web applications against clickjacking. It instructs the browser whether the content can be displayed within frames.
  - **deny**: No rendering within a frame.
  - **sameorigin**: No rendering if origin mismatch.
  - **allow-from: DOMAIN**: Allows rendering framed content if loaded from *DOMAIN*.
- **X-Content-Type-Options**: 
