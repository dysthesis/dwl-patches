import os

patchlist = os.listdir("./patches")
patchlist.sort()

for patch in patchlist:
    print(f"# {patch}\n")
    for file in os.listdir(f"./patches/{patch}"):
        if file.lower() == "readme.md":
            print(open(f"./patches/{patch}/{file}").read())
    print("---")

print("# STALE PATCHES")

patchlist = os.listdir("./_STALE_PATCHES")
patchlist.sort()
for patch in patchlist:
    print(f"## {patch.split(".")[0]}\n")
    if (os.path.isdir(f"./_STALE_PATCHES/{patch}")):
        for file in os.listdir(f"./_STALE_PATCHES/{patch}"):
            if file.lower() == "readme.md":
                print(open(f"./_STALE_PATCHES/{patch}/{file}").read())
    else:
        print(open(f"./_STALE_PATCHES/{patch}").read())
    print("---")
