import json
import subprocess
import secrets
import time

while True:
    confs = json.load(open("c.json","rb"))
    ii=0

    def getPrivKey():
        return subprocess.check_output("xray x25519").decode().split(": ")[1].split("\n")[0]

    def getShortId():
        return secrets.token_hex(8)

    for i in confs["inbounds"]:
        try:
            if(i["streamSettings"]["security"] == "reality"):
                print(confs["inbounds"][ii]["streamSettings"]["realitySettings"]["privateKey"],"\n to ")
                confs["inbounds"][ii]["streamSettings"]["realitySettings"]["privateKey"] = getPrivKey()
                print(confs["inbounds"][ii]["streamSettings"]["realitySettings"]["privateKey"],"\n---")
                confs["inbounds"][ii]["streamSettings"]["realitySettings"]["shortIds"][0] = getShortId()
                confs["inbounds"][ii]["streamSettings"]["realitySettings"]["shortIds"][1] = getShortId()
            ii+=1
        except KeyError:
            ii+=1

    open("c2.json","w").write(json.dumps(confs,indent=4))

    print("12h sleep...")
    time.sleep(43200)