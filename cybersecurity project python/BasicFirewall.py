import random
import logging


logging.basicConfig(filename="BasicFirewall.log", level=logging.INFO, format='%(asctime)s - %(message)s')

def LogEvent(message):
    logging.info(message)

def TrackConnections(Ip, AllowedConnections):
    if Ip not in AllowedConnections:
        AllowedConnections.append(Ip)
        return "Allow"

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
    AllowedConnections = []  

    for _ in range(5):
        IpAddress = GenerateRandomIp()
        Action = CheckFirewallRule(IpAddress, FirewallRules)
        RandomNumber = random.randint(0, 99)

        LogMessage = f"IP: {IpAddress} RND: {RandomNumber} Action: {Action}"

        if Action == "block":
            BlockedIp.append(f"Ip : {IpAddress}  RND : {RandomNumber}")
            LogEvent(f"Blocked {LogMessage}")
        else:
           
            Action = TrackConnections(IpAddress, AllowedConnections)
            AllowedIp.append(f"Ip : {IpAddress}  RND : {RandomNumber}")
            LogEvent(f"Allowed {LogMessage}")

    print("\n<--- Blocked IP -->")
    print("\n".join(BlockedIp) if BlockedIp else "No IPs blocked.")

    print("\n<--- Allowed IP --->")
    print("\n".join(AllowedIp) if AllowedIp else "No IPs allowed.")

if __name__ == "__main__":
    main()
