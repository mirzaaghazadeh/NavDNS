import subprocess
import sys

# List of required packages
required_packages = ['dnspython', 'simple-term-menu']

# Install missing packages
for package in required_packages:
    try:
        __import__(package)
    except ImportError:
        subprocess.check_call([sys.executable, '-m', 'pip', 'install', package])

# Now import the modules after ensuring they are installed
import dns.resolver
from simple_term_menu import TerminalMenu
import argparse

def query_dns(domain, record_type):
    try:
        answers = dns.resolver.resolve(domain, record_type)
        for rdata in answers:
            print(f'{record_type} Record: {rdata.to_text()}')
    except dns.resolver.NoAnswer:
        print(f'No {record_type} record found for {domain}')
    except dns.resolver.NXDOMAIN:
        print(f'Domain {domain} does not exist')
    except Exception as e:
        print(f'An error occurred: {e}')

def interactive_menu():
    options = ["A - Address record", "AAAA - IPv6 address record", "MX - Mail exchange record", 
               "NS - Name server record", "TXT - Text record", "Exit"]
    terminal_menu = TerminalMenu(options, title="NavDNS - What do you want to query?")
    menu_entry_index = terminal_menu.show()
    
    if menu_entry_index is None or options[menu_entry_index] == "Exit":
        sys.exit()

    record_type = options[menu_entry_index].split()[0]
    domain = input("Enter the domain name: ")
    query_dns(domain, record_type)

if __name__ == "__main__":
    ascii_art = """
 ****     **                    *******   ****     **  ********
/**/**   /**                   /**////** /**/**   /** **////// 
/**//**  /**  ******   **    **/**    /**/**//**  /**/**       
/** //** /** //////** /**   /**/**    /**/** //** /**/*********
/**  //**/**  ******* //** /** /**    /**/**  //**/**////////**
/**   //**** **////**  //****  /**    ** /**   //****       /**
/**    //***//********  //**   /*******  /**    //*** ******** 
//      ///  ////////    //    ///////   //      /// ////////  
    """

    print(ascii_art)
    print("Use with caution. You are responsible for your actions.")
    print("Developers assume no liability and are not responsible for any misuse or damage.\n")

    parser = argparse.ArgumentParser(description="NavDNS - A simple DNS query tool")
    parser.add_argument("-u", "--url", help="Domain name to query")
    parser.add_argument("-t", "--type", default="A", help="DNS record type (A, AAAA, MX, NS, TXT)")

    args = parser.parse_args()

    if args.url:
        query_dns(args.url, args.type)
    else:
        interactive_menu()
