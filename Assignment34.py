#Greedy algorithm: solve allocation of workstations --
#problem and solution is given .. Just read it and try to implement it again.

dest = set(['chennai','pune','mumbai','bangalore','pathankot','hyderabad','nagpur','aurangabad','satara','kolhapur'])

stat_list = {}
stat_list['one'] = set(['bangalore','pathankot','hyderabad'])
stat_list['two'] = set(['pune','bangalore','hyderabad','satara'])
stat_list['three'] = set(['mumbai','pathankot','nagpur'])
stat_list['four'] = set(['pathankot','chennai','kolhapur'])
stat_list['five'] = set(['bangalore','aurangabad'])

station = set()
counter = 0

print("Stations remaining ==> " , dest)
print("")

while(dest):
    best_stat = None
    dest_covered = set()
    counter += 1
    for no, selected_stat in stat_list.items():
        covered = selected_stat & dest
        # if(len(covered)==0):
        #     print("Station " + no + " already traversed")
        if(len(covered)>len(dest_covered)):
            best_stat = no
            dest_covered = covered

    dest -= dest_covered
    print("Station " + best_stat + " selected after " + str(counter) + " iteration")
    print("Stations covered ==> " , dest_covered)
    print("Stations remaining ==> " , dest)
    print("")
    station.add(best_stat)

print("Stations selected for greedy algorithm are : " , station)