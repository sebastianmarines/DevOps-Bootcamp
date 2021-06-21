# LEMP

LEMP is another web stack, and instead of using Apache for the web server it uses Nginx.

## Apache vs Nginx

### Apache

- Oldest of the two
- Needs to spawn processes for every request, making it slow under heavy load.
- Drops requests when the connection limit is reached.
- Threads contending for CPU and RAM.

### Nginx

- Event-driven and asynchronous. Does not create threads for each connection.
- Modules are included at compile time.
- Worker based.
