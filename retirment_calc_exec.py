import retirement_calc as ut

def main():

    my_fund = ut.Retirement(2000)
    print(my_fund.deposit(5000))
    print(my_fund.yearly_interest(6))
    print(my_fund.deposit(6000))
    print(my_fund.yearly_interest(7))
if __name__ == "__main__":
    main()