# SSH

## Keys

SSH keys use an asymmetrical encryption algorithm to authenticate the users.

In an asymmetrical encryption algorithm, the public key contains only the encryption function, and the private key contains the decription function.

This way, when you want to authenticate using keys, the server encrypts a random string and sends it along with the session ID. Then, the client has to decrypt the random string using the private key and send its MD5 hash. When the server receives the hash it compares it with the hash it generated and if they are the same it establishes an SSL tunnel between the server and the client.
