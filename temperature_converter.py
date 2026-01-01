import argparse

parser = argparse.ArgumentParser(description="Konverter Suhu")

group = parser.add_mutually_exclusive_group(required=True)

group.add_argument("-c", "--celsius", type=float, help="Suhu dalam Celsius")
group.add_argument("-f", "--fahrenheit", type=float, help="Suhu dalam Fahrenheit")
group.add_argument("-k", "--kelvin", type=float, help="Suhu dalam Kelvin")

args = parser.parse_args()

if args.celsius:
    f = (args.celsius * 9/5) + 32
    k = args.celsius + 273.15
    print(f"{args.celsius}°C = {f:.1f}°F = {k:.1f}K")
    
elif args.fahrenheit:
    c = (args.fahrenheit - 32) * 5/9
    k = c + 273.15
    print(f"{args.fahrenheit}°F = {c:.1f}°C = {k:.1f}K")
    
elif args.kelvin:
    c = args.kelvin - 273.15
    f = (c * 9/5) + 32
    print(f"{args.kelvin}K = {c:.1f}°C = {f:.1f}°F")