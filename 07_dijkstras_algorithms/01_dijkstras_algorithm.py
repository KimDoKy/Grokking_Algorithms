# 그래프
graph = {}
graph['start'] = {}
graph['start']['a'] = 6
graph['start']['b'] = 2

graph['a'] = {}
graph['a']['fin'] = 1

graph['b'] = {}
graph['b']['a'] = 3
graph['b']['fin'] = 5

graph['fin'] = {}


infinity = float('inf')  # 무한대

# 가격
costs = {}
costs['a'] = 6
costs['b'] = 2
costs['fin'] = infinity

# 부모
parents = {}
parents['a'] = 'start'
parents['b'] = 'start'
parents['fin'] = None

# 처리한 정점 추적을 위한 배열
processed = []

def find_lowest_cost_node(costs):
    lowest_cost = float('inf')
    lowest_cost_node = None
    for node in costs:  # 모든 정점을 확인
        cost = costs[node]  # 아직 처리되지 않은 정점 중 더 싼것 이 있다면
        if cost < lowest_cost and node not in processed:
            lowest_cost = cost  # 새로운 최저 정점으로 설정
            lowest_cost_node = node
    return lowest_cost_node

# 아직 처리하지 않은 가장 싼 정점을 찾음
node = find_lowest_cost_node(costs)

# 모든 정점을 처리하면 반복문이 종료
while node is not None:
    cost = costs[node]
    neighbors = graph[node]
    for n in neighbors.keys(): # 모든 이웃에 대해 반복
        new_cost = cost + neighbors[n]
        if costs[n] > new_cost: # 만약 이 정점을 지나는 것이 더 싸다면
            costs[n] = new_cost # 정점의 가격을 갱신
            parents[n] = node   # 부모를 이 정점으로 재 설정
    processed.append(node)      # 정점 수정을 기록
    node = find_lowest_cost_node(costs)  # 다음을 처리할 정점을 찾아 반복

print('Cost from the start to each node:')
print(costs)
