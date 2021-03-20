# Kafka fake data producer and consumer in python

Example how to produce fake massages into kafka topic.

## Setup

If you don't have kafka server yet use `install-kafka.sh` script under `scripts` path.

```bash
./install-kafka.sh
```

Script download kafka server and create local `KAFKA_HOME` variable, under `.env` file.

## Run

### Kafka

Open new terminal under `scripts` path, run shell script and do not stop script.

```bash
./run-zookeeper.sh
```

Same for kafka server:

```bash
./run-kafka.sh
```

Once either zookeeper and kafka server is up and running. It is possible to produce messages and consume messages.

### Producer

```bash
./run-producer.sh 
```

result:

```console
(venv) ➜  scripts ./run-producer.sh 
(...)
20-03-2021 13:10:12: {'id': 925986450141, 'name': 'Melissa Arroyo', 'date': '2008-12-16T14:19:13', 'address': '18393 Evans Loaf South Cathyview, CA 31555', 'startGate': 'Lake Derrick', 'exitGate': 'New Linda', 'price': {'net': 13, 'taxPercentage': 12, 'total': 14.56}}
20-03-2021 13:10:15: {'id': 680313917348, 'name': 'Mr. Todd Cain', 'date': '2020-12-19T14:45:05', 'address': '5025 Brian Groves Apt. 525 Sharpburgh, TX 30168', 'startGate': 'Youngbury', 'exitGate': 'Lewishaven', 'price': {'net': 11, 'taxPercentage': 12, 'total': 12.32}}
20-03-2021 13:10:15: {'id': 161040876785, 'name': 'Emily Elliott', 'date': '2004-03-24T02:10:12', 'address': '401 Lane Spring Brownstad, DC 48250', 'startGate': 'Onealhaven', 'exitGate': 'East Erinborough', 'price': {'net': 14, 'taxPercentage': 12, 'total': 15.68}}
20-03-2021 13:10:17: {'id': 984247320856, 'name': 'Ronald Thomas', 'date': '2006-05-03T01:15:07', 'address': 'Unit 0203 Box 8507 DPO AA 17868', 'startGate': 'Harmonland', 'exitGate': 'New Richard', 'price': {'net': 10, 'taxPercentage': 12, 'total': 11.2}}
20-03-2021 13:10:19: {'id': 887133430421, 'name': 'Heather Jordan', 'date': '2020-03-09T03:58:30', 'address': '169 Hatfield Loop Suite 881 New Christinachester, MN 15999', 'startGate': 'New Peter', 'exitGate': 'Grossshire', 'price': {'net': 6, 'taxPercentage': 12, 'total': 6.72}}
20-03-2021 13:10:21: {'id': 453323447158, 'name': 'Melissa Pope', 'date': '2011-06-11T06:56:36', 'address': '404 Daniels Run Apt. 654 Amyburgh, NM 85246', 'startGate': 'West Tylerbury', 'exitGate': 'Jamesville', 'price': {'net': 9, 'taxPercentage': 12, 'total': 10.08}}
20-03-2021 13:10:23: {'id': 583159808644, 'name': 'Aaron Morton', 'date': '2010-12-05T12:03:12', 'address': '28465 Jones Rue Suite 398 East Kevinland, AR 50399', 'startGate': 'Williamside', 'exitGate': 'Ericborough', 'price': {'net': 3, 'taxPercentage': 12, 'total': 3.36}}
20-03-2021 13:10:26: {'id': 413921923894, 'name': 'Victoria Robles', 'date': '2016-05-30T05:09:28', 'address': '61987 Nathaniel Court Suite 070 New Danielle, WA 93192', 'startGate': 'West James', 'exitGate': 'Parsonstown', 'price': {'net': 10, 'taxPercentage': 12, 'total': 11.2}}
20-03-2021 13:10:26: {'id': 748822493921, 'name': 'Robert Little', 'date': '2020-10-21T05:50:25', 'address': '8686 Hoover Vista Natashahaven, TN 39885', 'startGate': 'Lake Brandon', 'exitGate': 'Wileyland', 'price': {'net': 7, 'taxPercentage': 12, 'total': 7.84}}
20-03-2021 13:10:28: {'id': 29328782314, 'name': 'Mary Johnson', 'date': '2002-04-07T06:27:22', 'address': '1247 Jones Tunnel Annchester, NH 24639', 'startGate': 'Lopezville', 'exitGate': 'New Mitchell', 'price': {'net': 9, 'taxPercentage': 12, 'total': 10.08}}
20-03-2021 13:10:28: {'id': 725452978099, 'name': 'Charles Keller', 'date': '2007-08-21T03:11:36', 'address': '27421 Tricia Valley Emmamouth, IN 68727', 'startGate': 'Whitneyberg', 'exitGate': 'New Rachel', 'price': {'net': 14, 'taxPercentage': 12, 'total': 15.68}}
20-03-2021 13:10:29: {'id': 895662165044, 'name': 'Joshua Jimenez', 'date': '2012-02-15T14:31:46', 'address': '8479 Martinez Courts Apt. 537 Richardfort, ID 11088', 'startGate': 'Mitchellburgh', 'exitGate': 'North Christopherstad', 'price': {'net': 9, 'taxPercentage': 12, 'total': 10.08}}
20-03-2021 13:10:30: {'id': 352567971260, 'name': 'Meghan Thomas', 'date': '2020-05-04T17:38:32', 'address': '65890 Kristy Union Jeremiahstad, NY 81311', 'startGate': 'Munozport', 'exitGate': 'Choishire', 'price': {'net': 3, 'taxPercentage': 12, 'total': 3.36}}
20-03-2021 13:10:31: {'id': 151887806225, 'name': 'Bianca Wade', 'date': '2019-05-29T14:31:32', 'address': '2116 Morrow Keys Suite 365 South Nicolechester, NE 89115', 'startGate': 'Joshuaside', 'exitGate': 'South Jeffrey', 'price': {'net': 9, 'taxPercentage': 12, 'total': 10.08}}
20-03-2021 13:10:34: {'id': 690543850754, 'name': 'Alvin Cole', 'date': '2004-12-01T06:40:48', 'address': '797 Kathy Rest Apt. 272 South Shelby, WA 19413', 'startGate': 'West Davidchester', 'exitGate': 'New Scottstad', 'price': {'net': 12, 'taxPercentage': 12, 'total': 13.44}}
20-03-2021 13:10:36: {'id': 700364478862, 'name': 'Lisa Morris', 'date': '2006-02-15T06:28:13', 'address': '3531 Morales Trail Suite 196 Rubenhaven, DC 62005', 'startGate': 'North Elizabethshire', 'exitGate': 'Grayville', 'price': {'net': 13, 'taxPercentage': 12, 'total': 14.56}}
20-03-2021 13:10:38: {'id': 464166797700, 'name': 'Brenda Douglas', 'date': '2009-01-15T11:11:56', 'address': '313 Michael Parkways Lake Anthonychester, AR 71981', 'startGate': 'East Timothy', 'exitGate': 'North Pamelaton', 'price': {'net': 3, 'taxPercentage': 12, 'total': 3.36}}
20-03-2021 13:10:38: {'id': 469917056163, 'name': 'Ricky Obrien', 'date': '2019-07-26T04:43:05', 'address': '71937 Sophia Vista Apt. 666 Jonathantown, OK 53053', 'startGate': 'Port Sandraberg', 'exitGate': 'North Heatherside', 'price': {'net': 15, 'taxPercentage': 12, 'total': 16.8}}
20-03-2021 13:10:40: {'id': 292780357987, 'name': 'Jason Conner', 'date': '2009-03-05T13:17:01', 'address': '16250 Reyes Via West Ashleyview, IA 79615', 'startGate': 'Nicholasville', 'exitGate': 'Roberttown', 'price': {'net': 7, 'taxPercentage': 12, 'total': 7.84}}
20-03-2021 13:10:41: {'id': 787053688218, 'name': 'Seth Daniels', 'date': '2010-02-02T09:53:10', 'address': '283 Betty Key Apt. 834 Jonesburgh, MT 57602', 'startGate': 'Kennedyburgh', 'exitGate': 'New Jennifer', 'price': {'net': 8, 'taxPercentage': 12, 'total': 8.96}}
20-03-2021 13:10:41: {'id': 69566601496, 'name': 'Mr. Cody Rodriguez', 'date': '2011-03-28T11:08:58', 'address': '886 Nunez Orchard Suite 274 Garciaborough, IA 98628', 'startGate': 'Jaimebury', 'exitGate': 'Pierceside', 'price': {'net': 15, 'taxPercentage': 12, 'total': 16.8}}
20-03-2021 13:10:43: {'id': 188532360932, 'name': 'Brandon Smith', 'date': '2012-04-27T08:41:15', 'address': 'Unit 9004 Box 9947 DPO AA 39118', 'startGate': 'Davisside', 'exitGate': 'Aprilfort', 'price': {'net': 13, 'taxPercentage': 12, 'total': 14.56}}
20-03-2021 13:10:44: {'id': 481244745407, 'name': 'Jennifer Smith', 'date': '2004-12-05T00:54:40', 'address': '96044 Green Forges Suite 719 North Yolandaburgh, MD 45703', 'startGate': 'North Sarah', 'exitGate': 'West Melissa', 'price': {'net': 14, 'taxPercentage': 12, 'total': 15.68}}
20-03-2021 13:10:46: {'id': 757019959800, 'name': 'Lauren Holmes', 'date': '2015-07-02T12:35:03', 'address': '0727 Sarah Fort Kristaville, MT 40188', 'startGate': 'Hendricksbury', 'exitGate': 'Jacobtown', 'price': {'net': 6, 'taxPercentage': 12, 'total': 6.72}}
20-03-2021 13:10:47: {'id': 665659661354, 'name': 'Mark Ballard', 'date': '2020-06-26T08:30:47', 'address': '666 Lopez Road Suite 896 Clarkechester, MO 45561', 'startGate': 'Jenniferhaven', 'exitGate': 'West Gregory', 'price': {'net': 6, 'taxPercentage': 12, 'total': 6.72}}
20-03-2021 13:10:48: {'id': 553387864312, 'name': 'Tiffany Rivera', 'date': '2009-09-08T03:44:38', 'address': '504 Kimberly Inlet Apt. 858 Port Jacobmouth, TX 54360', 'startGate': 'Andrewton', 'exitGate': 'North Thomas', 'price': {'net': 4, 'taxPercentage': 12, 'total': 4.48}}
20-03-2021 13:10:48: {'id': 492051634616, 'name': 'Jeff Johnson', 'date': '2012-09-16T17:54:56', 'address': '51432 Hector Spur Suite 686 Port Angela, WA 05371', 'startGate': 'Brownshire', 'exitGate': 'Cassandrabury', 'price': {'net': 11, 'taxPercentage': 12, 'total': 12.32}}
20-03-2021 13:10:49: {'id': 306538330058, 'name': 'Steven Moore', 'date': '2015-12-28T06:46:44', 'address': '9057 Cox Street North Paultown, AR 89897', 'startGate': 'Lake Danieltown', 'exitGate': 'North Emilyborough', 'price': {'net': 13, 'taxPercentage': 12, 'total': 14.56}}
20-03-2021 13:10:50: {'id': 62415743328, 'name': 'Ryan Taylor', 'date': '2002-04-25T22:59:55', 'address': '0167 Ramirez Junction Apt. 927 South Matthew, MD 71979', 'startGate': 'Lake Robertborough', 'exitGate': 'Obrienland', 'price': {'net': 12, 'taxPercentage': 12, 'total': 13.44}}
20-03-2021 13:10:52: {'id': 565710357451, 'name': 'Andrea Williams', 'date': '2015-05-31T07:14:26', 'address': 'USNS Ray FPO AA 08840', 'startGate': 'Nicholasville', 'exitGate': 'Tamaramouth', 'price': {'net': 6, 'taxPercentage': 12, 'total': 6.72}}
20-03-2021 13:10:52: {'id': 579065084482, 'name': 'Kayla Kelly', 'date': '2002-08-26T14:25:52', 'address': '66125 Burnett Rest Suite 072 Careymouth, TX 43080', 'startGate': 'Wardville', 'exitGate': 'North Deborahshire', 'price': {'net': 15, 'taxPercentage': 12, 'total': 16.8}}
20-03-2021 13:10:53: {'id': 281421655400, 'name': 'Kevin Moran', 'date': '2007-11-15T16:28:26', 'address': '898 Robert Garden Apt. 291 Bradstad, WY 43774', 'startGate': 'New Shawn', 'exitGate': 'North Karenstad', 'price': {'net': 15, 'taxPercentage': 12, 'total': 16.8}}
20-03-2021 13:10:55: {'id': 525827299940, 'name': 'Gregory Gray', 'date': '2015-04-30T08:17:32', 'address': '82191 Jacob Lights Suite 657 East David, AZ 39818', 'startGate': 'Port Jerry', 'exitGate': 'South Kurtfort', 'price': {'net': 8, 'taxPercentage': 12, 'total': 8.96}}
20-03-2021 13:10:57: {'id': 432643481311, 'name': 'Andrea Brown', 'date': '2003-06-23T08:25:59', 'address': '18170 Medina Plains Scottport, AZ 34335', 'startGate': 'North Mitchellberg', 'exitGate': 'Lake Lisa', 'price': {'net': 12, 'taxPercentage': 12, 'total': 13.44}}
20-03-2021 13:10:58: {'id': 768115839059, 'name': 'Diana Lee', 'date': '2004-04-02T23:00:04', 'address': '988 Matthew Well Jenningsmouth, ME 24238', 'startGate': 'East Danielleland', 'exitGate': 'East Warrenland', 'price': {'net': 4, 'taxPercentage': 12, 'total': 4.48}}
20-03-2021 13:11:00: {'id': 6439793125, 'name': 'Deanna Harper', 'date': '2019-07-26T11:00:00', 'address': '8522 Donald Burg Apt. 517 New Jonathonhaven, WY 74342', 'startGate': 'Johnsonbury', 'exitGate': 'North Mirandamouth', 'price': {'net': 15, 'taxPercentage': 12, 'total': 16.8}}
20-03-2021 13:11:03: {'id': 503887816750, 'name': 'Amber Humphrey', 'date': '2018-08-07T07:55:33', 'address': '7060 Morgan Key Davidborough, AZ 16728', 'startGate': 'Wilsonhaven', 'exitGate': 'Valenciaton', 'price': {'net': 15, 'taxPercentage': 12, 'total': 16.8}}
20-03-2021 13:11:05: {'id': 61464751601, 'name': 'Kayla Ramirez', 'date': '2012-01-09T01:29:25', 'address': '07171 Gregory Park Lake Davidborough, MI 16929', 'startGate': 'South William', 'exitGate': 'Kimfurt', 'price': {'net': 3, 'taxPercentage': 12, 'total': 3.36}}
20-03-2021 13:11:08: {'id': 109888108140, 'name': 'Deanna Murphy', 'date': '2017-06-24T12:46:38', 'address': 'USNV Roberson FPO AP 12363', 'startGate': 'Destinyberg', 'exitGate': 'New Melissa', 'price': {'net': 3, 'taxPercentage': 12, 'total': 3.36}}
20-03-2021 13:11:08: {'id': 43044778741, 'name': 'Eric Simmons', 'date': '2018-12-22T10:08:05', 'address': '08795 Kathryn Union Apt. 316 Port Ashleyport, FL 69622', 'startGate': 'Port Gary', 'exitGate': 'North Ashley', 'price': {'net': 10, 'taxPercentage': 12, 'total': 11.2}}
20-03-2021 13:11:09: {'id': 681566045861, 'name': 'Dennis Blake', 'date': '2009-05-19T19:51:40', 'address': '28748 Latasha Cove Apt. 713 Dustinshire, IA 48241', 'startGate': 'North Jefferyfort', 'exitGate': 'West Sara', 'price': {'net': 8, 'taxPercentage': 12, 'total': 8.96}}
20-03-2021 13:11:10: {'id': 799291996707, 'name': 'Tony Larson', 'date': '2009-02-08T23:00:23', 'address': '6605 Michael Unions Ricechester, OK 15922', 'startGate': 'Margaretton', 'exitGate': 'New Stephen', 'price': {'net': 13, 'taxPercentage': 12, 'total': 14.56}}
```

### Consumer

```bash
./run-consumer.sh
```

```result
(...)
[20-03-2021 13:10:41][invoices:0:0]: b'{"id": 925986450141, "name": "Melissa Arroyo", "date": "2008-12-16T14:19:13", "address": "18393 Evans Loaf South Cathyview, CA 31555", "startGate": "Lake Derrick", "exitGate": "New Linda", "price": {"net": 13, "taxPercentage": 12, "total": 14.56}}'
[20-03-2021 13:10:41][invoices:0:1]: b'{"id": 680313917348, "name": "Mr. Todd Cain", "date": "2020-12-19T14:45:05", "address": "5025 Brian Groves Apt. 525 Sharpburgh, TX 30168", "startGate": "Youngbury", "exitGate": "Lewishaven", "price": {"net": 11, "taxPercentage": 12, "total": 12.32}}'
[20-03-2021 13:10:41][invoices:0:2]: b'{"id": 161040876785, "name": "Emily Elliott", "date": "2004-03-24T02:10:12", "address": "401 Lane Spring Brownstad, DC 48250", "startGate": "Onealhaven", "exitGate": "East Erinborough", "price": {"net": 14, "taxPercentage": 12, "total": 15.68}}'
[20-03-2021 13:10:41][invoices:0:3]: b'{"id": 984247320856, "name": "Ronald Thomas", "date": "2006-05-03T01:15:07", "address": "Unit 0203 Box 8507 DPO AA 17868", "startGate": "Harmonland", "exitGate": "New Richard", "price": {"net": 10, "taxPercentage": 12, "total": 11.2}}'
[20-03-2021 13:10:41][invoices:0:4]: b'{"id": 887133430421, "name": "Heather Jordan", "date": "2020-03-09T03:58:30", "address": "169 Hatfield Loop Suite 881 New Christinachester, MN 15999", "startGate": "New Peter", "exitGate": "Grossshire", "price": {"net": 6, "taxPercentage": 12, "total": 6.72}}'
[20-03-2021 13:10:41][invoices:0:5]: b'{"id": 453323447158, "name": "Melissa Pope", "date": "2011-06-11T06:56:36", "address": "404 Daniels Run Apt. 654 Amyburgh, NM 85246", "startGate": "West Tylerbury", "exitGate": "Jamesville", "price": {"net": 9, "taxPercentage": 12, "total": 10.08}}'
[20-03-2021 13:10:41][invoices:0:6]: b'{"id": 583159808644, "name": "Aaron Morton", "date": "2010-12-05T12:03:12", "address": "28465 Jones Rue Suite 398 East Kevinland, AR 50399", "startGate": "Williamside", "exitGate": "Ericborough", "price": {"net": 3, "taxPercentage": 12, "total": 3.36}}'
[20-03-2021 13:10:41][invoices:0:7]: b'{"id": 413921923894, "name": "Victoria Robles", "date": "2016-05-30T05:09:28", "address": "61987 Nathaniel Court Suite 070 New Danielle, WA 93192", "startGate": "West James", "exitGate": "Parsonstown", "price": {"net": 10, "taxPercentage": 12, "total": 11.2}}'
[20-03-2021 13:10:41][invoices:0:8]: b'{"id": 748822493921, "name": "Robert Little", "date": "2020-10-21T05:50:25", "address": "8686 Hoover Vista Natashahaven, TN 39885", "startGate": "Lake Brandon", "exitGate": "Wileyland", "price": {"net": 7, "taxPercentage": 12, "total": 7.84}}'
[20-03-2021 13:10:41][invoices:0:9]: b'{"id": 29328782314, "name": "Mary Johnson", "date": "2002-04-07T06:27:22", "address": "1247 Jones Tunnel Annchester, NH 24639", "startGate": "Lopezville", "exitGate": "New Mitchell", "price": {"net": 9, "taxPercentage": 12, "total": 10.08}}'
[20-03-2021 13:10:41][invoices:0:10]: b'{"id": 725452978099, "name": "Charles Keller", "date": "2007-08-21T03:11:36", "address": "27421 Tricia Valley Emmamouth, IN 68727", "startGate": "Whitneyberg", "exitGate": "New Rachel", "price": {"net": 14, "taxPercentage": 12, "total": 15.68}}'
[20-03-2021 13:10:41][invoices:0:11]: b'{"id": 895662165044, "name": "Joshua Jimenez", "date": "2012-02-15T14:31:46", "address": "8479 Martinez Courts Apt. 537 Richardfort, ID 11088", "startGate": "Mitchellburgh", "exitGate": "North Christopherstad", "price": {"net": 9, "taxPercentage": 12, "total": 10.08}}'
[20-03-2021 13:10:41][invoices:0:12]: b'{"id": 352567971260, "name": "Meghan Thomas", "date": "2020-05-04T17:38:32", "address": "65890 Kristy Union Jeremiahstad, NY 81311", "startGate": "Munozport", "exitGate": "Choishire", "price": {"net": 3, "taxPercentage": 12, "total": 3.36}}'
[20-03-2021 13:10:41][invoices:0:13]: b'{"id": 151887806225, "name": "Bianca Wade", "date": "2019-05-29T14:31:32", "address": "2116 Morrow Keys Suite 365 South Nicolechester, NE 89115", "startGate": "Joshuaside", "exitGate": "South Jeffrey", "price": {"net": 9, "taxPercentage": 12, "total": 10.08}}'
[20-03-2021 13:10:41][invoices:0:14]: b'{"id": 690543850754, "name": "Alvin Cole", "date": "2004-12-01T06:40:48", "address": "797 Kathy Rest Apt. 272 South Shelby, WA 19413", "startGate": "West Davidchester", "exitGate": "New Scottstad", "price": {"net": 12, "taxPercentage": 12, "total": 13.44}}'
[20-03-2021 13:10:41][invoices:0:15]: b'{"id": 700364478862, "name": "Lisa Morris", "date": "2006-02-15T06:28:13", "address": "3531 Morales Trail Suite 196 Rubenhaven, DC 62005", "startGate": "North Elizabethshire", "exitGate": "Grayville", "price": {"net": 13, "taxPercentage": 12, "total": 14.56}}'
[20-03-2021 13:10:41][invoices:0:16]: b'{"id": 464166797700, "name": "Brenda Douglas", "date": "2009-01-15T11:11:56", "address": "313 Michael Parkways Lake Anthonychester, AR 71981", "startGate": "East Timothy", "exitGate": "North Pamelaton", "price": {"net": 3, "taxPercentage": 12, "total": 3.36}}'
[20-03-2021 13:10:41][invoices:0:17]: b'{"id": 469917056163, "name": "Ricky Obrien", "date": "2019-07-26T04:43:05", "address": "71937 Sophia Vista Apt. 666 Jonathantown, OK 53053", "startGate": "Port Sandraberg", "exitGate": "North Heatherside", "price": {"net": 15, "taxPercentage": 12, "total": 16.8}}'
[20-03-2021 13:10:41][invoices:0:18]: b'{"id": 292780357987, "name": "Jason Conner", "date": "2009-03-05T13:17:01", "address": "16250 Reyes Via West Ashleyview, IA 79615", "startGate": "Nicholasville", "exitGate": "Roberttown", "price": {"net": 7, "taxPercentage": 12, "total": 7.84}}'
[20-03-2021 13:10:41][invoices:0:19]: b'{"id": 787053688218, "name": "Seth Daniels", "date": "2010-02-02T09:53:10", "address": "283 Betty Key Apt. 834 Jonesburgh, MT 57602", "startGate": "Kennedyburgh", "exitGate": "New Jennifer", "price": {"net": 8, "taxPercentage": 12, "total": 8.96}}'
[20-03-2021 13:10:41][invoices:0:20]: b'{"id": 69566601496, "name": "Mr. Cody Rodriguez", "date": "2011-03-28T11:08:58", "address": "886 Nunez Orchard Suite 274 Garciaborough, IA 98628", "startGate": "Jaimebury", "exitGate": "Pierceside", "price": {"net": 15, "taxPercentage": 12, "total": 16.8}}'
[20-03-2021 13:10:43][invoices:0:21]: b'{"id": 188532360932, "name": "Brandon Smith", "date": "2012-04-27T08:41:15", "address": "Unit 9004 Box 9947 DPO AA 39118", "startGate": "Davisside", "exitGate": "Aprilfort", "price": {"net": 13, "taxPercentage": 12, "total": 14.56}}'
[20-03-2021 13:10:44][invoices:0:22]: b'{"id": 481244745407, "name": "Jennifer Smith", "date": "2004-12-05T00:54:40", "address": "96044 Green Forges Suite 719 North Yolandaburgh, MD 45703", "startGate": "North Sarah", "exitGate": "West Melissa", "price": {"net": 14, "taxPercentage": 12, "total": 15.68}}'
[20-03-2021 13:10:46][invoices:0:23]: b'{"id": 757019959800, "name": "Lauren Holmes", "date": "2015-07-02T12:35:03", "address": "0727 Sarah Fort Kristaville, MT 40188", "startGate": "Hendricksbury", "exitGate": "Jacobtown", "price": {"net": 6, "taxPercentage": 12, "total": 6.72}}'
[20-03-2021 13:10:47][invoices:0:24]: b'{"id": 665659661354, "name": "Mark Ballard", "date": "2020-06-26T08:30:47", "address": "666 Lopez Road Suite 896 Clarkechester, MO 45561", "startGate": "Jenniferhaven", "exitGate": "West Gregory", "price": {"net": 6, "taxPercentage": 12, "total": 6.72}}'
[20-03-2021 13:10:48][invoices:0:25]: b'{"id": 553387864312, "name": "Tiffany Rivera", "date": "2009-09-08T03:44:38", "address": "504 Kimberly Inlet Apt. 858 Port Jacobmouth, TX 54360", "startGate": "Andrewton", "exitGate": "North Thomas", "price": {"net": 4, "taxPercentage": 12, "total": 4.48}}'
[20-03-2021 13:10:48][invoices:0:26]: b'{"id": 492051634616, "name": "Jeff Johnson", "date": "2012-09-16T17:54:56", "address": "51432 Hector Spur Suite 686 Port Angela, WA 05371", "startGate": "Brownshire", "exitGate": "Cassandrabury", "price": {"net": 11, "taxPercentage": 12, "total": 12.32}}'
[20-03-2021 13:10:49][invoices:0:27]: b'{"id": 306538330058, "name": "Steven Moore", "date": "2015-12-28T06:46:44", "address": "9057 Cox Street North Paultown, AR 89897", "startGate": "Lake Danieltown", "exitGate": "North Emilyborough", "price": {"net": 13, "taxPercentage": 12, "total": 14.56}}'
[20-03-2021 13:10:50][invoices:0:28]: b'{"id": 62415743328, "name": "Ryan Taylor", "date": "2002-04-25T22:59:55", "address": "0167 Ramirez Junction Apt. 927 South Matthew, MD 71979", "startGate": "Lake Robertborough", "exitGate": "Obrienland", "price": {"net": 12, "taxPercentage": 12, "total": 13.44}}'
[20-03-2021 13:10:52][invoices:0:29]: b'{"id": 565710357451, "name": "Andrea Williams", "date": "2015-05-31T07:14:26", "address": "USNS Ray FPO AA 08840", "startGate": "Nicholasville", "exitGate": "Tamaramouth", "price": {"net": 6, "taxPercentage": 12, "total": 6.72}}'
[20-03-2021 13:10:52][invoices:0:30]: b'{"id": 579065084482, "name": "Kayla Kelly", "date": "2002-08-26T14:25:52", "address": "66125 Burnett Rest Suite 072 Careymouth, TX 43080", "startGate": "Wardville", "exitGate": "North Deborahshire", "price": {"net": 15, "taxPercentage": 12, "total": 16.8}}'
[20-03-2021 13:10:53][invoices:0:31]: b'{"id": 281421655400, "name": "Kevin Moran", "date": "2007-11-15T16:28:26", "address": "898 Robert Garden Apt. 291 Bradstad, WY 43774", "startGate": "New Shawn", "exitGate": "North Karenstad", "price": {"net": 15, "taxPercentage": 12, "total": 16.8}}'
[20-03-2021 13:10:55][invoices:0:32]: b'{"id": 525827299940, "name": "Gregory Gray", "date": "2015-04-30T08:17:32", "address": "82191 Jacob Lights Suite 657 East David, AZ 39818", "startGate": "Port Jerry", "exitGate": "South Kurtfort", "price": {"net": 8, "taxPercentage": 12, "total": 8.96}}'
[20-03-2021 13:10:57][invoices:0:33]: b'{"id": 432643481311, "name": "Andrea Brown", "date": "2003-06-23T08:25:59", "address": "18170 Medina Plains Scottport, AZ 34335", "startGate": "North Mitchellberg", "exitGate": "Lake Lisa", "price": {"net": 12, "taxPercentage": 12, "total": 13.44}}'
[20-03-2021 13:10:58][invoices:0:34]: b'{"id": 768115839059, "name": "Diana Lee", "date": "2004-04-02T23:00:04", "address": "988 Matthew Well Jenningsmouth, ME 24238", "startGate": "East Danielleland", "exitGate": "East Warrenland", "price": {"net": 4, "taxPercentage": 12, "total": 4.48}}'
[20-03-2021 13:11:00][invoices:0:35]: b'{"id": 6439793125, "name": "Deanna Harper", "date": "2019-07-26T11:00:00", "address": "8522 Donald Burg Apt. 517 New Jonathonhaven, WY 74342", "startGate": "Johnsonbury", "exitGate": "North Mirandamouth", "price": {"net": 15, "taxPercentage": 12, "total": 16.8}}'
[20-03-2021 13:11:03][invoices:0:36]: b'{"id": 503887816750, "name": "Amber Humphrey", "date": "2018-08-07T07:55:33", "address": "7060 Morgan Key Davidborough, AZ 16728", "startGate": "Wilsonhaven", "exitGate": "Valenciaton", "price": {"net": 15, "taxPercentage": 12, "total": 16.8}}'
[20-03-2021 13:11:05][invoices:0:37]: b'{"id": 61464751601, "name": "Kayla Ramirez", "date": "2012-01-09T01:29:25", "address": "07171 Gregory Park Lake Davidborough, MI 16929", "startGate": "South William", "exitGate": "Kimfurt", "price": {"net": 3, "taxPercentage": 12, "total": 3.36}}'
[20-03-2021 13:11:08][invoices:0:38]: b'{"id": 109888108140, "name": "Deanna Murphy", "date": "2017-06-24T12:46:38", "address": "USNV Roberson FPO AP 12363", "startGate": "Destinyberg", "exitGate": "New Melissa", "price": {"net": 3, "taxPercentage": 12, "total": 3.36}}'
[20-03-2021 13:11:08][invoices:0:39]: b'{"id": 43044778741, "name": "Eric Simmons", "date": "2018-12-22T10:08:05", "address": "08795 Kathryn Union Apt. 316 Port Ashleyport, FL 69622", "startGate": "Port Gary", "exitGate": "North Ashley", "price": {"net": 10, "taxPercentage": 12, "total": 11.2}}'
[20-03-2021 13:11:09][invoices:0:40]: b'{"id": 681566045861, "name": "Dennis Blake", "date": "2009-05-19T19:51:40", "address": "28748 Latasha Cove Apt. 713 Dustinshire, IA 48241", "startGate": "North Jefferyfort", "exitGate": "West Sara", "price": {"net": 8, "taxPercentage": 12, "total": 8.96}}'
[20-03-2021 13:11:10][invoices:0:41]: b'{"id": 799291996707, "name": "Tony Larson", "date": "2009-02-08T23:00:23", "address": "6605 Michael Unions Ricechester, OK 15922", "startGate": "Margaretton", "exitGate": "New Stephen", "price": {"net": 13, "taxPercentage": 12, "total": 14.56}}'
```