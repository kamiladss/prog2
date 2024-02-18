import json
with open('sample-data.json','r') as f:
    data=json.load(f)

intf = data.get('imdata', [])
print("Interface Status")
print("=" * 80)
print("{:<35} {:<15} {:<20} {:<8} {:<6}".format("DN", ".x", "Description", "Speed", "MTU"))
print("-" * 50, "-" * 20, "-" * 8, "-" * 6)

for i in intf:
    l1physif = i.get('l1PhysIf', {})
    att = l1physif.get('attributes', {})
    dn = att.get('dn', '')
    describtion = att.get('descr', '')
    speed = att.get('speed', 'inherit')
    mtu = att.get('mtu', '')
    
    print("{:<50} {:<20} {:<8} {:<6}".format(dn, describtion, speed, mtu))