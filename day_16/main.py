#!/usr/bin/python3
import functools as ft
import operator as op
from enum import Enum

HEX_BASE = 16
BIN_BASE = 2
BIN_DATA_SIZE = 4
PACKET_VERSION_LENGTH = 3
PACKET_TYPE_ID_LENGTH = 3
PACKET_HEADER_LENGTH = PACKET_VERSION_LENGTH + PACKET_TYPE_ID_LENGTH
LITERAL_VALUE_BITS_GROUP_SIZE = 5
BITS_NUM_LENGTH_TYPE_ID_0 = 15
BITS_NUM_LENGTH_TYPE_ID_1 = 11

class TypeId(Enum):
    SUM = 0
    PROD = 1
    MIN = 2
    MAX = 3
    LITERAL = 4
    GT = 5
    LT = 6
    EQ = 7 

def load_input(file_name):
    with open(file_name) as f:
        return hex_to_bin(f.readline())

def hex_to_bin(transmission):
    return bin(int(transmission, HEX_BASE))[2:].zfill(BIN_DATA_SIZE * len(transmission))

def bin_to_dec(bin_str):
    return int(bin_str, BIN_BASE)

def parse_packet(transmission):
    packets = []
    parse_packet_rec(transmission, 0, packets)
    return packets

def parse_packet_rec(transmission, offset, packets):
    version, type_id = parse_header(transmission, offset)
    packet_base = {'version': version, 'typeId': type_id}
    offset += PACKET_HEADER_LENGTH
    if type_id == TypeId.LITERAL:
        literal_value, upd_offset = parse_literal_value(transmission, offset)
        offset += upd_offset
        literal_value_packet = packet_base | {'literalValue': literal_value}
        packets.append(literal_value_packet)
    else:
        length_type_id, total_length, subpackets_num, upd_offset = parse_operator(transmission, offset)
        offset += upd_offset
        if total_length:
            current_offset = offset
            operator_packet = packet_base | {'lengthTypeId': length_type_id, 'totalLength': total_length}
            packets.append(operator_packet)
            while current_offset - offset < total_length:
                current_offset = parse_packet_rec(transmission, current_offset, packets)
            offset = current_offset
        elif subpackets_num:
            operator_packet = packet_base | {'lengthTypeId': length_type_id, 'subpacketsNum': subpackets_num}
            packets.append(operator_packet)
            for _ in range(subpackets_num):
                current_offset = parse_packet_rec(transmission, offset, packets)
                offset = current_offset
    return offset

def parse_header(transmission, offset):
    return bin_to_dec(transmission[offset:offset+PACKET_VERSION_LENGTH]), TypeId(bin_to_dec(transmission[offset+PACKET_VERSION_LENGTH:offset+PACKET_HEADER_LENGTH]))

def parse_literal_value(transmission, offset):
    i = 0
    literal_value = ''
    while bin_to_dec(transmission[offset+i]) == 1:
        literal_value += transmission[offset+i+1:offset+i+LITERAL_VALUE_BITS_GROUP_SIZE]
        i += LITERAL_VALUE_BITS_GROUP_SIZE
    literal_value += transmission[offset+i+1:offset+i+5]
    i += LITERAL_VALUE_BITS_GROUP_SIZE
    literal_value_dec = bin_to_dec(literal_value)
    return literal_value_dec, i

def parse_operator(transmission, offset):
    length_type_id = bin_to_dec(transmission[offset])
    i = 1
    total_length = None
    subpackets_num = None
    if length_type_id == 0:
        total_length = bin_to_dec(transmission[offset+i:offset+i+BITS_NUM_LENGTH_TYPE_ID_0])
        i += BITS_NUM_LENGTH_TYPE_ID_0
    elif length_type_id == 1:
        subpackets_num = bin_to_dec(transmission[offset+i:offset+i+BITS_NUM_LENGTH_TYPE_ID_1])
        i += BITS_NUM_LENGTH_TYPE_ID_1
    return length_type_id, total_length, subpackets_num, i

def evaluate(transmission):
    res, _ = evaluate_packet_rec(transmission, 0)
    return res

def evaluate_packet_rec(transmission, offset):
    _, type_id = parse_header(transmission, offset)
    offset += PACKET_HEADER_LENGTH
    if type_id == TypeId.LITERAL:
        literal_value, upd_offset = parse_literal_value(transmission, offset)
        offset += upd_offset
        return literal_value, offset
    else:
        _, total_length, subpackets_num, upd_offset = parse_operator(transmission, offset)
        offset += upd_offset
        partial_res = []
        if total_length:
            current_offset = offset
            while current_offset - offset < total_length:
                partial, current_offset = evaluate_packet_rec(transmission, current_offset)
                partial_res.append(partial)
            offset = current_offset
            return evaluate_operator(type_id, partial_res), offset
        elif subpackets_num:
            for _ in range(subpackets_num):
                partial, current_offset = evaluate_packet_rec(transmission, offset)
                offset = current_offset
                partial_res.append(partial)
            return evaluate_operator(type_id, partial_res), offset

def evaluate_operator(operator, operands):
    match operator:
        case TypeId.SUM:
            return ft.reduce(op.add, operands)
        case TypeId.PROD:
            return ft.reduce(op.mul, operands) 
        case TypeId.MIN:
            return ft.reduce(min, operands) 
        case TypeId.MAX:
            return ft.reduce(max, operands) 
        case TypeId.GT:
            return int(ft.reduce(op.gt, operands)) 
        case TypeId.LT:
            return int(ft.reduce(op.lt, operands)) 
        case TypeId.EQ:
            return int(ft.reduce(op.eq, operands)) 

def main():
    transmission = load_input('input.txt')
    packets = parse_packet(transmission)
    # PART 1
    versions_sum = ft.reduce(lambda acc, cur: acc + cur['version'], packets, 0)
    print(f'PART 1: {versions_sum}')
    # PART 2
    value = evaluate(transmission)
    print(f'PART 2: {value}')

if __name__ == '__main__':
    main()
