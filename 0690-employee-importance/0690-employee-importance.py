"""
# Definition for Employee.
class Employee:
    def __init__(self, id: int, importance: int, subordinates: List[int]):
        self.id = id
        self.importance = importance
        self.subordinates = subordinates
"""

class Solution:
    def getImportance(self, employees: List['Employee'], id: int) -> int:
        '''
        # Here we are given a data structure thats storing a graph.
        # We have to first build an adjacency list to know subordinates for each id
        # Visualise this like, you have been given graph but cannot directly access the subordinates, you can just know them, so have to first build a list consisting connections and the importance of the emp
        '''
        def importance():
            que = deque()
            emp_data = {}
            root_emp = 0
            for emp in employees:
                emp_data[emp.id] = emp
            
            que.append(id)

            imp_sum = 0
            while que:
                emp_id = que.popleft()
                imp_sum += emp_data[emp_id].importance

                for i in emp_data[emp_id].subordinates:
                    que.append(i)
            
            return imp_sum
        
        return importance()


