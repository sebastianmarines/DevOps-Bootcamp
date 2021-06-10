# Network interfaces

## Elastic IP vs static IP

Elastic IPs are a service that AWS provides to allocate static IP addresses to instances, this way, when the instance is rebooted it keeps the same IP every time.

The main difference with a "classic" static IP is that Elastic IPs can be remapped to any instance.

For example, if your domain is linked to the IP of an instance, and that instance fails, you can remap the elastic IP to another instance immediately instead of having to modify the DNS records and waiting for them to propagate, making the domain unusable while this happens.

## VPCs & subnets

VPCs are isolated networks inside your AWS cloud, dedicated to your account. VPCs can span across availability zones but are restricted to a single region.

VPCs allow you to isolate resources inside your AWS network.

Subnets are part of a VPC, and can be configured to either be public or private. You can also configure if you want new instances created inside a subnet should have a public IPv4 address assigned.

Also, security groups should be linked to one VPC and can only be used by resources under that VPC.
