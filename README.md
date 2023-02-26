# Python Socket Server #
This is a Python socket server which connects to a MetaTrader 5 client. The server in itself is nothing different than a normal TCP socket server but the assossiated methodes are designed for a typical use case in algotrading. 
The connection is TCP and over IPv4.

Note that the commenting is done with absolute begginer's needs in mind.

## The Calculation Part ##
`socketserver.py` contains a part which should be changed before the usage. As this file was designed for our particular purpose you should remove `pivotBreakStrategy()` and the assossiated `import` and put something instead. Here are some examples:

### Recording the data in a .CSV file ###
Add the following lines to your code to record the recieved data in a .csv file:
```
    header = ['Data']
    values = chartdata

    with open('data.csv', 'w') as file:
        writer = csv.writer(file)
        writer.writerow(header)
        writer.writerows(values)
```

## To-Do List ##
- [x] Commenting
- [ ] Detailed Documention
- [x] requirements.txt