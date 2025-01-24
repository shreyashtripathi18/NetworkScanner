# Network Scanner

This project is a simple network scanner written in Python. It allows you to scan a network and retrieve information about the devices connected to it.

## Requirements

- Python 3.x
- Scapy library

## Installation

1. Clone the repository:
    ```bash
    git clone https://github.com/yourusername/NetworkScanner.git
    ```
2. Navigate to the project directory:
    ```bash
    cd NetworkScanner
    ```
3. Install the required dependencies:
    ```bash
    pip install -r requirements.txt
    ```

## Usage

To run the network scanner, use the following command:
```bash
python network_scanner.py -t <target>
```
Replace `<target>` with the IP address or range you want to scan.

## Example

```bash
python network_scanner.py -t 192.168.1.1/24
```

This will scan the network range `192.168.1.1/24` and display the connected devices.

## Example Response

```
IP Address: 192.168.1.2    MAC Address: 00:0a:95:9d:68:16
IP Address: 192.168.1.3    MAC Address: 00:0a:95:9d:68:17
IP Address: 192.168.1.4    MAC Address: 00:0a:95:9d:68:18
```

## License

This project is licensed under the MIT License. See the [LICENSE](LICENSE) file for details.

## Contributing

Contributions are welcome! Please open an issue or submit a pull request for any changes.

## Contact

For any questions or inquiries, please contact [your email].
