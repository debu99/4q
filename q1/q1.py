
import itertools

# get user input and change to dictionary
def input_to_dict(type_name):
    input_str = input("Input the AZ Id each {} is located, like A B C D E or A B C A B : ".format(type_name))
    input_list = input_str.split()
    ret_dict={}
    for i in input_list:
        ret_dict[i] = input_list.count(i)
    return ret_dict

def allocate_subnet_to_gateway(subnet_num, gateway_num):
    gateway_with_its_subnets={}
    # populate the dictionary with gateway as the key
    for i in range(gateway_num):
        gateway_with_its_subnets["GW" + str(i)] = []
    # if number of gateway is more than or equal to number of subnets
    if subnet_num <= gateway_num:
        for i in range(subnet_num):
            gateway_with_its_subnets["GW" + str(i)].append("Subnet" + str(i))     
    else:
        for i in range(gateway_num):
            gateway_with_its_subnets["GW" + str(i)].append("Subnet" + str(i)) 
        # for extra subnets
        extra = subnet_num - gateway_num
        # if extra subnets less than gateway number, re-allocate the subnet from the first gateway
        if extra < gateway_num:
            for i in range(extra):
                gateway_with_its_subnets["GW" + str(i)].append("Subnet" + str(i + extra + 1))
        else:
            #loop over 2 lists, repeating the shortest until end of longest
            for x,y in zip([str(t + extra + 1) for t in range(extra)], itertools.cycle([str(t) for t in range(gateway_num)])):
                gateway_with_its_subnets["GW" + str(y)].append("Subnet" + str(x))
    return gateway_with_its_subnets


def main():
    
    # get the gateway in each AZ
    AZ_GW=input_to_dict("Gateway")

    # get the subnet in each AZ
    AZ_Subnet=input_to_dict("Subnet")

    Result={}

    # for each subnet which has gateway in their AZ
    for AZ in AZ_Subnet.keys():
        if AZ in AZ_GW.keys():
                Result[AZ] = allocate_subnet_to_gateway(AZ_Subnet[AZ], AZ_GW[AZ])

    # for each subnet which doesn't have the gateway in their AZ
    for Subnet_AZ in AZ_Subnet.keys():
        if Subnet_AZ not in AZ_GW.keys():
            # for each subnet_id in that region which doesn't have gateway
            for Subnet_ID in range(AZ_Subnet[Subnet_AZ]):
                # set the first gateway in the Result dictionary has the minimum number of subnets
                min_az = list(Result)[0]
                min_gw = list(Result[min_az])[0]
                min = len(min_gw)
                # find the gateway with minimum subnet in all the AZ
                for AZ in Result.keys():
                    for GW in Result[AZ].keys():
                        if len(Result[AZ][GW])<min:
                            min = len(Result[AZ][GW])
                            min_az = AZ
                            min_gw = GW
                # allocate the subnet to the gateway with minimum number of subnet
                Result[min_az][min_gw].append(Subnet_AZ + "-Subnet" + str(Subnet_ID))

    print(Result)

if __name__ == "__main__":
    main()
