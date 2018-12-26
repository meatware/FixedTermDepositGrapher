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

def calc_freq(scheme_label):

    cum_freq = 1 # yearly
    cum_days = 1

    scheme_fmt = scheme_label.lower()
    if "quart" in scheme_fmt:
        cum_freq = 4
        cum_days = 91.25
    elif "month" in scheme_fmt:
        cum_freq = 12
        cum_days = 30 #??

    return {"cum_freq": cum_freq, "cum_days": cum_days}

def print_calc_verific(ref_string, maturity_val, ref_maturity_Amount):

    print("\n\nref_maturity_Amount", ref_maturity_Amount)
    print(ref_string, maturity_val)

    print("\ndelta", round(ref_maturity_Amount - maturity_val, 2) )

    return

def calc_approx_maturity(depo_dict):
    principal = depo_dict["initial_deposit"]
    irate = depo_dict["interest_rate"]/100
    month_period = depo_dict["period"]

    # insert calcs
    get_freq = calc_freq(depo_dict["scheme"])
    freq = get_freq["cum_freq"]

    power_calc = freq * (month_period/12)
    maturity_val = principal * (1 + irate/freq)**power_calc

    return round(maturity_val, 2)

def calculate_daily_maturity(depo_dict):
    # https://en.wikipedia.org/wiki/Rounding#Round_half_to_even
    #https://money.stackexchange.com/questions/10796/daily-interest-calculation-combined-with-monthly-compounding-why-do-banks-do-th
    principal = depo_dict["initial_deposit"]
    irate = depo_dict["interest_rate"]/100
    month_period = depo_dict["period"]

    start_date = string_to_datetime(depo_dict["start_date"])
    end_date = string_to_datetime(depo_dict["ref_end_date"])

    day_delta = end_date - start_date
    day_period = day_delta.days
    print("day_period", day_period)

    daily_irate = irate/365
    print("daily_irate", daily_irate)

    # figure out n left over compounding days
    get_day_cmpnds = calc_freq(depo_dict["scheme"])
    day_cmpnds = get_day_cmpnds["cum_days"]

    full_n_cmpnds = floor(day_period/day_cmpnds) # in the case of quarterly compundsing 30x4
    remain_cmpnd_days = day_period - (full_n_cmpnds * day_cmpnds)
    cmpnd_days_list = [day_cmpnds for _ in range(full_n_cmpnds)]
    cmpnd_days_list.append(remain_cmpnd_days)

    month_interest_li = []
    month_maturity_li = []
    maturity_val = principal
    for qdays in cmpnd_days_list:

        month_interest = (daily_irate * maturity_val)* qdays
        month_interest_li.append(month_interest)
        print("month_interest", month_interest)

        maturity_val = maturity_val + month_interest
        month_maturity_li.append(maturity_val)

    print("cmpnd_days_list", cmpnd_days_list)
    print("\nmonth_interest_li", month_interest_li)
    print("\nmonth_maturity_li", month_maturity_li)

    return {"idaily_maturity": month_maturity_li[-1],
            "cmpnd_days_list": cmpnd_days_list,
            "month_interest_li": month_interest_li,
            "month_maturity_li": month_maturity_li}







if __name__ == "__main__":
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
                aprox_maturity_val = calc_approx_maturity(deposit_item)

                print_calc_verific("aprox_maturity_calc", aprox_maturity_val, deposit_item["ref_maturity_Amount"])

                #################################################
                print("\n################")
                idaily_maturity_dic = calculate_daily_maturity(deposit_item)

                print_calc_verific("idaily_maturity", idaily_maturity_dic["idaily_maturity"], deposit_item["ref_maturity_Amount"])
                sys.exit(0)

                ## file
                dep_name = deposit_item["acc_no"]
                all_deposits[dep_name] = deposit_item

            for key, value in all_deposits.items():
                print(key, value)

                #sys.exit(0)


