import subprocess

# User driven menu


def networkInfo():
    print("===============================")
    print("     Network Information")
    print("===============================")

    print("[1] Network Interfaces")
    print("[2] Ip addresses")
    print("[3] MAC Addresses")
    print("[4] Default Gateway")
    print("[5] DNS Configuration")
    print("[6] Routing Table")
    print("[0] Back")

    choice=input("Enter your choice: ")

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
    print("Hello")

# Ip Addresses

def ipAddresses():
    print("Hello")

# MAC Adresses

def macAddresses():
    print("Hello")


# Default Gateway

def defaultGateway():
    print("Hello")


# DNS Configuration

def dnsConfiguration():
    print("Hello")


# Routing Table

def routingTable():
    print("Hello")


