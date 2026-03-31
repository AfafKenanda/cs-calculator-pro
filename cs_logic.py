
import ipaddress
import re


def safe_eval(value, base):
    value = value.upper()
    tokens = re.findall(r"[0-9A-F]+|[\+\-\*/]", value)
    expr = []
    for t in tokens:
        if t in ["+", "-", "*", "/"]:
            expr.append(t)
        else:
            expr.append(str(int(t, base)))
    return eval(" ".join(expr))


def calculate_conversion(value, conversion):
    try:
        if any(c in value for c in "01") and re.fullmatch(r"[01+\-*/. ]+", value):
            result = safe_eval(value, 2)
        elif re.search(r"[A-F]", value.upper()):
            result = safe_eval(value, 16)
        else:
            result = eval(value)

        if conversion == "Dec->Bin":
            return bin(int(result))[2:]
        elif conversion == "Bin->Dec":
            return str(int(result))
        elif conversion == "Dec->Hex":
            return hex(int(result))[2:].upper()
        elif conversion == "Hex->Dec":
            return str(int(result))
        elif conversion == "Bin->Hex":
            return hex(int(result))[2:].upper()
        elif conversion == "Hex->Bin":
            return bin(int(result))[2:]
    except Exception:
        return "Error"


def validate_ip(ip):
    try:
        ipaddress.IPv4Address(ip)
        first_octet = int(ip.split(".")[0])
        if 1 <= first_octet <= 126:
            ip_class = "Classe A"
            mask = "255.0.0.0"
        elif 128 <= first_octet <= 191:
            ip_class = "Classe B"
            mask = "255.255.0.0"
        elif 192 <= first_octet <= 223:
            ip_class = "Classe C"
            mask = "255.255.255.0"
        else:
            ip_class = "Speciale"
            mask = "255.255.255.0"
        net = ipaddress.IPv4Network(f"{ip}/{mask}", strict=False)
        return {
            "valid": True,
            "class": ip_class,
            "mask": mask,
            "network": str(net.network_address),
            "broadcast": str(net.broadcast_address),
        }
    except Exception:
        return {"valid": False}


def ip_to_binary(ip):
    try:
        return ".".join([format(int(o), "08b") for o in ip.split(".")])
    except Exception:
        return "Error"
