raw = "  Alpha Rover  "
print(f"[{raw}]")
print(f"[{raw.strip()}]")
print(raw.strip().lower())
print(raw.strip().upper())
print(raw.strip().replace(" ", "_"))
print("Alpha" in raw)

# ------------------------------------------

packet = "T:30;H:65;B:80"
fields = packet.split(";")
print(fields)

key, value = "", ""
for field in fields:
    key, value = field.split(":")
    print(key, "->", float(value))

print(key, value)

# ------------------------------------------
