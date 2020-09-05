
import csv
import testing


f = open( 'companyList.csv', 'r' )

with open('scraped_data.csv', 'a') as csvfile:
    fieldnames = ['rank', 'business_name', 'telephone', 'business_page', 'category', 'website', 'rating',
                  'street', 'locality', 'region', 'zipcode', 'listing_url']
    writer = csv.DictWriter(csvfile, fieldnames=fieldnames, quoting=csv.QUOTE_ALL)
    writer.writeheader()


    for line in f:
        cells = line.split( "," )

        scraped_data = testing.parse_listing(cells[ 2 ] , cells[ 3 ] +","+ cells[ 0 ])

        if scraped_data:

                    for data in scraped_data:
                        writer.writerow(data)


f.close()