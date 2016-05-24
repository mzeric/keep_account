Ren.objects.get(id=1)
Charge.objects.filter(ren=a)
all_ = ChiFan.objects.all()
asdf = ChiFan_Sep.objects.all()
for  a in asdf:

t_balance[t_ren]= 0

def get_ren_with_total(fan):
    all_sep = ChiFan_Sep.objects.filter(chifan = fan)
    all_ren = fan.ren.all()
    t_total = fan.total
    t_sep_sum = 0
    for sep in all_sep:
        t_ren = sep.ren
        t_cost = sep.cost
        t_balance[t_ren] = t_balance[t_ren] - t_cost
        t_sep_sum = t_sep_sum + t_cost

    t_share = t_total - t_sep_sum
    t_sep_share = t_share/len(all_ren)
    for all_ren_this_chifan :
        

def get_ren_with_share(fan):
    pass
    

def get_share():
    if share != 0:
        return share
    if total == 0:
        return 0

