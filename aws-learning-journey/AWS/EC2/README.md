# Amazon EC2 (Elastic Compute Cloud)

Amazon EC2 (Elastic Compute Cloud) is a web service that provides secure, scalable, and resizable virtual servers in the cloud. It enables users to launch and manage instances on demand without investing in physical infrastructure.

---

## Table of Contents

- What is Amazon EC2?
- Key Features
- EC2 Pricing Models
- EC2 Instance Families
- EC2 Instance Lifecycle
- Amazon Machine Image (AMI)
- Key Pairs
- Security Groups
- Common Network Ports
- Elastic Block Store (EBS)
- Elastic IP
- Connecting to EC2
- Monitoring with CloudWatch
- Best Practices
- Hands-on Tasks

---

# What is Amazon EC2?

Amazon EC2 allows you to create virtual machines called **instances** in the AWS Cloud. These instances can run Linux, Windows, or other operating systems and are commonly used for:

- Hosting websites
- Running web applications
- Databases
- APIs
- Machine Learning workloads
- Dev/Test environments
- Enterprise applications

---

# Key Features

- Resizable compute capacity
- Multiple operating system support
- Secure access using Key Pairs
- Elastic Block Storage (EBS)
- Auto Scaling support
- Elastic Load Balancer integration
- Monitoring through CloudWatch
- High Availability using Multiple Availability Zones
- Pay-as-you-go pricing

---

# EC2 Pricing Models

## 1. On-Demand
- Pay only for the time you use.
- Best for short-term workloads.

## 2. Reserved Instances
- Commit for 1 or 3 years.
- Lower cost compared to On-Demand.

## 3. Spot Instances
- Purchase unused AWS capacity.
- Lowest price.
- Can be interrupted by AWS.

## 4. Dedicated Hosts / Dedicated Instances
- Physical server dedicated to one customer.
- Used for licensing and compliance requirements.

---

# EC2 Instance Families

## General Purpose
Balanced CPU and memory.

Examples:
- t2
- t3
- t4g
- m5
- m6i

Use Cases:
- Web servers
- Small databases
- Development

---

## Compute Optimized

Examples:
- c5
- c6i
- c7g

Use Cases:
- Gaming servers
- High-performance computing
- Batch processing

---

## Memory Optimized

Examples:
- r5
- r6i
- x2idn

Use Cases:
- SAP
- In-memory databases
- Big Data analytics

---

## Storage Optimized

Examples:
- i3
- i4i
- d3

Use Cases:
- Data warehouses
- NoSQL databases
- Log processing

---

## Accelerated Computing

Examples:
- p5
- g5
- inf2

Use Cases:
- Artificial Intelligence
- Deep Learning
- Graphics rendering

---

# EC2 Instance Lifecycle

```
Pending
    ↓
Running
 ↓     ↓
Stop  Reboot
 ↓
Stopped
 ↓
Start
 ↓
Running
 ↓
Terminate
```

### States

- Pending
- Running
- Stopping
- Stopped
- Rebooting
- Shutting-down
- Terminated

---

# Amazon Machine Image (AMI)

An AMI is a template used to launch an EC2 instance.

It contains:

- Operating System
- Application software
- Configuration
- Storage information

Types:

- Public AMI
- Private AMI
- AWS Marketplace AMI

---

# Key Pairs

Key Pairs provide secure authentication when connecting to Linux EC2 instances.

Components:

- Public Key
- Private Key (.pem)

The private key should never be shared.

---

# Security Groups

A Security Group acts as a virtual firewall for EC2 instances.

Rules include:

- Inbound Rules
- Outbound Rules

Example:

| Type | Port | Source |
|------|------|---------|
| SSH | 22 | Your IP |
| HTTP | 80 | Anywhere |
| HTTPS | 443 | Anywhere |

---

# Common Network Ports

| Port | Protocol | Service |
|------|----------|----------|
| 22 | TCP | SSH |
| 80 | TCP | HTTP |
| 443 | TCP | HTTPS |
| 3389 | TCP | RDP |
| 21 | TCP | FTP |
| 25 | TCP | SMTP |
| 53 | TCP/UDP | DNS |
| 110 | TCP | POP3 |
| 143 | TCP | IMAP |
| 3306 | TCP | MySQL |
| 5432 | TCP | PostgreSQL |
| 1433 | TCP | Microsoft SQL Server |
| 1521 | TCP | Oracle Database |
| 6379 | TCP | Redis |
| 27017 | TCP | MongoDB |
| 8080 | TCP | HTTP Alternate |
| 8443 | TCP | HTTPS Alternate |

---

# Elastic Block Store (EBS)

Amazon EBS provides persistent block storage for EC2 instances.

Features:

- Persistent storage
- Snapshots
- Encryption
- SSD and HDD options
- Resize volumes

Volume Types:

- gp3
- io2
- st1
- sc1

---

# Elastic IP

Elastic IP is a static public IPv4 address.

Benefits:

- Fixed public IP
- Easy instance replacement
- High availability

---

# Connecting to EC2

## Linux

```
ssh -i my-key.pem ec2-user@<Public-IP>
```

Ubuntu:

```
ssh -i my-key.pem ubuntu@<Public-IP>
```

---

## Windows

Connect using:

- Remote Desktop Protocol (RDP)
- Port 3389

---

# Monitoring with CloudWatch

CloudWatch monitors EC2 resources.

Metrics include:

- CPU Utilization
- Disk Read/Write
- Network In/Out
- Status Checks
- Memory (with CloudWatch Agent)

CloudWatch can trigger alarms based on thresholds.

---

# Best Practices

- Use IAM Roles instead of storing AWS credentials.
- Restrict SSH access to trusted IP addresses.
- Use Security Groups instead of opening all ports.
- Enable EBS encryption.
- Create regular snapshots.
- Keep operating systems updated.
- Use Auto Scaling for high availability.
- Place resources in multiple Availability Zones.
- Enable CloudWatch monitoring and alarms.
- Stop unused instances to reduce costs.

---

# Hands-on Tasks

- Launch an EC2 instance.
- Create a Key Pair.
- Configure Security Groups.
- Connect using SSH.
- Install Nginx or Apache.
- Host a sample web page.
- Attach an EBS volume.
- Allocate an Elastic IP.
- Monitor the instance using CloudWatch.
- Stop, Start, Reboot, and Terminate the instance.

---

# Learning Outcomes

After completing this module, you should be able to:

- Understand Amazon EC2 architecture.
- Choose the appropriate instance family.
- Launch and manage EC2 instances.
- Configure secure access using Key Pairs and Security Groups.
- Manage storage using Amazon EBS.
- Connect to Linux and Windows instances.
- Monitor resources using CloudWatch.
- Apply AWS best practices for performance, security, and cost optimisation.

---

## Author

**Sabhya Agrawal**

Learning AWS Cloud Engineering through hands-on projects and documentation.
