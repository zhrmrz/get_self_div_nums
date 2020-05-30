class Sol:
    def get_self_div_nums(self,left,right):
        list=[]
        for num in range(left,right+1):
            if self.self_dividing(num)==True:
                list.append(num)
        return list

    def self_dividing(self,num):
        for d in str(num):
            if int(d)==0 or num%int(d)!=0:
                return False
        return True

if __name__ == '__main__':
    p=Sol()
    print(p.get_self_div_nums(1,22))
