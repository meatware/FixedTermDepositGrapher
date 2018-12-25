#!/usr/bin/python3.6
import os, sys

def calculate_maturity(depo_dict):
    #http://www.allbankingsolutions.com/fdcal.htm
    # https://www.thecalculatorsite.com/articles/finance/compound-interest-formula.php
    pri = depo_dict["initial_deposit"]
    irate = depo_dict["interest_rate"]/100
    period = depo_dict["period"]

    # insert calcs
    freq =  4.0  #depo_dict["initial_deposit"]

    maturity_val = 0
    #for _ in range(4):
    power_calc = freq * (period/12)
    maturity_val = pri * (1 + irate/freq)**power_calc

    print("\n\nref_maturity_Amount", depo_dict["ref_maturity_Amount"])
    print("maturity_val", round(maturity_val, 1))

    print("\ndiff", round(depo_dict["ref_maturity_Amount"] - maturity_val, 2) )
    sys.exit(0)

    return

for filename in sys.argv[1:]:
    with open(filename, 'r') as FHO:

        all_deposits = {}
        for line in FHO:
            print(line)

            split_line = line.split(",")

            print(len(split_line), split_line)

            deposit_item = {}
            for idx, value in enumerate(split_line):
                print("xx", idx, value)
                if value == "":
                    pass
                else:
                    if idx == 2:
                        dkey= "start_date"
                        deposit_item[dkey] = str(value)
                    elif idx == 3:
                        dkey= "interest_rate"
                        deposit_item[dkey] = float(value)
                    elif idx == 4:
                        dkey= "period"
                        month_value = value.split(" ")
                        deposit_item[dkey] = int(month_value[0])
                    elif idx == 5:
                        dkey= "ref_end_date"
                        # calculate
                        deposit_item[dkey] = str(value)
                    elif idx == 6:
                        dkey= "initial_deposit"
                        deposit_item[dkey] = float(value)
                    elif idx == 7:
                        dkey= "ref_maturity_Amount"
                        # calculate
                        deposit_item[dkey] = float(value)
                    elif idx == 8:
                        dkey= "scheme"
                        deposit_item[dkey] = str(value)
                    elif idx == 9:
                        dkey= "acc_no"
                        deposit_item[dkey] = str(value).strip("\n")
                    else:
                        print("hello")

            ##
            print(deposit_item)
            recalc_depo = calculate_maturity(deposit_item)
            print(recalc_depo)
            sys.exit(0)

            ## file
            dep_name = deposit_item["acc_no"]
            all_deposits[dep_name] = deposit_item

        for key, value in all_deposits.items():
            print(key, value)

            #sys.exit(0)


