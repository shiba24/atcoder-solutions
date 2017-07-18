# -*- coding: utf-8 -*-

import numpy as np
        
# class Tree(object):
#     """docstring for Tree"""
#     def __init__(self, arg):
#         self.arg = arg
        
#     self.parent = hoge
#     self.child = []



N = input()

MAX_SIZE = N
MAX_VALUE = 0x10000000
# グローバル変数
visited = [False] * MAX_SIZE
cost = [MAX_VALUE] * MAX_SIZE
prev = [None] * MAX_SIZE
edges = [[0 for k in range(0, N)] for k in range(0, N)]

# f = [1]
# s = [N]

for i in range(0, N - 1):
    edge = list(map(int, raw_input().split()))
    edges[edge[0] - 1][edge[1] - 1] = 1
    edges[edge[1] - 1][edge[0] - 1] = 1

# np.sort(np.array(edges), axis=1)


def search(start):
    cost[start] = 0
    prev[start] = start
    while True:
        min = MAX_VALUE
        next = -1
        visited[start] = True
        for i in xrange(MAX_SIZE):
            if visited[i]: continue
            if edges[start][i]:
                d = cost[start] + edges[start][i]
                if d < cost[i]:
                    cost[i] = d
                    prev[i] = start
            if min > cost[i]:
                min = cost[i]
                next = i
        start = next
        if next == -1: break
    # 経路の表示
    # for i in xrange(MAX_SIZE):
    #     print "%d, prev = %d, cost = %d" %  (i, prev[i], cost[i])

    ways = np.array([cost[i] - cost[MAX_SIZE - 1] for i in range(0, MAX_SIZE)])
    if abs(sum(ways[ways < 0])) > abs(sum(ways[ways > 0])):
        print 'Fennec'
    else:
        print 'Snuke'
    # if 

    # minimum_way = [MAX_SIZE - 1]
    # i = MAX_SIZE    
    # while i != 0:
    #     minimum_way.append(prev[i - 1])
    #     i = prev[i - 1]
    # minimum_way.reverse()
    # print minimum_way

search(0)
# search(MAX_SIZE - 1)





# get middle point between 1 and N

# if 1-part have larger nodes, print Fennec
# else print Snuke



# print abs(2 * cur_sum - sum_a)



"""
import math

route_list = [[0, 50, 80, 0, 0],
[0, 0, 20, 15, 0 ],
[0, 0, 0, 10, 15], 
[0, 0, 0, 0, 30], 
[0, 0, 0, 0, 0]] # 初期のノード間の距離のリスト

node_num = len(route_list) #ノードの数

unsearched_nodes = list(range(node_num)) # 未探索ノード
distance = [math.inf] * node_num # ノードごとの距離のリスト
previous_nodes = [-1] * node_num # 最短経路でそのノードのひとつ前に到達するノードのリスト
distance[0] = 0 # 初期のノードの距離は0とする

# @GDaigo さんのコメントより関数の追加 2017/03/18
def get_target_min_index(min_index, distance, unsearched_nodes):
    start = 0
    while True:
        index = distance.index(min_index, start)
        found = index in unsearched_nodes
        if found:
            return index
        else:
            start = index + 1

while(len(unsearched_nodes) != 0): #未探索ノードがなくなるまで繰り返す
    # まず未探索ノードのうちdistanceが最小のものを選択する
    posible_min_distance = math.inf # 最小のdistanceを見つけるための一時的なdistance。初期値は inf に設定。
    for node_index in unsearched_nodes: # 未探索のノードのループ
        if posible_min_distance > distance[node_index]: 
            posible_min_distance = distance[node_index] # より小さい値が見つかれば更新
    target_min_index = get_target_min_index(posible_min_distance, distance, unsearched_nodes) # 未探索ノードのうちで最小のindex番号を取得
    unsearched_nodes.remove(target_min_index) # ここで探索するので未探索リストから除去

    target_edge = route_list[target_min_index] # ターゲットになるノードからのびるエッジのリスト
    for index, route_dis in enumerate(target_edge):
        if route_dis != 0:
            if distance[index] > (distance[ target_min_index] + route_dis):
                distance[index] = distance[ target_min_index] + route_dis # 過去に設定されたdistanceよりも小さい場合はdistanceを更新
                previous_nodes[index] =  target_min_index #　ひとつ前に到達するノードのリストも更新

# 以下で結果の表示

print("-----経路-----")
previous_node = node_num - 1
while previous_node != -1:
    if previous_node !=0:
        print(str(previous_node + 1) + " <- ", end='')
    else:
        print(str(previous_node + 1))
    previous_node = previous_nodes[previous_node]

print("-----距離-----")
print(distance[node_num - 1])
"""