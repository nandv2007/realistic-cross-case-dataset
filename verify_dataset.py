import glob,os
root=os.path.dirname(__file__)
for p in glob.glob(os.path.join(root,"case_*","*")):
    if not os.path.isfile(p): continue
    txt=open(p,encoding="utf-8").read()
    bad=[x for x in ["Operative ","Complainant / Target", "Investigated Suspect", "Alias-", "Code-", "ACC-MULE-", "ACC-HAWALA-"] if x in txt]
    if bad: print("WARNING",p,bad)
print("Verification complete.")
