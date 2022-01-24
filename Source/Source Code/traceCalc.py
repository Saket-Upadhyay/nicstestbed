import traceanalyzer as tr
import os


node_to_study = '7'
node_name = "SW5"
# Throughput

files = os.listdir(".")

if "attack_out.tr" in files:
    print("Calc. Attack Throughput")
    throughput1 = tr.Throughput('attack_out.tr', node_to_study)
    throughput1.sample()
    throughput1.plot('', str(node_name + "A"))
    # getting data
    time = throughput1.time_sample
    throughput = throughput1.throughput_sample

    print(time)
    print(throughput)
    print("MAX = " + str(max(throughput)))
    print("MIN = " + str(min(throughput)))
    print("AVG = " + str(sum(throughput) / len(throughput)))
    # idx = 0
    # for instant in time:
    #     print(instant, ' ', throughput[idx])
    #     idx += 1
if "normal_out.tr" in files:
    print("\nCalc. Normal Throughput")
    throughput2 = tr.Throughput('normal_out.tr', node_to_study)
    throughput2.sample()
    throughput2.plot('', str(node_name + "N"))
    # getting data
    timeN = throughput2.time_sample
    throughputN = throughput2.throughput_sample
    print(timeN)
    print(throughputN)
    print("MAX = " + str(max(throughputN)))
    print("MIN = " + str(min(throughputN)))
    print("AVG = " + str(sum(throughputN) / len(throughputN)))
    # idx = 0
    # for instant in time:
    #     print(instant, ' ', throughput[idx])
    #     idx += 1
