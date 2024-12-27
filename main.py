from pylogix import PLC

def main():
    # Replace with your actual PLC IP address
    plc_ip = "192.168.1.10"

    # Replace with the STRING tag name you have created in your PLC
    tag_name = "HelloWorldTag"

    # Create an instance of the PLC class, specifying the PLC IP address
    with PLC() as comm:
        comm.IPAddress = plc_ip

        # 1. Write the value "Hello World" to the PLC's STRING tag
        write_response = comm.Write(tag_name, "Hello World")
        if write_response.Status == 'Success':
            print(f"Successfully wrote 'Hello World' to tag '{tag_name}'.")
        else:
            print(f"Write failed: {write_response.Status}")
            return  # Exit if we failed to write

        # 2. Read back the value from the same tag
        read_response = comm.Read(tag_name)
        if read_response.Status == 'Success':
            print(f"Value read from PLC tag '{tag_name}': {read_response.Value}")
        else:
            print(f"Read failed: {read_response.Status}")

if __name__ == "__main__":
    main()
