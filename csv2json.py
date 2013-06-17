import csv, json
def csv2json(filename, *fieldnames):
    f = open( filename, 'r' )
    reader = csv.DictReader( f, fieldnames = fieldnames  )
    reader.next()
    out = json.dumps( [ row for row in reader ] )
    new_file = open(f.name.replace('csv', 'json'), 'w')
    new_file.write(out)
    f.close
    return new_file

if __name__ == '__main__':
    csv2json('data/counties.csv', 'ID', 'Geography', 'USA', 'population', 'unemployment', 'high school', 'grads', 'gdp', 'lat', 'lon')
