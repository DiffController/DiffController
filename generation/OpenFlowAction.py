delay_times = [1]

dup_nums = [2]

drop_flag = [
    True,
]

message_type =  [
    
]

message_transmission_actions = [
    ["DROP", "DROP,f={0}", drop_flag],
	["DUP", "DUP,n={0}", dup_nums],
	["DELAY", "DELAY,s={0}", delay_times],
]

message_modify_actions = [
    ["MOD", "MOD,field=({0})&val=({1})"]
]

message_block_actions = [
    ["ADD", "ADD,field=({0})&val=({1})"],
    ["DEL", "DEL,field=({0})"]

]

message_build_actions = [
    ["BUILD", 'BUILD,type=({0})&val=({1})'],
]

field_operation = [
	"="
]

field_values = [
    'uint8',
    'uint16',
    'uint32',
    'uint48', # hw_addr
    'uint64',
    'uint128', # ipv6_src
    'uint256',
    'port'
]
