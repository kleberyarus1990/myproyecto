from pandas import pandas

def main():
 print("hello")

 df = pandas.read_csv('../data/COPYDATA_20180515_1.csv',sep=';')
 print(df)

if __name__ == "__main__":
 main()