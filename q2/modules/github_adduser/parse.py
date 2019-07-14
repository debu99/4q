import csv, json, sys

def main():
    args = json.load(sys.stdin)
    with open(args['path'] + "/" + args['filename'], newline='') as csvfile:
        reader = csv.DictReader(csvfile)
        headers = reader.fieldnames
        row_dict = list(reader)
        teams = ""
        members = ""
        for i in range(1,len(headers)):
            teams = teams + headers[i] + ","
            for row in row_dict:
                if row[headers[i]] != '' and row[headers[i]] == 'maintainer':
                    members = members + headers[i] + "|" + row['Username'] + "|maintainer" + ","
                if row[headers[i]] != '' and row[headers[i]] == 'member':
                    members = members + headers[i] + "|" + row['Username'] + "|member" + ","

    output = {}
    output['teams']=teams[:-1]
    output['members']=members[:-1]
    print(json.dumps(output))

if __name__ == "__main__":
    main()