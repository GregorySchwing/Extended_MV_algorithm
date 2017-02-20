#!/apps/anaconda-2.3.0/bin/python

import networkx as nx
import numpy as np
import mv_algorithm_fast_test_dfs as mv0f
import time
import os
import csv
import sys
import random

def writeLog(fil, table):
    c1 = csv.writer(fil)
    for val in table:
        c1.writerow(val)

test_arr = []
node_array = range(9,15)

for n_exp in node_array:
    for t in range(0,10):
        test_arr.append([n_exp,t])

param = [12,1]
# param = test_arr[58]
node_exp = param[0]

n = int(2**(node_exp))
h = nx.Graph()
random_list = range(int(3*n))
h.add_nodes_from(random_list)
random.shuffle(random_list)
trials = 1
results = []

triangle_list = []
triangle_count = 0
for i in range(n-1):
    h.add_edge(random_list[3 * i], random_list[3 * i + 1])
    h.add_edge(random_list[3 * i + 1], random_list[3 * i + 2])
    h.add_edge(random_list[3 * i + 2], random_list[3 * i])
for i in range(n-2):
    h.add_edge(random_list[3 * i], random_list[3 * i + 3])
    h.add_edge(random_list[3 * i + 1], random_list[3 * i + 4])
    h.add_edge(random_list[3 * i + 2], random_list[3 * i + 5])


len_edges = len(h.edges())
deg_arr = []
for n1 in h.nodes():
    deg_arr.append(h.degree(n1))

start_time = time.clock()
l0, pid0, pm0 = mv0f.mv_max_cardinality(h, 1, False, 1)
print len(l0)/2.0
l0_time = time.clock() - start_time
print 'solve time: ' + str(l0_time)
print ' '

start_time = time.clock()
l1, pid1, pm1 = mv0f.mv_max_cardinality(h, 1, True, 1)
print len(l1)/2.0
l1_time = time.clock() - start_time
print 'solve time: ' + str(l1_time)
print ' '

start_time = time.clock()
l2, pid2, pm2 = mv0f.mv_max_cardinality(h, 1, False, 100)
print len(l2)/2.0
l2_time = time.clock() - start_time
print 'solve time: ' + str(l2_time)
print ' '

start_time = time.clock()
l3, pid3, pm3 = mv0f.mv_max_cardinality(h, 1, True, 100)
print len(l3)/2.0
l3_time = time.clock() - start_time
print 'solve time: ' + str(l3_time)
print ' '
results.append(['expected_degree','node_exponent','N','E',
                'phases_0','phases_1','phases_2','phases_3',
                'time_0','time_1','time_2','time_3',
                'percent_matched_0', 'percent_matched_1','percent_matched_2','percent_matched_3'])
results.append([node_exp, n, len_edges, pid0, pid1, pid2, pid3, l0_time, l1_time, l2_time, l3_time, pm0, pm1, pm2, pm3])
print results
fil = open(os.getcwd() + "/results_3_triangle_" + str(node_exp) + "_" + str(param[1]) + ".csv", "wb")
writeLog(fil, results)