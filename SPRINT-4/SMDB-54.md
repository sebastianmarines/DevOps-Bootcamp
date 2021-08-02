# Highly available environments

## Load Balancers

Elastic Load Balancer is a load balancing service offered by AWS.

ELB automatically distributes incoming traffic and scales resources to meet traffic demands.

There are 4 types of load balancers:

- ALB (Application Load Balancer)
- NLB (Network Load Balancer)
- CLB (Classic Load Balancer)
- GLB (Gateway Load Balancer)

###  ALB

An Application Load Balancer is a type of load balancer that functions at the application layer of the OSI model.

When an ALB receives a request, it evaluates the listener rules in priority order to determine which rule to apply, then selects a target from the target group.

## Availability Zones

An availability zone is one or more data centers in an AWS region.

They are independent of each other and have redundant power, networking, and connectivity.
