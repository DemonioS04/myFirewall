import subprocess
import re

# User driven menu


def networkInfo():
    print("\n\n===============================")
    print("     Network Information")
    print("===============================\n\n")

    print("[1] Network Interfaces")
    print("[2] Ip addresses")
    print("[3] MAC Addresses")
    print("[4] Default Gateway")
    print("[5] DNS Configuration")
    print("[6] Routing Table")
    print("[0] Back")

    choice=input("\nEnter your choice: ")

    if choice=="1":
        networkInterfaces()
        return
    elif choice=="2":
        ipAddresses()
        return
    elif choice=="3":
        macAddresses()
        return
    elif choice=="4":
        defaultGateway()
        return
    elif choice=="5":
        dnsConfiguration()
        return
    elif choice=="6":
        routingTable()
        return
    elif choice=="0":
        return
    else:
        print("Invalid Choice")


# Network Interfaces

def networkInterfaces():
    print("\n")
    output=subprocess.run(
        "nmcli device status",
        shell=True,
        capture_output=True,
        text=True
    )

    if output.returncode!=0:
        print("Unexpected error occured")
        return

    print(output.stdout)
    
# Ip Addresses

def ipAddresses():
    print("\n")
    output=subprocess.run(
        "ifconfig",
        capture_output=True,
        text=True
    )
    if output.returncode!=0:
        print("Unexpected error occured")
        return

    interfaces=re.split(r"\n(?=\S)",output.stdout)

    for interface in interfaces:
        name=interface.split()[0].rstrip(":")

        ipv4 = re.search(r"inet(?: addr:)?\s*(\d{1,3}(?:\.\d{1,3}){3})", interface)

        if ipv4:
            print(f"{name} : {ipv4.group(1)}")

        else:
            print(f"{name} : No ip")

# MAC Adresses

def macAddresses():
    print("\n")

    output=subprocess.run(
        "ifconfig",
        capture_output=True,
        text=True
    )


    if output.returncode!=0:
        print("Unexpected error occured")
        return

    macs=re.split(r"\n(?=\S)",output.stdout)

    for mac in macs:
        name=mac.split()[0].rstrip(":")

        if name=="lo":
            continue
        else:
            macaddr = re.search(r"ether\s+([0-9a-fA-F]{2}(?::[0-9a-fA-F]{2}){5})", mac)
            if macaddr:
                print(f"{name} : {macaddr.group(1)}")
            else:
                print(f"{name} : Couldn't detect")

# Default Gateway

def defaultGateway():
    print("\n")

    output=subprocess.run(
        "ip route",
        shell=True,
        capture_output=True,
        text=True
    )

    if output.returncode!=0:
        print("Unexpected error occured")
        return


    gateway = re.search(r"default via (\d{1,3}\.\d{1,3}\.\d{1,3}\.\d{1,3})",output.stdout)
    if gateway:
        print(f"Default gateway: {gateway.group(1)}")
    else:
        print("No default gateway found")


# DNS Configuration

def dnsConfiguration():
    print("\n")

    output=subprocess.run("resolvectl dns",
                          shell=True,
                          capture_output=True,
                          text=True
                          )

    if output.returncode!=0:
        print("Unexpected error occured")
        return

    dnses=re.split(r"\n(?=\S)",output.stdout)

    for dns in dnses:
        link=dns.split()[0].rstrip(":")
        if link=="Link":
            num=dns.split()[1]
        else:
            num=""

        record = re.search(r"(\d{1,3}\.\d{1,3}\.\d{1,3}\.\d{1,3})",dns)

        if record is None:
            print(f"{link} {num} : No DNS found")
        else:
            print(f"{link} {num} : {record.group(1)}")

# Routing Table

def routingTable():
    print("\n")

    output=subprocess.run(
        "ip route",
        shell=True,
        capture_output=True,
        text=True
    )

    if output.returncode!=0:
        print("Unexpected error occured")
        return

    print(output.stdout)

# Connectionn Monitor


def connectionMonitor():

    print("==============================")
    print("     Connection Monitor")
    print("==============================")
    print("\n\n")
    output=subprocess.run(
        "ss -tunap",
        shell=True,
        capture_output=True,
        text=True
    )

    if output.returncode!=0:
        print("Unexpected error occured")
        return

    print(output.stdout)