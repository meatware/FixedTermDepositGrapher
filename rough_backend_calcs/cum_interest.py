#!/usr/bin/python3.6
import os, sys
from datetime import datetime, timedelta
from math import floor

def datetime_to_string(dt_obj):
    """Convert datetime object into string."""
    return dt_obj.strftime('%a_%b_%d_%H:%M:%S')

# 19/09/18
def string_to_datetime(in_str, fmt_def='%d/%m/%y'):
    dt_obj = datetime.strptime(in_str, fmt_def)
    return dt_obj

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
    #sys.exit(0)

    return

def calculate_daily_maturity(depo_dict):
    # https://en.wikipedia.org/wiki/Rounding#Round_half_to_even
    #https://money.stackexchange.com/questions/10796/daily-interest-calculation-combined-with-monthly-compounding-why-do-banks-do-th
    pri = depo_dict["initial_deposit"]
    irate = depo_dict["interest_rate"]/100
    period = depo_dict["period"] # months
    start_date = string_to_datetime(depo_dict["start_date"])
    end_date = string_to_datetime(depo_dict["ref_end_date"])

    day_delta = end_date - start_date
    day_period = day_delta.days # in days
    print("day_period", day_period)
    print("dayx", (period/12)*365)

    daily_irate = (depo_dict["interest_rate"]/100)/365
    print("daily_irate", daily_irate)

    # figure out n left over compounding days
    full_n_cmpds = floor(day_period/91.25) # in the case ogf quarterly compundsing 30x4
    remain_cmpd_days = day_period - (full_n_cmpds * 91.25)
    cmpdd_day_list = [91.25 for _ in range(full_n_cmpds)]
    cmpdd_day_list.append(remain_cmpd_days)

    print("cmpdd_day_list", cmpdd_day_list)

    maturity_val = pri
    mat_list = []
    # insert calcs
    for qdays in cmpdd_day_list:

        monthly_interest = (daily_irate * maturity_val)* qdays
        print("monthly_interest", monthly_interest)
        maturity_val = maturity_val + monthly_interest
        mat_list.append(maturity_val)

    print("\nmat_list", mat_list)
    print("\ndiff", round(depo_dict["ref_maturity_Amount"] - maturity_val, 2))
    print("\ndiff", round(depo_dict["ref_maturity_Amount"] - mat_list[-1], 2))









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

            print("\n################")
            recalc_depo2 = calculate_daily_maturity(deposit_item)
            sys.exit(0)

            ## file
            dep_name = deposit_item["acc_no"]
            all_deposits[dep_name] = deposit_item

        for key, value in all_deposits.items():
            print(key, value)

            #sys.exit(0)


