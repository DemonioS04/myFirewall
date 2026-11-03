import subprocess
import re
import ipaddress

# Firewall Status

def firewallStatus():
    print("============================")
    print("     Firewall Status")
    print("============================")
    print("\n")

    output=subprocess.run(
        "sudo ufw status verbose",
        shell=True,
        capture_output=True,
        text=True
    )

    if output.returncode!=0:
        print("Unexpected error occured")
        return
    print(output.stdout)

    print("\n")

    status=output.stdout.split()[1].lower()

    if status=="active":
        opt=input("Your firewall is active. Do you want deactivate? (y/n): ").lower()
        if opt=="y":
            rc=subprocess.run("sudo ufw disable",shell=True,capture_output=True,text=True)

            if rc.returncode==0:
                print("Your UFW firewall has been successfully inactivated")

    elif status=="inactive":
        opt=input("Your firewall is inactive. Do you want to activate? (y/n): ").lower()
        if opt=="y":
            rc=subprocess.run("sudo ufw enable",shell=True,capture_output=True,text=True)

            if rc.returncode==0:
                print("Your UFW firewall has been successfully activated")





# View Firewall Rules

def view_firewallRules():

    print("================================")
    print("     View Firewall Rules")
    print("================================")

    output=subprocess.run(
        "sudo ufw status numbered",
        shell=True,
        capture_output=True,
        text=True
    )

    if output.returncode!=0:
        print("Unexpected error occured")
        return

    print(output.stdout)


# Manage Firewall Rules

def manage_firewallRules():



    print("==================================")
    print("     Manage Firewall Rules")
    print("==================================")

    while True:
        print("[1] Allow Port")
        print("[2] Deny Port")
        print("[3] Allow IP Address")
        print("[4] Deny IP Address")
        print("[5] Reset Firewall Rules")
        print("[0]Back")

        print("\n")
        choice=input("Enter your choice: ")

        if choice=="1":
            allowPort()
        if choice=="2":
            denyPort()
        if choice=="3":
            allowIpAddress()
        if choice=="4":
            denyIpAddress()
        if choice=="5":
            reset()
        if choice=="0":
            return


# Allow Port

def allowPort():

    print("\n")
    port=input("Enter the port: ")
    protocol=input("Enter the protocol (tcp/udp/enter blank if regardless of protocol): ")

    arg=(f"{port}/{protocol}").rstrip("/")

    output=subprocess.run(
        f"sudo ufw allow {arg}",
        shell=True,
        capture_output=True,
        text=True
    )

    if output.returncode!=0:
        print(output.stderr)
        return

    print(f"Port {port} allowed")

    

# Deny Port

def denyPort():
    print("\n")
    port=input("Enter the port: ")
    protocol=input("Enter the protocol (tcp/udp/enter blank if regardless of protocol): ")

    arg=(f"{port}/{protocol}").rstrip("/")

    output=subprocess.run(
        f"sudo ufw deny {arg}",
        shell=True,
        capture_output=True,
        text=True
    )

    if output.returncode!=0:
        print(output.stderr)
        return

    print(f"Port {port} denied")

# Allow IP Address

def allowIpAddress():
    print("\n")

    ip=input("Enter the IP adress: ")
    if ipaddress.ip_address(ip):
        output=subprocess.run(
            f"sudo ufw allow from {ip}",
            shell=True,
            capture_output=True,
            text=True
        )

        if output.returncode!=0:
            print("Unexpected error occured")
            return

        print(f"IP {ip} allowed")


# Deny IP Address

def denyIpAddress():

    print("\n")

    ip=input("Enter the IP adress: ")
    if ipaddress.ip_address(ip):
        output=subprocess.run(
            f"sudo ufw deny from {ip}",
            shell=True,
            capture_output=True,
            text=True
        )

        if output.returncode!=0:
            print("Unexpected error occured")
            return

        print(f"IP {ip} denied")

# Reset Firewall Rules

def reset():
    print("\n")

    output=subprocess.run(
        "sudo ufw reset",
        shell=True,
        capture_output=True,
        text=True
    )

    if output.returncode!=0:
        print("Unexpected error occured")
        return

    print("UFW firewall reset to default")