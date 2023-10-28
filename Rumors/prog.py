num_relations = int(input())

relations = []

for i in range(num_relations):
    relations.append(input().split())

possible_first_spreaders = [] # People who are possible to spread the rumor
certain_listeners = [] # People who are certain to hear the rumor

for i in relations:
    if i[1] == "->":
        if i[0] not in possible_first_spreaders and i[0] not in certain_listeners:
            possible_first_spreaders.append(i[0])
        if i[2] in possible_first_spreaders:
            possible_first_spreaders.remove(i[2])
        if i[2] not in certain_listeners:
            certain_listeners.append(i[2])
    elif i[1] == "??":
        if i[0] not in possible_first_spreaders and i[0] not in certain_listeners and i[2] not in certain_listeners:
            possible_first_spreaders.append(i[0])
        if i[2] not in possible_first_spreaders and i[2] not in certain_listeners and i[0] not in certain_listeners:
            possible_first_spreaders.append(i[2])
# print possible first spreaders sorted alphabetically
print(*sorted(possible_first_spreaders), sep="\n")

# alice ?? bob
# bob -> chuck
# bob -> dev
# dev ?? eve
# eve -> alice