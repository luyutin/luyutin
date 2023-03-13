import argparse
import numpy as np
import time
import sys
sys.setrecursionlimit(5000)

class mono_routing():
    def __init__(self, args):
        pass
    def parser(self): #You can modify it by yourself.
        with open("%s" % args.input, 'r', newline='') as file_in:
            f = file_in.read().splitlines()
            for lines in f:
                if lines.startswith("BoundaryIndex"):
                    value_list = lines.split(' ')
                    self.Bx1 = int(value_list[1])
                    self.By1 = int(value_list[2])
                    self.Bx2 = int(value_list[3])
                    self.By2 = int(value_list[4])
                if lines.startswith("DefaultCost"):
                    value_list = lines.split(' ')
                    self.default_cost = int(value_list[-1])
                if lines.startswith("NumNonDefaultCost"):
                    value_list = lines.split(' ')
                    self.size = int(value_list[-1])
                    break
            
            source_list = list(f[-2].split(' '))
            target_list = list(f[-1].split(' '))
            self.sx = source_list[1]
            self.sy = source_list[2]
            self.tx = target_list[1]
            self.ty = target_list[2]
            """Saving cost"""
            self.NDcost = {}
            for x in range(self.Bx2+1):
                for y in range(self.By2+1):
                    #self.NDcost['%d%d%d%d' %(x,y,x,y+1)] = self.default_cost --> this is wrong
                    self.NDcost[(x,y,x,y+1)] = self.default_cost
            for y in range(self.By2+1):
                for x in range(self.Bx2+1):
                    #self.NDcost['%d%d%d%d' %(x,y,x+1,y)] = self.default_cost --> this is wrong
                    self.NDcost[(x,y,x+1,y)] = self.default_cost
            num_cost = f[3:3+int(self.size)]
            for NDcost in num_cost:
                NDcost_list = NDcost.split(' ')
                self.NDcost[(int(NDcost_list[0]), int(NDcost_list[1]), int(NDcost_list[2]), int(NDcost_list[3]))] += int(NDcost_list[4])
        
        """Print parameters"""
        print('BoundaryIndex:',self.Bx1,self.By1,self.Bx2,self.By2)
        print('DefaultCost:',self.default_cost)
        print('NumNonDefaultCost:',self.size)
        for i in range(len(num_cost)):
            print(num_cost[i])
        print('Source:',self.sx, self.sy)
        print('Target:',self.tx, self.ty)

    def routing(self):
        self.routing_path = {}
        self.grid_cost = np.zeros((self.Bx2+1,self.By2+1),dtype=int)
        self.costofPaths(self.Bx2,self.By2)
        self.pathlist(self.Bx2,self.By2)
        

    def costofPaths(self, m, n):      
        # ---TODO:
        # Write down your routing algorithm by using dynamic programming.
        # ---
        # Base Condition
        # If sub problem is previously solved tehn return it.
        if self.grid_cost[m][n] != 0:
            return self.grid_cost[m][n]
        elif (m<=0 and n<=0):
            self.grid_cost[m][n] = 0
            self.routing_path[(m, n)] = (0,0)
            return 0
        elif (m>=1 and n>=1):
            self.grid_cost[m][n] = min(self.costofPaths(m-1, n)+ self.NDcost[(m-1,n,m,n)],
                                       self.costofPaths(m, n-1)+ self.NDcost[(m,n-1,m,n)])
            if self.grid_cost[m][n] == self.costofPaths(m-1, n)+ self.NDcost[(m-1,n,m,n)]:
                self.routing_path[(m, n)] = (m-1, n)
            else:
                self.routing_path[(m, n)] = (m, n-1)
            return self.grid_cost[m][n]
        elif (m>=1 and n<=0):
            self.grid_cost[m][n] = self.costofPaths(m-1,n)+self.NDcost[(m-1,n,m,n)]
            self.routing_path[(m, n)] = (m-1, n)
            return self.grid_cost[m][n]
        elif (m<=0 and n>=1):
            self.grid_cost[m][n] = self.costofPaths(m,n-1)+self.NDcost[(m,n-1,m,n)]
            self.routing_path[(m, n)] = (m, n-1)
            return self.grid_cost[m][n]

    def pathlist(self,m,n):
        a = self.routing_path[(m,n)]
        l1 = []
        l1.append((m,n))
        i = 0
        while i <= (m+n-1):
            l1.append(a)
            a = self.routing_path[a]
            i += 1
        self.l2 = []
        while l1:
            self.l2.append(l1.pop())


    def output(self): # You can modify it by yourself, but the output format should be correct.
        with open("%s" % args.output, 'w', newline='') as file_out:
            file_out.writelines('RoutingCost %d'% self.grid_cost[self.Bx2][self.By2])
            file_out.writelines('\nRoutingPath %d'% len(self.l2))
            for i in range(len(self.l2)):
                file_out.writelines('\n%d %d'% (self.l2[i][0], self.l2[i][1]))
            
        
if __name__ == '__main__':
    parser = argparse.ArgumentParser()
    parser.add_argument("--input", type=str, default = './5000x4000.in',help="Input file root.")
    parser.add_argument("--output", type=str, default = './5000x4000.out',help="Output file root.")
    args = parser.parse_args()

    print('#################################################')
    print('#              Monotonic Routing                #')
    print('################################################# \n')

    routing = mono_routing(args)
    """Parser"""
    routing.parser()
    print('################ Parser Down ####################')
    """monotonic route"""
    start = time.time()
    routing.routing()
    print('run time:', round(time.time()-start,3))
    """output"""
    routing.output()