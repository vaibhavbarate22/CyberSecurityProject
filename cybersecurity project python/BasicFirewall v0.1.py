import subprocess

def UpdateFirewall(IpAddress, Action):
    try:
        if Action == "block":
            
            subprocess.run(["sudo", "iptables", "-A", "INPUT", "-s", IpAddress, "-j", "DROP"], check=True)
            print(f"Blocked IP: {IpAddress}")
        elif Action == "allow":
            # Add a rule to allow the IP
            subprocess.run(["sudo", "iptables", "-A", "INPUT", "-s", IpAddress, "-j", "ACCEPT"], check=True)
            print(f"Allowed IP: {IpAddress}")
    except subprocess.CalledProcessError as e:
        print(f"Error updating firewall rule for IP: {IpAddress}. Error: {e}")

# Example Usage
UpdateFirewall("192.168.1.100", "block")
UpdateFirewall("192.168.1.200", "allow")
