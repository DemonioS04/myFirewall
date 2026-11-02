# Basic Network And Firewall Manager

import subprocess
import networkManager
import firewallManager

if __name__ == "__main__":


    # Command line menu


    print("===========================================")
    print("   LINUX NETWORK AND FIREWALL MANAGER")
    print("===========================================")


    while True:
        print("\n\n")
        print("[1] Network Information")
        print("[2] Connection Monitor")
        print("[3] Firewall Status")
        print("[4] Manage Firewall Rules")
        print("[5] View Firewall Rules")
        print("[0] Exit")

        print("\n")

        choice=int(input("Enter your choice: "))

        if choice==1:
            networkManager.networkIinfo()
        elif choice==2:
            networkManager.connectionMonitor()
        elif choice==3:
            firewallManager.firewallStatus()
        elif choice==4:
            firewallManager.manage_firewallRules()
        elif choice==5:
            firewallManager.view_firewallRules()
        elif choice==0:
            exit()
        else:
            print("Invalid Input")


    
            
            


