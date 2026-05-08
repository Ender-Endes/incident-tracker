import json

try:
    with open("incidents.json", "r", encoding="utf-8") as f:
        existing = json.load(f)
except:
    existing = []


print("1. Yeni hata ekle")
print("2. Hataları listele")
print("3. Hata sil")
print("4. Değiştir")

test = input("Giriş bekleniyor")

if str(test) == "1":
    reason = input("Hatanın sebebi: ")
    date = input("Tarih: ")
    affected = input("Etkilenen: ")
    root_cause = input("Kök sebep: ")
    error3 = {"id": len(existing) + 1, "reason": reason, "date": date, "affected": affected, "root_cause": root_cause, "status": "open"}
    errors = []
    errors.append(error3)

    existing.extend(errors)

    with open("incidents.json", "w", encoding="utf-8") as f:
        json.dump(existing, f, ensure_ascii=False, indent=2)    


elif str(test) == "2":
    for hata in existing:
        for key, value in hata.items():
            print(f"{key}: {value}")
        print("---")

elif str(test) == "3":

    deleted = input("Silinmesi istenen ID: ")

    existing = [hata for hata in existing if hata["id"] != int(deleted)]

    with open("incidents.json", "w", encoding="utf-8") as f:
        json.dump(existing, f, ensure_ascii=False, indent=2)    

elif str(test) == "4":

    changed = input("Değişmesi istenen ID: ")

    for hata in existing:
        if hata["id"] == int(changed):
            reason = input("Hatanın sebebi: ")
            date = input("Tarih: ")
            affected = input("Etkilenen: ")
            root_cause = input("Kök sebep: ")
            hata["reason"] = reason
            hata["date"] = date
            hata["affected"] = affected
            hata["root_cause"] = root_cause 
            with open("incidents.json", "w", encoding="utf-8") as f:
                json.dump(existing, f, ensure_ascii=False, indent=2)    

