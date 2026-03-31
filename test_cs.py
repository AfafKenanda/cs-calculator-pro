
import pytest
from cs_logic import safe_eval, calculate_conversion, validate_ip, ip_to_binary


# ===== TESTS safe_eval =====

def test_safe_eval_hex_simple():
    assert safe_eval("FF", 16) == 255

def test_safe_eval_hex_addition():
    assert safe_eval("A+5", 16) == 15

def test_safe_eval_binary_simple():
    assert safe_eval("1010", 2) == 10

def test_safe_eval_binary_addition():
    assert safe_eval("101+10", 2) == 7


# ===== TESTS calculate_conversion =====

def test_dec_to_bin():
    assert calculate_conversion("8", "Dec->Bin") == "1000"

def test_bin_to_dec():
    assert calculate_conversion("1010", "Bin->Dec") == "10"

def test_dec_to_hex():
    assert calculate_conversion("255", "Dec->Hex") == "FF"

def test_hex_to_dec():
    assert calculate_conversion("FF", "Hex->Dec") == "255"

def test_bin_to_hex():
    assert calculate_conversion("11111111", "Bin->Hex") == "FF"

def test_hex_to_bin():
    assert calculate_conversion("FF", "Hex->Bin") == "11111111"


# ===== TESTS validate_ip =====

def test_ip_valid_classe_a():
    result = validate_ip("10.0.0.1")
    assert result["valid"] is True
    assert result["class"] == "Classe A"
    assert result["mask"] == "255.0.0.0"

def test_ip_valid_classe_b():
    result = validate_ip("172.16.0.1")
    assert result["valid"] is True
    assert result["class"] == "Classe B"

def test_ip_valid_classe_c():
    result = validate_ip("192.168.1.1")
    assert result["valid"] is True
    assert result["class"] == "Classe C"
    assert result["mask"] == "255.255.255.0"

def test_ip_network_address():
    result = validate_ip("192.168.1.50")
    assert result["network"] == "192.168.1.0"

def test_ip_broadcast_address():
    result = validate_ip("192.168.1.50")
    assert result["broadcast"] == "192.168.1.255"

def test_ip_invalide():
    result = validate_ip("999.999.999.999")
    assert result["valid"] is False

def test_ip_invalide_texte():
    result = validate_ip("hello")
    assert result["valid"] is False


# ===== TESTS ip_to_binary =====

def test_ip_to_binary_normal():
    assert ip_to_binary("192.168.1.1") == "11000000.10101000.00000001.00000001"

def test_ip_to_binary_zeros():
    assert ip_to_binary("0.0.0.0") == "00000000.00000000.00000000.00000000"

def test_ip_to_binary_max():
    assert ip_to_binary("255.255.255.255") == "11111111.11111111.11111111.11111111"

def test_ip_to_binary_invalide():
    assert ip_to_binary("abc.def") == "Error"
