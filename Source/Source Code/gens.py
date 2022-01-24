# NS2 Script Generator
import os
import math
import datetime

activate_mal=False  # do we want malware node?
CNUMER = 10         # Total number of nodes in a cluster
run_time = 10.0     # Runtime in seconds


#Initialisation
if activate_mal:
    ns_file_name = "attack.tcl"
else:
    ns_file_name = "normal.tcl"
os.system("rm " + ns_file_name)  # to prevent overwriting

if activate_mal:
    trace_and_nam_file_name="attack_out"
else:
    trace_and_nam_file_name="normal_out"

tracefile_name = trace_and_nam_file_name+".tr"
namfile_name = trace_and_nam_file_name+".nam"


CLUSTER_ONE_NODE_POPULATION = CNUMER
CLUSTER_TWO_NODE_POPULATION = CNUMER
CLUSTER_THREE_NODE_POPULATION = CNUMER
CLUSTER_FOUR_NODE_POPULATION = CNUMER
CLUSTER_FIVE_NODE_POPULATION = CNUMER

cluster_one_node_list = []
cluster_two_node_list = []
cluster_three_node_list = []
cluster_four_node_list = []
wireless_cluster_five_node_list = []
malicious_node_list = []

cluster_one_name_suffix = "clusterone_node_"
cluster_two_name_suffix = "clustertwo_node_"
cluster_three_name_suffix = "clusterthree_node_"
cluster_four_name_suffix = "clusterfour_node_"
cluster_five_name_suffix = "clusterfive_node_"
malicious_node_name_suffix = "malicious_node_"

cluster_one_switch_node = "c1switch"
cluster_two_switch_node = "c2switch"
cluster_three_switch_node = "c3switch"
cluster_four_switch_node = "c4switch"
cluster_five_switch_node = "c5switch"

router1_node = "r1node"
router2_node = "r2node"
router3_node = "r3node"

# creating base setup

with open(ns_file_name, 'a') as ns_file:
    ns_file.write("""
#===================================    
# Simulation Script Generated by XSFM
#===================================
#     Simulation parameters setup
#===================================
set val(stop)   """ + str(run_time) + """                         ;# time of simulation end

#===================================
#        Initialization        
#===================================
#Create a ns simulator
set ns [new Simulator -multicast on]

#Open the NS trace file
set tracefile [open """ + tracefile_name + """ w]
$ns trace-all $tracefile

#Open the NAM trace file
set namfile [open """ + namfile_name + """ w]
$ns namtrace-all $namfile
    """)

## setting up nodes

# Cluster 1
for i in range(0, CLUSTER_ONE_NODE_POPULATION):
    cluster_one_node_list.append(str(cluster_one_name_suffix) + str(i))

# Cluster 2
for i in range(0, CLUSTER_TWO_NODE_POPULATION):
    cluster_two_node_list.append(str(cluster_two_name_suffix) + str(i))

# Cluster 3
for i in range(0, CLUSTER_THREE_NODE_POPULATION):
    cluster_three_node_list.append(str(cluster_three_name_suffix) + str(i))

# Cluster 4
for i in range(0, CLUSTER_FOUR_NODE_POPULATION):
    cluster_four_node_list.append(str(cluster_four_name_suffix) + str(i))

# Cluster 5
for i in range(0, CLUSTER_FIVE_NODE_POPULATION):
    wireless_cluster_five_node_list.append(str(cluster_five_name_suffix) + str(i))

# Malicious Node Def.

malicious_node_list.append(str(malicious_node_name_suffix) + str("1"))

# saving the node info in file

with open(ns_file_name, 'a') as nf:
    nf.write("""
#===================================
#        Nodes Definition        
#===================================\n""")

# router nodes
with open(ns_file_name, 'a') as nf:
    nf.write("set " + router1_node + " [$ns node]\n")
    nf.write("set " + router2_node + " [$ns node]\n")
    nf.write("set " + router3_node + " [$ns node]\n")
    nf.write("$" + router1_node + " label \"Router1\"\n")
    nf.write("$" + router2_node + " label \"Router2\"\n")
    nf.write("$" + router3_node + " label \"Router3\"\n")

# switch nodes
with open(ns_file_name, 'a') as nf:
    nf.write("set " + cluster_one_switch_node + " [$ns node]\n")
    nf.write("set " + cluster_two_switch_node + " [$ns node]\n")
    nf.write("set " + cluster_three_switch_node + " [$ns node]\n")
    nf.write("set " + cluster_four_switch_node + " [$ns node]\n")
    nf.write("set " + cluster_five_switch_node + " [$ns node]\n")

    nf.write("$" + cluster_one_switch_node + " label \"C1SW\"\n")
    nf.write("$" + cluster_two_switch_node + " label \"C2SW\"\n")
    nf.write("$" + cluster_three_switch_node + " label \"C3SW\"\n")
    nf.write("$" + cluster_four_switch_node + " label \"C4SW\"\n")
    nf.write("$" + cluster_five_switch_node + " label \"C5SW\"\n")

# cluster 1
c1i = 0
for node in cluster_one_node_list:
    with open(ns_file_name, 'a') as nf:
        nf.write("set " + node + " [$ns node]\n")
        nf.write("$" + node + " label \"C1N" + str(c1i) + "\" \n")
    c1i += 1

# cluster 2
c2i = 0
for node in cluster_two_node_list:
    with open(ns_file_name, 'a') as nf:
        nf.write("set " + node + " [$ns node]\n")
        nf.write("$" + node + " label \"C2N" + str(c2i) + "\" \n")
    c2i += 1
# cluster 3
c3i = 0
for node in cluster_three_node_list:
    with open(ns_file_name, 'a') as nf:
        nf.write("set " + node + " [$ns node]\n")
        nf.write("$" + node + " label \"C3N" + str(c3i) + "\" \n")
    c3i += 1
# cluster 4
c4i = 0
for node in cluster_four_node_list:
    with open(ns_file_name, 'a') as nf:
        nf.write("set " + node + " [$ns node]\n")
        nf.write("$" + node + " label \"C4N" + str(c4i) + "\" \n")
    c4i += 1
# cluster 5
c5i = 0
for node in wireless_cluster_five_node_list:
    with open(ns_file_name, 'a') as nf:
        nf.write("set " + node + " [$ns node]\n")
        nf.write("$" + node + " label \"C5N" + str(c5i) + "\" \n")
    c5i += 1

# malicious node write
if activate_mal:
    with open(ns_file_name, 'a') as nf:
        nf.write("set " + malicious_node_list[0] + " [$ns node]\n")
        nf.write("$" + malicious_node_list[0] + " label \"MALN1\" \n")

##Link Definition

with open(ns_file_name, 'a') as nf:
    nf.write("""
#===================================
#         Links Definition         
#===================================\n""")

# router_nodes interconnection
with open(ns_file_name, 'a') as nf:
    nf.write("$ns duplex-link $" + router1_node + " $" + router2_node + " 1000.0Mb 5ms DropTail\n")
    nf.write("$ns queue-limit $" + router1_node + " $" + router2_node + " 50\n")

    nf.write("$ns duplex-link $" + router1_node + " $" + router3_node + " 1000.0Mb 5ms DropTail\n")
    nf.write("$ns queue-limit $" + router1_node + " $" + router3_node + " 50\n")

    nf.write("$ns duplex-link $" + router2_node + " $" + router3_node + " 1000.0Mb 5ms DropTail\n")
    nf.write("$ns queue-limit $" + router2_node + " $" + router3_node + " 50\n")

# connecting switches
with open(ns_file_name, 'a') as nf:
    nf.write("$ns duplex-link $" + router1_node + " $" + cluster_one_switch_node + " 100.0Mb 10ms DropTail\n")
    nf.write("$ns queue-limit $" + router1_node + " $" + cluster_one_switch_node + " 50\n")

    nf.write("$ns duplex-link $" + router1_node + " $" + cluster_two_switch_node + " 100.0Mb 10ms DropTail\n")
    nf.write("$ns queue-limit $" + router1_node + " $" + cluster_two_switch_node + " 50\n")

    nf.write("$ns duplex-link $" + router2_node + " $" + cluster_three_switch_node + " 100.0Mb 10ms DropTail\n")
    nf.write("$ns queue-limit $" + router2_node + " $" + cluster_three_switch_node + " 50\n")

    nf.write("$ns duplex-link $" + router3_node + " $" + cluster_four_switch_node + " 100.0Mb 10ms DropTail\n")
    nf.write("$ns queue-limit $" + router3_node + " $" + cluster_four_switch_node + " 50\n")

    nf.write("$ns duplex-link $" + router3_node + " $" + cluster_five_switch_node + " 100.0Mb 10ms DropTail\n")
    nf.write("$ns queue-limit $" + router3_node + " $" + cluster_five_switch_node + " 50\n")

## Connecting Clusters
print("Connecting Clusters.")
## Cluster 1 connection
with open(ns_file_name, 'a') as nf:
    nf.write(
        "$ns duplex-link $" + cluster_one_switch_node + " $" + cluster_one_node_list[0] + " 200.0Mb 10ms DropTail\n")
    nf.write("$ns queue-limit $" + cluster_one_switch_node + " $" + cluster_one_node_list[0] + " 50\n")

with open(ns_file_name, 'a') as nf:
    for i in range(0, len(cluster_one_node_list)):
        nf.write("$ns duplex-link $" + cluster_one_node_list[0] + " $" + cluster_one_node_list[
            i] + " 100.0Mb 10ms DropTail\n")
        nf.write("$ns queue-limit $" + cluster_one_node_list[0] + " $" + cluster_one_node_list[i] + " 50\n")

## Cluster 2 connection
with open(ns_file_name, 'a') as nf:
    nf.write(
        "$ns duplex-link $" + cluster_two_switch_node + " $" + cluster_two_node_list[0] + " 200.0Mb 10ms DropTail\n")
    nf.write("$ns queue-limit $" + cluster_two_switch_node + " $" + cluster_two_node_list[0] + " 50\n")

with open(ns_file_name, 'a') as nf:
    for i in range(1, len(cluster_two_node_list)):
        nf.write("$ns duplex-link $" + cluster_two_node_list[i - 1] + " $" + cluster_two_node_list[
            i] + " 100.0Mb 10ms DropTail\n")
        nf.write("$ns queue-limit $" + cluster_two_node_list[i - 1] + " $" + cluster_two_node_list[i] + " 50\n")

with open(ns_file_name, 'a') as nf:
    nf.write(
        "$ns duplex-link $" + cluster_two_node_list[(len(cluster_two_node_list) - 1)] + " $" + cluster_two_node_list[
            0] + " 200.0Mb 10ms DropTail\n")
    nf.write(
        "$ns queue-limit $" + cluster_two_node_list[(len(cluster_two_node_list) - 1)] + " $" + cluster_two_node_list[
            0] + " 50\n")

## Cluster 3 connection (all directly to switch)

with open(ns_file_name, 'a') as nf:
    for i in range(0, len(cluster_three_node_list)):
        nf.write("$ns duplex-link $" + cluster_three_switch_node + " $" + cluster_three_node_list[
            i] + " 100.0Mb 10ms DropTail\n")
        nf.write("$ns queue-limit $" + cluster_three_switch_node + " $" + cluster_three_node_list[i] + " 50\n")

##Cluster 4 connection (two-part)

with open(ns_file_name, 'a') as nf:
    nf.write(
        "$ns duplex-link $" + cluster_four_switch_node + " $" + cluster_four_node_list[0] + " 200.0Mb 10ms DropTail\n")
    nf.write("$ns queue-limit $" + cluster_four_switch_node + " $" + cluster_four_node_list[0] + " 50\n")

# determine separation
with open(ns_file_name, 'a') as nf:
    for i in range(1, int(CLUSTER_FOUR_NODE_POPULATION // 2) + 1):
        nf.write("$ns duplex-link $" + cluster_four_node_list[0] + " $" + cluster_four_node_list[
            i] + " 200.0Mb 10ms DropTail\n")
        nf.write("$ns queue-limit $" + cluster_four_node_list[0] + " $" + cluster_four_node_list[i] + " 50\n")

    for i in range(int(CLUSTER_FOUR_NODE_POPULATION // 2) + 1, CLUSTER_FOUR_NODE_POPULATION):
        nf.write("$ns duplex-link $" + cluster_four_node_list[int(CLUSTER_FOUR_NODE_POPULATION // 2)] + " $" +
                 cluster_four_node_list[i] + " 200.0Mb 10ms DropTail\n")
        nf.write("$ns queue-limit $" + cluster_four_node_list[int(CLUSTER_FOUR_NODE_POPULATION // 2)] + " $" +
                 cluster_four_node_list[i] + " 50\n")

# # Cluster 5 connection (wireless) [Wired for now as we were having problems in connecting wireless with the asset.]

with open(ns_file_name, 'a') as nf:
    nf.write("$ns duplex-link $" + cluster_five_switch_node + " $" + wireless_cluster_five_node_list[
        0] + " 200.0Mb 10ms DropTail\n")
    nf.write("$ns queue-limit $" + cluster_five_switch_node + " $" + wireless_cluster_five_node_list[0] + " 50\n")

with open(ns_file_name, 'a') as nf:
    for i in range(0, len(wireless_cluster_five_node_list)):

        for j in range(i + 1, len(wireless_cluster_five_node_list)):
            if j == len(wireless_cluster_five_node_list):
                break
            else:
                nf.write(
                    "$ns duplex-link $" + wireless_cluster_five_node_list[i] + " $" + wireless_cluster_five_node_list[
                        j] + " 200.0Mb 10ms DropTail\n")
                nf.write(
                    "$ns queue-limit $" + wireless_cluster_five_node_list[i] + " $" + wireless_cluster_five_node_list[
                        j] + " 50\n")

            ## =============================================================================


# Adding Malicious Nodes here

if activate_mal:
    with open(ns_file_name, 'a') as nf:
        nf.write("$ns duplex-link $" + malicious_node_list[0] + " $" + cluster_five_switch_node + " 1.5Mb 20ms DropTail\n")
        nf.write("$ns queue-limit $" + malicious_node_list[0] + " $" + cluster_five_switch_node + " 50\n")

## =============================================================================

print("Setting Up NAM Coord")

# ##NAM coordinate setup (POS)
# with open(ns_file_name,'a') as nf:
#     nf.write("""
# #===================================
# #         Node Positions for NAM        
# #===================================\n""")


# with open(ns_file_name,'a') as nf:
#     nf.write("$"+router1_node+" set X_ 500\n")
#     nf.write("$"+router1_node+" set Y_ 500\n")
#     nf.write("$"+router1_node+" set Z_ 0.0\n")

#     nf.write("$"+router2_node+" set X_ 540\n")
#     nf.write("$"+router2_node+" set Y_ 460\n")
#     nf.write("$"+router2_node+" set Z_ 0.0\n")

#     nf.write("$"+router3_node+" set X_ 460\n")
#     nf.write("$"+router3_node+" set Y_ 460\n")
#     nf.write("$"+router3_node+" set Z_ 0.0\n")

#    #cluster1 mapping
#     nf.write("$"+cluster_one_switch_node+" set X_ 350\n")
#     nf.write("$"+cluster_one_switch_node+" set Y_ 650\n")
#     nf.write("$"+cluster_one_switch_node+" set Z_ 0.0\n")

#     c1x=350
#     c1y=650
#     gridcounter=0

#     for node in cluster_one_node_list:
#         c1x=c1x-50
#         if(gridcounter > 9):
#             gridcounter=0
#             c1x=350
#             c1y=c1y+50
#         nf.write("$"+node+" set X_ "+str(c1x)+"\n")
#         nf.write("$"+node+" set Y_ "+str(c1y)+"\n")
#         gridcounter=gridcounter+1

#     #cluster2 mapping
#     nf.write("$"+cluster_two_switch_node+" set X_ 650\n")
#     nf.write("$"+cluster_two_switch_node+" set Y_ 650\n")
#     nf.write("$"+cluster_two_switch_node+" set Z_ 0.0\n")


#     # nf.write("$"+cluster_two_node_list[0]+" set Y_ 580\n")
#     # nf.write("$"+cluster_two_node_list[0]+" set X_ 580\n")

#     # trying to create a ring topo formation
#     # arch fun
#     def point(centre_x, centre_y, radius,qval):
#         # print(q)
#         theta = qval * 2 * math.pi
#         return centre_x + math.cos(theta) * radius, centre_y + math.sin(theta) * radius

#     for i in range(CLUSTER_TWO_NODE_POPULATION):
#         CORDX,CORDY=point(700,700,20,i/10)

#         nf.write("$"+cluster_two_node_list[i]+" set Y_ "+str(round(CORDY,3))+"\n")
#         nf.write("$"+cluster_two_node_list[i]+" set X_ "+str(round(CORDX,3))+"\n")
#         nf.write("$"+cluster_two_node_list[i]+" set Z_ 0.0\n")


#     #cluster3 mapping

#     nf.write("$"+cluster_three_switch_node+" set X_ 690\n")
#     nf.write("$"+cluster_three_switch_node+" set Y_ 360\n")
#     nf.write("$"+cluster_three_switch_node+" set Z_ 0.0\n")

#     c3x=720
#     c3y=360
#     gridcounter3=0

#     for node in cluster_three_node_list:
#         c3y=c3y-50
#         if(gridcounter3 > 9):
#             c3y=360
#             gridcounter3=0
#             c3x=c3x+100
#         nf.write("$"+node+" set X_ "+str(c3x)+"\n")
#         nf.write("$"+node+" set Y_ "+str(c3y)+"\n")
#         nf.write("$"+node+" set Z_ 0.0\n")

#         gridcounter3=gridcounter3+1

#     #cluster4 mapping

#     nf.write("$"+cluster_four_switch_node+" set X_ 310\n")
#     nf.write("$"+cluster_four_switch_node+" set Y_ 350\n")
#     nf.write("$"+cluster_four_switch_node+" set Z_ 0.0\n")


#     nf.write("$"+cluster_four_node_list[int(0)]+" set X_ "+str("250")+"\n")
#     nf.write("$"+cluster_four_node_list[int(0)]+" set Y_ "+str("340")+"\n")
#     nf.write("$"+cluster_four_node_list[int(0)]+" set Z_ 0\n")


#     nf.write("$"+cluster_four_node_list[int(CLUSTER_FOUR_NODE_POPULATION//2)]+" set X_ "+str("240")+"\n")
#     nf.write("$"+cluster_four_node_list[int(CLUSTER_FOUR_NODE_POPULATION//2)]+" set Y_ "+str("250")+"\n")
#     nf.write("$"+cluster_four_node_list[int(CLUSTER_FOUR_NODE_POPULATION//2)]+" set Z_ 0.0\n")


#     c4x=250
#     c4y=340
#     gridcounter4=0

#     for i in range(1,int(CLUSTER_FOUR_NODE_POPULATION//2)):
#         c4y-=50
#         if(gridcounter4 > 9):
#             gridcounter4=0
#             c3y=300
#             c3x=c3x-50
#         nf.write("$"+cluster_four_node_list[i]+" set X_ "+str(c4x)+"\n")
#         nf.write("$"+cluster_four_node_list[i]+" set Y_ "+str(c4y)+"\n")
#         nf.write("$"+cluster_four_node_list[i]+" set Z_ 0\n")


#     c4x=150
#     c4y=240
#     gridcounter4=0
#     for i in range(int(CLUSTER_FOUR_NODE_POPULATION//2)+1,CLUSTER_FOUR_NODE_POPULATION):
#         c4x+=30
#         if(gridcounter4 > 9):
#             gridcounter4=0
#             c3x=150
#             c3y=c3y-50
#         nf.write("$"+cluster_four_node_list[i]+" set X_ "+str(c4x)+"\n")
#         nf.write("$"+cluster_four_node_list[i]+" set Y_ "+str(c4y)+"\n")
#         nf.write("$"+cluster_four_node_list[i]+" set Z_ 0.0\n")


#     #cluster5 mapping
#     nf.write("$"+cluster_five_switch_node+" set X_ 500\n")
#     nf.write("$"+cluster_five_switch_node+" set Y_ 100\n")
#     nf.write("$"+cluster_five_switch_node+" set Z_ 0.0\n")

#     c5x,c5y={450,80}
#     grid5counter=0


#     for node in wireless_cluster_five_node_list:
#         nf.write("$"+node+" set X_ "+str(c5x)+"\n")
#         nf.write("$"+node+" set Y_ "+str(c5y)+"\n")
#         nf.write("$"+node+" set Z_ 0.0\n")
#         grid5counter+=1
#         c5x+=50
#         if grid5counter > 5:
#             c5y-=20
#             c5x=450

print("Installing Applications")

# INSTALLING TCP LAYER

with open(ns_file_name, 'a') as nf:
    # CLUSTER 1 TCP INSTALL
    tcpindex = 0
    tcppacketsize = 1500

    for i in range(1, len(cluster_one_node_list)):
        tcpindex += 1
        node = cluster_one_node_list[i]
        # CUrrently sending data to last node of network cluster 5 from all nodes of C1 via C1N0 ,C1SW, R1 and R3
        nf.write("""
set C1tcp""" + str(tcpindex) + """ [new Agent/TCP]
$ns attach-agent $""" + node + """ $C1tcp""" + str(tcpindex) + """

$C1tcp""" + str(tcpindex) + """ set packetSize_ """ + str(tcppacketsize) + """
set sinkC1S""" + str(tcpindex) + """ [new Agent/TCPSink]
$ns attach-agent $""" + wireless_cluster_five_node_list[-1] + """ $sinkC1S""" + str(tcpindex) + """
$ns connect $C1tcp""" + str(tcpindex) + """ $sinkC1S""" + str(tcpindex) + """
                """)

    # CLUSTER 1 TELNET APPLICATION INSTALL

    telnetPacketSize = "500Mb"
    telnetappcount = 0
    for i in range(1, len(cluster_one_node_list)):
        telnetappcount += 1
        nf.write("""
set telnet""" + str(telnetappcount) + """ [new Application/Telnet]
$telnet""" + str(telnetappcount) + """ attach-agent $C1tcp""" + str(telnetappcount) + """
$telnet""" + str(telnetappcount) + """ set packetSize_ """ + telnetPacketSize + """
$telnet""" + str(telnetappcount) + """ set interval_ 0.01
$ns at 0.1 "$telnet""" + str(telnetappcount) + """ start"

""")
    # ================================================================================

    # CLUSTER 2 TCP INSTALL
    tcpindex = 0
    tcppacketsize = 1500

    for i in range(1, len(cluster_two_node_list)):
        tcpindex += 1
        node = cluster_two_node_list[i]
        # initailly connected to cluster_two_node_list[0], now to cluster_4 last node
        nf.write("""
set C2tcp""" + str(tcpindex) + """ [new Agent/TCP]
$ns attach-agent $""" + node + """ $C2tcp""" + str(tcpindex) + """
$C2tcp""" + str(tcpindex) + """ set packetSize_ """ + str(tcppacketsize) + """

set sinkC2S""" + str(tcpindex) + """ [new Agent/TCPSink]
$ns attach-agent $""" + cluster_four_node_list[-1] + """ $sinkC2S""" + str(tcpindex) + """

$ns connect $C2tcp""" + str(tcpindex) + """ $sinkC2S""" + str(tcpindex) + """
""")

    # CLUSTER 2 FTP APPLICATION INSTALL

    ftpPacketSize = "500Mb"
    FTPappcount = 0
    for i in range(1, len(cluster_two_node_list)):
        FTPappcount += 1
        nf.write("""
set ftp""" + str(FTPappcount) + """ [new Application/FTP]
$ftp""" + str(FTPappcount) + """ attach-agent $C2tcp""" + str(FTPappcount) + """
$ftp""" + str(FTPappcount) + """ set packetSize_ """ + ftpPacketSize + """
$ftp""" + str(FTPappcount) + """ set interval_ 0.01
$ns at 0.1 "$ftp""" + str(FTPappcount) + """ start"

""")

    # ================================================================================

    # Cluster3 SMTP Application agent install
    # sending data to cluster 1 last node
    # udpindex=0
    for i in range(0, len(cluster_three_node_list)):
        node = cluster_three_node_list[i]
        nf.write("""
set smtp_UDP_agent""" + str(i) + """ [new Agent/UDP]
set smtp_UDP_sink""" + str(i) + """ [new Agent/UDP]
$ns attach-agent $""" + cluster_three_node_list[i] + """ $smtp_UDP_agent""" + str(i) + """
$ns attach-agent $""" + cluster_one_node_list[-1] + """ $smtp_UDP_sink""" + str(i) + """
$ns connect $smtp_UDP_agent""" + str(i) + """ $smtp_UDP_sink""" + str(i) + """
set smtp_UDP_source""" + str(i) + """ [new Application/Traffic/Exponential]
$smtp_UDP_source""" + str(i) + """ attach-agent $smtp_UDP_agent""" + str(i) + """
$smtp_UDP_source""" + str(i) + """ set packetSize_ 210
$smtp_UDP_source""" + str(i) + """ set burst_time_ 50ms
$smtp_UDP_source""" + str(i) + """ set idle_time_ 50ms
$smtp_UDP_source""" + str(i) + """ set rate_ 100k
$ns at 0.1 "$smtp_UDP_source""" + str(i) + """ start" 
""")

    # ================================================================================

    # Cluster 4 CBR setup
    # sending data to cluster 3 last node
    for i in range(0, len(cluster_four_node_list)):
        node = cluster_four_node_list[i]
        nf.write("""
set C4TCPA""" + str(i) + """ [new Agent/TCP]
set C4TCPS""" + str(i) + """ [new Agent/TCPSink]
$ns attach-agent $""" + cluster_four_node_list[i] + """ $C4TCPA""" + str(i) + """
$ns attach-agent $""" + cluster_three_node_list[-1] + """ $C4TCPS""" + str(i) + """

$ns connect $C4TCPA""" + str(i) + """ $C4TCPS""" + str(i) + """
set C4CBRsrc""" + str(i) + """ [new Application/Traffic/CBR]
$C4CBRsrc""" + str(i) + """ attach-agent $C4TCPA""" + str(i) + """

$C4CBRsrc""" + str(i) + """ set packetSize_ 1000
$C4CBRsrc""" + str(i) + """ set rate_ 1.0Mb
$ns at 0.1 \"$C4CBRsrc""" + str(i) + """ start\"

""")

    # ================================================================================

    ##CLUSTER 5 CBR SETUP

    # for i in range(0,len(wireless_cluster_five_node_list)):
    #     for j in range(i+1,len(wireless_cluster_five_node_list)):
    #         if j > (len(wireless_cluster_five_node_list)-1):
    #             break
    #         else:
    #             nodeSrc=wireless_cluster_five_node_list[i]
    #             nodeDest=wireless_cluster_five_node_list[j]
    #             nf.write("""
    # set C5TCPA"""+str(i)+str(j)+""" [new Agent/TCP]
    # set C5TCPS"""+str(i)+str(j)+""" [new Agent/TCPSink]
    # $ns attach-agent $"""+wireless_cluster_five_node_list[i]+""" $C5TCPA"""+str(i)+str(j)+"""
    # $ns attach-agent $"""+wireless_cluster_five_node_list[j]+""" $C5TCPS"""+str(i)+str(j)+"""

    # $ns connect $C5TCPA"""+str(i)+str(j)+""" $C5TCPS"""+str(i)+str(j)+"""
    # set C5CBRsrc"""+str(i)+str(j)+""" [new Application/Traffic/CBR]
    # $C5CBRsrc"""+str(i)+str(j)+""" attach-agent $C5TCPA"""+str(i)+str(j)+"""

    # $C5CBRsrc"""+str(i)+str(j)+""" set packetSize_ 1000
    # $C5CBRsrc"""+str(i)+str(j)+""" set rate_ 1.0Mb
    # $ns at 0.1 \"$C5CBRsrc"""+str(i)+str(j)+""" start\"

    #         """)

    ## Sending data to last node of cluster one

    for i in range(0, len(wireless_cluster_five_node_list)):
        for j in range(i + 1, len(wireless_cluster_five_node_list)):
            if j > (len(wireless_cluster_five_node_list) - 1):
                break
            else:
                nodeSrc = wireless_cluster_five_node_list[i]
                nodeDest = cluster_one_node_list[-1]
                nf.write("""
    set C5TCPA""" + str(i) + str(j) + """ [new Agent/TCP]
    set C5TCPS""" + str(i) + str(j) + """ [new Agent/TCPSink]
    $ns attach-agent $""" + wireless_cluster_five_node_list[i] + """ $C5TCPA""" + str(i) + str(j) + """
    $ns attach-agent $""" + nodeDest + """ $C5TCPS""" + str(i) + str(j) + """

    $ns connect $C5TCPA""" + str(i) + str(j) + """ $C5TCPS""" + str(i) + str(j) + """
    set C5CBRsrc""" + str(i) + str(j) + """ [new Application/Traffic/CBR]
    $C5CBRsrc""" + str(i) + str(j) + """ attach-agent $C5TCPA""" + str(i) + str(j) + """

    $C5CBRsrc""" + str(i) + str(j) + """ set packetSize_ 1000
    $C5CBRsrc""" + str(i) + str(j) + """ set rate_ 1.0Mb
    $ns at 0.1 \"$C5CBRsrc""" + str(i) + str(j) + """ start\"

            """)

## MAL Node Application Install
if activate_mal:
    with open(ns_file_name, 'a') as nf:
        nf.write("""
        set MAL1A [new Agent/TCP]
        set MAL1S [new Agent/TCPSink]
        $ns attach-agent $""" + malicious_node_list[0] + """ $MAL1A
        $ns attach-agent $""" + wireless_cluster_five_node_list[-1] + """ $MAL1S
    
        $ns connect $MAL1A $MAL1S
        set MALCBRsrc [new Application/Traffic/CBR]
        $MALCBRsrc attach-agent $MAL1A
    
        $MALCBRsrc set packetSize_ 1000
        $MALCBRsrc set rate_ 5Mb
        $ns at 0.2 \"$MALCBRsrc start\"
    
                """)

##TERMINATION

# ===================================
#        Termination        
# ===================================
# Define a 'finish' procedure


with open(ns_file_name, 'a') as nf:
    nf.write("""
proc finish {} {
    global ns tracefile namfile
    $ns flush-trace
    close $tracefile
    close $namfile
    exit 0
}
$ns at """ + str(run_time) + """ "$ns nam-end-wireless $val(stop)"
$ns at """ + str(run_time) + """ "finish"
$ns at """ + str(run_time) + """ "puts \\"done\\" ; $ns halt"
$ns run""")


# from os import system as sys
#
# try:
#     sys("ns result.tcl")
# except Exception:
#     print("Error in Execution of ns")
