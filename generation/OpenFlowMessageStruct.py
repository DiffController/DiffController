
fields_of_aggregate_stats_reply = [
	{'name':'version', 'type':'uint8'},
	{'name':'type', 'type':'uint8'},
	{'name':'length', 'type':'uint16'},
	{'name':'xid', 'type':'uint32'},
	{'name':'flags', 'type':'uint16'},
	{'name':'packet_count', 'type':'uint64'},
	{'name':'byte_count', 'type':'uint64'},
	{'name':'flow_count', 'type':'uint32'},
]

fields_of_aggregate_stats_request = [
	{'name':'version', 'type':'uint8'},
	{'name':'type', 'type':'uint8'},
	{'name':'length', 'type':'uint16'},
	{'name':'xid', 'type':'uint32'},
	{'name':'flags', 'type':'uint16'},
	{'name':'table_id', 'type':'uint8'},
	{'name':'out_port', 'type':'uint32'},
	{'name':'out_group', 'type':'uint32'},
	{'name':'cookie', 'type':'uint64'},
	{'name':'cookie_mask', 'type':'uint64'},
	{'name':'match', 'fields': [
		{'name':'match','fields':[
			{'name':'oxm_list','type':'list','fields':[
				{'name':'in_port', 'type':'port'}, #0
				{'name':'in_phy_port', 'type':'port'}, #1
				{'name':'metadata', 'type':'uint64'}, #2
				{'name':'eth_dst', 'type':'uint48'}, #3
				{'name':'eth_src', 'type':'uint48'}, #4
				{'name':'eth_type', 'type':'uint16'}, #5
				{'name':'vlan_vid', 'type':'uint16','range':'[[0x0,0x0],[0x1000,0x1fff]]'}, #6
				{'name':'vlan_pcp', 'type':'uint8','range':'[[0x0,0x7]]'}, #7
				{'name':'ip_dscp', 'type':'uint8','range':'[[0x0,0x3f]]'}, #8
				{'name':'ip_ecn', 'type':'uint8','range':'[[0x0,0x3]]'}, #9
				{'name':'ip_proto', 'type':'uint8'}, #10
				{'name':'ipv4_src', 'type':'uint32'}, #11
				{'name':'ipv4_dst', 'type':'uint32'}, #12
				{'name':'tcp_src', 'type':'uint16'}, #13
				{'name':'tcp_dst', 'type':'uint16'}, #14
				{'name':'udp_src', 'type':'uint16'}, #15
				{'name':'udp_dst', 'type':'uint16'}, #16
				{'name':'sctp_src', 'type':'uint16'}, #17
				{'name':'sctp_dst', 'type':'uint16'}, #18
				{'name':'icmpv4_type', 'type':'uint8'}, #19
				{'name':'icmpv4_code', 'type':'uint8'}, #20
				{'name':'arp_op', 'type':'uint16'}, #21
				{'name':'arp_spa', 'type':'uint32'}, #22
				{'name':'arp_tpa', 'type':'uint32'}, #23
				{'name':'arp_sha', 'type':'uint48'}, #24
				{'name':'arp_tha', 'type':'uint48'}, #25
				{'name':'ipv6_src', 'type':'uint128'}, #26
				{'name':'ipv6_dst', 'type':'uint128'}, #27
				{'name':'ipv6_flabel', 'type':'uint32'}, #28
				{'name':'icmpv6_type', 'type':'uint8'}, #29
				{'name':'icmpv6_code', 'type':'uint8'}, #30
				{'name':'ipv6_nd_target', 'type':'uint128'}, #31
				{'name':'ipv6_nd_sll', 'type':'uint48'}, #32
				{'name':'ipv6_nd_tll', 'type':'uint48'}, #33
				{'name':'mpls_label', 'type':'uint32'},	#34
				{'name':'mpls_tc', 'type':'uint8'},	#35
				{'name':'mpls_bos', 'type':'uint8'}, #36
				{'name':'pbb_isid', 'impl':False, 'type':'uint64'}, #37
				{'name':'tunnel_id', 'type':'uint64'},	#38
				{'name':'ipv6_exthdr', 'type':'uint16'}, #39
			]}
		]},
	]},

	# {'name':'match', 'fields': [
	# 	{'name':'version', 'type':'uint8'},
	# 	{'name':'fields', 'fields':[
	# 		{'name':'in_port', 'type':'port'}, #uint32
	# 		{'name':'in_phy_port', 'type':'port'}, #uint32
	# 		{'name':'metadata', 'type':'uint64'},
	# 		{'name':'eth_dst', 'type':'uint48'},
	# 		{'name':'eth_src', 'type':'uint48'},
	# 		{'name':'eth_type', 'type':'uint16'},
	# 		{'name':'vlan_vid', 'type':'uint16'},
	# 		{'name':'vlan_pcp', 'type':'uint8'},
	# 		{'name':'ip_dscp', 'type':'uint8'},
	# 		{'name':'ip_ecn', 'type':'uint8'},
	# 		{'name':'ip_proto', 'type':'uint8'},
	# 		{'name':'ipv4_src', 'type':'uint32'},
	# 		{'name':'ipv4_dst', 'type':'uint32'},
	# 		{'name':'tcp_src', 'type':'uint16'},
	# 		{'name':'tcp_dst', 'type':'uint16'},
	# 		{'name':'udp_src', 'type':'uint16'},
	# 		{'name':'udp_dst', 'type':'uint16'},
	# 		{'name':'sctp_src', 'type':'uint16'},
	# 		{'name':'sctp_dst', 'type':'uint16'},
	# 		{'name':'icmpv4_type', 'type':'uint8'},
	# 		{'name':'icmpv4_code', 'type':'uint8'},
	# 		{'name':'arp_op', 'type':'uint16'},
	# 		{'name':'arp_spa', 'type':'uint32'},
	# 		{'name':'arp_tpa', 'type':'uint32'},
	# 		{'name':'arp_sha', 'type':'uint48'},
	# 		{'name':'arp_tha', 'type':'uint48'},
	# 		{'name':'ipv6_src', 'impl':False, 'type':'uint128'},
	# 		{'name':'ipv6_dst', 'impl':False, 'type':'uint128'},
	# 		{'name':'ipv6_flabel', 'type':'uint32'},
	# 		{'name':'icmpv6_type', 'type':'uint8'},
	# 		{'name':'icmpv6_code', 'type':'uint8'},
	# 		{'name':'ipv6_nd_target', 'impl':False, 'type':'uint128'},
	# 		{'name':'ipv6_nd_sll', 'type':'uint48'},
	# 		{'name':'ipv6_nd_tll', 'type':'uint48'},
	# 		{'name':'mpls_label', 'type':'uint32'},
	# 		{'name':'mpls_tc', 'type':'uint8'},
	# 		{'name':'mpls_bos', 'type':'uint8'},
	# 		{'name':'tunnel_id', 'type':'uint64'},
	# 		{'name':'ipv6_exthdr', 'type':'uint16'},
	# 		{'name':'pbb_uca', 'type':'uint8'},
	# 		{'name':'tunnel_ipv4_src', 'type':'uint32'},
	# 		{'name':'tunnel_ipv4_dst', 'type':'uint32'},
	# 	]},
	# 	{'name':'masks', 'fields':[
	# 		{'name':'in_port', 'type':'uint32'},
	# 		{'name':'in_phy_port', 'type':'uint32'},
	# 		{'name':'metadata', 'type':'uint64'},
	# 		{'name':'eth_dst', 'type':'uint48'},
	# 		{'name':'eth_src', 'type':'uint48'},
	# 		{'name':'eth_type', 'type':'uint16'},
	# 		{'name':'vlan_vid', 'type':'uint16'},
	# 		{'name':'vlan_pcp', 'type':'uint8'},
	# 		{'name':'ip_dscp', 'type':'uint8'},
	# 		{'name':'ip_ecn', 'type':'uint8'},
	# 		{'name':'ip_proto', 'type':'uint8'},
	# 		{'name':'ipv4_src', 'type':'uint32'},
	# 		{'name':'ipv4_dst', 'type':'uint32'},
	# 		{'name':'tcp_src', 'type':'uint16'},
	# 		{'name':'tcp_dst', 'type':'uint16'},
	# 		{'name':'udp_src', 'type':'uint16'},
	# 		{'name':'udp_dst', 'type':'uint16'},
	# 		{'name':'sctp_src', 'type':'uint16'},
	# 		{'name':'sctp_dst', 'type':'uint16'},
	# 		{'name':'icmpv4_type', 'type':'uint8'},
	# 		{'name':'icmpv4_code', 'type':'uint8'},
	# 		{'name':'arp_op', 'type':'uint16'},
	# 		{'name':'arp_spa', 'type':'uint32'},
	# 		{'name':'arp_tpa', 'type':'uint32'},
	# 		{'name':'arp_sha', 'type':'uint48'},
	# 		{'name':'arp_tha', 'type':'uint48'},
	# 		{'name':'ipv6_src', 'impl':False, 'type':'uint128'},
	# 		{'name':'ipv6_dst', 'impl':False, 'type':'uint128'},
	# 		{'name':'ipv6_flabel', 'type':'uint32'},
	# 		{'name':'icmpv6_type', 'type':'uint8'},
	# 		{'name':'icmpv6_code', 'type':'uint8'},
	# 		{'name':'ipv6_nd_target', 'impl':False, 'type':'uint128'},
	# 		{'name':'ipv6_nd_sll', 'type':'uint48'},
	# 		{'name':'ipv6_nd_tll', 'type':'uint48'},
	# 		{'name':'mpls_label', 'type':'uint32'},
	# 		{'name':'mpls_tc', 'type':'uint8'},
	# 		{'name':'mpls_bos', 'type':'uint8'},
	# 		{'name':'tunnel_id', 'type':'uint64'},
	# 		{'name':'ipv6_exthdr', 'type':'uint16'},
	# 		{'name':'pbb_uca', 'type':'uint8'},
	# 		{'name':'tunnel_ipv4_src', 'type':'uint32'},
	# 		{'name':'tunnel_ipv4_dst', 'type':'uint32'},
	# 	]},
	# ]}
]

fields_of_async_config_failed_error_msg = [
	{'name':'version', 'type':'uint8'},
	{'name':'type', 'type':'uint8'},
	{'name':'length', 'type':'uint16'},
	{'name':'xid', 'type':'uint32'},
	{'name':'code', 'type':'uint16'},
	{'name':'data', 'impl':False},
]

fields_of_async_get_reply = [
	{'name':'version', 'type':'uint8'},
	{'name':'type', 'type':'uint8'},
	{'name':'length', 'type':'uint16'},
	{'name':'xid', 'type':'uint32'},
	# {'name':'properties', 'fields': [
	# 	##TODO: This Handling is bad
	# 	{'name':'element','type':'TLV', 'fields':[
	# 		{'name':'mask', 'type':'uint32'},
	# 	]},
	# ]},
	{'name':'packet_in_mask_equal_master', 'type':'uint32'},
	{'name':'packet_in_mask_slave', 'type':'uint32'},
	{'name':'port_status_mask_equal_master', 'type':'uint32'},
	{'name':'port_status_mask_slave', 'type':'uint32'},
	{'name':'flow_removed_mask_equal_master', 'type':'uint32'},
	{'name':'flow_removed_mask_slave', 'type':'uint32'},
]

fields_of_async_get_request = [
	{'name':'version', 'type':'uint8'},
	{'name':'type', 'type':'uint8'},
	{'name':'length', 'type':'uint16'},
	{'name':'xid', 'type':'uint32'},
	# {'name':'properties', 'fields': [
	# 	##TODO: This Handling is bad
	# 	{'name':'element','type':'TLV','fields':[
	# 		{'name':'mask', 'type':'uint32'},
	# 	]},
	# ]},
	# {'name':'packet_in_mask_equal_master', 'type':'uint32'},
	# {'name':'packet_in_mask_slave', 'type':'uint32'},
	# {'name':'port_status_mask_equal_master', 'type':'uint32'},
	# {'name':'port_status_mask_slave', 'type':'uint32'},
	# {'name':'flow_removed_mask_equal_master', 'type':'uint32'},
	# {'name':'flow_removed_mask_slave', 'type':'uint32'},
]

fields_of_async_set = [
	{'name':'version', 'type':'uint8'},
	{'name':'type', 'type':'uint8'},
	{'name':'length', 'type':'uint16'},
	{'name':'xid', 'type':'uint32'},
	# {'name':'properties', 'fields': [
	# 	##TODO: This Handling is bad
	# 	{'name':'element','type':'TLV','fields':[
	# 		{'name':'mask', 'type':'uint32'},
	# 	]},
	# ]},
	{'name':'packet_in_mask_equal_master', 'type':'uint32'},
	{'name':'packet_in_mask_slave', 'type':'uint32'},
	{'name':'port_status_mask_equal_master', 'type':'uint32'},
	{'name':'port_status_mask_slave', 'type':'uint32'},
	{'name':'flow_removed_mask_equal_master', 'type':'uint32'},
	{'name':'flow_removed_mask_slave', 'type':'uint32'},
]

fields_of_bad_action_error_msg = [
	{'name':'version', 'type':'uint8'},
	{'name':'type', 'type':'uint8'},
	{'name':'length', 'type':'uint16'},
	{'name':'xid', 'type':'uint32'},
	{'name':'code', 'type':'uint16'},
	{'name':'data', 'impl':False},
]

fields_of_bad_instruction_error_msg = [
	{'name':'version', 'type':'uint8'},
	{'name':'type', 'type':'uint8'},
	{'name':'length', 'type':'uint16'},
	{'name':'xid', 'type':'uint32'},
	{'name':'code', 'type':'uint16'},
	{'name':'data', 'impl':False},
]

fields_of_bad_match_error_msg = [
	{'name':'version', 'type':'uint8'},
	{'name':'type', 'type':'uint8'},
	{'name':'length', 'type':'uint16'},
	{'name':'xid', 'type':'uint32'},
	{'name':'code', 'type':'uint16'},
	{'name':'data', 'impl':False},
]

fields_of_bad_property_error_msg = [
	{'name':'version', 'type':'uint8'},
	{'name':'type', 'type':'uint8'},
	{'name':'length', 'type':'uint16'},
	{'name':'xid', 'type':'uint32'},
	{'name':'code', 'type':'uint16'},
	{'name':'data', 'impl':False},
]

fields_of_bad_request_error_msg = [
	{'name':'version', 'type':'uint8'},
	{'name':'type', 'type':'uint8'},
	{'name':'length', 'type':'uint16'},
	{'name':'xid', 'type':'uint32'},
	{'name':'code', 'type':'uint16'},
	{'name':'data', 'impl':False},
]

fields_of_barrier_reply = [
	{'name':'version', 'type':'uint8'},
	{'name':'type', 'type':'uint8'},
	{'name':'length', 'type':'uint16'},
	{'name':'xid', 'type':'uint32'},
]

fields_of_barrier_request = [
	{'name':'version', 'type':'uint8'},
	{'name':'type', 'type':'uint8'},
	{'name':'length', 'type':'uint16'},
	{'name':'xid', 'type':'uint32'},
]

fields_of_bundle_add_msg = [
	{'name':'version', 'type':'uint8'},
	{'name':'type', 'type':'uint8'},
	{'name':'length', 'type':'uint16'},
	{'name':'xid', 'type':'uint32'},
	{'name':'bundle_id', 'type':'uint32'},
	{'name':'flags', 'type':'uint16'},
	{'name':'data', 'impl':False},
]

fields_of_bundle_ctrl_msg = [
	{'name':'version', 'type':'uint8'},
	{'name':'type', 'type':'uint8'},
	{'name':'length', 'type':'uint16'},
	{'name':'xid', 'type':'uint32'},
	{'name':'bundle_id', 'type':'uint32'},
	{'name':'bundle_ctrl_type', 'type':'uint16'},
	{'name':'flags', 'type':'uint16'},
	{'name':'properties', 'fields': [
		##TODO: This Handling is bad
		{'name':'element','type':'TLV', 'max':2, 'fields':[
			{'name':'seconds', 'type':'uint32'},
			{'name':'nanoseconds', 'type':'uint32'},
		]},
	]},
]

fields_of_bundle_failed_error_msg = [
	{'name':'version', 'type':'uint8'},
	{'name':'type', 'type':'uint8'},
	{'name':'length', 'type':'uint16'},
	{'name':'xid', 'type':'uint32'},
	{'name':'code', 'type':'uint16'},
	{'name':'data', 'impl':False},
]

fields_of_desc_stats_reply = [
	{'name':'version', 'type':'uint8'},
	{'name':'type', 'type':'uint8'},
	{'name':'length', 'type':'uint16'},
	{'name':'xid', 'type':'uint32'},
	{'name':'flags', 'type':'uint16'},
	{'name':'mfr_desc', 'type':'string'},
	{'name':'hw_desc', 'type':'string'},
	{'name':'sw_desc', 'type':'string'},
	{'name':'serial_num', 'type':'string'},
	{'name':'dp_desc', 'type':'string'},
	# {'name':'mfr_desc', 'impl':False},
	# {'name':'hw_desc', 'impl':False},
	# {'name':'sw_desc', 'impl':False},
	# {'name':'serial_desc', 'impl':False},
	# {'name':'dp_desc', 'impl':False},
]

fields_of_desc_stats_request = [
	{'name':'version', 'type':'uint8'},
	{'name':'type', 'type':'uint8'},
	{'name':'length', 'type':'uint16'},
	{'name':'xid', 'type':'uint32'},
	{'name':'flags', 'type':'uint16'},
]

fields_of_echo_reply = [
	# {'name':'version', 'type':'uint8'},
	# {'name':'type', 'type':'uint8'},
	# {'name':'length', 'type':'uint16'},
	# {'name':'xid', 'type':'uint32'},
	# {'name':'data', 'impl':False},
	{'name':'version', 'type':'uint8'},
	{'name':'type', 'type':'uint8'},
	{'name':'length', 'type':'uint16'},
	{'name':'xid', 'type':'uint32'},
	{'name':'data', 'type':'string'},	
]

fields_of_echo_request = [
	# {'name':'version', 'type':'uint8'},
	# {'name':'type', 'type':'uint8'},
	# {'name':'length', 'type':'uint16'},
	# {'name':'xid', 'type':'uint32'},
	# {'name':'data', 'impl':False},
	{'name':'version', 'type':'uint8'},
	{'name':'type', 'type':'uint8'},
	{'name':'length', 'type':'uint16'},
	{'name':'xid', 'type':'uint32'},
	{'name':'data', 'type':'string'},
]

fields_of_experimenter = [
	{'name':'version', 'type':'uint8'},
	{'name':'type', 'type':'uint8'},
	{'name':'length', 'type':'uint16'},
	{'name':'xid', 'type':'uint32'},
	{'name':'experimenter', 'impl':False},
	{'name':'exp_type', 'impl':False},
]

fields_of_experimenter_error_msg = [
	{'name':'version', 'type':'uint8'},
	{'name':'type', 'type':'uint8'},
	{'name':'length', 'type':'uint16'},
	{'name':'xid', 'type':'uint32'},
	{'name':'code', 'type':'uint16'},
	{'name':'data', 'impl':False},
]

fields_of_experimenter_stats_reply = [
	{'name':'version', 'type':'uint8'},
	{'name':'type', 'type':'uint8'},
	{'name':'length', 'type':'uint16'},
	{'name':'xid', 'type':'uint32'},
	{'name':'experimenter', 'impl':False},
	{'name':'exp_type', 'impl':False},
]

fields_of_experimenter_stats_request = [
	{'name':'version', 'type':'uint8'},
	{'name':'type', 'type':'uint8'},
	{'name':'length', 'type':'uint16'},
	{'name':'xid', 'type':'uint32'},
	{'name':'experimenter', 'impl':False},
	{'name':'exp_type', 'impl':False},
]

fields_of_features_reply = [
	# {'name':'version', 'type':'uint8'},
	# {'name':'type', 'type':'uint8'},
	# {'name':'length', 'type':'uint16'},
	# {'name':'xid', 'type':'uint32'},
	# {'name':'datapath_id', 'type':'uint64'},
	# {'name':'n_buffers', 'type':'uint32'},
	# {'name':'n_tables', 'type':'uint8'},
	# {'name':'auxilary_id', 'type':'uint8'},
	# {'name':'capabilities', 'type':'uint32'},
	# {'name':'reserved', 'type':'uint32'},
	# {'name':'ports', 'fields':[
	# 	{'name':'element','type':'list', 'fields':[
	# 		{'name':'port_no', 'type':'port'}, #uint32
	# 		{'name':'hw_addr', 'type':'uint48'},
	# 		{'name':'name', 'impl':False},
	# 		{'name':'config', 'type':'uint32'},
	# 		{'name':'state', 'type':'uint32'},
	# 		{'name':'properties', 'fields':[
	# 			##TODO: This Handling is bad
	# 			{'name':'element','type':'TLV', 'max':3, 'fields':[
	# 				{'name':'curr', 'type':'uint32'},
	# 				{'name':'advertised', 'type':'uint32'},
	# 				{'name':'supported', 'type':'uint32'},
	# 				{'name':'peer', 'type':'uint32'},
	# 				{'name':'curr_speed', 'type':'uint32'},
	# 				{'name':'max_speed', 'type':'uint32'},
	# 				{'name':'rx_grid_freq_lmda', 'type':'uint32'},
	# 				{'name':'tx_pwr_min', 'type':'uint32'},
	# 				{'name':'tx_pwr_max', 'type':'uint32'},
	# 			]},
	# 		]},
	# 		{'name':'curr', 'type':'uint32'},
	# 		{'name':'advertised', 'type':'uint32'},
	# 		{'name':'supported', 'type':'uint32'},
	# 		{'name':'peer', 'type':'uint32'},
	# 		{'name':'curr_speed', 'type':'uint32'},
	# 		{'name':'max_speed', 'type':'uint32'},
	# 	]},
	# ]},
	# {'name':'actions', 'type':'uint32'},
	{'name':'version', 'type':'uint8'},
	{'name':'type', 'type':'uint8'},
	{'name':'length', 'type':'uint16'},
	{'name':'xid', 'type':'uint32'},
	{'name':'datapath_id', 'type':'uint64','range':'[[0x0,0x0000ffffffffffff]]'},
	{'name':'n_buffers', 'type':'uint32'},
	{'name':'n_tables', 'type':'uint8'},
	{'name':'auxiliary_id', 'type':'uint8'},
	{'name':'capabilities', 'type':'uint32'},
	{'name':'reserved', 'type':'uint32'},
]

fields_of_features_request = [
	{'name':'version', 'type':'uint8'},
	{'name':'type', 'type':'uint8'},
	{'name':'length', 'type':'uint16'},
	{'name':'xid', 'type':'uint32'},
]

fields_of_flow_add = [
	{'name':'version', 'type':'uint8'},
	{'name':'type', 'type':'uint8'},
	{'name':'length', 'type':'uint16'},
	{'name':'xid', 'type':'uint32'},
	{'name':'cookie', 'type':'uint64'},
	{'name':'cookie_mask', 'type':'uint64'},
	{'name':'table_id', 'type':'uint8'},
	{'name':'idle_timeout', 'type':'uint16'},
	{'name':'hard_timeout', 'type':'uint16'},
	{'name':'priority', 'type':'uint16'},
	{'name':'buffer_id', 'type':'uint32'},
	{'name':'out_port', 'type':'uint32'},
	{'name':'out_group', 'type':'uint32'},
	{'name':'flags', 'type':'uint16'},
	{'name':'match', 'fields': [
		{'name':'match','fields':[
			{'name':'oxm_list','type':'list','fields':[
				{'name':'in_port', 'type':'port'}, #0
				{'name':'in_phy_port', 'type':'port'}, #1
				{'name':'metadata', 'type':'uint64'}, #2
				{'name':'eth_dst', 'type':'uint48'}, #3
				{'name':'eth_src', 'type':'uint48'}, #4
				{'name':'eth_type', 'type':'uint16'}, #5
				{'name':'vlan_vid', 'type':'uint16','range':'[[0x0,0x0],[0x1000,0x1fff]]'}, #6
				{'name':'vlan_pcp', 'type':'uint8','range':'[[0x0,0x7]]'}, #7
				{'name':'ip_dscp', 'type':'uint8','range':'[[0x0,0x3f]]'}, #8
				{'name':'ip_ecn', 'type':'uint8','range':'[[0x0,0x3]]'}, #9
				{'name':'ip_proto', 'type':'uint8'}, #10
				{'name':'ipv4_src', 'type':'uint32'}, #11
				{'name':'ipv4_dst', 'type':'uint32'}, #12
				{'name':'tcp_src', 'type':'uint16'}, #13
				{'name':'tcp_dst', 'type':'uint16'}, #14
				{'name':'udp_src', 'type':'uint16'}, #15
				{'name':'udp_dst', 'type':'uint16'}, #16
				{'name':'sctp_src', 'type':'uint16'}, #17
				{'name':'sctp_dst', 'type':'uint16'}, #18
				{'name':'icmpv4_type', 'type':'uint8'}, #19
				{'name':'icmpv4_code', 'type':'uint8'}, #20
				{'name':'arp_op', 'type':'uint16'}, #21
				{'name':'arp_spa', 'type':'uint32'}, #22
				{'name':'arp_tpa', 'type':'uint32'}, #23
				{'name':'arp_sha', 'type':'uint48'}, #24
				{'name':'arp_tha', 'type':'uint48'}, #25
				{'name':'ipv6_src', 'type':'uint128'}, #26
				{'name':'ipv6_dst', 'type':'uint128'}, #27
				{'name':'ipv6_flabel', 'type':'uint32'}, #28
				{'name':'icmpv6_type', 'type':'uint8'}, #29
				{'name':'icmpv6_code', 'type':'uint8'}, #30
				{'name':'ipv6_nd_target', 'type':'uint128'}, #31
				{'name':'ipv6_nd_sll', 'type':'uint48'}, #32
				{'name':'ipv6_nd_tll', 'type':'uint48'}, #33
				{'name':'mpls_label', 'type':'uint32'},	#34
				{'name':'mpls_tc', 'type':'uint8'},	#35
				{'name':'mpls_bos', 'type':'uint8'}, #36
				{'name':'pbb_isid', 'impl':False, 'type':'uint64'}, #37
				{'name':'tunnel_id', 'type':'uint64'},	#38
				{'name':'ipv6_exthdr', 'type':'uint16'}, #39
			]}
		]},
	]},
	{'name':'instructions','type':'list','fields':[
		{'name':'goto_table','fields':[
			{'name':'table_id', 'type':'uint8'},
		]}, #1
		{'name':'write_metadata','fields':[
			{'name':'metadata', 'type':'uint64'},
			{'name':'metadata_mask', 'type':'uint64'},
		]}, #2
		{'name':'write_actions','fields':[
			{'name':'actions','type':'list','fields':[
				{'name':'output','fields':[
					{'name':'port', 'type':'port'},
					{'name':'max_len', 'type':'uint16'}
				]}, #0
				{'name':'copy_ttl_out','type':''}, #11
				{'name':'copy_ttl_in','type':''}, #12
				{'name':'set_mpls_ttl','fields':[
					{'name':'mpls_ttl', 'type':'uint8'},
				]}, #15
				{'name':'dec_mpls_ttl','type':''}, #16
				{'name':'push_vlan','fields':[
					{'name':'ethertype', 'type':'uint16'},
				]}, #17
				{'name':'pop_vlan','type':''}, #18
				{'name':'push_mpls','fields':[
					{'name':'ethertype', 'type':'uint16'},
				]}, #19
				{'name':'pop_mpls','fields':[
					{'name':'ethertype', 'type':'uint16'},
				]}, #20
				{'name':'set_queue','fields':[
					{'name':'queue_id', 'type':'uint32'},
				]}, #21
				{'name':'group','fields':[
					{'name':'group_id', 'type':'uint32','range':'[[0x0,0xffffff00],[0xfffffffc,0xfffffffc],[0xffffffff,0xffffffff]]'},
				]}, #22
				{'name':'set_nw_ttl','fields':[
					{'name':'nw_ttl', 'type':'uint8'},
				]}, #23
				{'name':'dec_nw_ttl','type':''}, #24
				{'name':'set_field','impl':False}, #25 field is too difficulty to implement
				{'name':'push_pbb','fields':[
					{'name':'ethertype', 'type':'uint16'},
				]}, #26
				{'name':'pop_pbb','type':''}, #27
				{'name':'experimenter','impl':False}, #ffff experimenter is also difficulty to implement
			]},
		]}, #3
		{'name':'apply_actions','fields':[
			{'name':'actions','type':'list','fields':[
				{'name':'output','fields':[
					{'name':'port', 'type':'port'},
					{'name':'max_len', 'type':'uint16'}
				]}, #0
				{'name':'copy_ttl_out','type':''}, #11
				{'name':'copy_ttl_in','type':''}, #12
				{'name':'set_mpls_ttl','fields':[
					{'name':'mpls_ttl', 'type':'uint8'},
				]}, #15
				{'name':'dec_mpls_ttl','type':''}, #16
				{'name':'push_vlan','fields':[
					{'name':'ethertype', 'type':'uint16'},
				]}, #17
				{'name':'pop_vlan','type':''}, #18
				{'name':'push_mpls','fields':[
					{'name':'ethertype', 'type':'uint16'},
				]}, #19
				{'name':'pop_mpls','fields':[
					{'name':'ethertype', 'type':'uint16'},
				]}, #20
				{'name':'set_queue','fields':[
					{'name':'queue_id', 'type':'uint32'},
				]}, #21
				{'name':'group','fields':[
					{'name':'group_id', 'type':'uint32','range':'[[0x0,0xffffff00],[0xfffffffc,0xfffffffc],[0xffffffff,0xffffffff]]'},
				]}, #22
				{'name':'set_nw_ttl','fields':[
					{'name':'nw_ttl', 'type':'uint8'},
				]}, #23
				{'name':'dec_nw_ttl','type':''}, #24
				{'name':'set_field','impl':False}, #25 field is too difficulty to implement
				{'name':'push_pbb','fields':[
					{'name':'ethertype', 'type':'uint16'},
				]}, #26
				{'name':'pop_pbb','type':''}, #27
				{'name':'experimenter','impl':False}, #ffff experimenter is also difficulty to implement
			]},
		]}, #4
		{'name':'clear_actions','type':''}, #5
		{'name':'meter','fields':[
			{'name':'meter_id', 'type':'uint32','range':'[[0x0,0xffff0000],[0xfffffffd,0xffffffff]]'},
		]}, #6
		{'name':'experimenter','impl':False,}, #ffff
	]}
	# {'name':'importance', 'type':'uint16'},
	# {'name':'match', 'fields': [
	# 	{'name':'version', 'type':'uint8'},
	# 	{'name':'fields', 'fields':[
	# 		{'name':'in_port', 'type':'port'}, #uint32
	# 		{'name':'in_phy_port', 'type':'port'}, #uint32
	# 		{'name':'metadata', 'type':'uint64'},
	# 		{'name':'eth_dst', 'type':'uint48'},
	# 		{'name':'eth_src', 'type':'uint48'},
	# 		{'name':'eth_type', 'type':'uint16'},
	# 		{'name':'vlan_vid', 'type':'uint16'},
	# 		{'name':'vlan_pcp', 'type':'uint8'},
	# 		{'name':'ip_dscp', 'type':'uint8'},
	# 		{'name':'ip_ecn', 'type':'uint8'},
	# 		{'name':'ip_proto', 'type':'uint8'},
	# 		{'name':'ipv4_src', 'type':'uint32'},
	# 		{'name':'ipv4_dst', 'type':'uint32'},
	# 		{'name':'tcp_src', 'type':'uint16'},
	# 		{'name':'tcp_dst', 'type':'uint16'},
	# 		{'name':'udp_src', 'type':'uint16'},
	# 		{'name':'udp_dst', 'type':'uint16'},
	# 		{'name':'sctp_src', 'type':'uint16'},
	# 		{'name':'sctp_dst', 'type':'uint16'},
	# 		{'name':'icmpv4_type', 'type':'uint8'},
	# 		{'name':'icmpv4_code', 'type':'uint8'},
	# 		{'name':'arp_op', 'type':'uint16'},
	# 		{'name':'arp_spa', 'type':'uint32'},
	# 		{'name':'arp_tpa', 'type':'uint32'},
	# 		{'name':'arp_sha', 'type':'uint48'},
	# 		{'name':'arp_tha', 'type':'uint48'},
	# 		{'name':'ipv6_src', 'impl':False, 'type':'uint128'},
	# 		{'name':'ipv6_dst', 'impl':False, 'type':'uint128'},
	# 		{'name':'ipv6_flabel', 'type':'uint32'},
	# 		{'name':'icmpv6_type', 'type':'uint8'},
	# 		{'name':'icmpv6_code', 'type':'uint8'},
	# 		{'name':'ipv6_nd_target', 'impl':False, 'type':'uint128'},
	# 		{'name':'ipv6_nd_sll', 'type':'uint48'},
	# 		{'name':'ipv6_nd_tll', 'type':'uint48'},
	# 		{'name':'mpls_label', 'type':'uint32'},
	# 		{'name':'mpls_tc', 'type':'uint8'},
	# 		{'name':'mpls_bos', 'type':'uint8'},
	# 		{'name':'tunnel_id', 'type':'uint64'},
	# 		{'name':'ipv6_exthdr', 'type':'uint16'},
	# 		{'name':'pbb_uca', 'type':'uint8'},
	# 		{'name':'tunnel_ipv4_src', 'type':'uint32'},
	# 		{'name':'tunnel_ipv4_dst', 'type':'uint32'},
	# 	]},
	# 	{'name':'masks', 'fields':[
	# 		{'name':'in_port', 'type':'uint32'},
	# 		{'name':'in_phy_port', 'type':'uint32'},
	# 		{'name':'metadata', 'type':'uint64'},
	# 		{'name':'eth_dst', 'type':'uint48'},
	# 		{'name':'eth_src', 'type':'uint48'},
	# 		{'name':'eth_type', 'type':'uint16'},
	# 		{'name':'vlan_vid', 'type':'uint16'},
	# 		{'name':'vlan_pcp', 'type':'uint8'},
	# 		{'name':'ip_dscp', 'type':'uint8'},
	# 		{'name':'ip_ecn', 'type':'uint8'},
	# 		{'name':'ip_proto', 'type':'uint8'},
	# 		{'name':'ipv4_src', 'type':'uint32'},
	# 		{'name':'ipv4_dst', 'type':'uint32'},
	# 		{'name':'tcp_src', 'type':'uint16'},
	# 		{'name':'tcp_dst', 'type':'uint16'},
	# 		{'name':'udp_src', 'type':'uint16'},
	# 		{'name':'udp_dst', 'type':'uint16'},
	# 		{'name':'sctp_src', 'type':'uint16'},
	# 		{'name':'sctp_dst', 'type':'uint16'},
	# 		{'name':'icmpv4_type', 'type':'uint8'},
	# 		{'name':'icmpv4_code', 'type':'uint8'},
	# 		{'name':'arp_op', 'type':'uint16'},
	# 		{'name':'arp_spa', 'type':'uint32'},
	# 		{'name':'arp_tpa', 'type':'uint32'},
	# 		{'name':'arp_sha', 'type':'uint48'},
	# 		{'name':'arp_tha', 'type':'uint48'},
	# 		{'name':'ipv6_src', 'impl':False, 'type':'uint128'},
	# 		{'name':'ipv6_dst', 'impl':False, 'type':'uint128'},
	# 		{'name':'ipv6_flabel', 'type':'uint32'},
	# 		{'name':'icmpv6_type', 'type':'uint8'},
	# 		{'name':'icmpv6_code', 'type':'uint8'},
	# 		{'name':'ipv6_nd_target', 'impl':False, 'type':'uint128'},
	# 		{'name':'ipv6_nd_sll', 'type':'uint48'},
	# 		{'name':'ipv6_nd_tll', 'type':'uint48'},
	# 		{'name':'mpls_label', 'type':'uint32'},
	# 		{'name':'mpls_tc', 'type':'uint8'},
	# 		{'name':'mpls_bos', 'type':'uint8'},
	# 		{'name':'tunnel_id', 'type':'uint64'},
	# 		{'name':'ipv6_exthdr', 'type':'uint16'},
	# 		{'name':'pbb_uca', 'type':'uint8'},
	# 		{'name':'tunnel_ipv4_src', 'type':'uint32'},
	# 		{'name':'tunnel_ipv4_dst', 'type':'uint32'},
	# 	]},
	# ]},
	# {'name':'instructions', 'fields':[
	# 	##TODO: This Handling is bad
	# 	{'name':'element', 'type':'TLV', 'fields':[
	# 		{'name':'table_id', 'type':'uint48'},
	# 	]},
	# ]},
	# {'name':'actions', 'fields':[
	# 	##TODO: This Handling is bad
	# 	{'name':'element', 'type':'TLV', 'fields':[
	# 		{'name':'port', 'type':'port'}, #uint32
	# 		{'name':'max_len', 'type':'uint16'},
	# 	]},
	# ]},
]

fields_of_flow_delete = [
	{'name':'version', 'type':'uint8'},
	{'name':'type', 'type':'uint8'},
	{'name':'length', 'type':'uint16'},
	{'name':'xid', 'type':'uint32'},
	{'name':'cookie', 'type':'uint64'},
	{'name':'cookie_mask', 'type':'uint64'},
	{'name':'table_id', 'type':'uint8'},
	{'name':'idle_timeout', 'type':'uint16'},
	{'name':'hard_timeout', 'type':'uint16'},
	{'name':'priority', 'type':'uint16'},
	{'name':'buffer_id', 'type':'uint32'},
	{'name':'out_port', 'type':'uint32'},
	{'name':'out_group', 'type':'uint32'},
	{'name':'flags', 'type':'uint16'},
	{'name':'match', 'fields': [
		{'name':'match','fields':[
			{'name':'oxm_list','type':'list','fields':[
				{'name':'in_port', 'type':'port'}, #0
				{'name':'in_phy_port', 'type':'port'}, #1
				{'name':'metadata', 'type':'uint64'}, #2
				{'name':'eth_dst', 'type':'uint48'}, #3
				{'name':'eth_src', 'type':'uint48'}, #4
				{'name':'eth_type', 'type':'uint16'}, #5
				{'name':'vlan_vid', 'type':'uint16','range':'[[0x0,0x0],[0x1000,0x1fff]]'}, #6
				{'name':'vlan_pcp', 'type':'uint8','range':'[[0x0,0x7]]'}, #7
				{'name':'ip_dscp', 'type':'uint8','range':'[[0x0,0x3f]]'}, #8
				{'name':'ip_ecn', 'type':'uint8','range':'[[0x0,0x3]]'}, #9
				{'name':'ip_proto', 'type':'uint8'}, #10
				{'name':'ipv4_src', 'type':'uint32'}, #11
				{'name':'ipv4_dst', 'type':'uint32'}, #12
				{'name':'tcp_src', 'type':'uint16'}, #13
				{'name':'tcp_dst', 'type':'uint16'}, #14
				{'name':'udp_src', 'type':'uint16'}, #15
				{'name':'udp_dst', 'type':'uint16'}, #16
				{'name':'sctp_src', 'type':'uint16'}, #17
				{'name':'sctp_dst', 'type':'uint16'}, #18
				{'name':'icmpv4_type', 'type':'uint8'}, #19
				{'name':'icmpv4_code', 'type':'uint8'}, #20
				{'name':'arp_op', 'type':'uint16'}, #21
				{'name':'arp_spa', 'type':'uint32'}, #22
				{'name':'arp_tpa', 'type':'uint32'}, #23
				{'name':'arp_sha', 'type':'uint48'}, #24
				{'name':'arp_tha', 'type':'uint48'}, #25
				{'name':'ipv6_src', 'type':'uint128'}, #26
				{'name':'ipv6_dst', 'type':'uint128'}, #27
				{'name':'ipv6_flabel', 'type':'uint32'}, #28
				{'name':'icmpv6_type', 'type':'uint8'}, #29
				{'name':'icmpv6_code', 'type':'uint8'}, #30
				{'name':'ipv6_nd_target', 'type':'uint128'}, #31
				{'name':'ipv6_nd_sll', 'type':'uint48'}, #32
				{'name':'ipv6_nd_tll', 'type':'uint48'}, #33
				{'name':'mpls_label', 'type':'uint32'},	#34
				{'name':'mpls_tc', 'type':'uint8'},	#35
				{'name':'mpls_bos', 'type':'uint8'}, #36
				{'name':'pbb_isid', 'impl':False, 'type':'uint64'}, #37
				{'name':'tunnel_id', 'type':'uint64'},	#38
				{'name':'ipv6_exthdr', 'type':'uint16'}, #39
			]}
		]},
	]},
	{'name':'instructions','type':'list','fields':[
		{'name':'goto_table','fields':[
			{'name':'table_id', 'type':'uint8'},
		]}, #1
		{'name':'write_metadata','fields':[
			{'name':'metadata', 'type':'uint64'},
			{'name':'metadata_mask', 'type':'uint64'},
		]}, #2
		{'name':'write_actions','fields':[
			{'name':'actions','type':'list','fields':[
				{'name':'output','fields':[
					{'name':'port', 'type':'port'},
					{'name':'max_len', 'type':'uint16'}
				]}, #0
				{'name':'copy_ttl_out','type':''}, #11
				{'name':'copy_ttl_in','type':''}, #12
				{'name':'set_mpls_ttl','fields':[
					{'name':'mpls_ttl', 'type':'uint8'},
				]}, #15
				{'name':'dec_mpls_ttl','type':''}, #16
				{'name':'push_vlan','fields':[
					{'name':'ethertype', 'type':'uint16'},
				]}, #17
				{'name':'pop_vlan','type':''}, #18
				{'name':'push_mpls','fields':[
					{'name':'ethertype', 'type':'uint16'},
				]}, #19
				{'name':'pop_mpls','fields':[
					{'name':'ethertype', 'type':'uint16'},
				]}, #20
				{'name':'set_queue','fields':[
					{'name':'queue_id', 'type':'uint32'},
				]}, #21
				{'name':'group','fields':[
					{'name':'group_id', 'type':'uint32','range':'[[0x0,0xffffff00],[0xfffffffc,0xfffffffc],[0xffffffff,0xffffffff]]'},
				]}, #22
				{'name':'set_nw_ttl','fields':[
					{'name':'nw_ttl', 'type':'uint8'},
				]}, #23
				{'name':'dec_nw_ttl','type':''}, #24
				{'name':'set_field','impl':False}, #25 field is too difficulty to implement
				{'name':'push_pbb','fields':[
					{'name':'ethertype', 'type':'uint16'},
				]}, #26
				{'name':'pop_pbb','type':''}, #27
				{'name':'experimenter','impl':False}, #ffff experimenter is also difficulty to implement
			]},
		]}, #3
		{'name':'apply_actions','fields':[
			{'name':'actions','type':'list','fields':[
				{'name':'output','fields':[
					{'name':'port', 'type':'port'},
					{'name':'max_len', 'type':'uint16'}
				]}, #0
				{'name':'copy_ttl_out','type':''}, #11
				{'name':'copy_ttl_in','type':''}, #12
				{'name':'set_mpls_ttl','fields':[
					{'name':'mpls_ttl', 'type':'uint8'},
				]}, #15
				{'name':'dec_mpls_ttl','type':''}, #16
				{'name':'push_vlan','fields':[
					{'name':'ethertype', 'type':'uint16'},
				]}, #17
				{'name':'pop_vlan','type':''}, #18
				{'name':'push_mpls','fields':[
					{'name':'ethertype', 'type':'uint16'},
				]}, #19
				{'name':'pop_mpls','fields':[
					{'name':'ethertype', 'type':'uint16'},
				]}, #20
				{'name':'set_queue','fields':[
					{'name':'queue_id', 'type':'uint32'},
				]}, #21
				{'name':'group','fields':[
					{'name':'group_id', 'type':'uint32','range':'[[0x0,0xffffff00],[0xfffffffc,0xfffffffc],[0xffffffff,0xffffffff]]'},
				]}, #22
				{'name':'set_nw_ttl','fields':[
					{'name':'nw_ttl', 'type':'uint8'},
				]}, #23
				{'name':'dec_nw_ttl','type':''}, #24
				{'name':'set_field','impl':False}, #25 field is too difficulty to implement
				{'name':'push_pbb','fields':[
					{'name':'ethertype', 'type':'uint16'},
				]}, #26
				{'name':'pop_pbb','type':''}, #27
				{'name':'experimenter','impl':False}, #ffff experimenter is also difficulty to implement
			]},
		]}, #4
		{'name':'clear_actions','type':''}, #5
		{'name':'meter','fields':[
			{'name':'meter_id', 'type':'uint32','range':'[[0x0,0xffff0000],[0xfffffffd,0xffffffff]]'},
		]}, #6
		{'name':'experimenter','impl':False,}, #ffff
	]}

	# {'name':'importance', 'type':'uint16'},
	# {'name':'match', 'fields': [
	# 	{'name':'version', 'type':'uint8'},
	# 	{'name':'fields', 'fields':[
	# 		{'name':'in_port', 'type':'port'}, #uint32
	# 		{'name':'in_phy_port', 'type':'port'}, #uint32
	# 		{'name':'metadata', 'type':'uint64'},
	# 		{'name':'eth_dst', 'type':'uint48'},
	# 		{'name':'eth_src', 'type':'uint48'},
	# 		{'name':'eth_type', 'type':'uint16'},
	# 		{'name':'vlan_vid', 'type':'uint16'},
	# 		{'name':'vlan_pcp', 'type':'uint8'},
	# 		{'name':'ip_dscp', 'type':'uint8'},
	# 		{'name':'ip_ecn', 'type':'uint8'},
	# 		{'name':'ip_proto', 'type':'uint8'},
	# 		{'name':'ipv4_src', 'type':'uint32'},
	# 		{'name':'ipv4_dst', 'type':'uint32'},
	# 		{'name':'tcp_src', 'type':'uint16'},
	# 		{'name':'tcp_dst', 'type':'uint16'},
	# 		{'name':'udp_src', 'type':'uint16'},
	# 		{'name':'udp_dst', 'type':'uint16'},
	# 		{'name':'sctp_src', 'type':'uint16'},
	# 		{'name':'sctp_dst', 'type':'uint16'},
	# 		{'name':'icmpv4_type', 'type':'uint8'},
	# 		{'name':'icmpv4_code', 'type':'uint8'},
	# 		{'name':'arp_op', 'type':'uint16'},
	# 		{'name':'arp_spa', 'type':'uint32'},
	# 		{'name':'arp_tpa', 'type':'uint32'},
	# 		{'name':'arp_sha', 'type':'uint48'},
	# 		{'name':'arp_tha', 'type':'uint48'},
	# 		{'name':'ipv6_src', 'impl':False, 'type':'uint128'},
	# 		{'name':'ipv6_dst', 'impl':False, 'type':'uint128'},
	# 		{'name':'ipv6_flabel', 'type':'uint32'},
	# 		{'name':'icmpv6_type', 'type':'uint8'},
	# 		{'name':'icmpv6_code', 'type':'uint8'},
	# 		{'name':'ipv6_nd_target', 'impl':False, 'type':'uint128'},
	# 		{'name':'ipv6_nd_sll', 'type':'uint48'},
	# 		{'name':'ipv6_nd_tll', 'type':'uint48'},
	# 		{'name':'mpls_label', 'type':'uint32'},
	# 		{'name':'mpls_tc', 'type':'uint8'},
	# 		{'name':'mpls_bos', 'type':'uint8'},
	# 		{'name':'tunnel_id', 'type':'uint64'},
	# 		{'name':'ipv6_exthdr', 'type':'uint16'},
	# 		{'name':'pbb_uca', 'type':'uint8'},
	# 		{'name':'tunnel_ipv4_src', 'type':'uint32'},
	# 		{'name':'tunnel_ipv4_dst', 'type':'uint32'},
	# 	]},
	# 	{'name':'masks', 'fields':[
	# 		{'name':'in_port', 'type':'uint32'},
	# 		{'name':'in_phy_port', 'type':'uint32'},
	# 		{'name':'metadata', 'type':'uint64'},
	# 		{'name':'eth_dst', 'type':'uint48'},
	# 		{'name':'eth_src', 'type':'uint48'},
	# 		{'name':'eth_type', 'type':'uint16'},
	# 		{'name':'vlan_vid', 'type':'uint16'},
	# 		{'name':'vlan_pcp', 'type':'uint8'},
	# 		{'name':'ip_dscp', 'type':'uint8'},
	# 		{'name':'ip_ecn', 'type':'uint8'},
	# 		{'name':'ip_proto', 'type':'uint8'},
	# 		{'name':'ipv4_src', 'type':'uint32'},
	# 		{'name':'ipv4_dst', 'type':'uint32'},
	# 		{'name':'tcp_src', 'type':'uint16'},
	# 		{'name':'tcp_dst', 'type':'uint16'},
	# 		{'name':'udp_src', 'type':'uint16'},
	# 		{'name':'udp_dst', 'type':'uint16'},
	# 		{'name':'sctp_src', 'type':'uint16'},
	# 		{'name':'sctp_dst', 'type':'uint16'},
	# 		{'name':'icmpv4_type', 'type':'uint8'},
	# 		{'name':'icmpv4_code', 'type':'uint8'},
	# 		{'name':'arp_op', 'type':'uint16'},
	# 		{'name':'arp_spa', 'type':'uint32'},
	# 		{'name':'arp_tpa', 'type':'uint32'},
	# 		{'name':'arp_sha', 'type':'uint48'},
	# 		{'name':'arp_tha', 'type':'uint48'},
	# 		{'name':'ipv6_src', 'impl':False, 'type':'uint128'},
	# 		{'name':'ipv6_dst', 'impl':False, 'type':'uint128'},
	# 		{'name':'ipv6_flabel', 'type':'uint32'},
	# 		{'name':'icmpv6_type', 'type':'uint8'},
	# 		{'name':'icmpv6_code', 'type':'uint8'},
	# 		{'name':'ipv6_nd_target', 'impl':False, 'type':'uint128'},
	# 		{'name':'ipv6_nd_sll', 'type':'uint48'},
	# 		{'name':'ipv6_nd_tll', 'type':'uint48'},
	# 		{'name':'mpls_label', 'type':'uint32'},
	# 		{'name':'mpls_tc', 'type':'uint8'},
	# 		{'name':'mpls_bos', 'type':'uint8'},
	# 		{'name':'tunnel_id', 'type':'uint64'},
	# 		{'name':'ipv6_exthdr', 'type':'uint16'},
	# 		{'name':'pbb_uca', 'type':'uint8'},
	# 		{'name':'tunnel_ipv4_src', 'type':'uint32'},
	# 		{'name':'tunnel_ipv4_dst', 'type':'uint32'},
	# 	]},
	# ]},
	# {'name':'instructions', 'fields':[
	# 	##TODO: This Handling is bad
	# 	{'name':'element', 'type':'TLV', 'fields':[
	# 		{'name':'table_id', 'type':'uint48'},
	# 	]},
	# ]},
	# {'name':'actions', 'fields':[
	# 	##TODO: This Handling is bad
	# 	{'name':'element', 'type':'TLV', 'fields':[
	# 		{'name':'port', 'type':'port'}, #uint32
	# 		{'name':'max_len', 'type':'uint16'},
	# 	]},
	# ]},
]

fields_of_flow_delete_strict = [
	{'name':'version', 'type':'uint8'},
	{'name':'type', 'type':'uint8'},
	{'name':'length', 'type':'uint16'},
	{'name':'xid', 'type':'uint32'},
	{'name':'cookie', 'type':'uint64'},
	{'name':'cookie_mask', 'type':'uint64'},
	{'name':'table_id', 'type':'uint8'},
	{'name':'idle_timeout', 'type':'uint16'},
	{'name':'hard_timeout', 'type':'uint16'},
	{'name':'priority', 'type':'uint16'},
	{'name':'buffer_id', 'type':'uint32'},
	{'name':'out_port', 'type':'uint32'},
	{'name':'out_group', 'type':'uint32'},
	{'name':'flags', 'type':'uint16'},
	{'name':'match', 'fields': [
		{'name':'match','fields':[
			{'name':'oxm_list','type':'list','fields':[
				{'name':'in_port', 'type':'port'}, #0
				{'name':'in_phy_port', 'type':'port'}, #1
				{'name':'metadata', 'type':'uint64'}, #2
				{'name':'eth_dst', 'type':'uint48'}, #3
				{'name':'eth_src', 'type':'uint48'}, #4
				{'name':'eth_type', 'type':'uint16'}, #5
				{'name':'vlan_vid', 'type':'uint16','range':'[[0x0,0x0],[0x1000,0x1fff]]'}, #6
				{'name':'vlan_pcp', 'type':'uint8','range':'[[0x0,0x7]]'}, #7
				{'name':'ip_dscp', 'type':'uint8','range':'[[0x0,0x3f]]'}, #8
				{'name':'ip_ecn', 'type':'uint8','range':'[[0x0,0x3]]'}, #9
				{'name':'ip_proto', 'type':'uint8'}, #10
				{'name':'ipv4_src', 'type':'uint32'}, #11
				{'name':'ipv4_dst', 'type':'uint32'}, #12
				{'name':'tcp_src', 'type':'uint16'}, #13
				{'name':'tcp_dst', 'type':'uint16'}, #14
				{'name':'udp_src', 'type':'uint16'}, #15
				{'name':'udp_dst', 'type':'uint16'}, #16
				{'name':'sctp_src', 'type':'uint16'}, #17
				{'name':'sctp_dst', 'type':'uint16'}, #18
				{'name':'icmpv4_type', 'type':'uint8'}, #19
				{'name':'icmpv4_code', 'type':'uint8'}, #20
				{'name':'arp_op', 'type':'uint16'}, #21
				{'name':'arp_spa', 'type':'uint32'}, #22
				{'name':'arp_tpa', 'type':'uint32'}, #23
				{'name':'arp_sha', 'type':'uint48'}, #24
				{'name':'arp_tha', 'type':'uint48'}, #25
				{'name':'ipv6_src', 'type':'uint128'}, #26
				{'name':'ipv6_dst', 'type':'uint128'}, #27
				{'name':'ipv6_flabel', 'type':'uint32'}, #28
				{'name':'icmpv6_type', 'type':'uint8'}, #29
				{'name':'icmpv6_code', 'type':'uint8'}, #30
				{'name':'ipv6_nd_target', 'type':'uint128'}, #31
				{'name':'ipv6_nd_sll', 'type':'uint48'}, #32
				{'name':'ipv6_nd_tll', 'type':'uint48'}, #33
				{'name':'mpls_label', 'type':'uint32'},	#34
				{'name':'mpls_tc', 'type':'uint8'},	#35
				{'name':'mpls_bos', 'type':'uint8'}, #36
				{'name':'pbb_isid', 'impl':False, 'type':'uint64'}, #37
				{'name':'tunnel_id', 'type':'uint64'},	#38
				{'name':'ipv6_exthdr', 'type':'uint16'}, #39
			]}
		]},
	]},
	{'name':'instructions','type':'list','fields':[
		{'name':'goto_table','fields':[
			{'name':'table_id', 'type':'uint8'},
		]}, #1
		{'name':'write_metadata','fields':[
			{'name':'metadata', 'type':'uint64'},
			{'name':'metadata_mask', 'type':'uint64'},
		]}, #2
		{'name':'write_actions','fields':[
			{'name':'actions','type':'list','fields':[
				{'name':'output','fields':[
					{'name':'port', 'type':'port'},
					{'name':'max_len', 'type':'uint16'}
				]}, #0
				{'name':'copy_ttl_out','type':''}, #11
				{'name':'copy_ttl_in','type':''}, #12
				{'name':'set_mpls_ttl','fields':[
					{'name':'mpls_ttl', 'type':'uint8'},
				]}, #15
				{'name':'dec_mpls_ttl','type':''}, #16
				{'name':'push_vlan','fields':[
					{'name':'ethertype', 'type':'uint16'},
				]}, #17
				{'name':'pop_vlan','type':''}, #18
				{'name':'push_mpls','fields':[
					{'name':'ethertype', 'type':'uint16'},
				]}, #19
				{'name':'pop_mpls','fields':[
					{'name':'ethertype', 'type':'uint16'},
				]}, #20
				{'name':'set_queue','fields':[
					{'name':'queue_id', 'type':'uint32'},
				]}, #21
				{'name':'group','fields':[
					{'name':'group_id', 'type':'uint32','range':'[[0x0,0xffffff00],[0xfffffffc,0xfffffffc],[0xffffffff,0xffffffff]]'},
				]}, #22
				{'name':'set_nw_ttl','fields':[
					{'name':'nw_ttl', 'type':'uint8'},
				]}, #23
				{'name':'dec_nw_ttl','type':''}, #24
				{'name':'set_field','impl':False}, #25 field is too difficulty to implement
				{'name':'push_pbb','fields':[
					{'name':'ethertype', 'type':'uint16'},
				]}, #26
				{'name':'pop_pbb','type':''}, #27
				{'name':'experimenter','impl':False}, #ffff experimenter is also difficulty to implement
			]},
		]}, #3
		{'name':'apply_actions','fields':[
			{'name':'actions','type':'list','fields':[
				{'name':'output','fields':[
					{'name':'port', 'type':'port'},
					{'name':'max_len', 'type':'uint16'}
				]}, #0
				{'name':'copy_ttl_out','type':''}, #11
				{'name':'copy_ttl_in','type':''}, #12
				{'name':'set_mpls_ttl','fields':[
					{'name':'mpls_ttl', 'type':'uint8'},
				]}, #15
				{'name':'dec_mpls_ttl','type':''}, #16
				{'name':'push_vlan','fields':[
					{'name':'ethertype', 'type':'uint16'},
				]}, #17
				{'name':'pop_vlan','type':''}, #18
				{'name':'push_mpls','fields':[
					{'name':'ethertype', 'type':'uint16'},
				]}, #19
				{'name':'pop_mpls','fields':[
					{'name':'ethertype', 'type':'uint16'},
				]}, #20
				{'name':'set_queue','fields':[
					{'name':'queue_id', 'type':'uint32'},
				]}, #21
				{'name':'group','fields':[
					{'name':'group_id', 'type':'uint32','range':'[[0x0,0xffffff00],[0xfffffffc,0xfffffffc],[0xffffffff,0xffffffff]]'},
				]}, #22
				{'name':'set_nw_ttl','fields':[
					{'name':'nw_ttl', 'type':'uint8'},
				]}, #23
				{'name':'dec_nw_ttl','type':''}, #24
				{'name':'set_field','impl':False}, #25 field is too difficulty to implement
				{'name':'push_pbb','fields':[
					{'name':'ethertype', 'type':'uint16'},
				]}, #26
				{'name':'pop_pbb','type':''}, #27
				{'name':'experimenter','impl':False}, #ffff experimenter is also difficulty to implement
			]},
		]}, #4
		{'name':'clear_actions','type':''}, #5
		{'name':'meter','fields':[
			{'name':'meter_id', 'type':'uint32','range':'[[0x0,0xffff0000],[0xfffffffd,0xffffffff]]'},
		]}, #6
		{'name':'experimenter','impl':False,}, #ffff
	]}
	
	# {'name':'importance', 'type':'uint16'},
	# {'name':'match', 'fields': [
	# 	{'name':'version', 'type':'uint8'},
	# 	{'name':'fields', 'fields':[
	# 		{'name':'in_port', 'type':'port'}, #uint32
	# 		{'name':'in_phy_port', 'type':'port'}, #uint32
	# 		{'name':'metadata', 'type':'uint64'},
	# 		{'name':'eth_dst', 'type':'uint48'},
	# 		{'name':'eth_src', 'type':'uint48'},
	# 		{'name':'eth_type', 'type':'uint16'},
	# 		{'name':'vlan_vid', 'type':'uint16'},
	# 		{'name':'vlan_pcp', 'type':'uint8'},
	# 		{'name':'ip_dscp', 'type':'uint8'},
	# 		{'name':'ip_ecn', 'type':'uint8'},
	# 		{'name':'ip_proto', 'type':'uint8'},
	# 		{'name':'ipv4_src', 'type':'uint32'},
	# 		{'name':'ipv4_dst', 'type':'uint32'},
	# 		{'name':'tcp_src', 'type':'uint16'},
	# 		{'name':'tcp_dst', 'type':'uint16'},
	# 		{'name':'udp_src', 'type':'uint16'},
	# 		{'name':'udp_dst', 'type':'uint16'},
	# 		{'name':'sctp_src', 'type':'uint16'},
	# 		{'name':'sctp_dst', 'type':'uint16'},
	# 		{'name':'icmpv4_type', 'type':'uint8'},
	# 		{'name':'icmpv4_code', 'type':'uint8'},
	# 		{'name':'arp_op', 'type':'uint16'},
	# 		{'name':'arp_spa', 'type':'uint32'},
	# 		{'name':'arp_tpa', 'type':'uint32'},
	# 		{'name':'arp_sha', 'type':'uint48'},
	# 		{'name':'arp_tha', 'type':'uint48'},
	# 		{'name':'ipv6_src', 'impl':False, 'type':'uint128'},
	# 		{'name':'ipv6_dst', 'impl':False, 'type':'uint128'},
	# 		{'name':'ipv6_flabel', 'type':'uint32'},
	# 		{'name':'icmpv6_type', 'type':'uint8'},
	# 		{'name':'icmpv6_code', 'type':'uint8'},
	# 		{'name':'ipv6_nd_target', 'impl':False, 'type':'uint128'},
	# 		{'name':'ipv6_nd_sll', 'type':'uint48'},
	# 		{'name':'ipv6_nd_tll', 'type':'uint48'},
	# 		{'name':'mpls_label', 'type':'uint32'},
	# 		{'name':'mpls_tc', 'type':'uint8'},
	# 		{'name':'mpls_bos', 'type':'uint8'},
	# 		{'name':'tunnel_id', 'type':'uint64'},
	# 		{'name':'ipv6_exthdr', 'type':'uint16'},
	# 		{'name':'pbb_uca', 'type':'uint8'},
	# 		{'name':'tunnel_ipv4_src', 'type':'uint32'},
	# 		{'name':'tunnel_ipv4_dst', 'type':'uint32'},
	# 	]},
	# 	{'name':'masks', 'fields':[
	# 		{'name':'in_port', 'type':'uint32'},
	# 		{'name':'in_phy_port', 'type':'uint32'},
	# 		{'name':'metadata', 'type':'uint64'},
	# 		{'name':'eth_dst', 'type':'uint48'},
	# 		{'name':'eth_src', 'type':'uint48'},
	# 		{'name':'eth_type', 'type':'uint16'},
	# 		{'name':'vlan_vid', 'type':'uint16'},
	# 		{'name':'vlan_pcp', 'type':'uint8'},
	# 		{'name':'ip_dscp', 'type':'uint8'},
	# 		{'name':'ip_ecn', 'type':'uint8'},
	# 		{'name':'ip_proto', 'type':'uint8'},
	# 		{'name':'ipv4_src', 'type':'uint32'},
	# 		{'name':'ipv4_dst', 'type':'uint32'},
	# 		{'name':'tcp_src', 'type':'uint16'},
	# 		{'name':'tcp_dst', 'type':'uint16'},
	# 		{'name':'udp_src', 'type':'uint16'},
	# 		{'name':'udp_dst', 'type':'uint16'},
	# 		{'name':'sctp_src', 'type':'uint16'},
	# 		{'name':'sctp_dst', 'type':'uint16'},
	# 		{'name':'icmpv4_type', 'type':'uint8'},
	# 		{'name':'icmpv4_code', 'type':'uint8'},
	# 		{'name':'arp_op', 'type':'uint16'},
	# 		{'name':'arp_spa', 'type':'uint32'},
	# 		{'name':'arp_tpa', 'type':'uint32'},
	# 		{'name':'arp_sha', 'type':'uint48'},
	# 		{'name':'arp_tha', 'type':'uint48'},
	# 		{'name':'ipv6_src', 'impl':False, 'type':'uint128'},
	# 		{'name':'ipv6_dst', 'impl':False, 'type':'uint128'},
	# 		{'name':'ipv6_flabel', 'type':'uint32'},
	# 		{'name':'icmpv6_type', 'type':'uint8'},
	# 		{'name':'icmpv6_code', 'type':'uint8'},
	# 		{'name':'ipv6_nd_target', 'impl':False, 'type':'uint128'},
	# 		{'name':'ipv6_nd_sll', 'type':'uint48'},
	# 		{'name':'ipv6_nd_tll', 'type':'uint48'},
	# 		{'name':'mpls_label', 'type':'uint32'},
	# 		{'name':'mpls_tc', 'type':'uint8'},
	# 		{'name':'mpls_bos', 'type':'uint8'},
	# 		{'name':'tunnel_id', 'type':'uint64'},
	# 		{'name':'ipv6_exthdr', 'type':'uint16'},
	# 		{'name':'pbb_uca', 'type':'uint8'},
	# 		{'name':'tunnel_ipv4_src', 'type':'uint32'},
	# 		{'name':'tunnel_ipv4_dst', 'type':'uint32'},
	# 	]},
	# ]},
	# {'name':'instructions', 'fields':[
	# 	##TODO: This Handling is bad
	# 	{'name':'element', 'type':'TLV', 'fields':[
	# 		{'name':'table_id', 'type':'uint48'},
	# 	]},
	# ]},
	# {'name':'actions', 'fields':[
	# 	##TODO: This Handling is bad
	# 	{'name':'element', 'type':'TLV', 'fields':[
	# 		{'name':'port', 'type':'port'}, #uint32
	# 		{'name':'max_len', 'type':'uint16'},
	# 	]},
	# ]},
]

fields_of_flow_modify = [
	{'name':'version', 'type':'uint8'},
	{'name':'type', 'type':'uint8'},
	{'name':'length', 'type':'uint16'},
	{'name':'xid', 'type':'uint32'},
	{'name':'cookie', 'type':'uint64'},
	{'name':'cookie_mask', 'type':'uint64'},
	{'name':'table_id', 'type':'uint8'},
	{'name':'idle_timeout', 'type':'uint16'},
	{'name':'hard_timeout', 'type':'uint16'},
	{'name':'priority', 'type':'uint16'},
	{'name':'buffer_id', 'type':'uint32'},
	{'name':'out_port', 'type':'uint32'},
	{'name':'out_group', 'type':'uint32'},
	{'name':'flags', 'type':'uint16'},
	{'name':'match', 'fields': [
		{'name':'match','fields':[
			{'name':'oxm_list','type':'list','fields':[
				{'name':'in_port', 'type':'port'}, #0
				{'name':'in_phy_port', 'type':'port'}, #1
				{'name':'metadata', 'type':'uint64'}, #2
				{'name':'eth_dst', 'type':'uint48'}, #3
				{'name':'eth_src', 'type':'uint48'}, #4
				{'name':'eth_type', 'type':'uint16'}, #5
				{'name':'vlan_vid', 'type':'uint16','range':'[[0x0,0x0],[0x1000,0x1fff]]'}, #6
				{'name':'vlan_pcp', 'type':'uint8','range':'[[0x0,0x7]]'}, #7
				{'name':'ip_dscp', 'type':'uint8','range':'[[0x0,0x3f]]'}, #8
				{'name':'ip_ecn', 'type':'uint8','range':'[[0x0,0x3]]'}, #9
				{'name':'ip_proto', 'type':'uint8'}, #10
				{'name':'ipv4_src', 'type':'uint32'}, #11
				{'name':'ipv4_dst', 'type':'uint32'}, #12
				{'name':'tcp_src', 'type':'uint16'}, #13
				{'name':'tcp_dst', 'type':'uint16'}, #14
				{'name':'udp_src', 'type':'uint16'}, #15
				{'name':'udp_dst', 'type':'uint16'}, #16
				{'name':'sctp_src', 'type':'uint16'}, #17
				{'name':'sctp_dst', 'type':'uint16'}, #18
				{'name':'icmpv4_type', 'type':'uint8'}, #19
				{'name':'icmpv4_code', 'type':'uint8'}, #20
				{'name':'arp_op', 'type':'uint16'}, #21
				{'name':'arp_spa', 'type':'uint32'}, #22
				{'name':'arp_tpa', 'type':'uint32'}, #23
				{'name':'arp_sha', 'type':'uint48'}, #24
				{'name':'arp_tha', 'type':'uint48'}, #25
				{'name':'ipv6_src', 'type':'uint128'}, #26
				{'name':'ipv6_dst', 'type':'uint128'}, #27
				{'name':'ipv6_flabel', 'type':'uint32'}, #28
				{'name':'icmpv6_type', 'type':'uint8'}, #29
				{'name':'icmpv6_code', 'type':'uint8'}, #30
				{'name':'ipv6_nd_target', 'type':'uint128'}, #31
				{'name':'ipv6_nd_sll', 'type':'uint48'}, #32
				{'name':'ipv6_nd_tll', 'type':'uint48'}, #33
				{'name':'mpls_label', 'type':'uint32'},	#34
				{'name':'mpls_tc', 'type':'uint8'},	#35
				{'name':'mpls_bos', 'type':'uint8'}, #36
				{'name':'pbb_isid', 'impl':False, 'type':'uint64'}, #37
				{'name':'tunnel_id', 'type':'uint64'},	#38
				{'name':'ipv6_exthdr', 'type':'uint16'}, #39
			]}
		]},
	]},
	{'name':'instructions','type':'list','fields':[
		{'name':'goto_table','fields':[
			{'name':'table_id', 'type':'uint8'},
		]}, #1
		{'name':'write_metadata','fields':[
			{'name':'metadata', 'type':'uint64'},
			{'name':'metadata_mask', 'type':'uint64'},
		]}, #2
		{'name':'write_actions','fields':[
			{'name':'actions','type':'list','fields':[
				{'name':'output','fields':[
					{'name':'port', 'type':'port'},
					{'name':'max_len', 'type':'uint16'}
				]}, #0
				{'name':'copy_ttl_out','type':''}, #11
				{'name':'copy_ttl_in','type':''}, #12
				{'name':'set_mpls_ttl','fields':[
					{'name':'mpls_ttl', 'type':'uint8'},
				]}, #15
				{'name':'dec_mpls_ttl','type':''}, #16
				{'name':'push_vlan','fields':[
					{'name':'ethertype', 'type':'uint16'},
				]}, #17
				{'name':'pop_vlan','type':''}, #18
				{'name':'push_mpls','fields':[
					{'name':'ethertype', 'type':'uint16'},
				]}, #19
				{'name':'pop_mpls','fields':[
					{'name':'ethertype', 'type':'uint16'},
				]}, #20
				{'name':'set_queue','fields':[
					{'name':'queue_id', 'type':'uint32'},
				]}, #21
				{'name':'group','fields':[
					{'name':'group_id', 'type':'uint32','range':'[[0x0,0xffffff00],[0xfffffffc,0xfffffffc],[0xffffffff,0xffffffff]]'},
				]}, #22
				{'name':'set_nw_ttl','fields':[
					{'name':'nw_ttl', 'type':'uint8'},
				]}, #23
				{'name':'dec_nw_ttl','type':''}, #24
				{'name':'set_field','impl':False}, #25 field is too difficulty to implement
				{'name':'push_pbb','fields':[
					{'name':'ethertype', 'type':'uint16'},
				]}, #26
				{'name':'pop_pbb','type':''}, #27
				{'name':'experimenter','impl':False}, #ffff experimenter is also difficulty to implement
			]},
		]}, #3
		{'name':'apply_actions','fields':[
			{'name':'actions','type':'list','fields':[
				{'name':'output','fields':[
					{'name':'port', 'type':'port'},
					{'name':'max_len', 'type':'uint16'}
				]}, #0
				{'name':'copy_ttl_out','type':''}, #11
				{'name':'copy_ttl_in','type':''}, #12
				{'name':'set_mpls_ttl','fields':[
					{'name':'mpls_ttl', 'type':'uint8'},
				]}, #15
				{'name':'dec_mpls_ttl','type':''}, #16
				{'name':'push_vlan','fields':[
					{'name':'ethertype', 'type':'uint16'},
				]}, #17
				{'name':'pop_vlan','type':''}, #18
				{'name':'push_mpls','fields':[
					{'name':'ethertype', 'type':'uint16'},
				]}, #19
				{'name':'pop_mpls','fields':[
					{'name':'ethertype', 'type':'uint16'},
				]}, #20
				{'name':'set_queue','fields':[
					{'name':'queue_id', 'type':'uint32'},
				]}, #21
				{'name':'group','fields':[
					{'name':'group_id', 'type':'uint32','range':'[[0x0,0xffffff00],[0xfffffffc,0xfffffffc],[0xffffffff,0xffffffff]]'},
				]}, #22
				{'name':'set_nw_ttl','fields':[
					{'name':'nw_ttl', 'type':'uint8'},
				]}, #23
				{'name':'dec_nw_ttl','type':''}, #24
				{'name':'set_field','impl':False}, #25 field is too difficulty to implement
				{'name':'push_pbb','fields':[
					{'name':'ethertype', 'type':'uint16'},
				]}, #26
				{'name':'pop_pbb','type':''}, #27
				{'name':'experimenter','impl':False}, #ffff experimenter is also difficulty to implement
			]},
		]}, #4
		{'name':'clear_actions','type':''}, #5
		{'name':'meter','fields':[
			{'name':'meter_id', 'type':'uint32','range':'[[0x0,0xffff0000],[0xfffffffd,0xffffffff]]'},
		]}, #6
		{'name':'experimenter','impl':False,}, #ffff
	]}

	# {'name':'importance', 'type':'uint16'},

	# {'name':'match', 'fields': [
	# 	{'name':'version', 'type':'uint8'},
	# 	{'name':'fields', 'fields':[
	# 		{'name':'in_port', 'type':'port'}, #uint32
	# 		{'name':'in_phy_port', 'type':'port'}, #uint32
	# 		{'name':'metadata', 'type':'uint64'},
	# 		{'name':'eth_dst', 'type':'uint48'},
	# 		{'name':'eth_src', 'type':'uint48'},
	# 		{'name':'eth_type', 'type':'uint16'},
	# 		{'name':'vlan_vid', 'type':'uint16'},
	# 		{'name':'vlan_pcp', 'type':'uint8'},
	# 		{'name':'ip_dscp', 'type':'uint8'},
	# 		{'name':'ip_ecn', 'type':'uint8'},
	# 		{'name':'ip_proto', 'type':'uint8'},
	# 		{'name':'ipv4_src', 'type':'uint32'},
	# 		{'name':'ipv4_dst', 'type':'uint32'},
	# 		{'name':'tcp_src', 'type':'uint16'},
	# 		{'name':'tcp_dst', 'type':'uint16'},
	# 		{'name':'udp_src', 'type':'uint16'},
	# 		{'name':'udp_dst', 'type':'uint16'},
	# 		{'name':'sctp_src', 'type':'uint16'},
	# 		{'name':'sctp_dst', 'type':'uint16'},
	# 		{'name':'icmpv4_type', 'type':'uint8'},
	# 		{'name':'icmpv4_code', 'type':'uint8'},
	# 		{'name':'arp_op', 'type':'uint16'},
	# 		{'name':'arp_spa', 'type':'uint32'},
	# 		{'name':'arp_tpa', 'type':'uint32'},
	# 		{'name':'arp_sha', 'type':'uint48'},
	# 		{'name':'arp_tha', 'type':'uint48'},
	# 		{'name':'ipv6_src', 'impl':False, 'type':'uint128'},
	# 		{'name':'ipv6_dst', 'impl':False, 'type':'uint128'},
	# 		{'name':'ipv6_flabel', 'type':'uint32'},
	# 		{'name':'icmpv6_type', 'type':'uint8'},
	# 		{'name':'icmpv6_code', 'type':'uint8'},
	# 		{'name':'ipv6_nd_target', 'impl':False, 'type':'uint128'},
	# 		{'name':'ipv6_nd_sll', 'type':'uint48'},
	# 		{'name':'ipv6_nd_tll', 'type':'uint48'},
	# 		{'name':'mpls_label', 'type':'uint32'},
	# 		{'name':'mpls_tc', 'type':'uint8'},
	# 		{'name':'mpls_bos', 'type':'uint8'},
	# 		{'name':'tunnel_id', 'type':'uint64'},
	# 		{'name':'ipv6_exthdr', 'type':'uint16'},
	# 		{'name':'pbb_uca', 'type':'uint8'},
	# 		{'name':'tunnel_ipv4_src', 'type':'uint32'},
	# 		{'name':'tunnel_ipv4_dst', 'type':'uint32'},
	# 	]},
	# 	{'name':'masks', 'fields':[
	# 		{'name':'in_port', 'type':'uint32'},
	# 		{'name':'in_phy_port', 'type':'uint32'},
	# 		{'name':'metadata', 'type':'uint64'},
	# 		{'name':'eth_dst', 'type':'uint48'},
	# 		{'name':'eth_src', 'type':'uint48'},
	# 		{'name':'eth_type', 'type':'uint16'},
	# 		{'name':'vlan_vid', 'type':'uint16'},
	# 		{'name':'vlan_pcp', 'type':'uint8'},
	# 		{'name':'ip_dscp', 'type':'uint8'},
	# 		{'name':'ip_ecn', 'type':'uint8'},
	# 		{'name':'ip_proto', 'type':'uint8'},
	# 		{'name':'ipv4_src', 'type':'uint32'},
	# 		{'name':'ipv4_dst', 'type':'uint32'},
	# 		{'name':'tcp_src', 'type':'uint16'},
	# 		{'name':'tcp_dst', 'type':'uint16'},
	# 		{'name':'udp_src', 'type':'uint16'},
	# 		{'name':'udp_dst', 'type':'uint16'},
	# 		{'name':'sctp_src', 'type':'uint16'},
	# 		{'name':'sctp_dst', 'type':'uint16'},
	# 		{'name':'icmpv4_type', 'type':'uint8'},
	# 		{'name':'icmpv4_code', 'type':'uint8'},
	# 		{'name':'arp_op', 'type':'uint16'},
	# 		{'name':'arp_spa', 'type':'uint32'},
	# 		{'name':'arp_tpa', 'type':'uint32'},
	# 		{'name':'arp_sha', 'type':'uint48'},
	# 		{'name':'arp_tha', 'type':'uint48'},
	# 		{'name':'ipv6_src', 'impl':False, 'type':'uint128'},
	# 		{'name':'ipv6_dst', 'impl':False, 'type':'uint128'},
	# 		{'name':'ipv6_flabel', 'type':'uint32'},
	# 		{'name':'icmpv6_type', 'type':'uint8'},
	# 		{'name':'icmpv6_code', 'type':'uint8'},
	# 		{'name':'ipv6_nd_target', 'impl':False, 'type':'uint128'},
	# 		{'name':'ipv6_nd_sll', 'type':'uint48'},
	# 		{'name':'ipv6_nd_tll', 'type':'uint48'},
	# 		{'name':'mpls_label', 'type':'uint32'},
	# 		{'name':'mpls_tc', 'type':'uint8'},
	# 		{'name':'mpls_bos', 'type':'uint8'},
	# 		{'name':'tunnel_id', 'type':'uint64'},
	# 		{'name':'ipv6_exthdr', 'type':'uint16'},
	# 		{'name':'pbb_uca', 'type':'uint8'},
	# 		{'name':'tunnel_ipv4_src', 'type':'uint32'},
	# 		{'name':'tunnel_ipv4_dst', 'type':'uint32'},
	# 	]},
	# ]},
	# {'name':'instructions', 'fields':[
	# 	##TODO: This Handling is bad
	# 	{'name':'element', 'type':'TLV', 'fields':[
	# 		{'name':'table_id', 'type':'uint48'},
	# 	]},
	# ]},
	# {'name':'actions', 'fields':[
	# 	##TODO: This Handling is bad
	# 	{'name':'element', 'type':'TLV', 'fields':[
	# 		{'name':'port', 'type':'port'}, #uint32
	# 		{'name':'max_len', 'type':'uint16'},
	# 	]},
	# ]},
]

fields_of_flow_modify_strict = [
	{'name':'version', 'type':'uint8'},
	{'name':'type', 'type':'uint8'},
	{'name':'length', 'type':'uint16'},
	{'name':'xid', 'type':'uint32'},
	{'name':'cookie', 'type':'uint64'},
	{'name':'cookie_mask', 'type':'uint64'},
	{'name':'table_id', 'type':'uint8'},
	{'name':'idle_timeout', 'type':'uint16'},
	{'name':'hard_timeout', 'type':'uint16'},
	{'name':'priority', 'type':'uint16'},
	{'name':'buffer_id', 'type':'uint32'},
	{'name':'out_port', 'type':'uint32'},
	{'name':'out_group', 'type':'uint32'},
	{'name':'flags', 'type':'uint16'},
		{'name':'match', 'fields': [
		{'name':'match','fields':[
			{'name':'oxm_list','type':'list','fields':[
				{'name':'in_port', 'type':'port'}, #0
				{'name':'in_phy_port', 'type':'port'}, #1
				{'name':'metadata', 'type':'uint64'}, #2
				{'name':'eth_dst', 'type':'uint48'}, #3
				{'name':'eth_src', 'type':'uint48'}, #4
				{'name':'eth_type', 'type':'uint16'}, #5
				{'name':'vlan_vid', 'type':'uint16','range':'[[0x0,0x0],[0x1000,0x1fff]]'}, #6
				{'name':'vlan_pcp', 'type':'uint8','range':'[[0x0,0x7]]'}, #7
				{'name':'ip_dscp', 'type':'uint8','range':'[[0x0,0x3f]]'}, #8
				{'name':'ip_ecn', 'type':'uint8','range':'[[0x0,0x3]]'}, #9
				{'name':'ip_proto', 'type':'uint8'}, #10
				{'name':'ipv4_src', 'type':'uint32'}, #11
				{'name':'ipv4_dst', 'type':'uint32'}, #12
				{'name':'tcp_src', 'type':'uint16'}, #13
				{'name':'tcp_dst', 'type':'uint16'}, #14
				{'name':'udp_src', 'type':'uint16'}, #15
				{'name':'udp_dst', 'type':'uint16'}, #16
				{'name':'sctp_src', 'type':'uint16'}, #17
				{'name':'sctp_dst', 'type':'uint16'}, #18
				{'name':'icmpv4_type', 'type':'uint8'}, #19
				{'name':'icmpv4_code', 'type':'uint8'}, #20
				{'name':'arp_op', 'type':'uint16'}, #21
				{'name':'arp_spa', 'type':'uint32'}, #22
				{'name':'arp_tpa', 'type':'uint32'}, #23
				{'name':'arp_sha', 'type':'uint48'}, #24
				{'name':'arp_tha', 'type':'uint48'}, #25
				{'name':'ipv6_src', 'type':'uint128'}, #26
				{'name':'ipv6_dst', 'type':'uint128'}, #27
				{'name':'ipv6_flabel', 'type':'uint32'}, #28
				{'name':'icmpv6_type', 'type':'uint8'}, #29
				{'name':'icmpv6_code', 'type':'uint8'}, #30
				{'name':'ipv6_nd_target', 'type':'uint128'}, #31
				{'name':'ipv6_nd_sll', 'type':'uint48'}, #32
				{'name':'ipv6_nd_tll', 'type':'uint48'}, #33
				{'name':'mpls_label', 'type':'uint32'},	#34
				{'name':'mpls_tc', 'type':'uint8'},	#35
				{'name':'mpls_bos', 'type':'uint8'}, #36
				{'name':'pbb_isid', 'impl':False, 'type':'uint64'}, #37
				{'name':'tunnel_id', 'type':'uint64'},	#38
				{'name':'ipv6_exthdr', 'type':'uint16'}, #39
			]}
		]},
	]},
	{'name':'instructions','type':'list','fields':[
		{'name':'goto_table','fields':[
			{'name':'table_id', 'type':'uint8'},
		]}, #1
		{'name':'write_metadata','fields':[
			{'name':'metadata', 'type':'uint64'},
			{'name':'metadata_mask', 'type':'uint64'},
		]}, #2
		{'name':'write_actions','fields':[
			{'name':'actions','type':'list','fields':[
				{'name':'output','fields':[
					{'name':'port', 'type':'port'},
					{'name':'max_len', 'type':'uint16'}
				]}, #0
				{'name':'copy_ttl_out','type':''}, #11
				{'name':'copy_ttl_in','type':''}, #12
				{'name':'set_mpls_ttl','fields':[
					{'name':'mpls_ttl', 'type':'uint8'},
				]}, #15
				{'name':'dec_mpls_ttl','type':''}, #16
				{'name':'push_vlan','fields':[
					{'name':'ethertype', 'type':'uint16'},
				]}, #17
				{'name':'pop_vlan','type':''}, #18
				{'name':'push_mpls','fields':[
					{'name':'ethertype', 'type':'uint16'},
				]}, #19
				{'name':'pop_mpls','fields':[
					{'name':'ethertype', 'type':'uint16'},
				]}, #20
				{'name':'set_queue','fields':[
					{'name':'queue_id', 'type':'uint32'},
				]}, #21
				{'name':'group','fields':[
					{'name':'group_id', 'type':'uint32','range':'[[0x0,0xffffff00],[0xfffffffc,0xfffffffc],[0xffffffff,0xffffffff]]'},
				]}, #22
				{'name':'set_nw_ttl','fields':[
					{'name':'nw_ttl', 'type':'uint8'},
				]}, #23
				{'name':'dec_nw_ttl','type':''}, #24
				{'name':'set_field','impl':False}, #25 field is too difficulty to implement
				{'name':'push_pbb','fields':[
					{'name':'ethertype', 'type':'uint16'},
				]}, #26
				{'name':'pop_pbb','type':''}, #27
				{'name':'experimenter','impl':False}, #ffff experimenter is also difficulty to implement
			]},
		]}, #3
		{'name':'apply_actions','fields':[
			{'name':'actions','type':'list','fields':[
				{'name':'output','fields':[
					{'name':'port', 'type':'port'},
					{'name':'max_len', 'type':'uint16'}
				]}, #0
				{'name':'copy_ttl_out','type':''}, #11
				{'name':'copy_ttl_in','type':''}, #12
				{'name':'set_mpls_ttl','fields':[
					{'name':'mpls_ttl', 'type':'uint8'},
				]}, #15
				{'name':'dec_mpls_ttl','type':''}, #16
				{'name':'push_vlan','fields':[
					{'name':'ethertype', 'type':'uint16'},
				]}, #17
				{'name':'pop_vlan','type':''}, #18
				{'name':'push_mpls','fields':[
					{'name':'ethertype', 'type':'uint16'},
				]}, #19
				{'name':'pop_mpls','fields':[
					{'name':'ethertype', 'type':'uint16'},
				]}, #20
				{'name':'set_queue','fields':[
					{'name':'queue_id', 'type':'uint32'},
				]}, #21
				{'name':'group','fields':[
					{'name':'group_id', 'type':'uint32','range':'[[0x0,0xffffff00],[0xfffffffc,0xfffffffc],[0xffffffff,0xffffffff]]'},
				]}, #22
				{'name':'set_nw_ttl','fields':[
					{'name':'nw_ttl', 'type':'uint8'},
				]}, #23
				{'name':'dec_nw_ttl','type':''}, #24
				{'name':'set_field','impl':False}, #25 field is too difficulty to implement
				{'name':'push_pbb','fields':[
					{'name':'ethertype', 'type':'uint16'},
				]}, #26
				{'name':'pop_pbb','type':''}, #27
				{'name':'experimenter','impl':False}, #ffff experimenter is also difficulty to implement
			]},
		]}, #4
		{'name':'clear_actions','type':''}, #5
		{'name':'meter','fields':[
			{'name':'meter_id', 'type':'uint32','range':'[[0x0,0xffff0000],[0xfffffffd,0xffffffff]]'},
		]}, #6
		{'name':'experimenter','impl':False,}, #ffff
	]}
	# {'name':'importance', 'type':'uint16'},
	# {'name':'match', 'fields': [
	# 	{'name':'version', 'type':'uint8'},
	# 	{'name':'fields', 'fields':[
	# 		{'name':'in_port', 'type':'port'}, #uint32
	# 		{'name':'in_phy_port', 'type':'port'}, #uint32
	# 		{'name':'metadata', 'type':'uint64'},
	# 		{'name':'eth_dst', 'type':'uint48'},
	# 		{'name':'eth_src', 'type':'uint48'},
	# 		{'name':'eth_type', 'type':'uint16'},
	# 		{'name':'vlan_vid', 'type':'uint16'},
	# 		{'name':'vlan_pcp', 'type':'uint8'},
	# 		{'name':'ip_dscp', 'type':'uint8'},
	# 		{'name':'ip_ecn', 'type':'uint8'},
	# 		{'name':'ip_proto', 'type':'uint8'},
	# 		{'name':'ipv4_src', 'type':'uint32'},
	# 		{'name':'ipv4_dst', 'type':'uint32'},
	# 		{'name':'tcp_src', 'type':'uint16'},
	# 		{'name':'tcp_dst', 'type':'uint16'},
	# 		{'name':'udp_src', 'type':'uint16'},
	# 		{'name':'udp_dst', 'type':'uint16'},
	# 		{'name':'sctp_src', 'type':'uint16'},
	# 		{'name':'sctp_dst', 'type':'uint16'},
	# 		{'name':'icmpv4_type', 'type':'uint8'},
	# 		{'name':'icmpv4_code', 'type':'uint8'},
	# 		{'name':'arp_op', 'type':'uint16'},
	# 		{'name':'arp_spa', 'type':'uint32'},
	# 		{'name':'arp_tpa', 'type':'uint32'},
	# 		{'name':'arp_sha', 'type':'uint48'},
	# 		{'name':'arp_tha', 'type':'uint48'},
	# 		{'name':'ipv6_src', 'impl':False, 'type':'uint128'},
	# 		{'name':'ipv6_dst', 'impl':False, 'type':'uint128'},
	# 		{'name':'ipv6_flabel', 'type':'uint32'},
	# 		{'name':'icmpv6_type', 'type':'uint8'},
	# 		{'name':'icmpv6_code', 'type':'uint8'},
	# 		{'name':'ipv6_nd_target', 'impl':False, 'type':'uint128'},
	# 		{'name':'ipv6_nd_sll', 'type':'uint48'},
	# 		{'name':'ipv6_nd_tll', 'type':'uint48'},
	# 		{'name':'mpls_label', 'type':'uint32'},
	# 		{'name':'mpls_tc', 'type':'uint8'},
	# 		{'name':'mpls_bos', 'type':'uint8'},
	# 		{'name':'tunnel_id', 'type':'uint64'},
	# 		{'name':'ipv6_exthdr', 'type':'uint16'},
	# 		{'name':'pbb_uca', 'type':'uint8'},
	# 		{'name':'tunnel_ipv4_src', 'type':'uint32'},
	# 		{'name':'tunnel_ipv4_dst', 'type':'uint32'},
	# 	]},
	# 	{'name':'masks', 'fields':[
	# 		{'name':'in_port', 'type':'uint32'},
	# 		{'name':'in_phy_port', 'type':'uint32'},
	# 		{'name':'metadata', 'type':'uint64'},
	# 		{'name':'eth_dst', 'type':'uint48'},
	# 		{'name':'eth_src', 'type':'uint48'},
	# 		{'name':'eth_type', 'type':'uint16'},
	# 		{'name':'vlan_vid', 'type':'uint16'},
	# 		{'name':'vlan_pcp', 'type':'uint8'},
	# 		{'name':'ip_dscp', 'type':'uint8'},
	# 		{'name':'ip_ecn', 'type':'uint8'},
	# 		{'name':'ip_proto', 'type':'uint8'},
	# 		{'name':'ipv4_src', 'type':'uint32'},
	# 		{'name':'ipv4_dst', 'type':'uint32'},
	# 		{'name':'tcp_src', 'type':'uint16'},
	# 		{'name':'tcp_dst', 'type':'uint16'},
	# 		{'name':'udp_src', 'type':'uint16'},
	# 		{'name':'udp_dst', 'type':'uint16'},
	# 		{'name':'sctp_src', 'type':'uint16'},
	# 		{'name':'sctp_dst', 'type':'uint16'},
	# 		{'name':'icmpv4_type', 'type':'uint8'},
	# 		{'name':'icmpv4_code', 'type':'uint8'},
	# 		{'name':'arp_op', 'type':'uint16'},
	# 		{'name':'arp_spa', 'type':'uint32'},
	# 		{'name':'arp_tpa', 'type':'uint32'},
	# 		{'name':'arp_sha', 'type':'uint48'},
	# 		{'name':'arp_tha', 'type':'uint48'},
	# 		{'name':'ipv6_src', 'impl':False, 'type':'uint128'},
	# 		{'name':'ipv6_dst', 'impl':False, 'type':'uint128'},
	# 		{'name':'ipv6_flabel', 'type':'uint32'},
	# 		{'name':'icmpv6_type', 'type':'uint8'},
	# 		{'name':'icmpv6_code', 'type':'uint8'},
	# 		{'name':'ipv6_nd_target', 'impl':False, 'type':'uint128'},
	# 		{'name':'ipv6_nd_sll', 'type':'uint48'},
	# 		{'name':'ipv6_nd_tll', 'type':'uint48'},
	# 		{'name':'mpls_label', 'type':'uint32'},
	# 		{'name':'mpls_tc', 'type':'uint8'},
	# 		{'name':'mpls_bos', 'type':'uint8'},
	# 		{'name':'tunnel_id', 'type':'uint64'},
	# 		{'name':'ipv6_exthdr', 'type':'uint16'},
	# 		{'name':'pbb_uca', 'type':'uint8'},
	# 		{'name':'tunnel_ipv4_src', 'type':'uint32'},
	# 		{'name':'tunnel_ipv4_dst', 'type':'uint32'},
	# 	]},
	# ]},
	# {'name':'instructions', 'fields':[
	# 	##TODO: This Handling is bad
	# 	{'name':'element', 'type':'TLV', 'fields':[
	# 		{'name':'table_id', 'type':'uint48'},
	# 	]},
	# ]},
	# {'name':'actions', 'fields':[
	# 	##TODO: This Handling is bad
	# 	{'name':'element', 'type':'TLV', 'fields':[
	# 		{'name':'port', 'type':'port'}, #uint32
	# 		{'name':'max_len', 'type':'uint16'},
	# 	]},
	# ]},
]

fields_of_flow_mod_failed_error_msg = [
	{'name':'version', 'type':'uint8'},
	{'name':'type', 'type':'uint8'},
	{'name':'length', 'type':'uint16'},
	{'name':'xid', 'type':'uint32'},
	{'name':'code', 'type':'uint16'},
	{'name':'data', 'impl':False},
]

fields_of_flow_monitor_failed_error_msg = [
	{'name':'version', 'type':'uint8'},
	{'name':'type', 'type':'uint8'},
	{'name':'length', 'type':'uint16'},
	{'name':'xid', 'type':'uint32'},
	{'name':'code', 'type':'uint16'},
	{'name':'data', 'impl':False},
]

fields_of_flow_removed = [
	{'name':'version', 'type':'uint8'},
	{'name':'type', 'type':'uint8'},
	{'name':'length', 'type':'uint16'},
	{'name':'xid', 'type':'uint32'},
	{'name':'cookie', 'type':'uint64'},
	{'name':'priority', 'type':'uint16'},
	{'name':'reason', 'type':'uint8','range':'[[0x0,0x3]]'},
	{'name':'table_id', 'type':'uint8'},
	{'name':'duration_sec', 'type':'uint32'},
	{'name':'duration_nsec', 'type':'uint32'},
	{'name':'idle_timeout', 'type':'uint16'},
	{'name':'hard_timeout', 'type':'uint16'},
	{'name':'packet_count', 'type':'uint64'},
	{'name':'byte_count', 'type':'uint64'},
	{'name':'match', 'fields': [
		{'name':'match','fields':[
			{'name':'oxm_list','type':'list','fields':[
				{'name':'in_port', 'type':'port'}, #0
				{'name':'in_phy_port', 'type':'port'}, #1
				{'name':'metadata', 'type':'uint64'}, #2
				{'name':'eth_dst', 'type':'uint48'}, #3
				{'name':'eth_src', 'type':'uint48'}, #4
				{'name':'eth_type', 'type':'uint16'}, #5
				{'name':'vlan_vid', 'type':'uint16','range':'[[0x0,0x0],[0x1000,0x1fff]]'}, #6
				{'name':'vlan_pcp', 'type':'uint8','range':'[[0x0,0x7]]'}, #7
				{'name':'ip_dscp', 'type':'uint8','range':'[[0x0,0x3f]]'}, #8
				{'name':'ip_ecn', 'type':'uint8','range':'[[0x0,0x3]]'}, #9
				{'name':'ip_proto', 'type':'uint8'}, #10
				{'name':'ipv4_src', 'type':'uint32'}, #11
				{'name':'ipv4_dst', 'type':'uint32'}, #12
				{'name':'tcp_src', 'type':'uint16'}, #13
				{'name':'tcp_dst', 'type':'uint16'}, #14
				{'name':'udp_src', 'type':'uint16'}, #15
				{'name':'udp_dst', 'type':'uint16'}, #16
				{'name':'sctp_src', 'type':'uint16'}, #17
				{'name':'sctp_dst', 'type':'uint16'}, #18
				{'name':'icmpv4_type', 'type':'uint8'}, #19
				{'name':'icmpv4_code', 'type':'uint8'}, #20
				{'name':'arp_op', 'type':'uint16'}, #21
				{'name':'arp_spa', 'type':'uint32'}, #22
				{'name':'arp_tpa', 'type':'uint32'}, #23
				{'name':'arp_sha', 'type':'uint48'}, #24
				{'name':'arp_tha', 'type':'uint48'}, #25
				{'name':'ipv6_src', 'type':'uint128'}, #26
				{'name':'ipv6_dst', 'type':'uint128'}, #27
				{'name':'ipv6_flabel', 'type':'uint32'}, #28
				{'name':'icmpv6_type', 'type':'uint8'}, #29
				{'name':'icmpv6_code', 'type':'uint8'}, #30
				{'name':'ipv6_nd_target', 'type':'uint128'}, #31
				{'name':'ipv6_nd_sll', 'type':'uint48'}, #32
				{'name':'ipv6_nd_tll', 'type':'uint48'}, #33
				{'name':'mpls_label', 'type':'uint32'},	#34
				{'name':'mpls_tc', 'type':'uint8'},	#35
				{'name':'mpls_bos', 'type':'uint8'}, #36
				{'name':'pbb_isid', 'impl':False, 'type':'uint64'}, #37
				{'name':'tunnel_id', 'type':'uint64'},	#38
				{'name':'ipv6_exthdr', 'type':'uint16'}, #39
			]}
		]},
	]},
	# {'name':'match', 'fields': [
	# 	{'name':'version', 'type':'uint8'},
	# 	{'name':'fields', 'fields':[
	# 		{'name':'in_port', 'type':'port'}, #uint32
	# 		{'name':'in_phy_port', 'type':'port'}, #uint32
	# 		{'name':'metadata', 'type':'uint64'},
	# 		{'name':'eth_dst', 'type':'uint48'},
	# 		{'name':'eth_src', 'type':'uint48'},
	# 		{'name':'eth_type', 'type':'uint16'},
	# 		{'name':'vlan_vid', 'type':'uint16'},
	# 		{'name':'vlan_pcp', 'type':'uint8'},
	# 		{'name':'ip_dscp', 'type':'uint8'},
	# 		{'name':'ip_ecn', 'type':'uint8'},
	# 		{'name':'ip_proto', 'type':'uint8'},
	# 		{'name':'ipv4_src', 'type':'uint32'},
	# 		{'name':'ipv4_dst', 'type':'uint32'},
	# 		{'name':'tcp_src', 'type':'uint16'},
	# 		{'name':'tcp_dst', 'type':'uint16'},
	# 		{'name':'udp_src', 'type':'uint16'},
	# 		{'name':'udp_dst', 'type':'uint16'},
	# 		{'name':'sctp_src', 'type':'uint16'},
	# 		{'name':'sctp_dst', 'type':'uint16'},
	# 		{'name':'icmpv4_type', 'type':'uint8'},
	# 		{'name':'icmpv4_code', 'type':'uint8'},
	# 		{'name':'arp_op', 'type':'uint16'},
	# 		{'name':'arp_spa', 'type':'uint32'},
	# 		{'name':'arp_tpa', 'type':'uint32'},
	# 		{'name':'arp_sha', 'type':'uint48'},
	# 		{'name':'arp_tha', 'type':'uint48'},
	# 		{'name':'ipv6_src', 'impl':False, 'type':'uint128'},
	# 		{'name':'ipv6_dst', 'impl':False, 'type':'uint128'},
	# 		{'name':'ipv6_flabel', 'type':'uint32'},
	# 		{'name':'icmpv6_type', 'type':'uint8'},
	# 		{'name':'icmpv6_code', 'type':'uint8'},
	# 		{'name':'ipv6_nd_target', 'impl':False, 'type':'uint128'},
	# 		{'name':'ipv6_nd_sll', 'type':'uint48'},
	# 		{'name':'ipv6_nd_tll', 'type':'uint48'},
	# 		{'name':'mpls_label', 'type':'uint32'},
	# 		{'name':'mpls_tc', 'type':'uint8'},
	# 		{'name':'mpls_bos', 'type':'uint8'},
	# 		{'name':'tunnel_id', 'type':'uint64'},
	# 		{'name':'ipv6_exthdr', 'type':'uint16'},
	# 		{'name':'pbb_uca', 'type':'uint8'},
	# 		{'name':'tunnel_ipv4_src', 'type':'uint32'},
	# 		{'name':'tunnel_ipv4_dst', 'type':'uint32'},
	# 	]},
	# 	{'name':'masks', 'fields':[
	# 		{'name':'in_port', 'type':'uint32'},
	# 		{'name':'in_phy_port', 'type':'uint32'},
	# 		{'name':'metadata', 'type':'uint64'},
	# 		{'name':'eth_dst', 'type':'uint48'},
	# 		{'name':'eth_src', 'type':'uint48'},
	# 		{'name':'eth_type', 'type':'uint16'},
	# 		{'name':'vlan_vid', 'type':'uint16'},
	# 		{'name':'vlan_pcp', 'type':'uint8'},
	# 		{'name':'ip_dscp', 'type':'uint8'},
	# 		{'name':'ip_ecn', 'type':'uint8'},
	# 		{'name':'ip_proto', 'type':'uint8'},
	# 		{'name':'ipv4_src', 'type':'uint32'},
	# 		{'name':'ipv4_dst', 'type':'uint32'},
	# 		{'name':'tcp_src', 'type':'uint16'},
	# 		{'name':'tcp_dst', 'type':'uint16'},
	# 		{'name':'udp_src', 'type':'uint16'},
	# 		{'name':'udp_dst', 'type':'uint16'},
	# 		{'name':'sctp_src', 'type':'uint16'},
	# 		{'name':'sctp_dst', 'type':'uint16'},
	# 		{'name':'icmpv4_type', 'type':'uint8'},
	# 		{'name':'icmpv4_code', 'type':'uint8'},
	# 		{'name':'arp_op', 'type':'uint16'},
	# 		{'name':'arp_spa', 'type':'uint32'},
	# 		{'name':'arp_tpa', 'type':'uint32'},
	# 		{'name':'arp_sha', 'type':'uint48'},
	# 		{'name':'arp_tha', 'type':'uint48'},
	# 		{'name':'ipv6_src', 'impl':False, 'type':'uint128'},
	# 		{'name':'ipv6_dst', 'impl':False, 'type':'uint128'},
	# 		{'name':'ipv6_flabel', 'type':'uint32'},
	# 		{'name':'icmpv6_type', 'type':'uint8'},
	# 		{'name':'icmpv6_code', 'type':'uint8'},
	# 		{'name':'ipv6_nd_target', 'impl':False, 'type':'uint128'},
	# 		{'name':'ipv6_nd_sll', 'type':'uint48'},
	# 		{'name':'ipv6_nd_tll', 'type':'uint48'},
	# 		{'name':'mpls_label', 'type':'uint32'},
	# 		{'name':'mpls_tc', 'type':'uint8'},
	# 		{'name':'mpls_bos', 'type':'uint8'},
	# 		{'name':'tunnel_id', 'type':'uint64'},
	# 		{'name':'ipv6_exthdr', 'type':'uint16'},
	# 		{'name':'pbb_uca', 'type':'uint8'},
	# 		{'name':'tunnel_ipv4_src', 'type':'uint32'},
	# 		{'name':'tunnel_ipv4_dst', 'type':'uint32'},
	# 	]},
	# ]},
]

fields_of_flow_stats_reply = [
	{'name':'version', 'type':'uint8'},
	{'name':'type', 'type':'uint8'},
	{'name':'length', 'type':'uint16'},
	{'name':'xid', 'type':'uint32'},
	{'name':'flags', 'type':'uint16'},
	{'name':'entries', 'type':'list','fields':[
		{'name':'flow_stats_entry','fields':[
			{'name':'table_id', 'type':'uint8'},
			{'name':'duration_sec', 'type':'uint32'},
			{'name':'duration_nsec', 'type':'uint32'},
			{'name':'priority', 'type':'uint16'},
			{'name':'idle_timeout', 'type':'uint16'},
			{'name':'hard_timeout', 'type':'uint16'},
			{'name':'flags', 'type':'uint16'},
			{'name':'cookie', 'type':'uint32'},
			{'name':'packet_count', 'type':'uint64'},
			{'name':'byte_count', 'type':'uint64'},
			{'name':'match', 'fields': [
				{'name':'match','fields':[
					{'name':'oxm_list','type':'list','fields':[
						{'name':'in_port', 'type':'port'}, #0
						{'name':'in_phy_port', 'type':'port'}, #1
						{'name':'metadata', 'type':'uint64'}, #2
						{'name':'eth_dst', 'type':'uint48'}, #3
						{'name':'eth_src', 'type':'uint48'}, #4
						{'name':'eth_type', 'type':'uint16'}, #5
						{'name':'vlan_vid', 'type':'uint16','range':'[[0x0,0x0],[0x1000,0x1fff]]'}, #6
						{'name':'vlan_pcp', 'type':'uint8','range':'[[0x0,0x7]]'}, #7
						{'name':'ip_dscp', 'type':'uint8','range':'[[0x0,0x3f]]'}, #8
						{'name':'ip_ecn', 'type':'uint8','range':'[[0x0,0x3]]'}, #9
						{'name':'ip_proto', 'type':'uint8'}, #10
						{'name':'ipv4_src', 'type':'uint32'}, #11
						{'name':'ipv4_dst', 'type':'uint32'}, #12
						{'name':'tcp_src', 'type':'uint16'}, #13
						{'name':'tcp_dst', 'type':'uint16'}, #14
						{'name':'udp_src', 'type':'uint16'}, #15
						{'name':'udp_dst', 'type':'uint16'}, #16
						{'name':'sctp_src', 'type':'uint16'}, #17
						{'name':'sctp_dst', 'type':'uint16'}, #18
						{'name':'icmpv4_type', 'type':'uint8'}, #19
						{'name':'icmpv4_code', 'type':'uint8'}, #20
						{'name':'arp_op', 'type':'uint16'}, #21
						{'name':'arp_spa', 'type':'uint32'}, #22
						{'name':'arp_tpa', 'type':'uint32'}, #23
						{'name':'arp_sha', 'type':'uint48'}, #24
						{'name':'arp_tha', 'type':'uint48'}, #25
						{'name':'ipv6_src', 'type':'uint128'}, #26
						{'name':'ipv6_dst', 'type':'uint128'}, #27
						{'name':'ipv6_flabel', 'type':'uint32'}, #28
						{'name':'icmpv6_type', 'type':'uint8'}, #29
						{'name':'icmpv6_code', 'type':'uint8'}, #30
						{'name':'ipv6_nd_target', 'type':'uint128'}, #31
						{'name':'ipv6_nd_sll', 'type':'uint48'}, #32
						{'name':'ipv6_nd_tll', 'type':'uint48'}, #33
						{'name':'mpls_label', 'type':'uint32'},	#34
						{'name':'mpls_tc', 'type':'uint8'},	#35
						{'name':'mpls_bos', 'type':'uint8'}, #36
						{'name':'pbb_isid', 'impl':False, 'type':'uint64'}, #37
						{'name':'tunnel_id', 'type':'uint64'},	#38
						{'name':'ipv6_exthdr', 'type':'uint16'}, #39
					]}
				]},
			]},
			{'name':'instructions','type':'list','fields':[
				{'name':'goto_table','fields':[
					{'name':'table_id', 'type':'uint8'},
				]}, #1
				{'name':'write_metadata','fields':[
					{'name':'metadata', 'type':'uint64'},
					{'name':'metadata_mask', 'type':'uint64'},
				]}, #2
				{'name':'write_actions','fields':[
					{'name':'actions','type':'list','fields':[
						{'name':'output','fields':[
							{'name':'port', 'type':'port'},
							{'name':'max_len', 'type':'uint16'}
						]}, #0
						{'name':'copy_ttl_out','type':''}, #11
						{'name':'copy_ttl_in','type':''}, #12
						{'name':'set_mpls_ttl','fields':[
							{'name':'mpls_ttl', 'type':'uint8'},
						]}, #15
						{'name':'dec_mpls_ttl','type':''}, #16
						{'name':'push_vlan','fields':[
							{'name':'ethertype', 'type':'uint16'},
						]}, #17
						{'name':'pop_vlan','type':''}, #18
						{'name':'push_mpls','fields':[
							{'name':'ethertype', 'type':'uint16'},
						]}, #19
						{'name':'pop_mpls','fields':[
							{'name':'ethertype', 'type':'uint16'},
						]}, #20
						{'name':'set_queue','fields':[
							{'name':'queue_id', 'type':'uint32'},
						]}, #21
						{'name':'group','fields':[
							{'name':'group_id', 'type':'uint32','range':'[[0x0,0xffffff00],[0xfffffffc,0xfffffffc],[0xffffffff,0xffffffff]]'},
						]}, #22
						{'name':'set_nw_ttl','fields':[
							{'name':'nw_ttl', 'type':'uint8'},
						]}, #23
						{'name':'dec_nw_ttl','type':''}, #24
						{'name':'set_field','impl':False}, #25 field is too difficulty to implement
						{'name':'push_pbb','fields':[
							{'name':'ethertype', 'type':'uint16'},
						]}, #26
						{'name':'pop_pbb','type':''}, #27
						{'name':'experimenter','impl':False}, #ffff experimenter is also difficulty to implement
					]},
				]}, #3
				{'name':'apply_actions','fields':[
					{'name':'actions','type':'list','fields':[
						{'name':'output','fields':[
							{'name':'port', 'type':'port'},
							{'name':'max_len', 'type':'uint16'}
						]}, #0
						{'name':'copy_ttl_out','type':''}, #11
						{'name':'copy_ttl_in','type':''}, #12
						{'name':'set_mpls_ttl','fields':[
							{'name':'mpls_ttl', 'type':'uint8'},
						]}, #15
						{'name':'dec_mpls_ttl','type':''}, #16
						{'name':'push_vlan','fields':[
							{'name':'ethertype', 'type':'uint16'},
						]}, #17
						{'name':'pop_vlan','type':''}, #18
						{'name':'push_mpls','fields':[
							{'name':'ethertype', 'type':'uint16'},
						]}, #19
						{'name':'pop_mpls','fields':[
							{'name':'ethertype', 'type':'uint16'},
						]}, #20
						{'name':'set_queue','fields':[
							{'name':'queue_id', 'type':'uint32'},
						]}, #21
						{'name':'group','fields':[
							{'name':'group_id', 'type':'uint32','range':'[[0x0,0xffffff00],[0xfffffffc,0xfffffffc],[0xffffffff,0xffffffff]]'},
						]}, #22
						{'name':'set_nw_ttl','fields':[
							{'name':'nw_ttl', 'type':'uint8'},
						]}, #23
						{'name':'dec_nw_ttl','type':''}, #24
						{'name':'set_field','impl':False}, #25 field is too difficulty to implement
						{'name':'push_pbb','fields':[
							{'name':'ethertype', 'type':'uint16'},
						]}, #26
						{'name':'pop_pbb','type':''}, #27
						{'name':'experimenter','impl':False}, #ffff experimenter is also difficulty to implement
					]},
				]}, #4
				{'name':'clear_actions','type':''}, #5
				{'name':'meter','fields':[
					{'name':'meter_id', 'type':'uint32','range':'[[0x0,0xffff0000],[0xfffffffd,0xffffffff]]'},
				]}, #6
				{'name':'experimenter','impl':False,}, #ffff
			]}
		]}
	]}
	# {'name':'entries', 'fields':[
	# 	{'name':'element','type':'list', 'fields':[
	# 		{'name':'table_id', 'type':'uint8'},
	# 		{'name':'duration_sec', 'type':'uint64'},
	# 		{'name':'duration_nsec', 'type':'uint64'},
	# 		{'name':'priority', 'type':'uint16'},
	# 		{'name':'idle_timeout', 'type':'uint16'},
	# 		{'name':'hard_timeout', 'type':'uint16'},
	# 		{'name':'flags', 'type':'uint16'},
	# 		{'name':'importance', 'type':'uint16'},
	# 		{'name':'cookie', 'type':'uint32'},
	# 		{'name':'packet_count', 'type':'uint64'},
	# 		{'name':'byte_count', 'type':'uint64'},
	# 		{'name':'match', 'fields': [
	# 			{'name':'version', 'type':'uint8'},
	# 			{'name':'fields', 'fields':[
	# 				{'name':'in_port', 'type':'port'}, #uint32
	# 				{'name':'in_phy_port', 'type':'port'}, #uint32
	# 				{'name':'metadata', 'type':'uint64'},
	# 				{'name':'eth_dst', 'type':'uint48'},
	# 				{'name':'eth_src', 'type':'uint48'},
	# 				{'name':'eth_type', 'type':'uint16'},
	# 				{'name':'vlan_vid', 'type':'uint16'},
	# 				{'name':'vlan_pcp', 'type':'uint8'},
	# 				{'name':'ip_dscp', 'type':'uint8'},
	# 				{'name':'ip_ecn', 'type':'uint8'},
	# 				{'name':'ip_proto', 'type':'uint8'},
	# 				{'name':'ipv4_src', 'type':'uint32'},
	# 				{'name':'ipv4_dst', 'type':'uint32'},
	# 				{'name':'tcp_src', 'type':'uint16'},
	# 				{'name':'tcp_dst', 'type':'uint16'},
	# 				{'name':'udp_src', 'type':'uint16'},
	# 				{'name':'udp_dst', 'type':'uint16'},
	# 				{'name':'sctp_src', 'type':'uint16'},
	# 				{'name':'sctp_dst', 'type':'uint16'},
	# 				{'name':'icmpv4_type', 'type':'uint8'},
	# 				{'name':'icmpv4_code', 'type':'uint8'},
	# 				{'name':'arp_op', 'type':'uint16'},
	# 				{'name':'arp_spa', 'type':'uint32'},
	# 				{'name':'arp_tpa', 'type':'uint32'},
	# 				{'name':'arp_sha', 'type':'uint48'},
	# 				{'name':'arp_tha', 'type':'uint48'},
	# 				{'name':'ipv6_src', 'impl':False, 'type':'uint128'},
	# 				{'name':'ipv6_dst', 'impl':False, 'type':'uint128'},
	# 				{'name':'ipv6_flabel', 'type':'uint32'},
	# 				{'name':'icmpv6_type', 'type':'uint8'},
	# 				{'name':'icmpv6_code', 'type':'uint8'},
	# 				{'name':'ipv6_nd_target', 'impl':False, 'type':'uint128'},
	# 				{'name':'ipv6_nd_sll', 'type':'uint48'},
	# 				{'name':'ipv6_nd_tll', 'type':'uint48'},
	# 				{'name':'mpls_label', 'type':'uint32'},
	# 				{'name':'mpls_tc', 'type':'uint8'},
	# 				{'name':'mpls_bos', 'type':'uint8'},
	# 				{'name':'tunnel_id', 'type':'uint64'},
	# 				{'name':'ipv6_exthdr', 'type':'uint16'},
	# 				{'name':'pbb_uca', 'type':'uint8'},
	# 				{'name':'tunnel_ipv4_src', 'type':'uint32'},
	# 				{'name':'tunnel_ipv4_dst', 'type':'uint32'},
	# 			]},
	# 			{'name':'masks', 'fields':[
	# 				{'name':'in_port', 'type':'uint32'},
	# 				{'name':'in_phy_port', 'type':'uint32'},
	# 				{'name':'metadata', 'type':'uint64'},
	# 				{'name':'eth_dst', 'type':'uint48'},
	# 				{'name':'eth_src', 'type':'uint48'},
	# 				{'name':'eth_type', 'type':'uint16'},
	# 				{'name':'vlan_vid', 'type':'uint16'},
	# 				{'name':'vlan_pcp', 'type':'uint8'},
	# 				{'name':'ip_dscp', 'type':'uint8'},
	# 				{'name':'ip_ecn', 'type':'uint8'},
	# 				{'name':'ip_proto', 'type':'uint8'},
	# 				{'name':'ipv4_src', 'type':'uint32'},
	# 				{'name':'ipv4_dst', 'type':'uint32'},
	# 				{'name':'tcp_src', 'type':'uint16'},
	# 				{'name':'tcp_dst', 'type':'uint16'},
	# 				{'name':'udp_src', 'type':'uint16'},
	# 				{'name':'udp_dst', 'type':'uint16'},
	# 				{'name':'sctp_src', 'type':'uint16'},
	# 				{'name':'sctp_dst', 'type':'uint16'},
	# 				{'name':'icmpv4_type', 'type':'uint8'},
	# 				{'name':'icmpv4_code', 'type':'uint8'},
	# 				{'name':'arp_op', 'type':'uint16'},
	# 				{'name':'arp_spa', 'type':'uint32'},
	# 				{'name':'arp_tpa', 'type':'uint32'},
	# 				{'name':'arp_sha', 'type':'uint48'},
	# 				{'name':'arp_tha', 'type':'uint48'},
	# 				{'name':'ipv6_src', 'impl':False, 'type':'uint128'},
	# 				{'name':'ipv6_dst', 'impl':False, 'type':'uint128'},
	# 				{'name':'ipv6_flabel', 'type':'uint32'},
	# 				{'name':'icmpv6_type', 'type':'uint8'},
	# 				{'name':'icmpv6_code', 'type':'uint8'},
	# 				{'name':'ipv6_nd_target', 'impl':False, 'type':'uint128'},
	# 				{'name':'ipv6_nd_sll', 'type':'uint48'},
	# 				{'name':'ipv6_nd_tll', 'type':'uint48'},
	# 				{'name':'mpls_label', 'type':'uint32'},
	# 				{'name':'mpls_tc', 'type':'uint8'},
	# 				{'name':'mpls_bos', 'type':'uint8'},
	# 				{'name':'tunnel_id', 'type':'uint64'},
	# 				{'name':'ipv6_exthdr', 'type':'uint16'},
	# 				{'name':'pbb_uca', 'type':'uint8'},
	# 				{'name':'tunnel_ipv4_src', 'type':'uint32'},
	# 				{'name':'tunnel_ipv4_dst', 'type':'uint32'},
	# 			]},
	# 		]},
	# 		{'name':'instructions', 'fields':[
	# 			##TODO: This Handling is bad
	# 			{'name':'element', 'type':'TLV', 'fields':[
	# 				{'name':'table_id', 'type':'uint48'},
	# 			]},
	# 		]},
	# 		{'name':'actions', 'fields':[
	# 			##TODO: This Handling is bad
	# 			{'name':'element', 'type':'TLV', 'fields':[
	# 				{'name':'port', 'type':'port'}, #uint32
	# 				{'name':'max_len', 'type':'uint16'},
	# 			]},
	# 		]},
	# 	]},
	# ]},
]

fields_of_flow_stats_request = [
	{'name':'version', 'type':'uint8'},
	{'name':'type', 'type':'uint8'},
	{'name':'length', 'type':'uint16'},
	{'name':'xid', 'type':'uint32'},
	{'name':'flags', 'type':'uint16'},
	{'name':'table_id', 'type':'uint8'},
	{'name':'out_port', 'type':'uint16'},
	{'name':'out_group', 'type':'uint16'},
	{'name':'cookie', 'type':'uint32'},
	{'name':'cookie_mask', 'type':'uint32'},
	{'name':'match', 'fields': [
		{'name':'match','fields':[
			{'name':'oxm_list','type':'list','fields':[
				{'name':'in_port', 'type':'port'}, #0
				{'name':'in_phy_port', 'type':'port'}, #1
				{'name':'metadata', 'type':'uint64'}, #2
				{'name':'eth_dst', 'type':'uint48'}, #3
				{'name':'eth_src', 'type':'uint48'}, #4
				{'name':'eth_type', 'type':'uint16'}, #5
				{'name':'vlan_vid', 'type':'uint16','range':'[[0x0,0x0],[0x1000,0x1fff]]'}, #6
				{'name':'vlan_pcp', 'type':'uint8','range':'[[0x0,0x7]]'}, #7
				{'name':'ip_dscp', 'type':'uint8','range':'[[0x0,0x3f]]'}, #8
				{'name':'ip_ecn', 'type':'uint8','range':'[[0x0,0x3]]'}, #9
				{'name':'ip_proto', 'type':'uint8'}, #10
				{'name':'ipv4_src', 'type':'uint32'}, #11
				{'name':'ipv4_dst', 'type':'uint32'}, #12
				{'name':'tcp_src', 'type':'uint16'}, #13
				{'name':'tcp_dst', 'type':'uint16'}, #14
				{'name':'udp_src', 'type':'uint16'}, #15
				{'name':'udp_dst', 'type':'uint16'}, #16
				{'name':'sctp_src', 'type':'uint16'}, #17
				{'name':'sctp_dst', 'type':'uint16'}, #18
				{'name':'icmpv4_type', 'type':'uint8'}, #19
				{'name':'icmpv4_code', 'type':'uint8'}, #20
				{'name':'arp_op', 'type':'uint16'}, #21
				{'name':'arp_spa', 'type':'uint32'}, #22
				{'name':'arp_tpa', 'type':'uint32'}, #23
				{'name':'arp_sha', 'type':'uint48'}, #24
				{'name':'arp_tha', 'type':'uint48'}, #25
				{'name':'ipv6_src', 'type':'uint128'}, #26
				{'name':'ipv6_dst', 'type':'uint128'}, #27
				{'name':'ipv6_flabel', 'type':'uint32'}, #28
				{'name':'icmpv6_type', 'type':'uint8'}, #29
				{'name':'icmpv6_code', 'type':'uint8'}, #30
				{'name':'ipv6_nd_target', 'type':'uint128'}, #31
				{'name':'ipv6_nd_sll', 'type':'uint48'}, #32
				{'name':'ipv6_nd_tll', 'type':'uint48'}, #33
				{'name':'mpls_label', 'type':'uint32'},	#34
				{'name':'mpls_tc', 'type':'uint8'},	#35
				{'name':'mpls_bos', 'type':'uint8'}, #36
				{'name':'pbb_isid', 'impl':False, 'type':'uint64'}, #37
				{'name':'tunnel_id', 'type':'uint64'},	#38
				{'name':'ipv6_exthdr', 'type':'uint16'}, #39
			]}
		]},
	]},
	# {'name':'match', 'fields': [
	# 	{'name':'version', 'type':'uint8'},
	# 	{'name':'fields', 'fields':[
	# 		{'name':'in_port', 'type':'port'}, #uint32
	# 		{'name':'in_phy_port', 'type':'port'}, #uint32
	# 		{'name':'metadata', 'type':'uint64'},
	# 		{'name':'eth_dst', 'type':'uint48'},
	# 		{'name':'eth_src', 'type':'uint48'},
	# 		{'name':'eth_type', 'type':'uint16'},
	# 		{'name':'vlan_vid', 'type':'uint16'},
	# 		{'name':'vlan_pcp', 'type':'uint8'},
	# 		{'name':'ip_dscp', 'type':'uint8'},
	# 		{'name':'ip_ecn', 'type':'uint8'},
	# 		{'name':'ip_proto', 'type':'uint8'},
	# 		{'name':'ipv4_src', 'type':'uint32'},
	# 		{'name':'ipv4_dst', 'type':'uint32'},
	# 		{'name':'tcp_src', 'type':'uint16'},
	# 		{'name':'tcp_dst', 'type':'uint16'},
	# 		{'name':'udp_src', 'type':'uint16'},
	# 		{'name':'udp_dst', 'type':'uint16'},
	# 		{'name':'sctp_src', 'type':'uint16'},
	# 		{'name':'sctp_dst', 'type':'uint16'},
	# 		{'name':'icmpv4_type', 'type':'uint8'},
	# 		{'name':'icmpv4_code', 'type':'uint8'},
	# 		{'name':'arp_op', 'type':'uint16'},
	# 		{'name':'arp_spa', 'type':'uint32'},
	# 		{'name':'arp_tpa', 'type':'uint32'},
	# 		{'name':'arp_sha', 'type':'uint48'},
	# 		{'name':'arp_tha', 'type':'uint48'},
	# 		{'name':'ipv6_src', 'impl':False, 'type':'uint128'},
	# 		{'name':'ipv6_dst', 'impl':False, 'type':'uint128'},
	# 		{'name':'ipv6_flabel', 'type':'uint32'},
	# 		{'name':'icmpv6_type', 'type':'uint8'},
	# 		{'name':'icmpv6_code', 'type':'uint8'},
	# 		{'name':'ipv6_nd_target', 'impl':False, 'type':'uint128'},
	# 		{'name':'ipv6_nd_sll', 'type':'uint48'},
	# 		{'name':'ipv6_nd_tll', 'type':'uint48'},
	# 		{'name':'mpls_label', 'type':'uint32'},
	# 		{'name':'mpls_tc', 'type':'uint8'},
	# 		{'name':'mpls_bos', 'type':'uint8'},
	# 		{'name':'tunnel_id', 'type':'uint64'},
	# 		{'name':'ipv6_exthdr', 'type':'uint16'},
	# 		{'name':'pbb_uca', 'type':'uint8'},
	# 		{'name':'tunnel_ipv4_src', 'type':'uint32'},
	# 		{'name':'tunnel_ipv4_dst', 'type':'uint32'},
	# 	]},
	# 	{'name':'masks', 'fields':[
	# 		{'name':'in_port', 'type':'uint32'},
	# 		{'name':'in_phy_port', 'type':'uint32'},
	# 		{'name':'metadata', 'type':'uint64'},
	# 		{'name':'eth_dst', 'type':'uint48'},
	# 		{'name':'eth_src', 'type':'uint48'},
	# 		{'name':'eth_type', 'type':'uint16'},
	# 		{'name':'vlan_vid', 'type':'uint16'},
	# 		{'name':'vlan_pcp', 'type':'uint8'},
	# 		{'name':'ip_dscp', 'type':'uint8'},
	# 		{'name':'ip_ecn', 'type':'uint8'},
	# 		{'name':'ip_proto', 'type':'uint8'},
	# 		{'name':'ipv4_src', 'type':'uint32'},
	# 		{'name':'ipv4_dst', 'type':'uint32'},
	# 		{'name':'tcp_src', 'type':'uint16'},
	# 		{'name':'tcp_dst', 'type':'uint16'},
	# 		{'name':'udp_src', 'type':'uint16'},
	# 		{'name':'udp_dst', 'type':'uint16'},
	# 		{'name':'sctp_src', 'type':'uint16'},
	# 		{'name':'sctp_dst', 'type':'uint16'},
	# 		{'name':'icmpv4_type', 'type':'uint8'},
	# 		{'name':'icmpv4_code', 'type':'uint8'},
	# 		{'name':'arp_op', 'type':'uint16'},
	# 		{'name':'arp_spa', 'type':'uint32'},
	# 		{'name':'arp_tpa', 'type':'uint32'},
	# 		{'name':'arp_sha', 'type':'uint48'},
	# 		{'name':'arp_tha', 'type':'uint48'},
	# 		{'name':'ipv6_src', 'impl':False, 'type':'uint128'},
	# 		{'name':'ipv6_dst', 'impl':False, 'type':'uint128'},
	# 		{'name':'ipv6_flabel', 'type':'uint32'},
	# 		{'name':'icmpv6_type', 'type':'uint8'},
	# 		{'name':'icmpv6_code', 'type':'uint8'},
	# 		{'name':'ipv6_nd_target', 'impl':False, 'type':'uint128'},
	# 		{'name':'ipv6_nd_sll', 'type':'uint48'},
	# 		{'name':'ipv6_nd_tll', 'type':'uint48'},
	# 		{'name':'mpls_label', 'type':'uint32'},
	# 		{'name':'mpls_tc', 'type':'uint8'},
	# 		{'name':'mpls_bos', 'type':'uint8'},
	# 		{'name':'tunnel_id', 'type':'uint64'},
	# 		{'name':'ipv6_exthdr', 'type':'uint16'},
	# 		{'name':'pbb_uca', 'type':'uint8'},
	# 		{'name':'tunnel_ipv4_src', 'type':'uint32'},
	# 		{'name':'tunnel_ipv4_dst', 'type':'uint32'},
	# 	]},
	# ]},
]

fields_of_get_config_reply = [
	{'name':'version', 'type':'uint8'},
	{'name':'type', 'type':'uint8'},
	{'name':'length', 'type':'uint16'},
	{'name':'xid', 'type':'uint32'},
	{'name':'flags', 'type':'uint16'},
	{'name':'miss_send_len', 'type':'uint16','range':'[[0x0,0xffe5],[0xffff,0xffff]]'},
]

fields_of_get_config_request = [
	{'name':'version', 'type':'uint8'},
	{'name':'type', 'type':'uint8'},
	{'name':'length', 'type':'uint16'},
	{'name':'xid', 'type':'uint32'},
]

fields_of_group_add = [
	{'name':'version', 'type':'uint8'},
	{'name':'type', 'type':'uint8'},
	{'name':'length', 'type':'uint16'},
	{'name':'xid', 'type':'uint32'},
	# {'name':'flags', 'type':'uint16'},
	{'name':'group_type', 'type':'uint8','range':'[[0x0,0x03],[0xf0,0xff]]'},
	{'name':'group_id', 'type':'uint32','range':'[[0x0,0xffffff00],[0xfffffffc,0xfffffffc],[0xffffffff,0xffffffff]]'},
	{'name':'buckets','type':'list','fields':[
		{'name':'bucket','fields':[
			{'name':'weight', 'type':'uint16'},
			{'name':'watch_port', 'type':'port'}, #uint32
			{'name':'watch_group', 'type':'uint32'},
			{'name':'actions','type':'list','fields':[
				{'name':'output','fields':[
					{'name':'port', 'type':'port'},
					{'name':'max_len', 'type':'uint16'}
				]}, #0
				{'name':'copy_ttl_out','type':''}, #11
				{'name':'copy_ttl_in','type':''}, #12
				{'name':'set_mpls_ttl','fields':[
					{'name':'mpls_ttl', 'type':'uint8'},
				]}, #15
				{'name':'dec_mpls_ttl','type':''}, #16
				{'name':'push_vlan','fields':[
					{'name':'ethertype', 'type':'uint16'},
				]}, #17
				{'name':'pop_vlan','type':''}, #18
				{'name':'push_mpls','fields':[
					{'name':'ethertype', 'type':'uint16'},
				]}, #19
				{'name':'pop_mpls','fields':[
					{'name':'ethertype', 'type':'uint16'},
				]}, #20
				{'name':'set_queue','fields':[
					{'name':'queue_id', 'type':'uint32'},
				]}, #21
				{'name':'group','fields':[
					{'name':'group_id', 'type':'uint32','range':'[[0x0,0xffffff00],[0xfffffffc,0xfffffffc],[0xffffffff,0xffffffff]]'},
				]}, #22
				{'name':'set_nw_ttl','fields':[
					{'name':'nw_ttl', 'type':'uint8'},
				]}, #23
				{'name':'dec_nw_ttl','type':''}, #24
				{'name':'set_field','impl':False}, #25 field is too difficulty to implement
				{'name':'push_pbb','fields':[
					{'name':'ethertype', 'type':'uint16'},
				]}, #26
				{'name':'pop_pbb','type':''}, #27
				{'name':'experimenter','impl':False}, #ffff experimenter is also difficulty to implement
			]},
		]}
	]}
	# {'name':'buckets','fields':[
	# 	{'name':'element','type':'list', 'fields':[
	# 		{'name':'weight', 'type':'uint16'},
	# 		{'name':'watch_port', 'type':'port'}, #uint32
	# 		{'name':'watch_group', 'type':'uint32'},
	# 		{'name':'actions','fields':[
	# 			##TODO: This Handling is bad
	# 			{'name':'element','type':'TLV', 'fields': [
	# 				{'name':'port', 'type':'port'}, #uint32
	# 				{'name':'max_len', 'type':'uint16'},
	# 			]},
	# 		]},
	# 	]},
	# ]},
]

fields_of_group_delete = [
	{'name':'version', 'type':'uint8'},
	{'name':'type', 'type':'uint8'},
	{'name':'length', 'type':'uint16'},
	{'name':'xid', 'type':'uint32'},
	# {'name':'flags', 'type':'uint16'},
	{'name':'group_type', 'type':'uint8','range':'[[0x0,0x03],[0xf0,0xff]]'},
	{'name':'group_id', 'type':'uint32','range':'[[0x0,0xffffff00],[0xfffffffc,0xfffffffc],[0xffffffff,0xffffffff]]'},
	{'name':'buckets','type':'list','fields':[
		{'name':'bucket','fields':[
			{'name':'weight', 'type':'uint16'},
			{'name':'watch_port', 'type':'port'}, #uint32
			{'name':'watch_group', 'type':'uint32'},
			{'name':'actions','type':'list','fields':[
				{'name':'output','fields':[
					{'name':'port', 'type':'port'},
					{'name':'max_len', 'type':'uint16'}
				]}, #0
				{'name':'copy_ttl_out','type':''}, #11
				{'name':'copy_ttl_in','type':''}, #12
				{'name':'set_mpls_ttl','fields':[
					{'name':'mpls_ttl', 'type':'uint8'},
				]}, #15
				{'name':'dec_mpls_ttl','type':''}, #16
				{'name':'push_vlan','fields':[
					{'name':'ethertype', 'type':'uint16'},
				]}, #17
				{'name':'pop_vlan','type':''}, #18
				{'name':'push_mpls','fields':[
					{'name':'ethertype', 'type':'uint16'},
				]}, #19
				{'name':'pop_mpls','fields':[
					{'name':'ethertype', 'type':'uint16'},
				]}, #20
				{'name':'set_queue','fields':[
					{'name':'queue_id', 'type':'uint32'},
				]}, #21
				{'name':'group','fields':[
					{'name':'group_id', 'type':'uint32','range':'[[0x0,0xffffff00],[0xfffffffc,0xfffffffc],[0xffffffff,0xffffffff]]'},
				]}, #22
				{'name':'set_nw_ttl','fields':[
					{'name':'nw_ttl', 'type':'uint8'},
				]}, #23
				{'name':'dec_nw_ttl','type':''}, #24
				{'name':'set_field','impl':False}, #25 field is too difficulty to implement
				{'name':'push_pbb','fields':[
					{'name':'ethertype', 'type':'uint16'},
				]}, #26
				{'name':'pop_pbb','type':''}, #27
				{'name':'experimenter','impl':False}, #ffff experimenter is also difficulty to implement
			]},
		]}
	]}
	# {'name':'buckets','fields':[
	# 	{'name':'element','type':'list', 'fields':[
	# 		{'name':'weight', 'type':'uint16'},
	# 		{'name':'watch_port', 'type':'port'}, #uint32
	# 		{'name':'watch_group', 'type':'uint32'},
	# 		{'name':'actions','fields':[
	# 			##TODO: This Handling is bad
	# 			{'name':'element','type':'TLV', 'fields': [
	# 				{'name':'port', 'type':'port'}, #uint32
	# 				{'name':'max_len', 'type':'uint16'},
	# 			]},
	# 		]},
	# 	]},
	# ]},
]

fields_of_group_desc_stats_reply = [
	{'name':'version', 'type':'uint8'},
	{'name':'type', 'type':'uint8'},
	{'name':'length', 'type':'uint16'},
	{'name':'xid', 'type':'uint32'},
	{'name':'flags', 'type':'uint16'},
	{'name':'entries','type':'list', 'fields':[
		{'name':'group_desc_stats_entry', 'fields':[
			{'name':'group_type', 'type':'uint8','range':'[[0x0,0x03],[0xf0,0xff]]'},
			{'name':'group_id', 'type':'uint32','range':'[[0x0,0xffffff00],[0xfffffffc,0xfffffffc],[0xffffffff,0xffffffff]]'},
			{'name':'buckets','type':'list','fields':[
				{'name':'bucket','fields':[
					{'name':'weight', 'type':'uint16'},
					{'name':'watch_port', 'type':'port'}, #uint32
					{'name':'watch_group', 'type':'uint32'},
					{'name':'actions','type':'list','fields':[
						{'name':'output','fields':[
							{'name':'port', 'type':'port'},
							{'name':'max_len', 'type':'uint16'}
						]}, #0
						{'name':'copy_ttl_out','type':''}, #11
						{'name':'copy_ttl_in','type':''}, #12
						{'name':'set_mpls_ttl','fields':[
							{'name':'mpls_ttl', 'type':'uint8'},
						]}, #15
						{'name':'dec_mpls_ttl','type':''}, #16
						{'name':'push_vlan','fields':[
							{'name':'ethertype', 'type':'uint16'},
						]}, #17
						{'name':'pop_vlan','type':''}, #18
						{'name':'push_mpls','fields':[
							{'name':'ethertype', 'type':'uint16'},
						]}, #19
						{'name':'pop_mpls','fields':[
							{'name':'ethertype', 'type':'uint16'},
						]}, #20
						{'name':'set_queue','fields':[
							{'name':'queue_id', 'type':'uint32'},
						]}, #21
						{'name':'group','fields':[
							{'name':'group_id', 'type':'uint32','range':'[[0x0,0xffffff00],[0xfffffffc,0xfffffffc],[0xffffffff,0xffffffff]]'},
						]}, #22
						{'name':'set_nw_ttl','fields':[
							{'name':'nw_ttl', 'type':'uint8'},
						]}, #23
						{'name':'dec_nw_ttl','type':''}, #24
						{'name':'set_field','impl':False}, #25 field is too difficulty to implement
						{'name':'push_pbb','fields':[
							{'name':'ethertype', 'type':'uint16'},
						]}, #26
						{'name':'pop_pbb','type':''}, #27
						{'name':'experimenter','impl':False}, #ffff experimenter is also difficulty to implement
					]},
				]}
			]}
		]}
	]}
	# {'name':'entries', 'fields':[
	# 	{'name':'element','type':'list', 'fields':[
	# 		{'name':'group_type', 'type':'uint8'},
	# 		{'name':'group_id', 'type':'uint32'},
	# 		{'name':'buckets','fields':[
	# 			{'name':'element','type':'list', 'fields':[
	# 				{'name':'weight', 'type':'uint16'},
	# 				{'name':'watch_port', 'type':'port'}, #uint32
	# 				{'name':'watch_group', 'type':'uint32'},
	# 				{'name':'actions','fields':[
	# 					##TODO: This Handling is bad
	# 					{'name':'element','type':'TLV', 'fields': [
	# 						{'name':'port', 'type':'port'}, #uint32
	# 						{'name':'max_len', 'type':'uint16'},
	# 					]},
	# 				]},
	# 			]},
	# 		]},
	# 	]},
	# ]},
]

fields_of_group_desc_stats_request = [
	{'name':'version', 'type':'uint8'},
	{'name':'type', 'type':'uint8'},
	{'name':'length', 'type':'uint16'},
	{'name':'xid', 'type':'uint32'},
	{'name':'flags', 'type':'uint16'},
]

fields_of_group_features_stats_reply = [
	{'name':'version', 'type':'uint8'},
	{'name':'type', 'type':'uint8'},
	{'name':'length', 'type':'uint16'},
	{'name':'xid', 'type':'uint32'},
	{'name':'flags', 'type':'uint16'},
	{'name':'capabilities', 'type':'uint32'},
	{'name':'types', 'type':'uint32'},
	{'name':'max_groups_all', 'type':'uint32'},
	{'name':'max_groups_select', 'type':'uint32'},
	{'name':'max_groups_indirect', 'type':'uint32'},
	{'name':'max_groups_ff', 'type':'uint32'},
	{'name':'actions_all', 'type':'uint32'},
	{'name':'actions_select', 'type':'uint32'},
	{'name':'actions_indirect', 'type':'uint32'},
	{'name':'actions_ff', 'type':'uint32'},
]

fields_of_group_features_stats_request = [
	{'name':'version', 'type':'uint8'},
	{'name':'type', 'type':'uint8'},
	{'name':'length', 'type':'uint16'},
	{'name':'xid', 'type':'uint32'},
	{'name':'flags', 'type':'uint16'},
]

fields_of_group_mod_failed_error_msg = [
	{'name':'version', 'type':'uint8'},
	{'name':'type', 'type':'uint8'},
	{'name':'length', 'type':'uint16'},
	{'name':'xid', 'type':'uint32'},
	{'name':'code', 'type':'uint16'},
	{'name':'data', 'impl':False},
]

fields_of_group_modify = [
	{'name':'version', 'type':'uint8'},
	{'name':'type', 'type':'uint8'},
	{'name':'length', 'type':'uint16'},
	{'name':'xid', 'type':'uint32'},
	# {'name':'flags', 'type':'uint16'},
	{'name':'group_type', 'type':'uint8','range':'[[0x0,0x03],[0xf0,0xff]]'},
	{'name':'group_id', 'type':'uint32','range':'[[0x0,0xffffff00],[0xfffffffc,0xfffffffc],[0xffffffff,0xffffffff]]'},
	
	{'name':'buckets','type':'list','fields':[
		{'name':'bucket','fields':[
			{'name':'weight', 'type':'uint16'},
			{'name':'watch_port', 'type':'port'}, #uint32
			{'name':'watch_group', 'type':'uint32'},
			{'name':'actions','type':'list','fields':[
				{'name':'output','fields':[
					{'name':'port', 'type':'port'},
					{'name':'max_len', 'type':'uint16'}
				]}, #0
				{'name':'copy_ttl_out','type':''}, #11
				{'name':'copy_ttl_in','type':''}, #12
				{'name':'set_mpls_ttl','fields':[
					{'name':'mpls_ttl', 'type':'uint8'},
				]}, #15
				{'name':'dec_mpls_ttl','type':''}, #16
				{'name':'push_vlan','fields':[
					{'name':'ethertype', 'type':'uint16'},
				]}, #17
				{'name':'pop_vlan','type':''}, #18
				{'name':'push_mpls','fields':[
					{'name':'ethertype', 'type':'uint16'},
				]}, #19
				{'name':'pop_mpls','fields':[
					{'name':'ethertype', 'type':'uint16'},
				]}, #20
				{'name':'set_queue','fields':[
					{'name':'queue_id', 'type':'uint32'},
				]}, #21
				{'name':'group','fields':[
					{'name':'group_id', 'type':'uint32','range':'[[0x0,0xffffff00],[0xfffffffc,0xfffffffc],[0xffffffff,0xffffffff]]'},
				]}, #22
				{'name':'set_nw_ttl','fields':[
					{'name':'nw_ttl', 'type':'uint8'},
				]}, #23
				{'name':'dec_nw_ttl','type':''}, #24
				{'name':'set_field','impl':False}, #25 field is too difficulty to implement
				{'name':'push_pbb','fields':[
					{'name':'ethertype', 'type':'uint16'},
				]}, #26
				{'name':'pop_pbb','type':''}, #27
				{'name':'experimenter','impl':False}, #ffff experimenter is also difficulty to implement
			]},
		]}
	]}
	# {'name':'buckets','fields':[
	# 	{'name':'element','type':'list', 'fields':[
	# 		{'name':'weight', 'type':'uint16'},
	# 		{'name':'watch_port', 'type':'port'}, #uint32
	# 		{'name':'watch_group', 'type':'uint32'},
	# 		{'name':'actions','fields':[
	# 			##TODO: This Handling is bad
	# 			{'name':'element','type':'TLV', 'fields': [
	# 				{'name':'port', 'type':'port'}, #uint32
	# 				{'name':'max_len', 'type':'uint16'},
	# 			]},
	# 		]},
	# 	]},
	# ]},
]

fields_of_group_stats_reply = [
	{'name':'version', 'type':'uint8'},
	{'name':'type', 'type':'uint8'},
	{'name':'length', 'type':'uint16'},
	{'name':'xid', 'type':'uint32'},
	{'name':'flags', 'type':'uint16'},
	{'name':'entries', 'type':'list', 'fields':[
		{'name':'group_stats_entry', 'fields':[
			{'name':'group_id', 'type':'uint32','range':'[[0x0,0xffffff00],[0xfffffffc,0xfffffffc],[0xffffffff,0xffffffff]]'},
			{'name':'ref_count', 'type':'uint32'},
			{'name':'packet_count', 'type':'uint64'},
			{'name':'byte_count', 'type':'uint64'},
			{'name':'duration_sec', 'type':'uint32'},
			{'name':'duration_nsec', 'type':'uint32'},
			{'name':'bucket_stats','type':'list', 'fields':[
				{'name':'bucket_counter', 'fields':[
					{'name':'packet_count', 'type':'uint64'},
					{'name':'byte_count', 'type':'uint64'},
				]},
			]}
		]}
	]}
	# {'name':'entries', 'fields':[
	# 	{'name':'element','type':'list', 'fields':[
	# 		{'name':'group_id', 'type':'uint32'},
	# 		{'name':'ref_count', 'type':'uint32'},
	# 		{'name':'packet_count', 'type':'uint64'},
	# 		{'name':'byte_count', 'type':'uint64'},
	# 		{'name':'duration_sec', 'type':'uint32'},
	# 		{'name':'duration_nsec', 'type':'uint32'},
	# 		{'name':'bucket_stats', 'fields':[
	# 			{'name':'element','type':'list', 'fields':[
	# 				{'name':'packet_count', 'type':'uint64'},
	# 				{'name':'byte_count', 'type':'uint64'},
	# 			]},
	# 		]},
	# 	]},
	# ]},
]

fields_of_group_stats_request = [
	{'name':'version', 'type':'uint8'},
	{'name':'type', 'type':'uint8'},
	{'name':'length', 'type':'uint16'},
	{'name':'xid', 'type':'uint32'},
	{'name':'flags', 'type':'uint16'},
	{'name':'group_id', 'type':'uint32','range':'[[0x0,0xffffff00],[0xfffffffc,0xfffffffc],[0xffffffff,0xffffffff]]'},
]

fields_of_hello = [
	{'name':'version', 'type':'uint8'},
	{'name':'type', 'type':'uint8'},
	{'name':'length', 'type':'uint16'},
	{'name':'xid', 'type':'uint32'},
	{'name':'elements','type':'list','fields':[
		{'name':'hello_elem_versionbitmap','fields':[
			{'name':'bitmaps','type':'list','fields':[
				{'name':'uint32','fields':[
					{'name':'value','type':'uint32'}
				]}
			]}
		]},
		# {'name':'hello_elem_versionbitmap','fields':[
		# 	{'name':'bitmaps','type':'list','fields':[
		# 		{'name':'uint32','type':'uint32'}
		# 	]}
		# ]},
		# {'name':'element','type':'list', 'max':1, 'fields':[
		# 	{'name':'version_bitmap', 'fields':[
		# 		{'name':'element','type':'list', 'max':1, 'fields':[
		# 			{'name':'uint32', 'type':'uint32'},
		# 		]},
		# 	]},
		# ]},
	]},
]

fields_of_hello_failed_error_msg = [
	{'name':'version', 'type':'uint8'},
	{'name':'type', 'type':'uint8'},
	{'name':'length', 'type':'uint16'},
	{'name':'xid', 'type':'uint32'},
	{'name':'code', 'type':'uint16'},
	{'name':'data', 'impl':False},
]

fields_of_meter_config_stats_reply = [
	{'name':'version', 'type':'uint8'},
	{'name':'type', 'type':'uint8'},
	{'name':'length', 'type':'uint16'},
	{'name':'xid', 'type':'uint32'},
	{'name':'flags', 'type':'uint16'},
	{'name':'entries', 'type':'list', 'fields':[
		{'name':'meter_config','fields':[
			{'name':'flags', 'type':'uint16'},
			{'name':'meter_id', 'type':'uint32','range':'[[0x0,0xffff0000],[0xfffffffd,0xffffffff]]'},
			{'name':'entries', 'type':'list','fields':[
				{'name':'drop','fields':[
					{'name':'rate', 'type':'uint32'},
					{'name':'burst_size', 'type':'uint32'},
				]},
				{'name':'dscp_remark','fields':[
					{'name':'rate', 'type':'uint32'},
					{'name':'burst_size', 'type':'uint32'},
					{'name':'prec_level', 'type':'uint8'},
				]},
				{'name':'experimenter','impl':False},
			]}
		]}
	]}
	# {'name':'entries', 'fields':[
	# 	{'name':'element','type':'list','fields':[
	# 		{'name':'flags', 'type':'uint16'},
	# 		{'name':'meter_id', 'type':'uint32'},
	# 		{'name':'entries', 'fields':[
	# 			##TODO: This Handling is bad
	# 			{'name':'element','type':'TLV','fields':[
	# 				{'name':'rate', 'type':'uint32'},
	# 				{'name':'burst_size', 'type':'uint32'},
	# 				{'name':'prec_level', 'type':'uint8'},
	# 			]},
	# 		]},
	# 	]},
	# ]},
]

fields_of_meter_config_stats_request = [
	{'name':'version', 'type':'uint8'},
	{'name':'type', 'type':'uint8'},
	{'name':'length', 'type':'uint16'},
	{'name':'xid', 'type':'uint32'},
	{'name':'flags', 'type':'uint16'},
	{'name':'meter_id', 'type':'uint32','range':'[[0x0,0xffff0000],[0xfffffffd,0xffffffff]]'},
]

fields_of_meter_features_stats_reply = [
	{'name':'version', 'type':'uint8'},
	{'name':'type', 'type':'uint8'},
	{'name':'length', 'type':'uint16'},
	{'name':'xid', 'type':'uint32'},
	{'name':'flags', 'type':'uint16'},
	{'name':'features', 'fields':[
		{'name':'meter_features', 'fields':[
			{'name':'max_meter', 'type':'uint32'},
			{'name':'band_types', 'type':'uint32'},
			{'name':'capabilities', 'type':'uint32'},
			{'name':'max_bands', 'type':'uint8'},
			{'name':'max_color', 'type':'uint8'},
		]}
	]},
]

fields_of_meter_features_stats_request = [
	{'name':'version', 'type':'uint8'},
	{'name':'type', 'type':'uint8'},
	{'name':'length', 'type':'uint16'},
	{'name':'xid', 'type':'uint32'},
	{'name':'flags', 'type':'uint16'},
]

fields_of_meter_mod = [
	{'name':'version', 'type':'uint8'},
	{'name':'type', 'type':'uint8'},
	{'name':'length', 'type':'uint16'},
	{'name':'xid', 'type':'uint32'},
	{'name':'command', 'type':'uint16'},
	{'name':'flags', 'type':'uint16'},
	{'name':'meter_id', 'type':'uint32','range':'[[0x0,0xffff0000],[0xfffffffd,0xffffffff]]'},
	{'name':'meters', 'type':'list', 'fields':[
		{'name':'drop','fields':[
			{'name':'rate', 'type':'uint32'},
			{'name':'burst_size', 'type':'uint32'},
		]},
		{'name':'dscp_remark','fields':[
			{'name':'rate', 'type':'uint32'},
			{'name':'burst_size', 'type':'uint32'},
			{'name':'prec_level', 'type':'uint8'},
		]},
		{'name':'experimenter','impl':False},
	]}
	# {'name':'bands', 'fields':[
	# 	##TODO: This Handling is bad
	# 	{'name':'element','type':'TLV','fields':[
	# 		{'name':'rate', 'type':'uint32'},
	# 		{'name':'burst_size', 'type':'uint32'},
	# 		{'name':'prec_level', 'type':'uint8'},
	# 	]},
	# ]},
	# {'name':'meters', 'fields':[
	# 	##TODO: This Handling is bad
	# 	{'name':'element','type':'TLV','fields':[
	# 		{'name':'rate', 'type':'uint32'},
	# 		{'name':'burst_size', 'type':'uint32'},
	# 		{'name':'prec_level', 'type':'uint8'},
	# 	]},
	# ]},
]

fields_of_meter_mod_failed_error_msg = [
	{'name':'version', 'type':'uint8'},
	{'name':'type', 'type':'uint8'},
	{'name':'length', 'type':'uint16'},
	{'name':'xid', 'type':'uint32'},
	{'name':'code', 'type':'uint16'},
	{'name':'data', 'impl':False},
]

fields_of_meter_stats_reply = [
	{'name':'version', 'type':'uint8'},
	{'name':'type', 'type':'uint8'},
	{'name':'length', 'type':'uint16'},
	{'name':'xid', 'type':'uint32'},
	{'name':'flags', 'type':'uint16'},
	{'name':'entries', 'type':'list', 'fields':[
		{'name':'meter_stats','fields':[
			{'name':'meter_id', 'type':'uint32','range':'[[0x0,0xffff0000],[0xfffffffd,0xffffffff]]'},
			{'name':'flow_count', 'type':'uint32'},
			{'name':'packet_in_count', 'type':'uint64'},
			{'name':'byte_in_count', 'type':'uint64'},
			{'name':'duration_sec', 'type':'uint32'},
			{'name':'duration_nsec', 'type':'uint32'},
			{'name':'band_stats', 'type':'list', 'fields':[
				{'name':'meter_band_stats','fields':[
					{'name':'packet_band_count', 'type':'uint64'},
					{'name':'byte_band_count', 'type':'uint64'},
				]}
			]}
		]}
	]}
	# {'name':'entries', 'fields':[
	# 	{'name':'element','type':'list','fields':[
	# 		{'name':'meter_id', 'type':'uint32'},
	# 		{'name':'flow_count', 'type':'uint32'},
	# 		{'name':'packet_in_count', 'type':'uint64'},
	# 		{'name':'byte_in_count', 'type':'uint64'},
	# 		{'name':'duration_sec', 'type':'uint32'},
	# 		{'name':'duration_nsec', 'type':'uint32'},
	# 		{'name':'band_stats', 'fields':[
	# 			{'name':'element','type':'list','fields':[
	# 				{'name':'packet_count', 'type':'uint64'},
	# 				{'name':'byte_count', 'type':'uint64'},
	# 			]},
	# 		]},
	# 	]},
	# ]},
]

fields_of_meter_stats_request = [
	{'name':'version', 'type':'uint8'},
	{'name':'type', 'type':'uint8'},
	{'name':'length', 'type':'uint16'},
	{'name':'xid', 'type':'uint32'},
	{'name':'flags', 'type':'uint16'},
	{'name':'meter_id', 'type':'uint32','range':'[[0x0,0xffff0000],[0xfffffffd,0xffffffff]]'},
]

fields_of_packet_in = [
	{'name':'version', 'type':'uint8'},
	{'name':'type', 'type':'uint8'},
	{'name':'length', 'type':'uint16'},
	{'name':'xid', 'type':'uint32'},
	{'name':'buffer_id', 'type':'uint32'},
	{'name':'total_len', 'type':'uint16'},
	{'name':'reason', 'type':'uint8','range':'[[0x0,0x2]]'},
	{'name':'table_id', 'type':'uint8'},
	{'name':'cookie', 'type':'uint64'},
	{'name':'match', 'fields': [
		{'name':'match','fields':[
			{'name':'oxm_list','type':'list','fields':[
				{'name':'in_port', 'type':'port'}, #0
				{'name':'in_phy_port', 'type':'port'}, #1
				{'name':'metadata', 'type':'uint64'}, #2
				{'name':'eth_dst', 'type':'uint48'}, #3
				{'name':'eth_src', 'type':'uint48'}, #4
				{'name':'eth_type', 'type':'uint16'}, #5
				{'name':'vlan_vid', 'type':'uint16','range':'[[0x0,0x0],[0x1000,0x1fff]]'}, #6
				{'name':'vlan_pcp', 'type':'uint8','range':'[[0x0,0x7]]'}, #7
				{'name':'ip_dscp', 'type':'uint8','range':'[[0x0,0x3f]]'}, #8
				{'name':'ip_ecn', 'type':'uint8','range':'[[0x0,0x3]]'}, #9
				{'name':'ip_proto', 'type':'uint8'}, #10
				{'name':'ipv4_src', 'type':'uint32'}, #11
				{'name':'ipv4_dst', 'type':'uint32'}, #12
				{'name':'tcp_src', 'type':'uint16'}, #13
				{'name':'tcp_dst', 'type':'uint16'}, #14
				{'name':'udp_src', 'type':'uint16'}, #15
				{'name':'udp_dst', 'type':'uint16'}, #16
				{'name':'sctp_src', 'type':'uint16'}, #17
				{'name':'sctp_dst', 'type':'uint16'}, #18
				{'name':'icmpv4_type', 'type':'uint8'}, #19
				{'name':'icmpv4_code', 'type':'uint8'}, #20
				{'name':'arp_op', 'type':'uint16'}, #21
				{'name':'arp_spa', 'type':'uint32'}, #22
				{'name':'arp_tpa', 'type':'uint32'}, #23
				# todo：value = [0,0,0,0,0,0]
				{'name':'arp_sha', 'type':'uint48'}, #24
				{'name':'arp_tha', 'type':'uint48'}, #25
				{'name':'ipv6_src', 'type':'uint128'}, #26
				{'name':'ipv6_dst', 'type':'uint128'}, #27
				{'name':'ipv6_flabel', 'type':'uint32'}, #28
				{'name':'icmpv6_type', 'type':'uint8'}, #29
				{'name':'icmpv6_code', 'type':'uint8'}, #30
				{'name':'ipv6_nd_target', 'type':'uint128'}, #31
				{'name':'ipv6_nd_sll', 'type':'uint48'}, #32
				{'name':'ipv6_nd_tll', 'type':'uint48'}, #33
				{'name':'mpls_label', 'type':'uint32'},	#34
				{'name':'mpls_tc', 'type':'uint8'},	#35
				{'name':'mpls_bos', 'type':'uint8'}, #36
				{'name':'pbb_isid', 'impl':False, 'type':'uint64'}, #37
				{'name':'tunnel_id', 'type':'uint64'},	#38
				{'name':'ipv6_exthdr', 'type':'uint16'}, #39
			]}
		]},
	]},
	{'name':'data', 'type':'string'},
	# {'name':'match', 'fields': [
	# 	{'name':'version', 'type':'uint8'},
	# 	{'name':'fields', 'fields':[
	# 		{'name':'in_port', 'type':'port'}, #uint32
	# 		{'name':'in_phy_port', 'type':'port'}, #uint32
	# 		{'name':'metadata', 'type':'uint64'},
	# 		{'name':'eth_dst', 'type':'uint48'},
	# 		{'name':'eth_src', 'type':'uint48'},
	# 		{'name':'eth_type', 'type':'uint16'},
	# 		{'name':'vlan_vid', 'type':'uint16'},
	# 		{'name':'vlan_pcp', 'type':'uint8'},
	# 		{'name':'ip_dscp', 'type':'uint8'},
	# 		{'name':'ip_ecn', 'type':'uint8'},
	# 		{'name':'ip_proto', 'type':'uint8'},
	# 		{'name':'ipv4_src', 'type':'uint32'},
	# 		{'name':'ipv4_dst', 'type':'uint32'},
	# 		{'name':'tcp_src', 'type':'uint16'},
	# 		{'name':'tcp_dst', 'type':'uint16'},
	# 		{'name':'udp_src', 'type':'uint16'},
	# 		{'name':'udp_dst', 'type':'uint16'},
	# 		{'name':'sctp_src', 'type':'uint16'},
	# 		{'name':'sctp_dst', 'type':'uint16'},
	# 		{'name':'icmpv4_type', 'type':'uint8'},
	# 		{'name':'icmpv4_code', 'type':'uint8'},
	# 		{'name':'arp_op', 'type':'uint16'},
	# 		{'name':'arp_spa', 'type':'uint32'},
	# 		{'name':'arp_tpa', 'type':'uint32'},
	# 		{'name':'arp_sha', 'type':'uint48'},
	# 		{'name':'arp_tha', 'type':'uint48'},
	# 		{'name':'ipv6_src', 'impl':False, 'type':'uint128'},
	# 		{'name':'ipv6_dst', 'impl':False, 'type':'uint128'},
	# 		{'name':'ipv6_flabel', 'type':'uint32'},
	# 		{'name':'icmpv6_type', 'type':'uint8'},
	# 		{'name':'icmpv6_code', 'type':'uint8'},
	# 		{'name':'ipv6_nd_target', 'impl':False, 'type':'uint128'},
	# 		{'name':'ipv6_nd_sll', 'type':'uint48'},
	# 		{'name':'ipv6_nd_tll', 'type':'uint48'},
	# 		{'name':'mpls_label', 'type':'uint32'},
	# 		{'name':'mpls_tc', 'type':'uint8'},
	# 		{'name':'mpls_bos', 'type':'uint8'},
	# 		{'name':'tunnel_id', 'type':'uint64'},
	# 		{'name':'ipv6_exthdr', 'type':'uint16'},
	# 		{'name':'pbb_uca', 'type':'uint8'},
	# 		{'name':'tunnel_ipv4_src', 'type':'uint32'},
	# 		{'name':'tunnel_ipv4_dst', 'type':'uint32'},
	# 	]},
	# 	{'name':'masks', 'fields':[
	# 		{'name':'in_port', 'type':'uint32'},
	# 		{'name':'in_phy_port', 'type':'uint32'},
	# 		{'name':'metadata', 'type':'uint64'},
	# 		{'name':'eth_dst', 'type':'uint48'},
	# 		{'name':'eth_src', 'type':'uint48'},
	# 		{'name':'eth_type', 'type':'uint16'},
	# 		{'name':'vlan_vid', 'type':'uint16'},
	# 		{'name':'vlan_pcp', 'type':'uint8'},
	# 		{'name':'ip_dscp', 'type':'uint8'},
	# 		{'name':'ip_ecn', 'type':'uint8'},
	# 		{'name':'ip_proto', 'type':'uint8'},
	# 		{'name':'ipv4_src', 'type':'uint32'},
	# 		{'name':'ipv4_dst', 'type':'uint32'},
	# 		{'name':'tcp_src', 'type':'uint16'},
	# 		{'name':'tcp_dst', 'type':'uint16'},
	# 		{'name':'udp_src', 'type':'uint16'},
	# 		{'name':'udp_dst', 'type':'uint16'},
	# 		{'name':'sctp_src', 'type':'uint16'},
	# 		{'name':'sctp_dst', 'type':'uint16'},
	# 		{'name':'icmpv4_type', 'type':'uint8'},
	# 		{'name':'icmpv4_code', 'type':'uint8'},
	# 		{'name':'arp_op', 'type':'uint16'},
	# 		{'name':'arp_spa', 'type':'uint32'},
	# 		{'name':'arp_tpa', 'type':'uint32'},
	# 		{'name':'arp_sha', 'type':'uint48'},
	# 		{'name':'arp_tha', 'type':'uint48'},
	# 		{'name':'ipv6_src', 'impl':False, 'type':'uint128'},
	# 		{'name':'ipv6_dst', 'impl':False, 'type':'uint128'},
	# 		{'name':'ipv6_flabel', 'type':'uint32'},
	# 		{'name':'icmpv6_type', 'type':'uint8'},
	# 		{'name':'icmpv6_code', 'type':'uint8'},
	# 		{'name':'ipv6_nd_target', 'impl':False, 'type':'uint128'},
	# 		{'name':'ipv6_nd_sll', 'type':'uint48'},
	# 		{'name':'ipv6_nd_tll', 'type':'uint48'},
	# 		{'name':'mpls_label', 'type':'uint32'},
	# 		{'name':'mpls_tc', 'type':'uint8'},
	# 		{'name':'mpls_bos', 'type':'uint8'},
	# 		{'name':'tunnel_id', 'type':'uint64'},
	# 		{'name':'ipv6_exthdr', 'type':'uint16'},
	# 		{'name':'pbb_uca', 'type':'uint8'},
	# 		{'name':'tunnel_ipv4_src', 'type':'uint32'},
	# 		{'name':'tunnel_ipv4_dst', 'type':'uint32'},
	# 	]},
	# ]},
	# {'name':'data', 'impl':False},
	# {'name':'in_port', 'type':'port'}, #uint32
	# {'name':'in_phy_port', 'type':'port'}, #uint32
]

fields_of_packet_out = [
	{'name':'version', 'type':'uint8'},
	{'name':'type', 'type':'uint8'},
	{'name':'length', 'type':'uint16'},
	{'name':'xid', 'type':'uint32'},
	{'name':'buffer_id', 'type':'uint32'},
	{'name':'in_port', 'type':'uint32'},
	{'name':'actions','type':'list','fields':[
		{'name':'output','fields':[
			{'name':'port', 'type':'port'},
			{'name':'max_len', 'type':'uint16'}
		]}, #0
		{'name':'copy_ttl_out','type':''}, #11
		{'name':'copy_ttl_in','type':''}, #12
		{'name':'set_mpls_ttl','fields':[
			{'name':'mpls_ttl', 'type':'uint8'},
		]}, #15
		{'name':'dec_mpls_ttl','type':''}, #16
		{'name':'push_vlan','fields':[
			{'name':'ethertype', 'type':'uint16'},
		]}, #17
		{'name':'pop_vlan','type':''}, #18
		{'name':'push_mpls','fields':[
			{'name':'ethertype', 'type':'uint16'},
		]}, #19
		{'name':'pop_mpls','fields':[
			{'name':'ethertype', 'type':'uint16'},
		]}, #20
		{'name':'set_queue','fields':[
			{'name':'queue_id', 'type':'uint32'},
		]}, #21
		{'name':'group','fields':[
			{'name':'group_id', 'type':'uint32','range':'[[0x0,0xffffff00],[0xfffffffc,0xfffffffc],[0xffffffff,0xffffffff]]'},
		]}, #22
		{'name':'set_nw_ttl','fields':[
			{'name':'nw_ttl', 'type':'uint8'},
		]}, #23
		{'name':'dec_nw_ttl','type':''}, #24
		{'name':'set_field','impl':False}, #25 field is too difficulty to implement
		{'name':'push_pbb','fields':[
			{'name':'ethertype', 'type':'uint16'},
		]}, #26
		{'name':'pop_pbb','type':''}, #27
		{'name':'experimenter','impl':False}, #ffff experimenter is also difficulty to implement
	]},
	# {'name':'actions','fields':[
	# 	##TODO: This Handling is bad
	# 	{'name':'element','type':'TLV', 'fields': [
	# 		{'name':'port', 'type':'port'}, #uint32
	# 		{'name':'max_len', 'type':'uint16'},
	# 	]},
	# ]},
	{'name':'data', 'type':'string'},
]

fields_of_port_desc_stats_reply = [
	{'name':'version', 'type':'uint8'},
	{'name':'type', 'type':'uint8'},
	{'name':'length', 'type':'uint16'},
	{'name':'xid', 'type':'uint32'},
	{'name':'flags', 'type':'uint16'},
	{'name':'entries','type':'list','fields':[
		{'name':'port_desc', 'fields':[
			{'name':'port_no', 'type':'port','range':'[[0x0,0xffffff00],[0xfffffff8,0xffffffff]]'},
			{'name':'hw_addr', 'type':'uint48'},
			{'name':'name', 'type':'string'},
			{'name':'config', 'type':'uint32'},
			{'name':'state', 'type':'uint32'},
			{'name':'curr', 'type':'uint32'},
			{'name':'advertised', 'type':'uint32'},
			{'name':'supported', 'type':'uint32'},
			{'name':'peer', 'type':'uint32'},
			{'name':'curr_speed', 'type':'uint32'},
			{'name':'max_speed', 'type':'uint32'},
		]}
	]}
	# {'name':'entries', 'fields':[
	# 	{'name':'element','type':'list', 'fields':[
	# 		{'name':'port_no', 'type':'port'}, #uint32
	# 		{'name':'hw_addr', 'type':'uint48'},
	# 		{'name':'name', 'impl':False},
	# 		{'name':'config', 'type':'uint32'},
	# 		{'name':'state', 'type':'uint32'},
	# 		{'name':'properties', 'fields':[
	# 			##TODO: This Handling is bad
	# 			{'name':'element','type':'TLV', 'max':3, 'fields':[
	# 				{'name':'curr', 'type':'uint32'},
	# 				{'name':'advertised', 'type':'uint32'},
	# 				{'name':'supported', 'type':'uint32'},
	# 				{'name':'peer', 'type':'uint32'},
	# 				{'name':'curr_speed', 'type':'uint32'},
	# 				{'name':'max_speed', 'type':'uint32'},
	# 				{'name':'rx_grid_freq_lmda', 'type':'uint32'},
	# 				{'name':'tx_pwr_min', 'type':'uint32'},
	# 				{'name':'tx_pwr_max', 'type':'uint32'},
	# 			]},
	# 		]},
	# 		{'name':'curr', 'type':'uint32'},
	# 		{'name':'advertised', 'type':'uint32'},
	# 		{'name':'supported', 'type':'uint32'},
	# 		{'name':'peer', 'type':'uint32'},
	# 		{'name':'curr_speed', 'type':'uint32'},
	# 		{'name':'max_speed', 'type':'uint32'},
	# 	]},
	# ]}
]

fields_of_port_desc_stats_request = [
	{'name':'version', 'type':'uint8'},
	{'name':'type', 'type':'uint8'},
	{'name':'length', 'type':'uint16'},
	{'name':'xid', 'type':'uint32'},
	{'name':'flags', 'type':'uint16'},
]

fields_of_port_mod = [
	{'name':'version', 'type':'uint8'},
	{'name':'type', 'type':'uint8'},
	{'name':'length', 'type':'uint16'},
	{'name':'xid', 'type':'uint32'},
	{'name':'port_no', 'type':'port','range':'[[0x0,0xffffff00],[0xfffffff8,0xffffffff]]'}, #uint32
	{'name':'hw_addr', 'type':'uint48'},
	# {'name':'hw_addr', 'impl':False},
	{'name':'config', 'type':'uint32'},
	{'name':'mask', 'type':'uint32'},
	# {'name':'properties', 'fields':[
	# 	##TODO: This Handling is bad
	# 	{'name':'element','type':'TLV', 'max':1, 'fields':[
	# 		{'name':'advertise', 'type':'uint32'},
	# 		{'name':'freq_ldma', 'type':'uint32'},
	# 		{'name':'fl_offset', 'type':'uint32'},
	# 		{'name':'grid_span', 'type':'uint32'},
	# 		{'name':'tx_pwr', 'type':'uint32'},
	# 	]},
	# ]},
	{'name':'advertise', 'type':'uint32'},
]

fields_of_port_mod_failed_error_msg = [
	{'name':'version', 'type':'uint8'},
	{'name':'type', 'type':'uint8'},
	{'name':'length', 'type':'uint16'},
	{'name':'xid', 'type':'uint32'},
	{'name':'code', 'type':'uint16'},
	{'name':'data', 'impl':False},
]

fields_of_port_stats_reply = [
	{'name':'version', 'type':'uint8'},
	{'name':'type', 'type':'uint8'},
	{'name':'length', 'type':'uint16'},
	{'name':'xid', 'type':'uint32'},
	{'name':'flags', 'type':'uint16'},
	{'name':'entries', 'type':'list','fields':[
		{'name':'port_stats_entry', 'fields':[
			{'name':'port_no', 'type':'port','range':'[[0x0,0xffffff00],[0xfffffff8,0xffffffff]]'}, #uint32
			{'name':'duration_sec', 'type':'uint32'},
			{'name':'duration_nsec', 'type':'uint32'},
			{'name':'rx_packets', 'type':'uint64'},
			{'name':'tx_packets', 'type':'uint64'},
			{'name':'rx_bytes', 'type':'uint64'},
			{'name':'tx_bytes', 'type':'uint64'},
			{'name':'rx_dropped', 'type':'uint64'},
			{'name':'tx_dropped', 'type':'uint64'},
			{'name':'rx_errors', 'type':'uint64'},
			{'name':'tx_errors', 'type':'uint64'},
			{'name':'rx_frame_err', 'type':'uint64'},
			{'name':'rx_over_err', 'type':'uint64'},
			{'name':'rx_crc_err', 'type':'uint64'},
			{'name':'collisions', 'type':'uint64'},
		]}
	]}
	# {'name':'entries', 'fields':[
	# 	{'name':'element','type':'list', 'fields':[
	# 		{'name':'port_no', 'type':'port'}, #uint32
	# 		{'name':'duration_sec', 'type':'uint32'},
	# 		{'name':'duration_nsec', 'type':'uint32'},
	# 		{'name':'rx_packets', 'type':'uint64'},
	# 		{'name':'tx_packets', 'type':'uint64'},
	# 		{'name':'rx_bytes', 'type':'uint64'},
	# 		{'name':'tx_bytes', 'type':'uint64'},
	# 		{'name':'rx_dropped', 'type':'uint64'},
	# 		{'name':'tx_dropped', 'type':'uint64'},
	# 		{'name':'rx_errors', 'type':'uint64'},
	# 		{'name':'tx_errors', 'type':'uint64'},
	# 		{'name':'properties', 'fields':[
	# 			##TODO: This Handling is bad
	# 			{'name':'element','type':'TLV', 'max':3, 'fields':[
	# 				{'name':'rx_frame_err', 'type':'uint64'},
	# 				{'name':'rx_over_err', 'type':'uint64'},
	# 				{'name':'rx_crc_err', 'type':'uint64'},
	# 				{'name':'collisions', 'type':'uint64'},
	# 				{'name':'rx_freq_lmda', 'type':'uint32'},
	# 				{'name':'rx_offset', 'type':'uint32'},
	# 				{'name':'rx_grid_span', 'type':'uint32'},
	# 				{'name':'tx_pwr', 'type':'uint16'},
	# 				{'name':'rx_pwr', 'type':'uint16'},
	# 				{'name':'bias_current', 'type':'uint16'},
	# 				{'name':'temperature', 'type':'uint16'},
	# 			]},
	# 		]},
	# 		{'name':'rx_frame_err', 'type':'uint64'},
	# 		{'name':'rx_over_err', 'type':'uint64'},
	# 		{'name':'rx_crc_err', 'type':'uint64'},
	# 		{'name':'collisions', 'type':'uint64'},
	# 	]},
	# ]}
]

fields_of_port_stats_request = [
	{'name':'version', 'type':'uint8'},
	{'name':'type', 'type':'uint8'},
	{'name':'length', 'type':'uint16'},
	{'name':'xid', 'type':'uint32'},
	{'name':'flags', 'type':'uint16'},
	{'name':'port_no', 'type':'port','range':'[[0x0,0xffffff00],[0xfffffff8,0xffffffff]]'}, #uint32
]

fields_of_port_status = [
	{'name':'version', 'type':'uint8'},
	{'name':'type', 'type':'uint8'},
	{'name':'length', 'type':'uint16'},
	{'name':'xid', 'type':'uint32'},
	{'name':'reason', 'type':'uint8','range':'[[0x0,0x2]]'},
	{'name':'desc', 'fields':[
		{'name':'port_desc', 'fields':[
			{'name':'port_no', 'type':'port','range':'[[0x0,0xffffff00],[0xfffffff8,0xffffffff]]'},
			{'name':'hw_addr', 'type':'uint48'},
			{'name':'name', 'type':'string'},
			{'name':'config', 'type':'uint32'},
			{'name':'state', 'type':'uint32'},
			{'name':'curr', 'type':'uint32'},
			{'name':'advertised', 'type':'uint32'},
			{'name':'supported', 'type':'uint32'},
			{'name':'peer', 'type':'uint32'},
			{'name':'curr_speed', 'type':'uint32'},
			{'name':'max_speed', 'type':'uint32'},
		]}
	]}
	# {'name':'desc', 'fields':[
	# 	{'name':'port_no', 'type':'port'}, #uint32
	# 	{'name':'hw_addr', 'type':'uint48'},
	# 	{'name':'name', 'impl':False},
	# 	{'name':'config', 'type':'uint32'},
	# 	{'name':'state', 'type':'uint32'},
	# 	{'name':'properties', 'fields':[
	# 		##TODO: This Handling is bad
	# 		{'name':'element','type':'TLV', 'max':3, 'fields':[
	# 			{'name':'curr', 'type':'uint32'},
	# 			{'name':'advertised', 'type':'uint32'},
	# 			{'name':'supported', 'type':'uint32'},
	# 			{'name':'peer', 'type':'uint32'},
	# 			{'name':'curr_speed', 'type':'uint32'},
	# 			{'name':'max_speed', 'type':'uint32'},
	# 			{'name':'rx_grid_freq_lmda', 'type':'uint32'},
	# 			{'name':'tx_pwr_min', 'type':'uint32'},
	# 			{'name':'tx_pwr_max', 'type':'uint32'},
	# 		]},
	# 	]},
	# 	{'name':'curr', 'type':'uint32'},
	# 	{'name':'advertised', 'type':'uint32'},
	# 	{'name':'supported', 'type':'uint32'},
	# 	{'name':'peer', 'type':'uint32'},
	# 	{'name':'curr_speed', 'type':'uint32'},
	# 	{'name':'max_speed', 'type':'uint32'},
	# ]},
]

fields_of_queue_desc_stats_reply = [
	{'name':'version', 'type':'uint8'},
	{'name':'type', 'type':'uint8'},
	{'name':'length', 'type':'uint16'},
	{'name':'xid', 'type':'uint32'},
	{'name':'flags', 'type':'uint16'},
	{'name':'entries', 'type':'list', 'fields':[
		
	]}
	# {'name':'entries', 'fields':[
	# 	{'name':'element','type':'list', 'fields':[
	# 		{'name':'port_no', 'type':'port'}, #uint32
	# 		{'name':'queue_id', 'type':'uint32'},
	# 		{'name':'properties', 'fields':[
	# 			##TODO: This Handling is bad
	# 			{'name':'element','type':'TLV', 'max':2, 'fields':[
	# 				{'name':'rate', 'type':'uint16'},
	# 			]},
	# 		]},
	# 	]},
	# ]},
]

fields_of_queue_desc_stats_request = [
	{'name':'version', 'type':'uint8'},
	{'name':'type', 'type':'uint8'},
	{'name':'length', 'type':'uint16'},
	{'name':'xid', 'type':'uint32'},
	{'name':'flags', 'type':'uint16'},
]

fields_of_queue_get_config_reply = [
	{'name':'version', 'type':'uint8'},
	{'name':'type', 'type':'uint8'},
	{'name':'length', 'type':'uint16'},
	{'name':'xid', 'type':'uint32'},
	{'name':'port', 'type':'port'}, #uint32
	{'name':'queues', 'type':'list',  'fields':[
		{'name':'packet_queue','fields':[
			{'name':'queue_id', 'type':'uint32'},
			{'name':'port', 'type':'port'}, #uint32
			{'name':'properties','type':'list','fields':[
				{'name':'queue_prop_max_rate', 'fields':[
					{'name':'rate', 'type':'uint16'},
				]}, #1				
				{'name':'queue_prop_min_rate', 'fields':[
					{'name':'rate', 'type':'uint16'},
				]}, #2
				{'name':'queue_prop_experimenter','impl':False,'fields':[
				]}, #ffff
			]}	
		]}
	]}
	# {'name':'queues', 'fields':[
	# 	{'name':'element','type':'list', 'fields':[
	# 		{'name':'queue_id', 'type':'uint32'},
	# 		{'name':'port', 'type':'port'}, #uint32
	# 		{'name':'properties', 'fields':[
	# 			##TODO: This Handling is bad
	# 			{'name':'element','type':'TLV', 'max':2, 'fields':[
	# 				{'name':'rate', 'type':'uint16'},
	# 			]},
	# 		]},
	# 	]},
	# ]},
]

fields_of_queue_get_config_request = [
	{'name':'version', 'type':'uint8'},
	{'name':'type', 'type':'uint8'},
	{'name':'length', 'type':'uint16'},
	{'name':'xid', 'type':'uint32'},
	{'name':'port', 'type':'port'}, #uint32
]

fields_of_queue_op_failed_error_msg = [
	{'name':'version', 'type':'uint8'},
	{'name':'type', 'type':'uint8'},
	{'name':'length', 'type':'uint16'},
	{'name':'xid', 'type':'uint32'},
	{'name':'code', 'type':'uint16'},
	{'name':'data', 'impl':False},
]

fields_of_queue_stats_reply = [
	{'name':'version', 'type':'uint8'},
	{'name':'type', 'type':'uint8'},
	{'name':'length', 'type':'uint16'},
	{'name':'xid', 'type':'uint32'},
	{'name':'flags', 'type':'uint16'},
	{'name':'entries','type':'list','fields':[
		{'name':'queue_stats_entry', 'fields':[
			{'name':'port_no', 'type':'port','range':'[[0x0,0xffffff00],[0xfffffff8,0xffffffff]]'}, #uint32
			{'name':'queue_id', 'type':'uint32'},
			{'name':'tx_bytes', 'type':'uint64'},
			{'name':'tx_packets', 'type':'uint64'},
			{'name':'tx_errors', 'type':'uint64'},
			{'name':'duration_sec', 'type':'uint32'},
			{'name':'duration_nsec', 'type':'uint32'},
		]}
	]}
	# {'name':'entries', 'fields':[
	# 	{'name':'element','type':'list', 'fields':[
	# 		{'name':'port_no', 'type':'port'}, #uint32
	# 		{'name':'queue_id', 'type':'uint32'},
	# 		{'name':'tx_bytes', 'type':'uint64'},
	# 		{'name':'tx_packets', 'type':'uint64'},
	# 		{'name':'tx_errors', 'type':'uint64'},
	# 		{'name':'duration_sec', 'type':'uint32'},
	# 		{'name':'duration_nsec', 'type':'uint32'},
	# 		{'name':'properties','impl':False,'fields':[
	# 			##TODO: This Handling is bad
	# 			{'name':'element','type':'TLV', 'fields':[
	# 			]},
	# 		]},
	# 	]},
	# ]},
]

fields_of_queue_stats_request = [
	{'name':'version', 'type':'uint8'},
	{'name':'type', 'type':'uint8'},
	{'name':'length', 'type':'uint16'},
	{'name':'xid', 'type':'uint32'},
	{'name':'flags', 'type':'uint16'},
	{'name':'port_no', 'type':'port','range':'[[0x0,0xffffff00],[0xfffffff8,0xffffffff]]'}, #uint32
	{'name':'queue_id', 'type':'uint32'},
]

fields_of_requestforward = [
	{'name':'version', 'type':'uint8'},
	{'name':'type', 'type':'uint8'},
	{'name':'length', 'type':'uint16'},
	{'name':'xid', 'type':'uint32'},
	{'name':'role', 'type':'uint32','range':'[[0x1,0x4]]'},
	{'name':'data', 'impl':False},
]

fields_of_role_reply = [
	{'name':'version', 'type':'uint8'},
	{'name':'type', 'type':'uint8'},
	{'name':'length', 'type':'uint16'},
	{'name':'xid', 'type':'uint32'},
	{'name':'role', 'type':'uint32','range':'[[0x1,0x4]]'},
	{'name':'generation_id', 'type':'uint64'},
]

fields_of_role_request = [
	{'name':'version', 'type':'uint8'},
	{'name':'type', 'type':'uint8'},
	{'name':'length', 'type':'uint16'},
	{'name':'xid', 'type':'uint32'},
	{'name':'role', 'type':'uint32','range':'[[0x1,0x4]]'},
	{'name':'generation_id', 'type':'uint64'},
]

fields_of_role_request_failed_error_msg = [
	{'name':'version', 'type':'uint8'},
	{'name':'type', 'type':'uint8'},
	{'name':'length', 'type':'uint16'},
	{'name':'xid', 'type':'uint32'},
	{'name':'code', 'type':'uint16'},
	{'name':'data', 'impl':False},
]

fields_of_role_status = [
	{'name':'version', 'type':'uint8'},
	{'name':'type', 'type':'uint8'},
	{'name':'length', 'type':'uint16'},
	{'name':'xid', 'type':'uint32'},
	{'name':'role', 'type':'uint32','range':'[[0x1,0x4]]'},
	{'name':'generation_id', 'type':'uint64'},
	{'name':'properties','impl':False,'fields':[
		##TODO: This Handling is bad
		{'name':'element','type':'TLV', 'fields':[
		]},
	]},
]

fields_of_set_config = [
	{'name':'version', 'type':'uint8'},
	{'name':'type', 'type':'uint8'},
	{'name':'length', 'type':'uint16'},
	{'name':'xid', 'type':'uint32'},
	{'name':'flags', 'type':'uint16'},
	{'name':'miss_send_len', 'type':'uint16','range':'[[0x0,0xffe5],[0xffff,0xffff]]'},
]

fields_of_switch_config_failed_error_msg = [
	{'name':'version', 'type':'uint8'},
	{'name':'type', 'type':'uint8'},
	{'name':'length', 'type':'uint16'},
	{'name':'xid', 'type':'uint32'},
	{'name':'code', 'type':'uint16'},
	{'name':'data', 'impl':False},
]

fields_of_table_desc_stats_reply = [
	{'name':'version', 'type':'uint8'},
	{'name':'type', 'type':'uint8'},
	{'name':'length', 'type':'uint16'},
	{'name':'xid', 'type':'uint32'},
	{'name':'flags', 'type':'uint16'},
	{'name':'entries', 'fields':[
		{'name':'element','type':'list', 'fields':[
			{'name':'table_id', 'type':'uint8'},
			{'name':'config', 'type':'uint32'},
		]},
	]},
]

fields_of_table_desc_stats_request = [
	{'name':'version', 'type':'uint8'},
	{'name':'type', 'type':'uint8'},
	{'name':'length', 'type':'uint16'},
	{'name':'xid', 'type':'uint32'},
	{'name':'flags', 'type':'uint16'},
]

fields_of_table_features_failed_error_msg = [
	{'name':'version', 'type':'uint8'},
	{'name':'type', 'type':'uint8'},
	{'name':'length', 'type':'uint16'},
	{'name':'xid', 'type':'uint32'},
	{'name':'code', 'type':'uint16'},
	{'name':'data', 'impl':False},
]

fields_of_table_features_stats_reply = [
	{'name':'version', 'type':'uint8'},
	{'name':'type', 'type':'uint8'},
	{'name':'length', 'type':'uint16'},
	{'name':'xid', 'type':'uint32'},
	{'name':'flags', 'type':'uint16'},
	{'name':'entries', 'type':'list','impl':False,'fields':[
		{'name':'table_features','impl':False,'fields':[
			{'name':'table_id', 'type':'uint8'},
			{'name':'name', 'type':'string'},
			{'name':'metadata_match', 'type':'uint64'},
			{'name':'metadata_write', 'type':'uint64'},
			{'name':'config', 'type':'uint32'},
			{'name':'max_entries', 'type':'uint32'},
			{'name':'properties','type':'list','impl':False,'fields':[
				{'name':'table_feature_prop_instructions','impl':False, 'fields':[
					{'name':'instruction_ids','type':'list','fields':[
						{'name':'instruction_id','fields':[
							{'name':'type','type':'uint16'}
						]}
					]}
				]}, #0 may be OK
				{'name':'table_feature_prop_instructions_miss', 'impl':False, 'fields':[
					{'name':'instruction_ids','type':'list','fields':[
						{'name':'instruction_id','fields':[
							{'name':'type','type':'uint16'}
						]}
					]}
				]}, #1 may be OK
				{'name':'table_feature_prop_next_tables', 'impl':False, 'fields':[
					{'name':'next_table_ids','type':'list','fields':[
						{'type':'uint8'}
					]}
				]}, #2
				{'name':'table_feature_prop_next_tables_miss','impl':False,'fields':[
					{'name':'next_table_ids','type':'list','fields':[
						{'type':'uint8'}
					]}
				]}, #3
				{'name':'table_feature_prop_write_actions','impl':False, 'fields':[
					{'name':'action_ids','type':'list','fields':[
						{'name':'action_id','fields':[
							{'name':'type','type':'uint16'}
						]}
					]}
				]}, #4 may be OK
				{'name':'table_feature_prop_write_actions_miss','impl':False, 'fields':[
					{'name':'action_ids','type':'list','fields':[
						{'name':'action_id','fields':[
							{'name':'type','type':'uint16'}
						]}
					]}
				]}, #5
				{'name':'table_feature_prop_apply_actions', 'impl':False, 'fields':[
					{'name':'action_ids','type':'list','fields':[
						{'name':'action_id','fields':[
							{'name':'type','type':'uint16'}
						]}
					]}
				]}, #6 may be OK
				{'name':'table_feature_prop_apply_actions_miss', 'impl':False, 'fields':[
					{'name':'action_ids','type':'list','fields':[
						{'name':'action_id','fields':[
							{'name':'type','type':'uint16'}
						]}
					]}
				]}, #7
				{'name':'table_feature_prop_match','impl':False, 'fields':[
					{'name':'oxm_ids','type':'list','fields':[
						# realate to match oxm , but parameter = null
						{'name':'in_port', 'type':''}, #0
						{'name':'in_phy_port', 'type':''}, #1
						{'name':'metadata', 'type':''}, #2
						{'name':'eth_dst', 'type':''}, #3
						{'name':'eth_src', 'type':''}, #4
						{'name':'eth_type', 'type':''}, #5
						{'name':'vlan_vid', 'type':'','range':'[[0x0,0x0],[0x1000,0x1fff]]'}, #6
						{'name':'vlan_pcp','type':'','range':'[[0x0,0x7]]'}, #7
						{'name':'ip_dscp', 'type':'','range':'[[0x0,0x3f]]'}, #8
						{'name':'ip_ecn', 'type':'','range':'[[0x0,0x3]]'}, #9
						{'name':'ip_proto', 'type':''}, #10
						{'name':'ipv4_src', 'type':''}, #11
						{'name':'ipv4_dst', 'type':''}, #12
						{'name':'tcp_src', 'type':''}, #13
						{'name':'tcp_dst', 'type':''}, #14
						{'name':'udp_src', 'type':''}, #15
						{'name':'udp_dst', 'type':''}, #16
						{'name':'sctp_src', 'type':''}, #17
						{'name':'sctp_dst', 'type':''}, #18
						{'name':'icmpv4_type', 'type':''}, #19
						{'name':'icmpv4_code', 'type':''}, #20
						{'name':'arp_op', 'type':''}, #21
						{'name':'arp_spa', 'type':''}, #22
						{'name':'arp_tpa', 'type':''}, #23
						{'name':'arp_sha', 'type':''}, #24
						{'name':'arp_tha', 'type':''}, #25
						{'name':'ipv6_src','type':''}, #26
						{'name':'ipv6_dst', 'type':''}, #27
						{'name':'ipv6_flabel', 'type':''}, #28
						{'name':'icmpv6_type', 'type':''}, #29
						{'name':'icmpv6_code', 'type':''}, #30
						{'name':'ipv6_nd_target', 'type':''}, #31
						{'name':'ipv6_nd_sll', 'type':''}, #32
						{'name':'ipv6_nd_tll', 'type':''}, #33
						{'name':'mpls_label', 'type':''},	#34
						{'name':'mpls_tc', 'type':''},	#35
						{'name':'mpls_bos', 'type':''}, #36
						{'name':'pbb_isid', 'impl':False, 'type':''}, #37
						{'name':'tunnel_id', 'type':''},	#38
						{'name':'ipv6_exthdr', 'type':''}, #39
					]}
				]}, #8
				{'name':'table_feature_prop_wildcards','impl':False,'fields':[
					{'name':'oxm_ids','type':'list','fields':[
						# realate to match oxm , but parameter = null
						{'name':'in_port', 'type':''}, #0
						{'name':'in_phy_port', 'type':''}, #1
						{'name':'metadata', 'type':''}, #2
						{'name':'eth_dst', 'type':''}, #3
						{'name':'eth_src', 'type':''}, #4
						{'name':'eth_type', 'type':''}, #5
						{'name':'vlan_vid', 'type':'','range':'[[0x0,0x0],[0x1000,0x1fff]]'}, #6
						{'name':'vlan_pcp','type':'','range':'[[0x0,0x7]]'}, #7
						{'name':'ip_dscp', 'type':'','range':'[[0x0,0x3f]]'}, #8
						{'name':'ip_ecn', 'type':'','range':'[[0x0,0x3]]'}, #9
						{'name':'ip_proto', 'type':''}, #10
						{'name':'ipv4_src', 'type':''}, #11
						{'name':'ipv4_dst', 'type':''}, #12
						{'name':'tcp_src', 'type':''}, #13
						{'name':'tcp_dst', 'type':''}, #14
						{'name':'udp_src', 'type':''}, #15
						{'name':'udp_dst', 'type':''}, #16
						{'name':'sctp_src', 'type':''}, #17
						{'name':'sctp_dst', 'type':''}, #18
						{'name':'icmpv4_type', 'type':''}, #19
						{'name':'icmpv4_code', 'type':''}, #20
						{'name':'arp_op', 'type':''}, #21
						{'name':'arp_spa', 'type':''}, #22
						{'name':'arp_tpa', 'type':''}, #23
						{'name':'arp_sha', 'type':''}, #24
						{'name':'arp_tha', 'type':''}, #25
						{'name':'ipv6_src','type':''}, #26
						{'name':'ipv6_dst', 'type':''}, #27
						{'name':'ipv6_flabel', 'type':''}, #28
						{'name':'icmpv6_type', 'type':''}, #29
						{'name':'icmpv6_code', 'type':''}, #30
						{'name':'ipv6_nd_target', 'type':''}, #31
						{'name':'ipv6_nd_sll', 'type':''}, #32
						{'name':'ipv6_nd_tll', 'type':''}, #33
						{'name':'mpls_label', 'type':''},	#34
						{'name':'mpls_tc', 'type':''},	#35
						{'name':'mpls_bos', 'type':''}, #36
						{'name':'pbb_isid', 'impl':False, 'type':''}, #37
						{'name':'tunnel_id', 'type':''},	#38
						{'name':'ipv6_exthdr', 'type':''}, #39
					]}
				]}, #10
				{'name':'table_feature_prop_write_setfield','impl':False, 'fields':[
					{'name':'oxm_ids','type':'list','fields':[
						# realate to match oxm , but parameter = null
						{'name':'in_port', 'type':''}, #0
						{'name':'in_phy_port', 'type':''}, #1
						{'name':'metadata', 'type':''}, #2
						{'name':'eth_dst', 'type':''}, #3
						{'name':'eth_src', 'type':''}, #4
						{'name':'eth_type', 'type':''}, #5
						{'name':'vlan_vid', 'type':'','range':'[[0x0,0x0],[0x1000,0x1fff]]'}, #6
						{'name':'vlan_pcp','type':'','range':'[[0x0,0x7]]'}, #7
						{'name':'ip_dscp', 'type':'','range':'[[0x0,0x3f]]'}, #8
						{'name':'ip_ecn', 'type':'','range':'[[0x0,0x3]]'}, #9
						{'name':'ip_proto', 'type':''}, #10
						{'name':'ipv4_src', 'type':''}, #11
						{'name':'ipv4_dst', 'type':''}, #12
						{'name':'tcp_src', 'type':''}, #13
						{'name':'tcp_dst', 'type':''}, #14
						{'name':'udp_src', 'type':''}, #15
						{'name':'udp_dst', 'type':''}, #16
						{'name':'sctp_src', 'type':''}, #17
						{'name':'sctp_dst', 'type':''}, #18
						{'name':'icmpv4_type', 'type':''}, #19
						{'name':'icmpv4_code', 'type':''}, #20
						{'name':'arp_op', 'type':''}, #21
						{'name':'arp_spa', 'type':''}, #22
						{'name':'arp_tpa', 'type':''}, #23
						{'name':'arp_sha', 'type':''}, #24
						{'name':'arp_tha', 'type':''}, #25
						{'name':'ipv6_src','type':''}, #26
						{'name':'ipv6_dst', 'type':''}, #27
						{'name':'ipv6_flabel', 'type':''}, #28
						{'name':'icmpv6_type', 'type':''}, #29
						{'name':'icmpv6_code', 'type':''}, #30
						{'name':'ipv6_nd_target', 'type':''}, #31
						{'name':'ipv6_nd_sll', 'type':''}, #32
						{'name':'ipv6_nd_tll', 'type':''}, #33
						{'name':'mpls_label', 'type':''},	#34
						{'name':'mpls_tc', 'type':''},	#35
						{'name':'mpls_bos', 'type':''}, #36
						{'name':'pbb_isid', 'impl':False, 'type':''}, #37
						{'name':'tunnel_id', 'type':''},	#38
						{'name':'ipv6_exthdr', 'type':''}, #39
					]}
				]}, #12
				{'name':'table_feature_prop_write_setfield_miss','impl':False, 'fields':[
					{'name':'oxm_ids','type':'list','fields':[
						# realate to match oxm , but parameter = null
						{'name':'in_port', 'type':''}, #0
						{'name':'in_phy_port', 'type':''}, #1
						{'name':'metadata', 'type':''}, #2
						{'name':'eth_dst', 'type':''}, #3
						{'name':'eth_src', 'type':''}, #4
						{'name':'eth_type', 'type':''}, #5
						{'name':'vlan_vid', 'type':'','range':'[[0x0,0x0],[0x1000,0x1fff]]'}, #6
						{'name':'vlan_pcp','type':'','range':'[[0x0,0x7]]'}, #7
						{'name':'ip_dscp', 'type':'','range':'[[0x0,0x3f]]'}, #8
						{'name':'ip_ecn', 'type':'','range':'[[0x0,0x3]]'}, #9
						{'name':'ip_proto', 'type':''}, #10
						{'name':'ipv4_src', 'type':''}, #11
						{'name':'ipv4_dst', 'type':''}, #12
						{'name':'tcp_src', 'type':''}, #13
						{'name':'tcp_dst', 'type':''}, #14
						{'name':'udp_src', 'type':''}, #15
						{'name':'udp_dst', 'type':''}, #16
						{'name':'sctp_src', 'type':''}, #17
						{'name':'sctp_dst', 'type':''}, #18
						{'name':'icmpv4_type', 'type':''}, #19
						{'name':'icmpv4_code', 'type':''}, #20
						{'name':'arp_op', 'type':''}, #21
						{'name':'arp_spa', 'type':''}, #22
						{'name':'arp_tpa', 'type':''}, #23
						{'name':'arp_sha', 'type':''}, #24
						{'name':'arp_tha', 'type':''}, #25
						{'name':'ipv6_src','type':''}, #26
						{'name':'ipv6_dst', 'type':''}, #27
						{'name':'ipv6_flabel', 'type':''}, #28
						{'name':'icmpv6_type', 'type':''}, #29
						{'name':'icmpv6_code', 'type':''}, #30
						{'name':'ipv6_nd_target', 'type':''}, #31
						{'name':'ipv6_nd_sll', 'type':''}, #32
						{'name':'ipv6_nd_tll', 'type':''}, #33
						{'name':'mpls_label', 'type':''},	#34
						{'name':'mpls_tc', 'type':''},	#35
						{'name':'mpls_bos', 'type':''}, #36
						{'name':'pbb_isid', 'impl':False, 'type':''}, #37
						{'name':'tunnel_id', 'type':''},	#38
						{'name':'ipv6_exthdr', 'type':''}, #39
					]}
				]}, #13
				{'name':'table_feature_prop_apply_setfield', 'impl':False,'fields':[
					{'name':'oxm_ids','type':'list','fields':[
						# realate to match oxm , but parameter = null
						{'name':'in_port', 'type':''}, #0
						{'name':'in_phy_port', 'type':''}, #1
						{'name':'metadata', 'type':''}, #2
						{'name':'eth_dst', 'type':''}, #3
						{'name':'eth_src', 'type':''}, #4
						{'name':'eth_type', 'type':''}, #5
						{'name':'vlan_vid', 'type':'','range':'[[0x0,0x0],[0x1000,0x1fff]]'}, #6
						{'name':'vlan_pcp','type':'','range':'[[0x0,0x7]]'}, #7
						{'name':'ip_dscp', 'type':'','range':'[[0x0,0x3f]]'}, #8
						{'name':'ip_ecn', 'type':'','range':'[[0x0,0x3]]'}, #9
						{'name':'ip_proto', 'type':''}, #10
						{'name':'ipv4_src', 'type':''}, #11
						{'name':'ipv4_dst', 'type':''}, #12
						{'name':'tcp_src', 'type':''}, #13
						{'name':'tcp_dst', 'type':''}, #14
						{'name':'udp_src', 'type':''}, #15
						{'name':'udp_dst', 'type':''}, #16
						{'name':'sctp_src', 'type':''}, #17
						{'name':'sctp_dst', 'type':''}, #18
						{'name':'icmpv4_type', 'type':''}, #19
						{'name':'icmpv4_code', 'type':''}, #20
						{'name':'arp_op', 'type':''}, #21
						{'name':'arp_spa', 'type':''}, #22
						{'name':'arp_tpa', 'type':''}, #23
						{'name':'arp_sha', 'type':''}, #24
						{'name':'arp_tha', 'type':''}, #25
						{'name':'ipv6_src','type':''}, #26
						{'name':'ipv6_dst', 'type':''}, #27
						{'name':'ipv6_flabel', 'type':''}, #28
						{'name':'icmpv6_type', 'type':''}, #29
						{'name':'icmpv6_code', 'type':''}, #30
						{'name':'ipv6_nd_target', 'type':''}, #31
						{'name':'ipv6_nd_sll', 'type':''}, #32
						{'name':'ipv6_nd_tll', 'type':''}, #33
						{'name':'mpls_label', 'type':''},	#34
						{'name':'mpls_tc', 'type':''},	#35
						{'name':'mpls_bos', 'type':''}, #36
						{'name':'pbb_isid', 'impl':False, 'type':''}, #37
						{'name':'tunnel_id', 'type':''},	#38
						{'name':'ipv6_exthdr', 'type':''}, #39
					]}
				]}, #14
				{'name':'table_feature_prop_apply_setfield_miss', 'impl':False,'fields':[
					{'name':'oxm_ids','type':'list','fields':[
						# realate to match oxm , but parameter = null
						{'name':'in_port', 'type':''}, #0
						{'name':'in_phy_port', 'type':''}, #1
						{'name':'metadata', 'type':''}, #2
						{'name':'eth_dst', 'type':''}, #3
						{'name':'eth_src', 'type':''}, #4
						{'name':'eth_type', 'type':''}, #5
						{'name':'vlan_vid', 'type':'','range':'[[0x0,0x0],[0x1000,0x1fff]]'}, #6
						{'name':'vlan_pcp','type':'','range':'[[0x0,0x7]]'}, #7
						{'name':'ip_dscp', 'type':'','range':'[[0x0,0x3f]]'}, #8
						{'name':'ip_ecn', 'type':'','range':'[[0x0,0x3]]'}, #9
						{'name':'ip_proto', 'type':''}, #10
						{'name':'ipv4_src', 'type':''}, #11
						{'name':'ipv4_dst', 'type':''}, #12
						{'name':'tcp_src', 'type':''}, #13
						{'name':'tcp_dst', 'type':''}, #14
						{'name':'udp_src', 'type':''}, #15
						{'name':'udp_dst', 'type':''}, #16
						{'name':'sctp_src', 'type':''}, #17
						{'name':'sctp_dst', 'type':''}, #18
						{'name':'icmpv4_type', 'type':''}, #19
						{'name':'icmpv4_code', 'type':''}, #20
						{'name':'arp_op', 'type':''}, #21
						{'name':'arp_spa', 'type':''}, #22
						{'name':'arp_tpa', 'type':''}, #23
						{'name':'arp_sha', 'type':''}, #24
						{'name':'arp_tha', 'type':''}, #25
						{'name':'ipv6_src','type':''}, #26
						{'name':'ipv6_dst', 'type':''}, #27
						{'name':'ipv6_flabel', 'type':''}, #28
						{'name':'icmpv6_type', 'type':''}, #29
						{'name':'icmpv6_code', 'type':''}, #30
						{'name':'ipv6_nd_target', 'type':''}, #31
						{'name':'ipv6_nd_sll', 'type':''}, #32
						{'name':'ipv6_nd_tll', 'type':''}, #33
						{'name':'mpls_label', 'type':''},	#34
						{'name':'mpls_tc', 'type':''},	#35
						{'name':'mpls_bos', 'type':''}, #36
						{'name':'pbb_isid', 'impl':False, 'type':''}, #37
						{'name':'tunnel_id', 'type':''},	#38
						{'name':'ipv6_exthdr', 'type':''}, #39
					]}
				]}, #15
				{'name':'table_feature_prop_experimenter', 'impl':False,'fields':[]}, #fffe
				{'name':'table_feature_prop_experimenter_miss', 'impl':False,'fields':[]}, #ffff
			]}
		]}
	]}
	# {'name':'entries', 'type':'list', 'fields':[
	# 	{'name':'table_features', 'fields':[
	# 		{'name':'table_id', 'type':'uint8'},
	# 		{'name':'name', 'type':'string'},
	# 		{'name':'metadata_match', 'type':'uint64'},
	# 		{'name':'metadata_write', 'type':'uint64'},
	# 		{'name':'config', 'type':'uint32'},
	# 		{'name':'max_entries', 'type':'uint32'},
	# 		{'name':'properties','type':'list','fields':[
	# 			{'name':'table_feature_prop_instructions', 'fields':[
	# 				{'name':'instruction_ids','type':'list','fields':[
	# 					{'name':'instruction_id','fields':[
	# 						{'name':'type','type':'uint16'}
	# 					]}
	# 				]}
	# 			]}, #0
	# 			{'name':'table_feature_prop_instructions_miss', 'fields':[
	# 				{'name':'instruction_ids','type':'list','fields':[
	# 					{'name':'instruction_id','fields':[
	# 						{'name':'type','type':'uint16'}
	# 					]}
	# 				]}
	# 			]}, #1
	# 			{'name':'table_feature_prop_next_tables', 'fields':[
	# 				{'name':'next_table_ids','type':'list','fields':[
	# 					{'type':'uint8'}
	# 				]}
	# 			]}, #2
	# 			{'name':'table_feature_prop_next_tables_miss', 'fields':[
	# 				{'name':'next_table_ids','type':'list','fields':[
	# 					{'type':'uint8'}
	# 				]}
	# 			]}, #3
	# 			{'name':'table_feature_prop_write_actions', 'fields':[
	# 				{'name':'action_ids','type':'list','fields':[
	# 					{'name':'action_id','fields':[
	# 						{'name':'type','type':'uint16'}
	# 					]}
	# 				]}
	# 			]}, #4
	# 			{'name':'table_feature_prop_write_actions_miss', 'fields':[
	# 				{'name':'action_ids','type':'list','fields':[
	# 					{'name':'action_id','fields':[
	# 						{'name':'type','type':'uint16'}
	# 					]}
	# 				]}
	# 			]}, #5
	# 			{'name':'table_feature_prop_apply_actions', 'fields':[
	# 				{'name':'action_ids','type':'list','fields':[
	# 					{'name':'action_id','fields':[
	# 						{'name':'type','type':'uint16'}
	# 					]}
	# 				]}
	# 			]}, #6
	# 			{'name':'table_feature_prop_apply_actions_miss', 'fields':[
	# 				{'name':'action_ids','type':'list','fields':[
	# 					{'name':'action_id','fields':[
	# 						{'name':'type','type':'uint16'}
	# 					]}
	# 				]}
	# 			]}, #7
	# 			{'name':'table_feature_prop_match', 'fields':[
	# 				{'name':'oxm_ids','type':'list','fields':[
	# 					# realate to match oxm , but parameter = null
	# 					{'name':'in_port', 'type':''}, #0
	# 					{'name':'in_phy_port', 'type':''}, #1
	# 					{'name':'metadata', 'type':''}, #2
	# 					{'name':'eth_dst', 'type':''}, #3
	# 					{'name':'eth_src', 'type':''}, #4
	# 					{'name':'eth_type', 'type':''}, #5
	# 					{'name':'vlan_vid', 'type':''}, #6
	# 					{'name':'vlan_pcp','type':''}, #7
	# 					{'name':'ip_dscp', 'type':''}, #8
	# 					{'name':'ip_ecn', 'type':''}, #9
	# 					{'name':'ip_proto', 'type':''}, #10
	# 					{'name':'ipv4_src', 'type':''}, #11
	# 					{'name':'ipv4_dst', 'type':''}, #12
	# 					{'name':'tcp_src', 'type':''}, #13
	# 					{'name':'tcp_dst', 'type':''}, #14
	# 					{'name':'udp_src', 'type':''}, #15
	# 					{'name':'udp_dst', 'type':''}, #16
	# 					{'name':'sctp_src', 'type':''}, #17
	# 					{'name':'sctp_dst', 'type':''}, #18
	# 					{'name':'icmpv4_type', 'type':''}, #19
	# 					{'name':'icmpv4_code', 'type':''}, #20
	# 					{'name':'arp_op', 'type':''}, #21
	# 					{'name':'arp_spa', 'type':''}, #22
	# 					{'name':'arp_tpa', 'type':''}, #23
	# 					{'name':'arp_sha', 'type':''}, #24
	# 					{'name':'arp_tha', 'type':''}, #25
	# 					{'name':'ipv6_src','type':''}, #26
	# 					{'name':'ipv6_dst', 'type':''}, #27
	# 					{'name':'ipv6_flabel', 'type':''}, #28
	# 					{'name':'icmpv6_type', 'type':''}, #29
	# 					{'name':'icmpv6_code', 'type':''}, #30
	# 					{'name':'ipv6_nd_target', 'type':''}, #31
	# 					{'name':'ipv6_nd_sll', 'type':''}, #32
	# 					{'name':'ipv6_nd_tll', 'type':''}, #33
	# 					{'name':'mpls_label', 'type':''},	#34
	# 					{'name':'mpls_tc', 'type':''},	#35
	# 					{'name':'mpls_bos', 'type':''}, #36
	# 					{'name':'pbb_isid', 'impl':False, 'type':''}, #37
	# 					{'name':'tunnel_id', 'type':''},	#38
	# 					{'name':'ipv6_exthdr', 'type':''}, #39
	# 				]}
	# 			]}, #8
	# 			{'name':'table_feature_prop_wildcards', 'fields':[
	# 				{'name':'oxm_ids','type':'list','fields':[
	# 					# realate to match oxm , but parameter = null
	# 					{'name':'in_port', 'type':''}, #0
	# 					{'name':'in_phy_port', 'type':''}, #1
	# 					{'name':'metadata', 'type':''}, #2
	# 					{'name':'eth_dst', 'type':''}, #3
	# 					{'name':'eth_src', 'type':''}, #4
	# 					{'name':'eth_type', 'type':''}, #5
	# 					{'name':'vlan_vid', 'type':''}, #6
	# 					{'name':'vlan_pcp','type':''}, #7
	# 					{'name':'ip_dscp', 'type':''}, #8
	# 					{'name':'ip_ecn', 'type':''}, #9
	# 					{'name':'ip_proto', 'type':''}, #10
	# 					{'name':'ipv4_src', 'type':''}, #11
	# 					{'name':'ipv4_dst', 'type':''}, #12
	# 					{'name':'tcp_src', 'type':''}, #13
	# 					{'name':'tcp_dst', 'type':''}, #14
	# 					{'name':'udp_src', 'type':''}, #15
	# 					{'name':'udp_dst', 'type':''}, #16
	# 					{'name':'sctp_src', 'type':''}, #17
	# 					{'name':'sctp_dst', 'type':''}, #18
	# 					{'name':'icmpv4_type', 'type':''}, #19
	# 					{'name':'icmpv4_code', 'type':''}, #20
	# 					{'name':'arp_op', 'type':''}, #21
	# 					{'name':'arp_spa', 'type':''}, #22
	# 					{'name':'arp_tpa', 'type':''}, #23
	# 					{'name':'arp_sha', 'type':''}, #24
	# 					{'name':'arp_tha', 'type':''}, #25
	# 					{'name':'ipv6_src','type':''}, #26
	# 					{'name':'ipv6_dst', 'type':''}, #27
	# 					{'name':'ipv6_flabel', 'type':''}, #28
	# 					{'name':'icmpv6_type', 'type':''}, #29
	# 					{'name':'icmpv6_code', 'type':''}, #30
	# 					{'name':'ipv6_nd_target', 'type':''}, #31
	# 					{'name':'ipv6_nd_sll', 'type':''}, #32
	# 					{'name':'ipv6_nd_tll', 'type':''}, #33
	# 					{'name':'mpls_label', 'type':''},	#34
	# 					{'name':'mpls_tc', 'type':''},	#35
	# 					{'name':'mpls_bos', 'type':''}, #36
	# 					{'name':'pbb_isid', 'impl':False, 'type':''}, #37
	# 					{'name':'tunnel_id', 'type':''},	#38
	# 					{'name':'ipv6_exthdr', 'type':''}, #39
	# 				]}
	# 			]}, #10
	# 			{'name':'table_feature_prop_write_setfield', 'fields':[
	# 				{'name':'oxm_ids','type':'list','fields':[
	# 					# realate to match oxm , but parameter = null
	# 					{'name':'in_port', 'type':''}, #0
	# 					{'name':'in_phy_port', 'type':''}, #1
	# 					{'name':'metadata', 'type':''}, #2
	# 					{'name':'eth_dst', 'type':''}, #3
	# 					{'name':'eth_src', 'type':''}, #4
	# 					{'name':'eth_type', 'type':''}, #5
	# 					{'name':'vlan_vid', 'type':''}, #6
	# 					{'name':'vlan_pcp','type':''}, #7
	# 					{'name':'ip_dscp', 'type':''}, #8
	# 					{'name':'ip_ecn', 'type':''}, #9
	# 					{'name':'ip_proto', 'type':''}, #10
	# 					{'name':'ipv4_src', 'type':''}, #11
	# 					{'name':'ipv4_dst', 'type':''}, #12
	# 					{'name':'tcp_src', 'type':''}, #13
	# 					{'name':'tcp_dst', 'type':''}, #14
	# 					{'name':'udp_src', 'type':''}, #15
	# 					{'name':'udp_dst', 'type':''}, #16
	# 					{'name':'sctp_src', 'type':''}, #17
	# 					{'name':'sctp_dst', 'type':''}, #18
	# 					{'name':'icmpv4_type', 'type':''}, #19
	# 					{'name':'icmpv4_code', 'type':''}, #20
	# 					{'name':'arp_op', 'type':''}, #21
	# 					{'name':'arp_spa', 'type':''}, #22
	# 					{'name':'arp_tpa', 'type':''}, #23
	# 					{'name':'arp_sha', 'type':''}, #24
	# 					{'name':'arp_tha', 'type':''}, #25
	# 					{'name':'ipv6_src','type':''}, #26
	# 					{'name':'ipv6_dst', 'type':''}, #27
	# 					{'name':'ipv6_flabel', 'type':''}, #28
	# 					{'name':'icmpv6_type', 'type':''}, #29
	# 					{'name':'icmpv6_code', 'type':''}, #30
	# 					{'name':'ipv6_nd_target', 'type':''}, #31
	# 					{'name':'ipv6_nd_sll', 'type':''}, #32
	# 					{'name':'ipv6_nd_tll', 'type':''}, #33
	# 					{'name':'mpls_label', 'type':''},	#34
	# 					{'name':'mpls_tc', 'type':''},	#35
	# 					{'name':'mpls_bos', 'type':''}, #36
	# 					{'name':'pbb_isid', 'impl':False, 'type':''}, #37
	# 					{'name':'tunnel_id', 'type':''},	#38
	# 					{'name':'ipv6_exthdr', 'type':''}, #39
	# 				]}
	# 			]}, #12
	# 			{'name':'table_feature_prop_write_setfield_miss', 'fields':[
	# 				{'name':'oxm_ids','type':'list','fields':[
	# 					# realate to match oxm , but parameter = null
	# 					{'name':'in_port', 'type':''}, #0
	# 					{'name':'in_phy_port', 'type':''}, #1
	# 					{'name':'metadata', 'type':''}, #2
	# 					{'name':'eth_dst', 'type':''}, #3
	# 					{'name':'eth_src', 'type':''}, #4
	# 					{'name':'eth_type', 'type':''}, #5
	# 					{'name':'vlan_vid', 'type':''}, #6
	# 					{'name':'vlan_pcp','type':''}, #7
	# 					{'name':'ip_dscp', 'type':''}, #8
	# 					{'name':'ip_ecn', 'type':''}, #9
	# 					{'name':'ip_proto', 'type':''}, #10
	# 					{'name':'ipv4_src', 'type':''}, #11
	# 					{'name':'ipv4_dst', 'type':''}, #12
	# 					{'name':'tcp_src', 'type':''}, #13
	# 					{'name':'tcp_dst', 'type':''}, #14
	# 					{'name':'udp_src', 'type':''}, #15
	# 					{'name':'udp_dst', 'type':''}, #16
	# 					{'name':'sctp_src', 'type':''}, #17
	# 					{'name':'sctp_dst', 'type':''}, #18
	# 					{'name':'icmpv4_type', 'type':''}, #19
	# 					{'name':'icmpv4_code', 'type':''}, #20
	# 					{'name':'arp_op', 'type':''}, #21
	# 					{'name':'arp_spa', 'type':''}, #22
	# 					{'name':'arp_tpa', 'type':''}, #23
	# 					{'name':'arp_sha', 'type':''}, #24
	# 					{'name':'arp_tha', 'type':''}, #25
	# 					{'name':'ipv6_src','type':''}, #26
	# 					{'name':'ipv6_dst', 'type':''}, #27
	# 					{'name':'ipv6_flabel', 'type':''}, #28
	# 					{'name':'icmpv6_type', 'type':''}, #29
	# 					{'name':'icmpv6_code', 'type':''}, #30
	# 					{'name':'ipv6_nd_target', 'type':''}, #31
	# 					{'name':'ipv6_nd_sll', 'type':''}, #32
	# 					{'name':'ipv6_nd_tll', 'type':''}, #33
	# 					{'name':'mpls_label', 'type':''},	#34
	# 					{'name':'mpls_tc', 'type':''},	#35
	# 					{'name':'mpls_bos', 'type':''}, #36
	# 					{'name':'pbb_isid', 'impl':False, 'type':''}, #37
	# 					{'name':'tunnel_id', 'type':''},	#38
	# 					{'name':'ipv6_exthdr', 'type':''}, #39
	# 				]}
	# 			]}, #13
	# 			{'name':'table_feature_prop_apply_setfield', 'fields':[
	# 				{'name':'oxm_ids','type':'list','fields':[
	# 					# realate to match oxm , but parameter = null
	# 					{'name':'in_port', 'type':''}, #0
	# 					{'name':'in_phy_port', 'type':''}, #1
	# 					{'name':'metadata', 'type':''}, #2
	# 					{'name':'eth_dst', 'type':''}, #3
	# 					{'name':'eth_src', 'type':''}, #4
	# 					{'name':'eth_type', 'type':''}, #5
	# 					{'name':'vlan_vid', 'type':''}, #6
	# 					{'name':'vlan_pcp','type':''}, #7
	# 					{'name':'ip_dscp', 'type':''}, #8
	# 					{'name':'ip_ecn', 'type':''}, #9
	# 					{'name':'ip_proto', 'type':''}, #10
	# 					{'name':'ipv4_src', 'type':''}, #11
	# 					{'name':'ipv4_dst', 'type':''}, #12
	# 					{'name':'tcp_src', 'type':''}, #13
	# 					{'name':'tcp_dst', 'type':''}, #14
	# 					{'name':'udp_src', 'type':''}, #15
	# 					{'name':'udp_dst', 'type':''}, #16
	# 					{'name':'sctp_src', 'type':''}, #17
	# 					{'name':'sctp_dst', 'type':''}, #18
	# 					{'name':'icmpv4_type', 'type':''}, #19
	# 					{'name':'icmpv4_code', 'type':''}, #20
	# 					{'name':'arp_op', 'type':''}, #21
	# 					{'name':'arp_spa', 'type':''}, #22
	# 					{'name':'arp_tpa', 'type':''}, #23
	# 					{'name':'arp_sha', 'type':''}, #24
	# 					{'name':'arp_tha', 'type':''}, #25
	# 					{'name':'ipv6_src','type':''}, #26
	# 					{'name':'ipv6_dst', 'type':''}, #27
	# 					{'name':'ipv6_flabel', 'type':''}, #28
	# 					{'name':'icmpv6_type', 'type':''}, #29
	# 					{'name':'icmpv6_code', 'type':''}, #30
	# 					{'name':'ipv6_nd_target', 'type':''}, #31
	# 					{'name':'ipv6_nd_sll', 'type':''}, #32
	# 					{'name':'ipv6_nd_tll', 'type':''}, #33
	# 					{'name':'mpls_label', 'type':''},	#34
	# 					{'name':'mpls_tc', 'type':''},	#35
	# 					{'name':'mpls_bos', 'type':''}, #36
	# 					{'name':'pbb_isid', 'impl':False, 'type':''}, #37
	# 					{'name':'tunnel_id', 'type':''},	#38
	# 					{'name':'ipv6_exthdr', 'type':''}, #39
	# 				]}
	# 			]}, #14
	# 			{'name':'table_feature_prop_apply_setfield_miss', 'fields':[
	# 				{'name':'oxm_ids','type':'list','fields':[
	# 					# realate to match oxm , but parameter = null
	# 					{'name':'in_port', 'type':''}, #0
	# 					{'name':'in_phy_port', 'type':''}, #1
	# 					{'name':'metadata', 'type':''}, #2
	# 					{'name':'eth_dst', 'type':''}, #3
	# 					{'name':'eth_src', 'type':''}, #4
	# 					{'name':'eth_type', 'type':''}, #5
	# 					{'name':'vlan_vid', 'type':''}, #6
	# 					{'name':'vlan_pcp','type':''}, #7
	# 					{'name':'ip_dscp', 'type':''}, #8
	# 					{'name':'ip_ecn', 'type':''}, #9
	# 					{'name':'ip_proto', 'type':''}, #10
	# 					{'name':'ipv4_src', 'type':''}, #11
	# 					{'name':'ipv4_dst', 'type':''}, #12
	# 					{'name':'tcp_src', 'type':''}, #13
	# 					{'name':'tcp_dst', 'type':''}, #14
	# 					{'name':'udp_src', 'type':''}, #15
	# 					{'name':'udp_dst', 'type':''}, #16
	# 					{'name':'sctp_src', 'type':''}, #17
	# 					{'name':'sctp_dst', 'type':''}, #18
	# 					{'name':'icmpv4_type', 'type':''}, #19
	# 					{'name':'icmpv4_code', 'type':''}, #20
	# 					{'name':'arp_op', 'type':''}, #21
	# 					{'name':'arp_spa', 'type':''}, #22
	# 					{'name':'arp_tpa', 'type':''}, #23
	# 					{'name':'arp_sha', 'type':''}, #24
	# 					{'name':'arp_tha', 'type':''}, #25
	# 					{'name':'ipv6_src','type':''}, #26
	# 					{'name':'ipv6_dst', 'type':''}, #27
	# 					{'name':'ipv6_flabel', 'type':''}, #28
	# 					{'name':'icmpv6_type', 'type':''}, #29
	# 					{'name':'icmpv6_code', 'type':''}, #30
	# 					{'name':'ipv6_nd_target', 'type':''}, #31
	# 					{'name':'ipv6_nd_sll', 'type':''}, #32
	# 					{'name':'ipv6_nd_tll', 'type':''}, #33
	# 					{'name':'mpls_label', 'type':''},	#34
	# 					{'name':'mpls_tc', 'type':''},	#35
	# 					{'name':'mpls_bos', 'type':''}, #36
	# 					{'name':'pbb_isid', 'impl':False, 'type':''}, #37
	# 					{'name':'tunnel_id', 'type':''},	#38
	# 					{'name':'ipv6_exthdr', 'type':''}, #39
	# 				]}
	# 			]}, #15
	# 			{'name':'table_feature_prop_experimenter', 'impl':False,'fields':[]}, #fffe
	# 			{'name':'table_feature_prop_experimenter_miss', 'impl':False,'fields':[]}, #ffff
	# 		]}
	# 	]}
	# ]}

	# {'name':'entries', 'fields':[
	# 	{'name':'element','type':'list', 'fields':[
	# 		{'name':'table_id', 'type':'uint8'},
	# 		{'name':'name', 'impl':False},
	# 		{'name':'metadata_match', 'type':'uint64'},
	# 		{'name':'matadata_write', 'type':'uint64'},
	# 		{'name':'config', 'type':'uint32'},
	# 		{'name':'max_entries', 'type':'uint32'},
	# 		{'name':'properties','impl':False,'fields':[
	# 			##TODO: This Handling is bad
	# 			{'name':'element','type':'TLV', 'max':14,'fields':[
	# 				{'name':'ids','impl':False,'fields':[
	# 					##TODO: This Handling is bad
	# 					{'name':'element','type':'TLV', 'fields':[
	# 						{'name':'field', 'type':'uint32'},
	# 					]},
	# 				]},
	# 			]},
	# 		]},
	# 	]},
	# ]},
]

fields_of_table_features_stats_request = [
	{'name':'version', 'type':'uint8'},
	{'name':'type', 'type':'uint8'},
	{'name':'length', 'type':'uint16'},
	{'name':'xid', 'type':'uint32'},
	{'name':'flags', 'type':'uint16'},
	{'name':'entries', 'type':'list', 'fields':[
		{'name':'table_features', 'impl':False, 'fields':[
			{'name':'table_id', 'type':'uint8'},
			{'name':'name', 'type':'string'},
			{'name':'metadata_match', 'type':'uint64'},
			{'name':'metadata_write', 'type':'uint64'},
			{'name':'config', 'type':'uint32'},
			{'name':'max_entries', 'type':'uint32'},
			{'name':'properties','type':'list','fields':[
				{'name':'table_feature_prop_instructions', 'fields':[
					{'name':'instruction_ids','type':'list','fields':[
						{'name':'instruction_id','fields':[
							{'name':'type','type':'uint16'}
						]}
					]}
				]}, #0
				{'name':'table_feature_prop_instructions_miss', 'fields':[
					{'name':'instruction_ids','type':'list','fields':[
						{'name':'instruction_id','fields':[
							{'name':'type','type':'uint16'}
						]}
					]}
				]}, #1
				{'name':'table_feature_prop_next_tables', 'impl':False, 'fields':[
					{'name':'next_table_ids','type':'list','fields':[
						{'type':'uint8'}
					]}
				]}, #2
				{'name':'table_feature_prop_next_tables_miss','impl':False,'fields':[
					{'name':'next_table_ids','type':'list','fields':[
						{'type':'uint8'}
					]}
				]}, #3
				{'name':'table_feature_prop_write_actions', 'fields':[
					{'name':'action_ids','type':'list','fields':[
						{'name':'action_id','fields':[
							{'name':'type','type':'uint16'}
						]}
					]}
				]}, #4
				{'name':'table_feature_prop_write_actions_miss', 'fields':[
					{'name':'action_ids','type':'list','fields':[
						{'name':'action_id','fields':[
							{'name':'type','type':'uint16'}
						]}
					]}
				]}, #5
				{'name':'table_feature_prop_apply_actions', 'fields':[
					{'name':'action_ids','type':'list','fields':[
						{'name':'action_id','fields':[
							{'name':'type','type':'uint16'}
						]}
					]}
				]}, #6
				{'name':'table_feature_prop_apply_actions_miss', 'fields':[
					{'name':'action_ids','type':'list','fields':[
						{'name':'action_id','fields':[
							{'name':'type','type':'uint16'}
						]}
					]}
				]}, #7
				{'name':'table_feature_prop_match','impl':False, 'fields':[
					{'name':'oxm_ids','type':'list','fields':[
						# realate to match oxm , but parameter = null
						{'name':'in_port', 'type':''}, #0
						{'name':'in_phy_port', 'type':''}, #1
						{'name':'metadata', 'type':''}, #2
						{'name':'eth_dst', 'type':''}, #3
						{'name':'eth_src', 'type':''}, #4
						{'name':'eth_type', 'type':''}, #5
						{'name':'vlan_vid', 'type':'','range':'[[0x0,0x0],[0x1000,0x1fff]]'}, #6
						{'name':'vlan_pcp','type':'','range':'[[0x0,0x7]]'}, #7
						{'name':'ip_dscp', 'type':'','range':'[[0x0,0x3f]]'}, #8
						{'name':'ip_ecn', 'type':'','range':'[[0x0,0x3]]'}, #9
						{'name':'ip_proto', 'type':''}, #10
						{'name':'ipv4_src', 'type':''}, #11
						{'name':'ipv4_dst', 'type':''}, #12
						{'name':'tcp_src', 'type':''}, #13
						{'name':'tcp_dst', 'type':''}, #14
						{'name':'udp_src', 'type':''}, #15
						{'name':'udp_dst', 'type':''}, #16
						{'name':'sctp_src', 'type':''}, #17
						{'name':'sctp_dst', 'type':''}, #18
						{'name':'icmpv4_type', 'type':''}, #19
						{'name':'icmpv4_code', 'type':''}, #20
						{'name':'arp_op', 'type':''}, #21
						{'name':'arp_spa', 'type':''}, #22
						{'name':'arp_tpa', 'type':''}, #23
						{'name':'arp_sha', 'type':''}, #24
						{'name':'arp_tha', 'type':''}, #25
						{'name':'ipv6_src','type':''}, #26
						{'name':'ipv6_dst', 'type':''}, #27
						{'name':'ipv6_flabel', 'type':''}, #28
						{'name':'icmpv6_type', 'type':''}, #29
						{'name':'icmpv6_code', 'type':''}, #30
						{'name':'ipv6_nd_target', 'type':''}, #31
						{'name':'ipv6_nd_sll', 'type':''}, #32
						{'name':'ipv6_nd_tll', 'type':''}, #33
						{'name':'mpls_label', 'type':''},	#34
						{'name':'mpls_tc', 'type':''},	#35
						{'name':'mpls_bos', 'type':''}, #36
						{'name':'pbb_isid', 'impl':False, 'type':''}, #37
						{'name':'tunnel_id', 'type':''},	#38
						{'name':'ipv6_exthdr', 'type':''}, #39
					]}
				]}, #8
				{'name':'table_feature_prop_wildcards','impl':False,'fields':[
					{'name':'oxm_ids','type':'list','fields':[
						# realate to match oxm , but parameter = null
						{'name':'in_port', 'type':''}, #0
						{'name':'in_phy_port', 'type':''}, #1
						{'name':'metadata', 'type':''}, #2
						{'name':'eth_dst', 'type':''}, #3
						{'name':'eth_src', 'type':''}, #4
						{'name':'eth_type', 'type':''}, #5
						{'name':'vlan_vid', 'type':'','range':'[[0x0,0x0],[0x1000,0x1fff]]'}, #6
						{'name':'vlan_pcp','type':'','range':'[[0x0,0x7]]'}, #7
						{'name':'ip_dscp', 'type':'','range':'[[0x0,0x3f]]'}, #8
						{'name':'ip_ecn', 'type':'','range':'[[0x0,0x3]]'}, #9
						{'name':'ip_proto', 'type':''}, #10
						{'name':'ipv4_src', 'type':''}, #11
						{'name':'ipv4_dst', 'type':''}, #12
						{'name':'tcp_src', 'type':''}, #13
						{'name':'tcp_dst', 'type':''}, #14
						{'name':'udp_src', 'type':''}, #15
						{'name':'udp_dst', 'type':''}, #16
						{'name':'sctp_src', 'type':''}, #17
						{'name':'sctp_dst', 'type':''}, #18
						{'name':'icmpv4_type', 'type':''}, #19
						{'name':'icmpv4_code', 'type':''}, #20
						{'name':'arp_op', 'type':''}, #21
						{'name':'arp_spa', 'type':''}, #22
						{'name':'arp_tpa', 'type':''}, #23
						{'name':'arp_sha', 'type':''}, #24
						{'name':'arp_tha', 'type':''}, #25
						{'name':'ipv6_src','type':''}, #26
						{'name':'ipv6_dst', 'type':''}, #27
						{'name':'ipv6_flabel', 'type':''}, #28
						{'name':'icmpv6_type', 'type':''}, #29
						{'name':'icmpv6_code', 'type':''}, #30
						{'name':'ipv6_nd_target', 'type':''}, #31
						{'name':'ipv6_nd_sll', 'type':''}, #32
						{'name':'ipv6_nd_tll', 'type':''}, #33
						{'name':'mpls_label', 'type':''},	#34
						{'name':'mpls_tc', 'type':''},	#35
						{'name':'mpls_bos', 'type':''}, #36
						{'name':'pbb_isid', 'impl':False, 'type':''}, #37
						{'name':'tunnel_id', 'type':''},	#38
						{'name':'ipv6_exthdr', 'type':''}, #39
					]}
				]}, #10
				{'name':'table_feature_prop_write_setfield','impl':False, 'fields':[
					{'name':'oxm_ids','type':'list','fields':[
						# realate to match oxm , but parameter = null
						{'name':'in_port', 'type':''}, #0
						{'name':'in_phy_port', 'type':''}, #1
						{'name':'metadata', 'type':''}, #2
						{'name':'eth_dst', 'type':''}, #3
						{'name':'eth_src', 'type':''}, #4
						{'name':'eth_type', 'type':''}, #5
						{'name':'vlan_vid', 'type':'','range':'[[0x0,0x0],[0x1000,0x1fff]]'}, #6
						{'name':'vlan_pcp','type':'','range':'[[0x0,0x7]]'}, #7
						{'name':'ip_dscp', 'type':'','range':'[[0x0,0x3f]]'}, #8
						{'name':'ip_ecn', 'type':'','range':'[[0x0,0x3]]'}, #9
						{'name':'ip_proto', 'type':''}, #10
						{'name':'ipv4_src', 'type':''}, #11
						{'name':'ipv4_dst', 'type':''}, #12
						{'name':'tcp_src', 'type':''}, #13
						{'name':'tcp_dst', 'type':''}, #14
						{'name':'udp_src', 'type':''}, #15
						{'name':'udp_dst', 'type':''}, #16
						{'name':'sctp_src', 'type':''}, #17
						{'name':'sctp_dst', 'type':''}, #18
						{'name':'icmpv4_type', 'type':''}, #19
						{'name':'icmpv4_code', 'type':''}, #20
						{'name':'arp_op', 'type':''}, #21
						{'name':'arp_spa', 'type':''}, #22
						{'name':'arp_tpa', 'type':''}, #23
						{'name':'arp_sha', 'type':''}, #24
						{'name':'arp_tha', 'type':''}, #25
						{'name':'ipv6_src','type':''}, #26
						{'name':'ipv6_dst', 'type':''}, #27
						{'name':'ipv6_flabel', 'type':''}, #28
						{'name':'icmpv6_type', 'type':''}, #29
						{'name':'icmpv6_code', 'type':''}, #30
						{'name':'ipv6_nd_target', 'type':''}, #31
						{'name':'ipv6_nd_sll', 'type':''}, #32
						{'name':'ipv6_nd_tll', 'type':''}, #33
						{'name':'mpls_label', 'type':''},	#34
						{'name':'mpls_tc', 'type':''},	#35
						{'name':'mpls_bos', 'type':''}, #36
						{'name':'pbb_isid', 'impl':False, 'type':''}, #37
						{'name':'tunnel_id', 'type':''},	#38
						{'name':'ipv6_exthdr', 'type':''}, #39
					]}
				]}, #12
				{'name':'table_feature_prop_write_setfield_miss','impl':False, 'fields':[
					{'name':'oxm_ids','type':'list','fields':[
						# realate to match oxm , but parameter = null
						{'name':'in_port', 'type':''}, #0
						{'name':'in_phy_port', 'type':''}, #1
						{'name':'metadata', 'type':''}, #2
						{'name':'eth_dst', 'type':''}, #3
						{'name':'eth_src', 'type':''}, #4
						{'name':'eth_type', 'type':''}, #5
						{'name':'vlan_vid', 'type':'','range':'[[0x0,0x0],[0x1000,0x1fff]]'}, #6
						{'name':'vlan_pcp','type':'','range':'[[0x0,0x7]]'}, #7
						{'name':'ip_dscp', 'type':'','range':'[[0x0,0x3f]]'}, #8
						{'name':'ip_ecn', 'type':'','range':'[[0x0,0x3]]'}, #9
						{'name':'ip_proto', 'type':''}, #10
						{'name':'ipv4_src', 'type':''}, #11
						{'name':'ipv4_dst', 'type':''}, #12
						{'name':'tcp_src', 'type':''}, #13
						{'name':'tcp_dst', 'type':''}, #14
						{'name':'udp_src', 'type':''}, #15
						{'name':'udp_dst', 'type':''}, #16
						{'name':'sctp_src', 'type':''}, #17
						{'name':'sctp_dst', 'type':''}, #18
						{'name':'icmpv4_type', 'type':''}, #19
						{'name':'icmpv4_code', 'type':''}, #20
						{'name':'arp_op', 'type':''}, #21
						{'name':'arp_spa', 'type':''}, #22
						{'name':'arp_tpa', 'type':''}, #23
						{'name':'arp_sha', 'type':''}, #24
						{'name':'arp_tha', 'type':''}, #25
						{'name':'ipv6_src','type':''}, #26
						{'name':'ipv6_dst', 'type':''}, #27
						{'name':'ipv6_flabel', 'type':''}, #28
						{'name':'icmpv6_type', 'type':''}, #29
						{'name':'icmpv6_code', 'type':''}, #30
						{'name':'ipv6_nd_target', 'type':''}, #31
						{'name':'ipv6_nd_sll', 'type':''}, #32
						{'name':'ipv6_nd_tll', 'type':''}, #33
						{'name':'mpls_label', 'type':''},	#34
						{'name':'mpls_tc', 'type':''},	#35
						{'name':'mpls_bos', 'type':''}, #36
						{'name':'pbb_isid', 'impl':False, 'type':''}, #37
						{'name':'tunnel_id', 'type':''},	#38
						{'name':'ipv6_exthdr', 'type':''}, #39
					]}
				]}, #13
				{'name':'table_feature_prop_apply_setfield', 'impl':False,'fields':[
					{'name':'oxm_ids','type':'list','fields':[
						# realate to match oxm , but parameter = null
						{'name':'in_port', 'type':''}, #0
						{'name':'in_phy_port', 'type':''}, #1
						{'name':'metadata', 'type':''}, #2
						{'name':'eth_dst', 'type':''}, #3
						{'name':'eth_src', 'type':''}, #4
						{'name':'eth_type', 'type':''}, #5
						{'name':'vlan_vid', 'type':'','range':'[[0x0,0x0],[0x1000,0x1fff]]'}, #6
						{'name':'vlan_pcp','type':'','range':'[[0x0,0x7]]'}, #7
						{'name':'ip_dscp', 'type':'','range':'[[0x0,0x3f]]'}, #8
						{'name':'ip_ecn', 'type':'','range':'[[0x0,0x3]]'}, #9
						{'name':'ip_proto', 'type':''}, #10
						{'name':'ipv4_src', 'type':''}, #11
						{'name':'ipv4_dst', 'type':''}, #12
						{'name':'tcp_src', 'type':''}, #13
						{'name':'tcp_dst', 'type':''}, #14
						{'name':'udp_src', 'type':''}, #15
						{'name':'udp_dst', 'type':''}, #16
						{'name':'sctp_src', 'type':''}, #17
						{'name':'sctp_dst', 'type':''}, #18
						{'name':'icmpv4_type', 'type':''}, #19
						{'name':'icmpv4_code', 'type':''}, #20
						{'name':'arp_op', 'type':''}, #21
						{'name':'arp_spa', 'type':''}, #22
						{'name':'arp_tpa', 'type':''}, #23
						{'name':'arp_sha', 'type':''}, #24
						{'name':'arp_tha', 'type':''}, #25
						{'name':'ipv6_src','type':''}, #26
						{'name':'ipv6_dst', 'type':''}, #27
						{'name':'ipv6_flabel', 'type':''}, #28
						{'name':'icmpv6_type', 'type':''}, #29
						{'name':'icmpv6_code', 'type':''}, #30
						{'name':'ipv6_nd_target', 'type':''}, #31
						{'name':'ipv6_nd_sll', 'type':''}, #32
						{'name':'ipv6_nd_tll', 'type':''}, #33
						{'name':'mpls_label', 'type':''},	#34
						{'name':'mpls_tc', 'type':''},	#35
						{'name':'mpls_bos', 'type':''}, #36
						{'name':'pbb_isid', 'impl':False, 'type':''}, #37
						{'name':'tunnel_id', 'type':''},	#38
						{'name':'ipv6_exthdr', 'type':''}, #39
					]}
				]}, #14
				{'name':'table_feature_prop_apply_setfield_miss', 'impl':False,'fields':[
					{'name':'oxm_ids','type':'list','fields':[
						# realate to match oxm , but parameter = null
						{'name':'in_port', 'type':''}, #0
						{'name':'in_phy_port', 'type':''}, #1
						{'name':'metadata', 'type':''}, #2
						{'name':'eth_dst', 'type':''}, #3
						{'name':'eth_src', 'type':''}, #4
						{'name':'eth_type', 'type':''}, #5
						{'name':'vlan_vid', 'type':'','range':'[[0x0,0x0],[0x1000,0x1fff]]'}, #6
						{'name':'vlan_pcp','type':'','range':'[[0x0,0x7]]'}, #7
						{'name':'ip_dscp', 'type':'','range':'[[0x0,0x3f]]'}, #8
						{'name':'ip_ecn', 'type':'','range':'[[0x0,0x3]]'}, #9
						{'name':'ip_proto', 'type':''}, #10
						{'name':'ipv4_src', 'type':''}, #11
						{'name':'ipv4_dst', 'type':''}, #12
						{'name':'tcp_src', 'type':''}, #13
						{'name':'tcp_dst', 'type':''}, #14
						{'name':'udp_src', 'type':''}, #15
						{'name':'udp_dst', 'type':''}, #16
						{'name':'sctp_src', 'type':''}, #17
						{'name':'sctp_dst', 'type':''}, #18
						{'name':'icmpv4_type', 'type':''}, #19
						{'name':'icmpv4_code', 'type':''}, #20
						{'name':'arp_op', 'type':''}, #21
						{'name':'arp_spa', 'type':''}, #22
						{'name':'arp_tpa', 'type':''}, #23
						{'name':'arp_sha', 'type':''}, #24
						{'name':'arp_tha', 'type':''}, #25
						{'name':'ipv6_src','type':''}, #26
						{'name':'ipv6_dst', 'type':''}, #27
						{'name':'ipv6_flabel', 'type':''}, #28
						{'name':'icmpv6_type', 'type':''}, #29
						{'name':'icmpv6_code', 'type':''}, #30
						{'name':'ipv6_nd_target', 'type':''}, #31
						{'name':'ipv6_nd_sll', 'type':''}, #32
						{'name':'ipv6_nd_tll', 'type':''}, #33
						{'name':'mpls_label', 'type':''},	#34
						{'name':'mpls_tc', 'type':''},	#35
						{'name':'mpls_bos', 'type':''}, #36
						{'name':'pbb_isid', 'impl':False, 'type':''}, #37
						{'name':'tunnel_id', 'type':''},	#38
						{'name':'ipv6_exthdr', 'type':''}, #39
					]}
				]}, #15
				{'name':'table_feature_prop_experimenter', 'impl':False,'fields':[]}, #fffe
				{'name':'table_feature_prop_experimenter_miss', 'impl':False,'fields':[]}, #ffff
			]}
		]}
	]}
	# {'name':'entries', 'type':'list', 'fields':[
	# 	{'name':'table_feature_prop_instructions','fields':[
	# 		{'name':'instruction_ids','type':'list', 'fields':[
	# 			{'name':'instruction_id','fields':[
	# 				{'name':'type', 'type':'uint16'}
	# 			]}
	# 		]}
	# 	]},#0
	# 	{'name':'table_feature_prop_instructions_miss','fields':[
	# 		{'name':'instruction_ids','type':'list', 'fields':[
	# 			{'name':'instruction_id','fields':[
	# 				{'name':'type', 'type':'uint16'}
	# 			]}
	# 		]}
	# 	]},#1
	# 	{'name':'table_feature_prop_next_tables','fields':[
	# 		{'name':'next_table_ids','type':'list', 'fields':[
	# 			{'name':'instruction_id','fields':[
	# 				{'name':'type', 'type':'uint16'}
	# 			]}
	# 		]}
	# 	]},#2
	# 	{'name':'table_feature_prop_next_tables_miss',},#3
	# 	{'name':'table_feature_prop_write_actions',},#4
	# 	{'name':'table_feature_prop_write_actions_miss',},#5
	# 	{'name':'table_feature_prop_apply_actions',},#6
	# 	{'name':'table_feature_prop_apply_actions_miss',},#7
	# 	{'name':'table_feature_prop_match',},#8
	# 	{'name':'table_feature_prop_wildcards',},#10
	# 	{'name':'table_feature_prop_write_setfield',},#12
	# 	{'name':'table_feature_prop_write_setfield_miss',},#13
	# 	{'name':'table_feature_prop_apply_setfield',},#14
	# 	{'name':'table_feature_prop_apply_setfield_miss',},#15
	# 	{'name':'table_feature_prop_experimenter',},#fffe
	# 	{'name':'table_feature_prop_experimenter_miss',},#ffff
	# ]}
	# {'name':'entries', 'fields':[
	# 	{'name':'element','type':'list', 'fields':[
	# 		{'name':'table_id', 'type':'uint8'},
	# 		{'name':'name', 'impl':False},
	# 		{'name':'metadata_match', 'type':'uint64'},
	# 		{'name':'matadata_write', 'type':'uint64'},
	# 		{'name':'config', 'type':'uint32'},
	# 		{'name':'max_entries', 'type':'uint32'},
	# 		{'name':'properties','impl':False,'fields':[
	# 			##TODO: This Handling is bad
	# 			{'name':'element','type':'TLV', 'max':14,'fields':[
	# 				{'name':'ids','impl':False,'fields':[
	# 					##TODO: This Handling is bad
	# 					{'name':'element','type':'TLV', 'fields':[
	# 						{'name':'field', 'type':'uint32'},
	# 					]},
	# 				]},
	# 			]},
	# 		]},
	# 	]},
	# ]},
]

fields_of_table_mod = [
	{'name':'version', 'type':'uint8'},
	{'name':'type', 'type':'uint8'},
	{'name':'length', 'type':'uint16'},
	{'name':'xid', 'type':'uint32'},
	{'name':'table_id', 'type':'uint8'},
	{'name':'config', 'type':'uint32'},
	# {'name':'properties','fields':[
	# 	##TODO: This Handling is bad
	# 	{'name':'element','type':'TLV', 'max':2,'fields':[
	# 		{'name':'vancancy_down', 'type':'uint8'},
	# 		{'name':'vancancy_up', 'type':'uint8'},
	# 		{'name':'vancancy_get', 'type':'uint8'},
	# 	]},
	# ]},
]

fields_of_table_mod_failed_error_msg = [
	{'name':'version', 'type':'uint8'},
	{'name':'type', 'type':'uint8'},
	{'name':'length', 'type':'uint16'},
	{'name':'xid', 'type':'uint32'},
	{'name':'code', 'type':'uint16'},
	{'name':'data', 'impl':False},
]

fields_of_table_stats_reply = [
	{'name':'version', 'type':'uint8'},
	{'name':'type', 'type':'uint8'},
	{'name':'length', 'type':'uint16'},
	{'name':'xid', 'type':'uint32'},
	{'name':'flags', 'type':'uint16'},
	{'name':'entries','type':'list','fields':[
		{'name':'table_stats_entry','fields':[
			{'name':'table_id', 'type':'uint8'},
			{'name':'active_count', 'type':'uint32'},
			{'name':'lookup_count', 'type':'uint64'},
			{'name':'matched_count', 'type':'uint64'},
		]}
	]}
	# {'name':'entries', 'fields':[
	# 	{'name':'element','type':'list', 'fields':[
	# 		{'name':'table_id', 'type':'uint8'},
	# 		{'name':'active_count', 'type':'uint32'},
	# 		{'name':'lookup_count', 'type':'uint64'},
	# 		{'name':'matched_count', 'type':'uint64'},
	# 		{'name':'name', 'impl':False},
	# 		{'name':'match', 'type':'uint64'},
	# 		{'name':'wildcards', 'type':'uint64'},
	# 		{'name':'write_actions', 'type':'uint32'},
	# 		{'name':'apply_actions', 'type':'uint32'},
	# 		{'name':'write_setfields', 'type':'uint64'},
	# 		{'name':'apply_setfields', 'type':'uint64'},
	# 		{'name':'metadata_match', 'type':'uint64'},
	# 		{'name':'metadata_write', 'type':'uint64'},
	# 		{'name':'instructions', 'type':'uint32'},
	# 		{'name':'config', 'type':'uint32'},
	# 		{'name':'max_entries', 'type':'uint32'},
	# 	]},
	# ]},
]

fields_of_table_stats_request = [
	{'name':'version', 'type':'uint8'},
	{'name':'type', 'type':'uint8'},
	{'name':'length', 'type':'uint16'},
	{'name':'xid', 'type':'uint32'},
	{'name':'flags', 'type':'uint16'},
]

fields_of_table_status = [
	{'name':'version', 'type':'uint8'},
	{'name':'type', 'type':'uint8'},
	{'name':'length', 'type':'uint16'},
	{'name':'xid', 'type':'uint32'},
	{'name':'role', 'type':'uint32','range':'[[0x1,0x4]]'},
	{'name':'reason', 'type':'uint8'},
	{'name':'table', 'type':'uint8'},
]

fields_of_nicira_controller_role_reply = [
	{'name':'version', 'type':'uint8'},
	{'name':'type', 'type':'uint8'},
	{'name':'length', 'type':'uint16'},
	{'name':'xid', 'type':'uint32'},
	{'name':'experimenter', 'type':'uint32'},
	{'name':'subtype', 'type':'uint32'},
	{'name':'role', 'type':'uint32','range':'[[0x1,0x4]]'},
]

fields_of_nicira_controller_role_request = [
	{'name':'version', 'type':'uint8'},
	{'name':'type', 'type':'uint8'},
	{'name':'length', 'type':'uint16'},
	{'name':'xid', 'type':'uint32'},
	{'name':'experimenter', 'type':'uint32'},
	{'name':'subtype', 'type':'uint32'},
	{'name':'role', 'type':'uint32','range':'[[0x1,0x4]]'},
]

openflow = [
	['of_aggregate_stats_reply', fields_of_aggregate_stats_reply],
	['of_aggregate_stats_request', fields_of_aggregate_stats_request],
	['of_async_config_failed_error_msg', fields_of_async_get_reply],
	['of_async_get_reply', fields_of_async_get_reply],
	['of_async_get_request', fields_of_async_get_request],
	['of_async_set', fields_of_async_set],
	['of_bad_action_error_msg', fields_of_bad_action_error_msg],
	['of_bad_instruction_error_msg', fields_of_bad_instruction_error_msg],
	['of_bad_match_error_msg', fields_of_bad_match_error_msg],
	['of_bad_property_error_msg', fields_of_bad_property_error_msg],
	['of_bad_request_error_msg', fields_of_bad_request_error_msg],
	['of_barrier_reply', fields_of_barrier_reply],
	['of_barrier_request', fields_of_barrier_request],
	['of_bundle_add_msg', fields_of_bundle_add_msg],
	['of_bundle_ctrl_msg', fields_of_bundle_ctrl_msg],
	['of_bundle_failed_error_msg', fields_of_bundle_failed_error_msg],
	['of_desc_stats_reply', fields_of_desc_stats_reply],
	['of_desc_stats_request', fields_of_desc_stats_request],
	['of_echo_reply', fields_of_echo_reply],
	['of_echo_request', fields_of_echo_request],
	['of_experimenter', fields_of_experimenter],
	['of_experimenter_error_msg', fields_of_experimenter_error_msg],
	['of_experimenter_stats_reply', fields_of_experimenter_stats_reply],
	['of_experimenter_stats_request', fields_of_experimenter_stats_request],
	['of_features_reply', fields_of_features_reply],
	['of_features_request', fields_of_features_request],
	['of_flow_add', fields_of_flow_add],
	['of_flow_delete', fields_of_flow_delete],
	['of_flow_delete_strict', fields_of_flow_delete_strict],
	['of_flow_mod_failed_error_msg', fields_of_flow_mod_failed_error_msg],
	['of_flow_modify', fields_of_flow_modify],
	['of_flow_modify_strict', fields_of_flow_modify_strict],
	['of_flow_monitor_failed_error_msg', fields_of_flow_monitor_failed_error_msg],
	['of_flow_removed', fields_of_flow_removed],
	['of_flow_stats_reply', fields_of_flow_stats_reply],
	['of_flow_stats_request', fields_of_flow_stats_request],
	['of_get_config_reply', fields_of_get_config_reply],
	['of_get_config_request', fields_of_get_config_request],
	['of_group_add', fields_of_group_add],
	['of_group_delete', fields_of_group_delete],
	['of_group_desc_stats_reply', fields_of_group_desc_stats_reply],
	['of_group_desc_stats_request', fields_of_group_desc_stats_request],
	['of_group_features_stats_reply', fields_of_group_features_stats_reply],
	['of_group_features_stats_request', fields_of_group_features_stats_request],
	['of_group_mod_failed_error_msg', fields_of_group_mod_failed_error_msg],
	['of_group_modify', fields_of_group_modify],
	['of_group_stats_reply', fields_of_group_stats_reply],
	['of_group_stats_request', fields_of_group_stats_request],
	['of_hello', fields_of_hello],
	['of_hello_failed_error_msg', fields_of_hello_failed_error_msg],
	['of_meter_config_stats_reply', fields_of_meter_config_stats_reply],
	['of_meter_config_stats_request', fields_of_meter_config_stats_request],
	['of_meter_features_stats_reply', fields_of_meter_features_stats_reply],
	['of_meter_features_stats_request', fields_of_meter_features_stats_request],
	['of_meter_mod', fields_of_meter_mod],
	['of_meter_mod_failed_error_msg', fields_of_meter_mod_failed_error_msg],
	['of_meter_stats_reply', fields_of_meter_stats_reply],
	['of_meter_stats_request', fields_of_meter_stats_request],
	['of_packet_in', fields_of_packet_in],
	['of_packet_out', fields_of_packet_out],
	['of_port_desc_stats_reply', fields_of_port_desc_stats_reply],
	['of_port_desc_stats_request', fields_of_port_desc_stats_request],
	['of_port_mod', fields_of_port_mod],
	['of_port_mod_failed_error_msg', fields_of_port_mod_failed_error_msg],
	['of_port_stats_reply', fields_of_port_stats_reply],
	['of_port_stats_request', fields_of_port_stats_request],
	['of_port_status', fields_of_port_status],
	# ['of_queue_desc_stats_reply', fields_of_queue_desc_stats_reply],
	# ['of_queue_desc_stats_request', fields_of_queue_desc_stats_request],
	['of_queue_get_config_reply', fields_of_queue_get_config_reply],
	['of_queue_get_config_request', fields_of_queue_get_config_request],
	['of_queue_op_failed_error_msg', fields_of_queue_op_failed_error_msg],
	['of_queue_stats_reply', fields_of_queue_stats_reply],
	['of_queue_stats_request', fields_of_queue_stats_request],
	['of_requestforward', fields_of_requestforward],
	['of_role_reply', fields_of_role_reply],
	['of_role_request', fields_of_role_request],
	['of_role_request_failed_error_msg', fields_of_role_request_failed_error_msg],
	['of_role_status', fields_of_role_status],
	['of_set_config', fields_of_set_config],
	['of_switch_config_failed_error_msg', fields_of_switch_config_failed_error_msg],
	# ['of_table_desc_stats_reply', fields_of_table_desc_stats_reply],
	# ['of_table_desc_stats_request', fields_of_table_desc_stats_request],
	['of_table_features_failed_error_msg', fields_of_table_features_failed_error_msg],
	['of_table_features_stats_reply', fields_of_table_features_stats_reply],
	['of_table_features_stats_request', fields_of_table_features_stats_request],
	['of_table_mod', fields_of_table_mod],
	['of_table_mod_failed_error_msg', fields_of_table_mod_failed_error_msg],
	['of_table_stats_reply', fields_of_table_stats_reply],
	['of_table_stats_request', fields_of_table_stats_request],
	['of_table_status', fields_of_table_status],
	['of_nicira_controller_role_reply', fields_of_nicira_controller_role_reply],
	['of_nicira_controller_role_request', fields_of_nicira_controller_role_request],
]


openflow_13 = [
	['of_aggregate_stats_reply', fields_of_aggregate_stats_reply],
	['of_aggregate_stats_request', fields_of_aggregate_stats_request],
	['of_async_get_reply', fields_of_async_get_reply],
	['of_async_get_request', fields_of_async_get_request],
	['of_async_set', fields_of_async_set],
	['of_barrier_reply', fields_of_barrier_reply],
	['of_barrier_request', fields_of_barrier_request],
	['of_desc_stats_reply', fields_of_desc_stats_reply],
	['of_desc_stats_request', fields_of_desc_stats_request],
	['of_echo_reply', fields_of_echo_reply],
	['of_echo_request', fields_of_echo_request],
	['of_features_reply', fields_of_features_reply],
	['of_features_request', fields_of_features_request],
	['of_flow_add', fields_of_flow_add],
	['of_flow_delete', fields_of_flow_delete],
	['of_flow_delete_strict', fields_of_flow_delete_strict],
	['of_flow_modify', fields_of_flow_modify],
	['of_flow_modify_strict', fields_of_flow_modify_strict],
	['of_flow_removed', fields_of_flow_removed],
	['of_flow_stats_reply', fields_of_flow_stats_reply],
	['of_flow_stats_request', fields_of_flow_stats_request],
	['of_get_config_reply', fields_of_get_config_reply],
	['of_get_config_request', fields_of_get_config_request],
	['of_group_add', fields_of_group_add],
	['of_group_delete', fields_of_group_delete],
	['of_group_desc_stats_reply', fields_of_group_desc_stats_reply],
	['of_group_desc_stats_request', fields_of_group_desc_stats_request],
	['of_group_features_stats_reply', fields_of_group_features_stats_reply],
	['of_group_features_stats_request', fields_of_group_features_stats_request],
	['of_group_modify', fields_of_group_modify],
	['of_group_stats_reply', fields_of_group_stats_reply],
	['of_group_stats_request', fields_of_group_stats_request],
	['of_hello', fields_of_hello],
	['of_meter_config_stats_reply', fields_of_meter_config_stats_reply],
	['of_meter_config_stats_request', fields_of_meter_config_stats_request],
	['of_meter_features_stats_reply', fields_of_meter_features_stats_reply],
	['of_meter_features_stats_request', fields_of_meter_features_stats_request],
	['of_meter_mod', fields_of_meter_mod],
	['of_meter_stats_reply', fields_of_meter_stats_reply],
	['of_meter_stats_request', fields_of_meter_stats_request],
	['of_packet_in', fields_of_packet_in],
	['of_packet_out', fields_of_packet_out],
	['of_port_desc_stats_reply', fields_of_port_desc_stats_reply],
	['of_port_desc_stats_request', fields_of_port_desc_stats_request],
	['of_port_mod', fields_of_port_mod],
	['of_port_stats_reply', fields_of_port_stats_reply],
	['of_port_stats_request', fields_of_port_stats_request],
	['of_port_status', fields_of_port_status],
	# ['of_queue_desc_stats_reply', fields_of_queue_desc_stats_reply],
	# ['of_queue_desc_stats_request', fields_of_queue_desc_stats_request],
	['of_queue_get_config_reply', fields_of_queue_get_config_reply],
	['of_queue_get_config_request', fields_of_queue_get_config_request],
	['of_queue_stats_reply', fields_of_queue_stats_reply],
	['of_queue_stats_request', fields_of_queue_stats_request],
	['of_role_reply', fields_of_role_reply],
	['of_role_request', fields_of_role_request],
	['of_set_config', fields_of_set_config],
	# ['of_table_desc_stats_reply', fields_of_table_desc_stats_reply],
	# ['of_table_desc_stats_request', fields_of_table_desc_stats_request],
	['of_table_features_stats_reply', fields_of_table_features_stats_reply],
	['of_table_features_stats_request', fields_of_table_features_stats_request],
	['of_table_mod', fields_of_table_mod],
	['of_table_stats_reply', fields_of_table_stats_reply],
	['of_table_stats_request', fields_of_table_stats_request],
]

openflow_13_occur = [
	['of_aggregate_stats_reply', fields_of_aggregate_stats_reply],
	['of_async_get_reply', fields_of_async_get_reply],
	['of_barrier_reply', fields_of_barrier_reply],
	['of_desc_stats_reply', fields_of_desc_stats_reply],
	['of_echo_reply', fields_of_echo_reply],
	['of_echo_request', fields_of_echo_request],
	['of_features_reply', fields_of_features_reply],
	['of_flow_removed', fields_of_flow_removed],
	['of_flow_stats_reply', fields_of_flow_stats_reply],
	['of_get_config_reply', fields_of_get_config_reply],
	['of_group_desc_stats_reply', fields_of_group_desc_stats_reply],
	['of_group_features_stats_reply', fields_of_group_features_stats_reply],
	['of_group_stats_reply', fields_of_group_stats_reply],
	['of_hello', fields_of_hello],
	['of_meter_config_stats_reply', fields_of_meter_config_stats_reply],
	['of_meter_features_stats_reply', fields_of_meter_features_stats_reply],
	['of_meter_stats_reply', fields_of_meter_stats_reply],
	['of_packet_in', fields_of_packet_in],
	['of_port_desc_stats_reply', fields_of_port_desc_stats_reply],
	['of_port_stats_reply', fields_of_port_stats_reply],
	['of_port_status', fields_of_port_status],
	# ['of_queue_desc_stats_reply', fields_of_queue_desc_stats_reply],
	['of_queue_get_config_reply', fields_of_queue_get_config_reply],
	['of_queue_stats_reply', fields_of_queue_stats_reply],
	['of_role_reply', fields_of_role_reply],
	# ['of_table_desc_stats_reply', fields_of_table_desc_stats_reply],
	['of_table_features_stats_reply', fields_of_table_features_stats_reply],
	['of_table_stats_reply', fields_of_table_stats_reply],
]

openflow_13_build = [
	['of_aggregate_stats_reply', fields_of_aggregate_stats_reply],
	['of_aggregate_stats_request', fields_of_aggregate_stats_request],
	['of_async_get_reply', fields_of_async_get_reply],
	['of_async_get_request', fields_of_async_get_request],
	['of_async_set', fields_of_async_set],
	['of_barrier_reply', fields_of_barrier_reply],
	['of_barrier_request', fields_of_barrier_request],
	['of_desc_stats_reply', fields_of_desc_stats_reply],
	['of_desc_stats_request', fields_of_desc_stats_request],
	['of_echo_reply', fields_of_echo_reply],
	['of_echo_request', fields_of_echo_request],
	['of_features_reply', fields_of_features_reply],
	['of_features_request', fields_of_features_request],
	['of_flow_add', fields_of_flow_add],
	['of_flow_delete', fields_of_flow_delete],
	['of_flow_delete_strict', fields_of_flow_delete_strict],
	['of_flow_modify', fields_of_flow_modify],
	['of_flow_modify_strict', fields_of_flow_modify_strict],
	['of_flow_removed', fields_of_flow_removed],
	['of_flow_stats_reply', fields_of_flow_stats_reply],
	['of_flow_stats_request', fields_of_flow_stats_request],
	['of_get_config_reply', fields_of_get_config_reply],
	['of_get_config_request', fields_of_get_config_request],
	['of_group_add', fields_of_group_add],
	['of_group_delete', fields_of_group_delete],
	['of_group_desc_stats_reply', fields_of_group_desc_stats_reply],
	['of_group_desc_stats_request', fields_of_group_desc_stats_request],
	['of_group_features_stats_reply', fields_of_group_features_stats_reply],
	['of_group_features_stats_request', fields_of_group_features_stats_request],
	['of_group_modify', fields_of_group_modify],
	['of_group_stats_reply', fields_of_group_stats_reply],
	['of_group_stats_request', fields_of_group_stats_request],
	['of_hello', fields_of_hello],
	['of_meter_config_stats_reply', fields_of_meter_config_stats_reply],
	['of_meter_config_stats_request', fields_of_meter_config_stats_request],
	['of_meter_features_stats_reply', fields_of_meter_features_stats_reply],
	['of_meter_features_stats_request', fields_of_meter_features_stats_request],
	['of_meter_mod', fields_of_meter_mod],
	['of_meter_mod_failed_error_msg', fields_of_meter_mod_failed_error_msg],
	['of_meter_stats_reply', fields_of_meter_stats_reply],
	['of_meter_stats_request', fields_of_meter_stats_request],
	['of_packet_in', fields_of_packet_in],
	['of_packet_out', fields_of_packet_out],
	['of_port_desc_stats_reply', fields_of_port_desc_stats_reply],
	['of_port_desc_stats_request', fields_of_port_desc_stats_request],
	['of_port_mod', fields_of_port_mod],
	['of_port_stats_reply', fields_of_port_stats_reply],
	['of_port_stats_request', fields_of_port_stats_request],
	['of_port_status', fields_of_port_status],
	# ['of_queue_desc_stats_reply', fields_of_queue_desc_stats_reply],
	# ['of_queue_desc_stats_request', fields_of_queue_desc_stats_request],
	['of_queue_get_config_reply', fields_of_queue_get_config_reply],
	['of_queue_get_config_request', fields_of_queue_get_config_request],
	['of_queue_stats_reply', fields_of_queue_stats_reply],
	['of_queue_stats_request', fields_of_queue_stats_request],
	['of_role_reply', fields_of_role_reply],
	['of_role_request', fields_of_role_request],
	['of_set_config', fields_of_set_config],
	# ['of_table_desc_stats_reply', fields_of_table_desc_stats_reply],
	# ['of_table_desc_stats_request', fields_of_table_desc_stats_request],
	['of_table_features_stats_reply', fields_of_table_features_stats_reply],
	['of_table_features_stats_request', fields_of_table_features_stats_request],
	['of_table_mod', fields_of_table_mod],
	['of_table_stats_reply', fields_of_table_stats_reply],
	['of_table_stats_request', fields_of_table_stats_request],
]

openflow_13_block =  [
	['of_packet_in', fields_of_packet_in],
	# not a list
	# ['of_port_status', fields_of_port_status],
	# not a list
	# ['of_desc_stats_reply', fields_of_desc_stats_reply],# 3.5.1
	['of_flow_stats_reply', fields_of_flow_stats_reply],# 3.5.2
	# ['of_aggregate_stats_reply', fields_of_aggregate_stats_reply],# 3.5.3
	# ['of_table_stats_reply', fields_of_table_stats_reply], # 3.5.4
	['of_port_stats_reply', fields_of_port_stats_reply], # 3.5.5
	# ['of_queue_stats_reply', fields_of_queue_stats_reply], # 3.5.6
	['of_group_stats_reply', fields_of_group_stats_reply], # 3.5.7
	['of_group_desc_stats_reply', fields_of_group_desc_stats_reply], # 3.5.8
	# ['of_group_features_stats_reply', fields_of_group_features_stats_reply], # 3.5.9
	['of_meter_stats_reply', fields_of_meter_stats_reply], # 3.5.10
	# ['of_meter_config_stats_reply', fields_of_meter_config_stats_reply], #3.5.11
	# not a list
	# ['of_meter_features_stats_reply', fields_of_meter_features_stats_reply], #3.5.12
	# ['of_table_features_stats_reply', fields_of_table_features_stats_reply], # 3.5.13
	['of_port_desc_stats_reply', fields_of_port_desc_stats_reply], # 3.5.14


]

ofp_packet_in_match = [
	{'name':'in_port', 'value':1 }
]

# ofp_match = [
# 	{'in_port':0xffffff01 },
# 	{'in_phy_port':0xffffff01 }
# ]

ofp_match = [
	{'name':'in_port', 'type':'uint32'},
	{'name':'in_phy_port', 'type':'uint32'},
	{'name':'eth_src', 'type':'list','value':[0x8e,0x8c,0x49,0x97,0xa6,0x36]},
	{'name':'eth_dst', 'type':'list','value':[0x56,0x75,0x6c,0xee,0x8c,0xf6]},
	{'name':'eth_type', 'type':'uint16'},
	{'name':'ip_proto', 'type':'uint8'}
]

ofp_instruction = [
	{'name':'goto_table', 'type':'uint8'},
	{'name':'meter', 'type':'uint32'},
	{'name':'group', 'type':'uint32'},
	{'name':'clear_actions', 'type':'uint32','value':None},
	{'name':'write_actions', 'type':'list'},
	{'name':'apply_actions', 'type':'list'}
]

port_desc = [
	{'name':'port_no', 'type':'uint16','range':'[[0x0,0xffffff00],[0xfffffff8,0xffffffff]]'},
	{'name':'hw_addr', 'type':'list'},
	{'name':'name', 'type':'uint128','value':"s1-eth5"},
	{'name':'config', 'type':'uint16'},
	{'name':'state', 'type':'uint16'},
	{'name':'curr', 'type':'uint16'},
	{'name':'advertised', 'type':'uint16'},
	{'name':'supported', 'type':'uint16'},
	{'name':'peer', 'type':'uint16'},
	{'name':'curr_speed', 'type':'uint16'},
	{'name':'max_speed', 'type':'uint16'}
]


# port_desc = {
# 	'port_no':0x02,
# 	'hw_addr':[0x1f,0x23,0x25,0xc7,0xb2,0xc4],
# 	'name':"s1-eth3", 
# 	'config':0x00000000,
# 	'state':0x00000004,
# 	'curr':0x00000840,
# 	'advertised':0x00,
# 	'supported':0x00,
# 	'peer':None,
# 	'curr_speed':None,
# 	'max_speed':0
# }

flow_stats_reply = [
	{'name':'table_id', 'type':'uint8','value':0},
	{'name':'duration_sec', 'type':'uint64','value':0},
	{'name':'duration_nsec', 'type':'uint64','value':0},
	{'name':'priority', 'type':'uint16'},
	{'name':'idle_timeout', 'type':'uint16'},
	{'name':'hard_timeout', 'type':'uint16'},
	{'name':'flags', 'type':'uint16'},
	{'name':'cookie', 'type':'uint32'},
	{'name':'packet_count', 'type':'uint64'},
	{'name':'byte_count', 'type':'uint64'},
	{'name':'match', 'type':'list'},
	{'name':'instructions','type':'list'}
]

table_stats_reply = [
	{'name':'table_id', 'type':'uint8'},
	{'name':'active_count', 'type':'uint32'},
	{'name':'lookup_count', 'type':'uint64'},
	{'name':'matched_count', 'type':'uint64'}
]

table_features_stats_reply =[
	{'name':'table_id', 'type':'uint8'},
	{'name':'name', 'type':'uint256','value':0x00000000},
	{'name':'metadata_match', 'type':'uint64','value':0xffffffffffffffff},
	{'name':'metadata_write', 'type':'uint64','value':0xffffffffffffffff},
	{'name':'config', 'type':'uint16','value':0x00000000},
	{'name':'max_entries', 'type':'uint16'},
	{'name':'properties', 'type':'list','value':[]},
]

port_stats_reply = [
	{'name':'port_no', 'type':'uint32','range':'[[0x0,0xffffff00],[0xfffffff8,0xffffffff]]'},
	{'name':'rx_packets', 'type':'uint64','value':0x0},
	{'name':'tx_packets', 'type':'uint64'},
	{'name':'rx_bytes', 'type':'uint64'},
	{'name':'tx_bytes', 'type':'uint64'},
	{'name':'rx_dropped', 'type':'uint64'},
	{'name':'tx_dropped', 'type':'uint64'},
	{'name':'rx_errors', 'type':'uint64'},
	{'name':'tx_errors', 'type':'uint64'},
	{'name':'rx_frame_err', 'type':'uint64'},
	{'name':'rx_over_err', 'type':'uint64'},
	{'name':'rx_crc_err', 'type':'uint64'},
	{'name':'collisions', 'type':'uint64'},
	{'name':'duration_sec', 'type':'uint32'},
	{'name':'duration_nsec', 'type':'uint32'}
]

queue_stats_reply = [
	{'name':'port_no', 'type':'uint32','range':'[[0x0,0xffffff00],[0xfffffff8,0xffffffff]]'},
	{'name':'queue_id', 'type':'uint32'},
	{'name':'tx_bytes', 'type':'uint64'},
	{'name':'tx_packet', 'type':'uint64'},
	{'name':'tx_errors', 'type':'uint64'},
	{'name':'duration_sec', 'type':'uint32'},
	{'name':'duration_nsec', 'type':'uint32'}
]

group_stats_reply = [
	{'name':'group_id', 'type':'uint32','range':'[[0x0,0xffffff00],[0xfffffffc,0xfffffffc],[0xffffffff,0xffffffff]]'},
	{'name':'ref_count', 'type':'uint32'},
	{'name':'packet_count', 'type':'uint64'},
	{'name':'byte_count', 'type':'uint64'},
	{'name':'duration_sec', 'type':'uint32'},
	{'name':'duration_nsec', 'type':'uint32'},
	{'name':'bucket_stats', 'type':'list'}
]

group_desc_stats_reply = [
	{'name':'group_type', 'type':'uint8','range':'[[0x0,0x03],[0xf0,0xff]]'},
	{'name':'group_id', 'type':'uint32','range':'[[0x0,0xffffff00],[0xfffffffc,0xfffffffc],[0xffffffff,0xffffffff]]'},
	{'name':'buckets', 'type':'list'},
]

meter_stats_reply = [ 
	{'name':'meter_id', 'type':'uint32','range':'[[0x0,0xffff0000],[0xfffffffd,0xffffffff]]'},
	{'name':'flow_count', 'type':'uint32'},
	{'name':' packet_in_count', 'type':'uint64'},
	{'name':'byte_in_count', 'type':'uint64'},
	{'name':'duration_sec', 'type':'uint32'},
	{'name':'duration_nsec', 'type':'uint32'},
	{'name':'band_stats', 'type':'list'}
]

meter_config_stats_reply = [
	{'name':'flags', 'type':'uint16'},
	{'name':'meter_id', 'type':'uint32','range':'[[0x0,0xffff0000],[0xfffffffd,0xffffffff]]'},
	{'name':' entries', 'type':'list'},
]

meter_features_stats_reply = [
	{'name':'max_meter', 'type':'uint32'},
	{'name':'band_types', 'type':'uint32'},
	{'name':'capabilities', 'type':'uint32'},
	{'name':'max_bands', 'type':'uint8'},
	{'name':'max_color', 'type':'uint8'},
]



block_field = {
	'of_packet_in':{'add_value': ofp_match },
	'of_port_status':{'add_value': port_desc},
	'of_flow_stats_reply':{'add_value': flow_stats_reply},
	'of_table_stats_reply':{'add_value': table_stats_reply},
	'of_table_features_stats_reply':{'add_value': table_features_stats_reply},
	'of_port_stats_reply':{'add_value': port_stats_reply}, 
	'of_port_desc_stats_reply':{'add_value': port_desc},
	'of_queue_stats_reply':{'add_value': queue_stats_reply},
	'of_group_stats_reply':{'add_value': group_stats_reply}, 
	'of_group_desc_stats_reply':{'add_value': group_desc_stats_reply}, 
	'of_meter_stats_reply':{'add_value': meter_stats_reply}, 
	'of_meter_config_stats_reply':{'add_value': meter_config_stats_reply},
	# 'of_meter_features_stats_reply':{'add_value': meter_features_stats_reply}, 
}


hw_addr_list = [0x1f,0x23,0x25,0xc7,0xb2,0xc4]