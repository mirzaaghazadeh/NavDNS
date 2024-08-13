# NavDNS

NavDNS is a simple DNS query tool built with Python.
 It allows you to perform various DNS queries directly from the command line, either interactively or by using command-line arguments.

## Features

- Supports various DNS record types: A, AAAA, MX, NS, TXT, and more.
- Command-line interface for quick DNS queries with minimal input.

## Installation

 **Clone the Repository**:
    ```bash
    git clone https://github.com/yourusername/NavDNS.git
    cd NavDNS
    ```



## Usage

### Interactive Mode

Simply run the script without any arguments to enter interactive mode. Use the arrow keys to select the DNS record type you want to query, and then enter the domain name.

```bash
python navdns.py
```

### Command-Line Mode

NavDNS also supports command-line arguments for quick queries. Below are the options:

- **-u, --url**: The domain name to query.
- **-t, --type**: The DNS record type to query (default is `A`).

#### Example Commands

- **Query A Record**:
    ```bash
    python3 navdns.py -u example.com -t A
    ```

- **Query MX Record**:
    ```bash
    python3 navdns.py -u example.com -t MX
    ```

- **Query AAAA Record (IPv6 Address)**:
    ```bash
    python3 navdns.py -u example.com -t AAAA
    ```

- **Query NS Record**:
    ```bash
    python3 navdns.py -u example.com -t NS
    ```

- **Query TXT Record**:
    ```bash
    python3 navdns.py -u example.com -t TXT
    ```



## License

This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details.

## Contributing

Contributions are welcome! Please fork this repository and submit a pull request with your improvements.

## Issues

If you encounter any issues or have any suggestions, feel free to open an issue on the [GitHub Issues](https://github.com/mirzaaghazadeh/NavDNS/issues) page.