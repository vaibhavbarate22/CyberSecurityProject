import random

def GenerateRandomIp():
    return f"192.168.1.{random.randint(10, 30)}"

def CheckFirewallRule(Ip, Rules):
    for RuleIp, Action in Rules.items():
        if Ip == RuleIp:
            return Action
    return "Allow"

def main():
    FirewallRules = {
        "192.168.1.1": "block",
        "192.168.1.4": "block",
        "192.168.1.9": "block",
        "192.168.1.13": "block",
        "192.168.1.16": "block",
        "192.168.1.19": "block"
    }

    BlockedIp = []  
    AllowedIp = []  

    for _ in range(5):
        IpAddress = GenerateRandomIp()
        Action = CheckFirewallRule(IpAddress, FirewallRules)
        RandomNumber = random.randint(0, 99)

        if Action == "block":
            BlockedIp.append(f"Ip : {IpAddress}  RND : {RandomNumber}")
        else:
            AllowedIp.append(f"Ip : {IpAddress}  RND : {RandomNumber}")

    print("\n<--- Blocked IP -->")
    print("\n".join(BlockedIp) 
    if BlockedIp 
    else "No IPs blocked.")

    print("\n<--- Allowed IP --->")
    print("\n".join(AllowedIp) 
    if AllowedIp 
    else "No IPs allowed.")

if __name__ == "__main__":
    main()
