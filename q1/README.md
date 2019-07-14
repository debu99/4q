There are mutiple Availability Zones (AZs) with m Private Subnets and n NAT Instances, we need to allocate subnets to the NAT Instances within the same AZ. If there are no healthy NAT Instances in the same AZ, only then will we allocate subnets to any NAT Instance in any other AZ.

- If there are no NAT Instances in an AZ, the private subnets of that AZ should be allocated to egress via available NAT Instances in other AZs.
- If there is still at least 1 NAT Instance in an AZ, the subnets of that AZ should still be allocated to that NAT Instance which is in the same AZ
- We try to have as close to the same number of private subnets allocated to each NAT Instance.

### Usage
1. Input the AZ Id for each Gateway is located, like AZ1 AZ2 AZ3 AZ1 or A B C A B
2. Input the AZ Id for each Private Subnet is located, like AZ1 AZ2 AZ3 AZ2 or A B C B B
- *Use space bettwen different AZ Id*

### Output
Output the Gateway and Private Subnet in each AZ
```bash
# python3 q1.py
Input the AZ Id each Gateway is located, like A B C D E or A B C A B : A B
Input the AZ Id each Subnet is located, like A B C D E or A B C A B : A A C
{'A': {'GW0': ['Subnet0', 'Subnet2', 'C-Subnet0']}}
```
```bash
# python3 q1.py
Input the AZ Id each Gateway is located, like A B C D E or A B C A B : A B C A B C C
Input the AZ Id each Subnet is located, like A B C D E or A B C A B : A B B B C C C D
{'A': {'GW0': ['Subnet0'], 'GW1': ['D-Subnet0']}, 'B': {'GW0': ['Subnet0', 'Subnet2'], 'GW1': ['Subnet1']}, 'C': {'GW0': ['Subnet0'], 'GW1': ['Subnet1'], 'GW2': ['Subnet2']}}
```

