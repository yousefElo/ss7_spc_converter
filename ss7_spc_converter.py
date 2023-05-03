def spc_to_383(spc):
    """
    Convert SS7 Signaling Point Code (SPC) to 3-8-3 format.
    input can be decimal or hexadecimal
    """
    if isinstance(spc, str):
        # Convert hexadecimal string to integer
        spc = int(spc, 16)

    # Convert SPC to binary and pad with leading zeros
    binary = '{0:b}'.format(spc).zfill(14)

    # Split the binary string into three parts: first 3 bits, next 8 bits, last 3 bits
    part1 = binary[:3]
    part2 = binary[3:11]
    part3 = binary[11:]

    # Convert each part to decimal format
    dec_part1 = int(part1, 2)
    dec_part2 = int(part2, 2)
    dec_part3 = int(part3, 2)

    # Format the parts as a string in 3-8-3 format
    spc_383 = '{}-{}-{}'.format(dec_part1, dec_part2, dec_part3)

    return spc_383

def spc_383_to_decimal(spc_383):
    """
    Convert SS7 Signaling Point Code (SPC) from 3-8-3 format to decimal format.
    """
    # Split the SPC into three parts using the '-' delimiter
    parts = spc_383.split('-')

    # Convert each part to binary format and concatenate them
    binary = '{:03b}{:08b}{:03b}'.format(int(parts[0]), int(parts[1]), int(parts[2]))

    # Convert the binary string to decimal format
    decimal = int(binary, 2)

    return decimal

def spc_383_to_hexa(spc_383):
    """
    Convert SS7 Signaling Point Code (SPC) from 3-8-3 format to decimal format.
    """
    # Split the SPC into three parts using the '-' delimiter
    parts = spc_383.split('-')

    # Convert each part to binary format and concatenate them
    binary = '{:03b}{:08b}{:03b}'.format(int(parts[0]), int(parts[1]), int(parts[2]))

    # Convert the binary string to decimal format
    decimal = int(binary, 2)
    hexa = hex(decimal)

    return hexa

result = spc_383_to_hexa("4-55-0")
print(result)
