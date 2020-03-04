from collections import Counter
votes = ["FVSHJIEMNGYPTQOURLWCZKAX","AITFQORCEHPVJMXGKSLNZWUY","OTERVXFZUMHNIYSCQAWGPKJL","VMSERIJYLZNWCPQTOKFUHAXG","VNHOZWKQCEFYPSGLAMXJIUTR","ANPHQIJMXCWOSKTYGULFVERZ","RFYUXJEWCKQOMGATHZVILNSP","SCPYUMQJTVEXKRNLIOWGHAFZ","VIKTSJCEYQGLOMPZWAHFXURN","SVJICLXKHQZTFWNPYRGMEUAO","JRCTHYKIGSXPOZLUQAVNEWFM","NGMSWJITREHFZVQCUKXYAPOL","WUXJOQKGNSYLHEZAFIPMRCVT","PKYQIOLXFCRGHZNAMJVUTWES","FERSGNMJVZXWAYLIKCPUQHTO","HPLRIUQMTSGYJVAXWNOCZEKF","JUVWPTEGCOFYSKXNRMHQALIZ","MWPIAZCNSLEYRTHFKQXUOVGJ","EZXLUNFVCMORSIWKTYHJAQPG","HRQNLTKJFIEGMCSXAZPYOVUW","LOHXVYGWRIJMCPSQENUAKTZF","XKUTWPRGHOAQFLVYMJSNEIZC","WTCRQMVKPHOSLGAXZUEFYNJI"]
result = ''
templist = {}
for vote in votes:
    for i in range(len(vote)-1):
        for j in range(i+1,len(vote)):
            if vote[i] not in templist:
                templist[vote[i]] = {vote[j]:1}
            else:
                if vote[j] not in templist[vote[i]]:
                    templist[vote[i]][vote[j]] = 1
                else:
                    templist[vote[i]][vote[j]] += 1
print(templist)
resultlist = []
for key,value in templist.items():
    resultlist.append([key,sum(value.values())])
for i in sorted(resultlist,key=lambda x: (-x[1],x[0])):
    result += i[0]

print(result)