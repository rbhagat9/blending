# Rohan Bhagat
# ISYE 3133
# Project 1
# Studio Section MW1
# GTID: 903657424

from gurobipy import GRB,Model
m = Model('Project 1')
m.setParam('OutputFlag', False)

d1 = m.addVar(name='Pounds of Drug 1')
d2 = m.addVar(name='Pounds of Drug 2')
p1 = m.addVar(vtype=GRB.INTEGER, name = 'Iterations of Process 1')
p2 = m.addVar(vtype=GRB.INTEGER, name = 'Iterations of Process 2')

m.addConstr(d1 <= 0.8*(3*p1 + 3*p2), name='c1') # drug 1 must be at least 80% chemical 1
m.addConstr(d2 <= 0.6*(3*p1 + 3*p2), name='c2') # drug 2 must be at least 60% chemical 1
m.addConstr(2*p1 + 3*p2 <= 90, name='c3') # skilled labor hours limited to 90
m.addConstr(3*p1 + 2*p2 <= 75, name='c4') # raw materials limited to 75

m.setObjective(7*d1 + 5*d2, GRB.MAXIMIZE)
m.optimize()
if m.status == 2:
    print("The solution found is optimal.")
    print(f"The optimal objective value is {m.objVal}")
    print("The optimal solution is")
    for v in m.getVars():
        print(f"{v.varName} = {v.x}")
else:
    print("The solution found is not optimal.")